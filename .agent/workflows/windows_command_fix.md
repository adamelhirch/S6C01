---
description: Fix for Windows command execution issues
---

# Windows Command Fix

When running commands on Windows, the `run_command` tool may append an extra quote or malform the command string, causing it to hang or fail.

## Solution

To fix this, wrap the command in `cmd /c` and append `& ::` to the end. This executes the command and then executes a comment, which safely absorbs any trailing garbage characters.

## Pattern

```
cmd /c <your_command> & ::
```

## Examples

### Example 1: Directory Listing

**Instead of:**
```
dir
```

**Use:**
```
cmd /c dir & ::
```

### Example 2: Running Python Scripts

**Instead of:**
```
python main.py
```

**Use:**
```
cmd /c python main.py & ::
```

### Example 3: Git Commands

**Instead of:**
```
git status
```

**Use:**
```
cmd /c git status & ::
```

## When to Apply

Apply this pattern to **all** commands run via the `run_command` tool on Windows systems to ensure reliable execution and prevent hanging or malformed command issues.
