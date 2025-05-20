# Hosting MCP Own Cursor Rules on GitHub

This guide explains how to host the MCP Own Cursor Rules server on GitHub, allowing Claude Desktop to access it directly without local installation.

## Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and sign in to your account
2. Click the "New" button to create a new repository
3. Name the repository `mcp-own-cursor-rules`
4. Add a description (optional)
5. Choose whether to make it public or private (public is recommended for easy access)
6. Click "Create repository"

## Step 2: Push the Code to GitHub

1. After creating the repository, follow the instructions on GitHub to push your existing repository:

```bash
git remote add origin https://github.com/MrZzE00/mcp-own-cursor-rules.git
git branch -M main
git push -u origin main
```

## Step 3: Configure Claude Desktop

1. Open the Claude Desktop configuration file:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - Linux: `~/.config/Claude/claude_desktop_config.json`

2. Add the MCP server to the configuration:
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

## Updating the Server

When you make changes to the server code:

1. Make your changes locally
2. Commit the changes: `git commit -am "Description of changes"`
3. Push to GitHub: `git push origin main`

Claude Desktop will access the updated code the next time it's started. 