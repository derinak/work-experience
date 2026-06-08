# Python Exercise 1 – Simple Sudoku Solver

## Aims
 * Gain familiarity with the Python syntax
 * Use some of Python’s built-in data types
 * Be confident with Python’s mutability concepts
 * Have fun!

## Task Description
The aim of the task is to write a simple brute force Sudoku solver. We assume that everyone is familiar with Sudoku and if not you’ll probably want to consult http://en.wikipedia.org/wiki/Sudoku  before continuing.

We’re using a simple brute force approach so that we can concentrate on the Python syntax, mutability of objects, etc. There are more elegant and efficient ways to solve the problem and we’ll be using them in the next exercise along with the objected-oriented aspects of Python. That said if you wish to try and implement a more efficient algorithm you are welcome to do so.

The suggested approach is to solve the Sudoku using a recursive function. The function should take the Sudoku grid to solve, a rows list, a columns list, a box list and the current index. Each list should contain 9 sets which contain the numbers in the appropriate row, column or sub-box. For example the set at index 2 in the rows list would contain the numbers that are currently in the third row (remember Python indexes from zero like C). There are then three possible flows through the function:
1. The given index is outside the grid which implies the Sudoku has been solved, the function should return Success.
1. The square at the given index already contains a value. We don’t want to change this value so the function should be called recursively on the current index plus one and the result of this call should be returned.
1. The square at the given index does not contain a value. In this case iterate over the possible values (i.e 1 to 9) and:
    * Check whether inserting the value in the square at the given index would breach the rules of Sudoku using the appropriate sets. If it would not:
    * Insert the value in the square at the given index and also add the value to the appropriate sets
    * Call the function recursively on the given index plus one.
    * If the recursive call returns success return success otherwise remove the value from the square at the current index and also remove the value from the appropriate sets.
    * If the iteration is complete return failure.
The initial call to the function should pass the grid, the lists of sets (which should be partially filled based on the initial state of the Sudoku) and an index of zero.

**Hint:** It often appears that filling in the initial state of the sets would be an ideal application of slice notation. This is true for the rows and columns but much less true for the boxes. The suggested approach is in fact to iterate over the initial grid of values. For each index (i) in the grid you can calculate what row, column and box it is in using the following:

```python
row_index = i // N
column_index = i % N
box_index = (row_index // BOX_SIZE) * N_BOXES + column_index // BOX_SIZE
```

You can then easily insert the value at index I into the appropriate sets. Also the above may be quite helpful in the recursive function. The focus of the exercise is supposed to be Python not the algorithm so if anything is unclear please just ask. 

## Instructions

A framework file [is provided here](exercise1/exercise1.py).

To start, create a git branch - this will make it very easy to see what changes you have made from the original version!
 
You can use whatever editor you like to edit the file and you can run the file as follows: 
```bash
$ ./exercise1.py
```
If it doesn’t run then it’s likely the file is not executable. To ensure the file is executable run 
```bash
$ chmod +x exercise1.py
```

Regardless of how you run the file it should print two copies of the initial Sudoku and a message showing how long the solver function took to run and what the result was. . You now need to fill in the stub implementation. Good luck!

### Framework details

The framework assumes the following:
* The Sudoku is represented as a single 81 element list. Although Python obviously support lists of lists it’s unclear that it is a better way to represent a Sudoku as it only represents the rows in a particularly helpful manner. The second exercise revisits this issue but if you have a particular representation you’d like to try then feel free to give it a go.
* A square with no value is represented as zero. This is mostly just for ease of string representation so if you want to use something else (e.g None) then feel free.
The framework file provides:
* A utility function that converts a Sudoku grid into a string representation.
* An example Sudoku to solve.
* Some code to print the example Sudoku, call your solver function and print the result along with timings.
* A stub solver function. The result of this is used to determine whether the Sudoku has been successfully solved. Obviously you can cheat and just return True but cheaters never prosper. Remember you’re free to use as much or as little of the framework as you want. If you are using the framework you’ll probably want to use the solve_sudoku function to construct the initial lists of sets and then have a separate function to perform the recursive solving.

## Extras
If you find you’ve completed the exercise with loads of time to spare or you’ve discovered a passion for Python Sudoku solvers and want to carry on in your own time then the following is a list of ideas for extras you could:
* Improve the `grid_to_string` function to make the output prettier/more readable/etc.
* Use a default argument to make the initial call to the recursive function require a minimum number of arguments.
* Create a check function that can determine whether a Sudoku has been successfully solved (in case your solver contains a bug and returns true erroneously). Can you handle all the possible edge cases?
* Modify your solution so that it finds all possible solutions rather than simply the first possible solution. A true Sudoku only has one possible solution so you should print an error in this case.
* Ensure your code can cope with arbitrary sized Sudokus (i.e with 4 or 16 values instead of 9). You might like to solve the XKCD binary Sudoku from comic 74.
* Track the number of calls made to the recursive function and print this as part of the final output.
* Anything else you can think of!

