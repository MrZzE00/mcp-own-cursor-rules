# MCP Own Cursor Rules

A Model Context Protocol (MCP) server that provides Claude Desktop with access to comprehensive code quality rules, best practices, and code examples from the Own Cursor Rules repository.

## Important Note About Rules Access

The MCP server is designed to access rules from the private repository `MrZzE00/own-cursor-rules`. For an end user to benefit from this MCP server, two options are available:

1. **Using a token access (recommended)**: The user needs a personal access token for the private repository. Configure Claude Desktop with this token in the `auth` field:
   ```json
   {
     "mcps": [
       {
         "name": "Cursor Rules",
         "url": "https://raw.githubusercontent.com/MrZzE00/mcp-own-cursor-rules/main",
         "auth": {
           "github": {
             "token": "YOUR_PERSONAL_ACCESS_TOKEN"
           }
         }
       }
     ]
   }
   ```

2. **Access without token (limited functionality)**: Users without access to the private repo will only be able to use the MCP server's code and structure, but will not have access to the actual rules content.

To grant users access to the private repo, you can add them as collaborators in the GitHub repository settings.

## Overview

This MCP server enables Claude Desktop to access and apply a rich set of coding standards and best practices across multiple domains:

- **Code Quality**: Variable naming, formatting, comments, etc.
- **Security**: Authentication, data validation, CSRF protection, etc.
- **Best Practices**: Design patterns, error handling, etc.
- **Architecture**: Layering, modularity, component design, etc.
- **Accessibility**: ARIA attributes, keyboard navigation, screen reader support, etc.
- **Performance**: Caching, lazy loading, optimization techniques, etc.
- **Testing**: Unit tests, integration tests, coverage, etc.
- **Internationalization**: Localization, text handling, etc.
- **Documentation**: Comments, JSDoc, documentation structure, etc.
- **Domain-Driven Design**: Bounded contexts, entities, value objects, etc.
- **CI/CD**: Continuous integration, deployment practices, etc.
- **Dependencies**: Dependency management, versioning, etc.
- **Scalability**: Database optimization, caching strategies, etc.

## Installation

### Prerequisites

- Claude Desktop application
- Python 3.10 or higher (only for local installation)

### Option 1: Use Directly from GitHub

You can use this MCP server directly from GitHub without local installation:

1. Open Claude Desktop
2. Add the following to your Claude Desktop configuration file (located at `~/Library/Application Support/Claude/claude_desktop_config.json`):
   ```json
   {
     "mcps": [
       {
         "name": "Cursor Rules",
         "url": "https://raw.githubusercontent.com/MrZzE00/mcp-own-cursor-rules/main"
       }
     ]
   }
   ```
3. Save the file and restart Claude Desktop

### Option 2: Install Using Claude Desktop

In Claude Desktop, you can install this MCP server directly by typing:

```
Please install this MCP server from GitHub: https://github.com/MrZzE00/own-cursor-rules
```

### Option 3: Manual Installation

1. Clone the repository and build the server:
   ```bash
   # Clone the original rules repository
   git clone https://github.com/MrZzE00/own-cursor-rules.git
   
   # Clone this MCP server repository
   git clone https://github.com/your-username/mcp-own-cursor-rules.git
   
   # Install the MCP server
   cd mcp-own-cursor-rules
   pip install -e .
   ```

2. Run the server:
   ```bash
   python run.py
   ```

3. Connect Claude Desktop to the server using the provided URL (typically `http://localhost:8000`)

## Using the MCP Server

Once installed, Claude Desktop will have access to all the rules and can:

1. **Generate Code Following Specific Rules**: Ask Claude to write code that follows specific rules
2. **Review Code Against Rules**: Ask Claude to analyze code for compliance with rules
3. **Provide Best Practices Examples**: Get examples of good/bad practices
4. **Access Code Templates**: Retrieve pre-built templates for common tasks

See the [examples/usage_examples.md](examples/usage_examples.md) file for detailed usage examples.

## Available Resources and Tools

### Resources

- **`rules://types`**: List all available rule types
- **`rules://{rule_type}`**: Get rules for a specific type (e.g., `rules://security`)
- **`rules://{rule_type}/{rule_name}`**: Get a specific rule
- **`templates://list`**: List all available code templates
- **`templates://{template_name}`**: Get a specific template

### Tools

- **`search_rules(keyword)`**: Search for rules containing a keyword
- **`analyze_code(code, rule_types)`**: Check code against specific rule types
- **`get_examples_for_rule_type(rule_type)`**: Get examples for a specific rule type

## Project Structure

```
mcp-own-cursor-rules/
├── src/                # Source code for the MCP server
│   ├── __init__.py     # Package initialization
│   └── main.py         # Main server implementation
├── examples/           # Usage examples
├── run.py              # Server runner script
├── pyproject.toml      # Python project configuration
├── README.md           # This file
├── INSTALLATION.md     # Detailed installation instructions
└── LICENSE             # License information
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Own Cursor Rules](https://github.com/MrZzE00/own-cursor-rules) for the original rules repository
- [FastMCP](https://github.com/jlowin/fastmcp) for the MCP server framework 