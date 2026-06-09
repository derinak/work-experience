# Python Debugger (pdb) Cheatsheet

## What is PDB?

PDB is Python's built-in interactive debugger. It lets you pause your code execution, inspect variables, step through code line-by-line, and understand what's happening at runtime.

## How to Start Debugging

Use the built-in `breakpoint()`:

```python
def my_function(x, y):
    result = x + y
    breakpoint()  # execution pauses here
    return result * 2
```

---

## Essential PDB Commands

| Command | Shortcut | Description |
|---------|----------|-------------|
| `breakpoint()` | - | Add this in your code to pause execution |
| `list` | `l` | Prints out the whole document/current location |
| `print(expr)` | `p` | Print value of a variable or expression |
| `pp expr` | `pp` | Pretty-print (better formatting for dicts/lists) |
| `bt` / `where` | `bt` | Backtrace - show the call stack |
| `args` | `a` | Show arguments of the function you're in |
| `next` | `n` | Go to next line (don't step into functions) |
| `continue` | `c` | Continue execution until next breakpoint |
| `step` | `s` | Step into functions |
| `return` | `r` | Carry on until current function returns |
| `up` | `u` | Go back to the point where the previous line was |
| `down` | `d` | Go down the stack |
| `jump line` | `j` | Jump to another line number |
| `break func` | `b` | Add another breakpoint (e.g., `break func_2`) |
| `break` | `b` | List all breakpoints |
| `clear` | - | Clear breakpoints |
| `quit` | `q` | Quit the debugger |

**Note:** You can set variables directly in PDB (e.g., `x = 10`)

---

## Quick Reference Card

```
breakpoint()     - Add in code to pause
l                - List/show code
p var            - Print variable
pp var           - Pretty-print
bt               - Backtrace (call stack)
a                - Arguments
n                - Next line
c                - Continue
s                - Step into
r                - Return from function
u                - Up stack
d                - Down stack
j 42             - Jump to line 42
b func           - Set breakpoint
b                - List breakpoints
clear            - Clear breakpoints
q                - Quit
```

---

## Practical Examples

### Example 1: Debugging a Loop

```python
def find_bug(numbers):
    total = 0
    for i, num in enumerate(numbers):
        breakpoint()  # Pause at each iteration
        total += num * i
    return total

result = find_bug([1, 2, 3, 4, 5])
```

**In PDB:**
```
(Pdb) p i          # Check loop counter
(Pdb) p num        # Check current number
(Pdb) p total      # Check running total
(Pdb) n            # Next iteration
```

### Example 2: Conditional Breakpoint

```python
def process_data(items):
    for item in items:
        # Only break when item is suspicious
        if item > 100:
            breakpoint()
        result = item * 2
    return result
```

Or set it from PDB:
```
(Pdb) b 5, item > 100    # Break at line 5 only when item > 100
```

### Example 3: Examining Function Calls

```python
def outer(x):
    return inner(x + 10)

def inner(y):
    breakpoint()
    return y * 2

outer(5)
```

**In PDB:**
```
(Pdb) where        # Show call stack
(Pdb) args         # Show current function arguments
(Pdb) up           # Move to outer function
(Pdb) p x          # Check x in outer
(Pdb) down         # Back to inner
```

### Example 4: Inspecting Complex Data

```python
data = {
    'users': [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25}
    ]
}
breakpoint()
print(data)
```

**In PDB:**
```
(Pdb) pp data                    # Pretty print whole structure
(Pdb) p data['users'][0]         # Access nested data
(Pdb) p [u['name'] for u in data['users']]  # List comprehension works!
```

---

## Common Workflow

1. **Start with breakpoint**: Add `breakpoint()` where you suspect an issue
2. **Run your code**: Execute normally until it hits the breakpoint
3. **Inspect state**: Use `p`, `pp`, `args` to check variables
4. **Step through**: Use `n` to step line by line
5. **Check deeply**: Use `s` to step into suspicious functions
6. **Continue or quit**: Use `c` to continue or `q` to quit

---