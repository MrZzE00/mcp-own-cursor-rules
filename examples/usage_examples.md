# MCP Own Cursor Rules - Usage Examples

This document provides examples of how to use the MCP Own Cursor Rules server with Claude Desktop.

## Asking Claude to Follow Specific Rules

You can request Claude to follow specific coding rules when generating code. Here are some examples:

### Example 1: Security-Focused React Component

```
Please create a React login form component that follows all the security rules from the cursor rules. Make sure to implement proper input validation, secure password handling, and protection against common web vulnerabilities.
```

### Example 2: Accessible UI Component

```
Generate a dropdown menu component that follows all the accessibility (a11y) rules. It should be keyboard navigable, have proper ARIA attributes, and work well with screen readers.
```

### Example 3: Performance-Optimized Code

```
Write a JavaScript function to fetch and display a list of user data that follows the performance rules. It should implement efficient data loading, caching, and rendering optimization.
```

## Reviewing Code Against Rules

You can ask Claude to review existing code against the cursor rules:

### Example 1: Security Review

```
Please review this code for security vulnerabilities according to the security rules:

```javascript
function authenticateUser(username, password) {
  const user = users.find(u => u.username === username && u.password === password);
  if (user) {
    const token = Math.random().toString(36).substring(2);
    return { success: true, token: token };
  }
  return { success: false };
}
```
```

### Example 2: Code Quality Review

```
Review this code for code quality issues according to the code quality rules:

```python
def calculate(x, y, z, type):
  if type == 'add':
    res = x + y + z
  if type == 'multiply':
    res = x * y * z
  if type == 'subtract':
    res = x - y - z
  return res
```
```

## Getting Examples for Specific Rule Types

You can ask Claude to provide examples for specific rule types:

### Example 1: DDD Examples

```
Show me examples of Domain-Driven Design patterns according to the cursor rules.
```

### Example 2: Testing Examples

```
Provide examples of good testing practices according to the testing rules.
```

## Applying Multiple Rule Types

You can ask Claude to consider multiple rule types at once:

```
Create a React form component that validates user input. Please follow the security, accessibility, and performance rules from the cursor rules.
```

## Getting Rule Details

You can ask Claude about specific rules:

```
What are the security rules related to SQL injection prevention?
```

## Customizing Implementation Based on Rules

You can ask Claude to customize existing code to follow the rules:

```
I have this existing React component:

```jsx
function UserProfile({ user }) {
  return (
    <div>
      <h1>{user.name}</h1>
      <p>Email: {user.email}</p>
      <button onClick={() => alert('Profile updated')}>Update Profile</button>
    </div>
  );
}
```

Please refactor it to follow the accessibility and best practices rules from the cursor rules.
```

Remember that Claude will have access to all the rules in the repository, so you can be specific about which rules you want to follow. 