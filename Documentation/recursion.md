# Understanding Recursion in Python

## Introduction

Recursion is a powerful programming technique where a function calls itself to solve a problem.

Think of it like this: instead of using a loop to repeat something, you write a function that calls itself repeatedly until it reaches a stopping point.

---

## Why Learn Recursion?

- Some problems are naturally recursive and easier to solve with recursion
- Recursion is commonly used in algorithms (tree traversal, sorting, searching)
- It's a fundamental concept in computer science
- Many coding interview questions test recursion knowledge

---

## The Basic Concept

A recursive function has two essential parts:

1. **Base Case**: The stopping condition that prevents infinite recursion
2. **Recursive Case**: The part where the function calls itself with a simpler version of the problem

```python
def recursive_function(parameters):
    # Base case - when to stop
    if stopping_condition:
        return simple_answer
    
    # Recursive case - call yourself with a simpler problem
    return recursive_function(modified_parameters)
```

---

## Example 1: Factorial

The factorial of a number `n` (written as `n!`) is the product of all positive integers from 1 to n.
- `5! = 5 × 4 × 3 × 2 × 1 = 120`
- `4! = 4 × 3 × 2 × 1 = 24`

Notice that `5! = 5 × 4!` - this is perfect for recursion!

### Using a For Loop
```python
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_loop(5))  # Output: 120
```

### Using Recursion
```python
def factorial_recursive(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: n! = n × (n-1)!
    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))  # Output: 120
```

**How it works:**
```
factorial_recursive(5)
= 5 * factorial_recursive(4)
= 5 * (4 * factorial_recursive(3))
= 5 * (4 * (3 * factorial_recursive(2)))
= 5 * (4 * (3 * (2 * factorial_recursive(1))))
= 5 * (4 * (3 * (2 * 1)))
= 5 * (4 * (3 * 2))
= 5 * (4 * 6)
= 5 * 24
= 120
```

---

## Example 2: Fibonacci Sequence

The Fibonacci sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21...

Each number is the sum of the two preceding ones:
- `fib(0) = 0`
- `fib(1) = 1`
- `fib(n) = fib(n-1) + fib(n-2)`

### Using a For Loop
```python
def fibonacci_loop(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

print(fibonacci_loop(7))  # Output: 13
```

### Using Recursion
```python
def fibonacci_recursive(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive case: fib(n) = fib(n-1) + fib(n-2)
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print(fibonacci_recursive(7))  # Output: 13
```

**How it works for `fibonacci_recursive(5)`:**
```
                    fib(5)
                   /      \
              fib(4)      fib(3)
             /     \      /    \
        fib(3)   fib(2) fib(2) fib(1)
        /   \    /   \   /   \
    fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
    /   \
fib(1) fib(0)
```

---

## When to Use Recursion vs Loops

### Use Recursion When:
- The problem naturally breaks down into smaller, similar subproblems
- Working with tree or graph structures
- The problem definition is already recursive (like Fibonacci)
- Code readability improves significantly

### Use Loops When:
- Simple iteration is all you need
- Performance is critical (recursion has overhead)
- You might hit Python's recursion limit (default is ~1000 calls)
- The iterative solution is clearer

---

## Common Pitfalls

### 1. Forgetting the Base Case
```python
# ❌ WRONG - This will cause infinite recursion!
def bad_countdown(n):
    print(n)
    bad_countdown(n - 1)  # Never stops!
```

### 2. Wrong Base Case
```python
# ❌ WRONG - Base case is never reached
def bad_factorial(n):
    if n == 0:
        return 1
    return n * bad_factorial(n + 1)  # n keeps growing!
```

### 3. Not Making Progress Toward Base Case
```python
# ❌ WRONG - Always calls with same value
def bad_sum(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + bad_sum(numbers)  # Should be numbers[1:]
```

---

## Key Takeaways

1. **Recursion = Function calling itself** with a simpler version of the problem
2. **Always need a base case** to stop the recursion
3. **Each recursive call should get closer to the base case**
4. **Recursion uses the call stack** - each call waits for the next one to complete
5. **Not always better than loops**, but great for certain problems

