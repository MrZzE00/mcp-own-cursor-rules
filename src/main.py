import json
import os
import glob
from typing import Dict, List, Optional, Any, Union
from fastmcp import FastMCP, Context

# Create a FastMCP server instance
mcp = FastMCP("Cursor Rules")

# Define the path to the rules directory
RULES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "own-cursor-rules", "rules"))
if not os.path.exists(RULES_DIR):
    raise FileNotFoundError(f"Rules directory not found at {RULES_DIR}")

# Define resource paths
RULES_TYPES = [
    "codequality", 
    "bestpractices", 
    "security", 
    "ddd", 
    "a11y", 
    "performance", 
    "testing", 
    "cicd", 
    "architecture", 
    "i18n", 
    "documentation", 
    "dependencies", 
    "scalability"
]

# Helper function to read rule files
def read_rules_file(rule_type: str) -> Dict[str, Any]:
    """Read a rules JSON file and return its contents."""
    file_path = os.path.join(RULES_DIR, f"{rule_type}_rules.json")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Rules file not found: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Helper function to read template file
def read_template_file(template_name: str) -> str:
    """Read a template file and return its contents."""
    template_path = os.path.join(RULES_DIR, "templates", template_name)
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template file not found: {template_path}")
    
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()

# Resource to list all available rule types
@mcp.resource("rules://types")
def get_rule_types() -> List[str]:
    """Get a list of all available rule types."""
    return RULES_TYPES

# Resource to get rules by type
@mcp.resource("rules://{rule_type}")
def get_rules_by_type(rule_type: str) -> Dict[str, Any]:
    """Get rules for a specific rule type."""
    if rule_type not in RULES_TYPES:
        return {"error": f"Unknown rule type: {rule_type}", "available_types": RULES_TYPES}
    
    try:
        return read_rules_file(rule_type)
    except Exception as e:
        return {"error": str(e)}

# Resource to get a specific rule by name
@mcp.resource("rules://{rule_type}/{rule_name}")
def get_rule_by_name(rule_type: str, rule_name: str) -> Dict[str, Any]:
    """Get a specific rule by its name."""
    if rule_type not in RULES_TYPES:
        return {"error": f"Unknown rule type: {rule_type}", "available_types": RULES_TYPES}
    
    try:
        rules_data = read_rules_file(rule_type)
        rules = rules_data.get("rules", [])
        
        for rule in rules:
            if rule.get("name") == rule_name:
                return rule
        
        return {"error": f"Rule not found: {rule_name}"}
    except Exception as e:
        return {"error": str(e)}

# Resource to list all available templates
@mcp.resource("templates://list")
def list_templates() -> Dict[str, List[str]]:
    """List all available templates."""
    templates_dir = os.path.join(RULES_DIR, "templates")
    
    # Regular files
    js_files = glob.glob(os.path.join(templates_dir, "*.js"))
    jsx_files = glob.glob(os.path.join(templates_dir, "*.jsx"))
    java_files = glob.glob(os.path.join(templates_dir, "*.java"))
    md_files = glob.glob(os.path.join(templates_dir, "*.md"))
    
    # Python examples directory
    python_dir = os.path.join(templates_dir, "securityExamplesPython")
    python_files = glob.glob(os.path.join(python_dir, "*.py")) if os.path.exists(python_dir) else []
    
    return {
        "javascript": [os.path.basename(f) for f in js_files],
        "react": [os.path.basename(f) for f in jsx_files],
        "java": [os.path.basename(f) for f in java_files],
        "markdown": [os.path.basename(f) for f in md_files],
        "python": [os.path.basename(f) for f in python_files]
    }

# Resource to get a specific template
@mcp.resource("templates://{template_name}")
def get_template(template_name: str) -> str:
    """Get a specific template by name."""
    try:
        return read_template_file(template_name)
    except FileNotFoundError:
        # Try in Python directory
        try:
            python_template = os.path.join("securityExamplesPython", template_name)
            return read_template_file(python_template)
        except FileNotFoundError:
            return f"Template not found: {template_name}"
    except Exception as e:
        return f"Error reading template: {str(e)}"

