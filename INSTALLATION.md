# Installing MCP Own Cursor Rules in Claude Desktop

This guide explains how to install and use the MCP Own Cursor Rules server with Claude Desktop.

## Prerequisites

- Claude Desktop application
- Python 3.10 or higher
- Access to the private GitHub repository `MrZzE00/own-cursor-rules` (optional, but required for full functionality)

## Configuration File Location

The Claude Desktop configuration file is located at:
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- Linux: `~/.config/Claude/claude_desktop_config.json`

## Installation Methods

### Method 1: Direct Installation in Claude Desktop

1. Open Claude Desktop
2. Type the following command:
   ```
   Please install this MCP server from GitHub: https://github.com/MrZzE00/mcp-own-cursor-rules
   ```
3. Claude will use the `mcp-installer` to install the server

### Method 2: Manual Installation

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/MrZzE00/own-cursor-rules.git
   cd own-cursor-rules
   ```

2. Create the MCP server directory:
   ```bash
   mkdir -p mcp-own-cursor-rules
   cd mcp-own-cursor-rules
   ```

3. Copy the files from this repository:
   ```bash
   # Copy the required files
   cp -r ../path/to/this/repo/* .
   ```

4. Install the dependencies:
   ```bash
   pip install -e .
   ```

5. Run the server:
   ```bash
   python run.py
   ```

6. In Claude Desktop, connect to the local MCP server using the URL provided in the server output (typically `localhost:8000`)

## Manual Configuration

If you need to manually configure Claude Desktop to use the MCP server:

1. Locate the Claude Desktop configuration file at the path shown above
2. Add the MCP server configuration to the file:
   ```json
   {
     "mcps": [
       {
         "name": "Cursor Rules",
         "url": "http://localhost:8000"
       }
     ]
   }
   ```
3. If you have access to the private rules repository, add your GitHub token:
   ```json
   {
     "mcps": [
       {
         "name": "Cursor Rules",
         "url": "http://localhost:8000",
         "auth": {
           "github": {
             "token": "YOUR_PERSONAL_ACCESS_TOKEN"
           }
         }
       }
     ]
   }
   ```
4. Save the file and restart Claude Desktop

## Getting Access to the Rules Repository

To get full access to the rules:

1. Contact the repository owner (MrZzE00) to be added as a collaborator
2. Or, generate a personal access token with the `repo` scope on your GitHub account:
   - Go to GitHub → Settings → Developer settings → Personal access tokens
   - Generate a new token with `repo` scope
   - Copy this token to your Claude Desktop configuration as shown above

## Using the MCP Server

Once installed, Claude will have access to all the coding rules and best practices. You can:

1. Ask Claude to follow specific coding standards
2. Request code quality improvements
3. Ask for security best practices
4. Get sample code templates

Example prompts:

- "Generate a React component following the best practices from the cursor rules"
- "Review this code according to the security rules"
- "How would I implement this feature according to DDD principles?"
- "Show me examples of accessibility rules I should follow"

## Available Resources

- **Rules Types**: `rules://types`
- **Rules by Type**: `rules://{rule_type}` (e.g., `rules://security`)
- **Templates**: `templates://list`

## Available Tools

- **search_rules**: Search for rules by keyword
- **analyze_code**: Check code against specific rule types
- **get_examples_for_rule_type**: Get examples for a specific rule type

## Troubleshooting

If you encounter any issues:

1. Make sure the MCP server is running (`python run.py`)
2. Check that Claude Desktop is properly configured to connect to MCP servers
3. Verify that the rules directory path is correctly set in the `main.py` file

For more help, refer to the Claude Desktop documentation on using MCP servers. 