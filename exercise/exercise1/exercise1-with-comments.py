#!/usr/bin/env python3


import time

N = 9
"""Number of different values in the Sudoku."""

BOX_SIZE = 3
"""Size of a single box."""

N_BOXES = 3
"""Number of boxes in each direction."""


# Pretty printer definitions.
GRID_SEPS = (
    (N * N, "\n"),
    (N * BOX_SIZE, "\n---+---+---\n"),
    (N, "\n"),
    (BOX_SIZE, "|"),
)


def grid_to_string(grid: list[int]) -> str:
    """Return a string representation of a grid suitable for printing."""
    output = ""
    for index, value in enumerate(grid):
        output += str(value) if value else " "
        for mod, sep in GRID_SEPS:
            if (index + 1) % mod == 0:
                output += sep
                break
    return output


def solve_sudoku_internal(grid: list[int], row_sets: list[set[int]], column_sets: list[set[int]], box_sets: list[set[int]], index: int = 0) -> bool:
    """
    Solves a sudoku.

    Input is expected to take the form of an 81 element list that represents
    the Sudoku. If a square is initally blank it should contain a value of
    zero.
    """

    # If the index is outside the grid, return True


    # If the value at the given index already contains a value, then we jump to the next index (index+1) and call the function recursively (call the solve_sudoku_internal())


    # Else, we test all possible values and attempt to recursively solve teh Sudoku for any values 
    # Here get the row, column and box index for the given index
    # For each possible value, 
    #    1. Check if adding the value at the current index would breach the
    #       rules of Sudoku.
    #    2. If the above check passes then add the value to all appropriate row, column and box sets and call this
    #       solver function recursively (on index+1). 
    #       a. If the recursive call returns True, then return True.
    #       b. If the recursive call returns False, then remove the value from the grid and the appropriate sets
    
    


def solve_sudoku(grid: list[int]) -> bool:
    """
    Solves a sudoku.

    Input is expected to take the form of an 81 element list that represents
    the Sudoku. If a square is initally blank it should contain a value of
    zero.

    Returns True if the sudoku is solved, False otherwise.

    """

    # Create 3 empty lists of sets for the rows, columns, and boxes


    # Add N empty sets to each list


    # Iterate over the grid with a loop
    # For each element, calculate the row, column and box index
    # Add the element to the appropriate set in each list if it contains a value other than zero



    # Call an internal function to solve the sudoku and return the result




    return False


# ------------------------------------------------------------------------------
# Main code
#


def main() -> None:
    """
    Main function.

    Prints the initial state of the sudoku, solves it and prints out the
    solution along with the time taken.

    """
    # Sudoku to solve
    # fmt: off
    example = [5, 3, 0, 0, 7, 0, 0, 0, 0, 
               6, 0, 0, 1, 9, 5, 0, 0, 0, 
               0, 9, 8, 0, 0, 0, 0, 6, 0, 
               8, 0, 0, 0, 6, 0, 0, 0, 3, 
               4, 0, 0, 8, 0, 3, 0, 0, 1, 
               7, 0, 0, 0, 2, 0, 0, 0, 6, 
               0, 6, 0, 0, 0, 0, 2, 8, 0, 
               0, 0, 0, 4, 1, 9, 0, 0, 5, 
               0, 0, 0, 0, 8, 0, 0, 7, 9]
    # fmt: on

    # Print the Sudoku in its initial state
    print(f"{grid_to_string(example)}\n\n")

    # Solve the Sudoku, storing the time before and after
    start_time = time.time()
    solved = solve_sudoku(example)
    finish_time = time.time()

    # Print the final state of the Sudoku and how long it took to get there
    print(
        f"{grid_to_string(example)}\n\nTook: {finish_time - start_time:.5f} "
        f"seconds to {'solve' if solved else 'not solve'}"
    )


# This code checks whether this code is running as a program or has been
# imported by other code. We"ll cover this later but this is generally
# considered good practice.
if __name__ == "__main__":
    main()