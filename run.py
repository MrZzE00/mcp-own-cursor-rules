#!/usr/bin/env python3
"""
Run script for MCP Own Cursor Rules server
"""

from src.main import mcp

if __name__ == "__main__":
    print("Starting MCP Own Cursor Rules server...")
    print("Access resources with:")
    print("  - rules://types - List all rule types")
    print("  - rules://<rule_type> - Get rules for a specific type")
    print("  - templates://list - List all templates")
    print("\nAvailable tools:")
    print("  - search_rules: Search rules by keyword")
    print("  - analyze_code: Check code against rules")
    print("  - get_examples_for_rule_type: Get examples for specific rule types")
    print("\nPress Ctrl+C to stop the server")
    mcp.run() 