# Tool to search for rules by keyword
@mcp.tool()
def search_rules(keyword: str) -> Dict[str, List[Dict[str, Any]]]:
    """
    Search for rules containing the specified keyword in name, pattern, or message.
    
    Args:
        keyword: The keyword to search for in rules
        
    Returns:
        Dictionary mapping rule types to matching rules
    """
    results = {}
    keyword = keyword.lower()
    
    for rule_type in RULES_TYPES:
        try:
            rules_data = read_rules_file(rule_type)
            rules = rules_data.get("rules", [])
            
            matching_rules = []
            for rule in rules:
                name = rule.get("name", "").lower()
                message = rule.get("message", "").lower()
                pattern = rule.get("pattern", "").lower()
                
                if (keyword in name) or (keyword in message) or (keyword in pattern):
                    matching_rules.append(rule)
            
            if matching_rules:
                results[rule_type] = matching_rules
        except Exception:
            # Skip files with errors
            pass
    
    return results

# Tool to analyze code against rules
@mcp.tool()
def analyze_code(code: str, rule_types: Optional[List[str]] = None) -> Dict[str, List[Dict[str, Any]]]:
    """
    Analyze code against specified rule types.
    
    Args:
        code: The code to analyze
        rule_types: Optional list of rule types to check against (defaults to all)
        
    Returns:
        Dictionary mapping rule types to matching rules
    """
    if rule_types is None:
        rule_types = RULES_TYPES
    else:
        # Validate rule types
        for rule_type in rule_types:
            if rule_type not in RULES_TYPES:
                return {"error": f"Unknown rule type: {rule_type}", "available_types": RULES_TYPES}
    
    import re
    results = {}
    
    for rule_type in rule_types:
        try:
            rules_data = read_rules_file(rule_type)
            rules = rules_data.get("rules", [])
            
            matching_rules = []
            for rule in rules:
                pattern = rule.get("pattern", "")
                if not pattern:
                    continue
                
                try:
                    # Try to compile and match the pattern
                    regex = re.compile(pattern)
                    if regex.search(code):
                        matching_rules.append({
                            "name": rule.get("name"),
                            "message": rule.get("message"),
                            "severity": rule.get("severity")
                        })
                except re.error:
                    # Skip invalid patterns
                    pass
            
            if matching_rules:
                results[rule_type] = matching_rules
        except Exception:
            # Skip files with errors
            pass
    
    return results

# Tool to get examples for a specific rule type
@mcp.tool()
def get_examples_for_rule_type(rule_type: str) -> Dict[str, Any]:
    """
    Get example files related to a specific rule type.
    
    Args:
        rule_type: The type of rules to get examples for
        
    Returns:
        Dictionary with example contents
    """
    if rule_type not in RULES_TYPES:
        return {"error": f"Unknown rule type: {rule_type}", "available_types": RULES_TYPES}
    
    examples = {}
    templates_dir = os.path.join(RULES_DIR, "templates")
    
    # Check for specific example files based on rule type
    potential_files = [
        f"{rule_type}Examples.js",
        f"{rule_type}_examples.js",
        f"{rule_type}Examples.jsx",
        f"{rule_type}Examples.java",
        f"{rule_type}Examples.py",
    ]
    
    for filename in potential_files:
        file_path = os.path.join(templates_dir, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                examples[filename] = f.read()
    
    # Check Python examples directory if related to security
    if rule_type == "security":
        python_dir = os.path.join(templates_dir, "securityExamplesPython")
        if os.path.exists(python_dir):
            python_files = glob.glob(os.path.join(python_dir, "*.py"))
            for file_path in python_files:
                filename = os.path.basename(file_path)
                with open(file_path, 'r', encoding='utf-8') as f:
                    examples[f"python/{filename}"] = f.read()
    
    return examples if examples else {"message": f"No examples found for rule type: {rule_type}"}

# Run the MCP server
if __name__ == "__main__":
    mcp.run() 