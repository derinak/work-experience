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
    (BOX_SIZE, "|"),)


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
    if index >= N*N:
        return True
    if grid[index] != 0:
        return solve_sudoku_internal(grid, row_sets, column_sets, box_sets, index + 1)
    row = index // N
    column = index % N
    box = (row // BOX_SIZE) * N_BOXES + column // BOX_SIZE
    for value in range(1,10):
        if (value not in row_sets[row] and value not in column_sets[column] and value not in box_sets[box]):
            grid[index] = value
            row_sets[row].add(value)
            column_sets[column].add(value)
            box_sets[box].add(value)
            if solve_sudoku_internal(grid, row_sets, column_sets, index + 1):
                return True
            grid[index] = 0
            row_sets[row].remove(value)
            column_sets[column].remove(value)
            box_sets[box].remove(value)
    return False


def valid(grid: list[int], row:int, column:int, num:int):
    row_start = row * N
    if num in grid[row_start: row_start + N]:
        return False
    if num in [grid[i * N + column] for i in range(N)]:
        return False
    box_row = (row//BOX_SIZE)*BOX_SIZE
    box_col = (column//BOX_SIZE)*BOX_SIZE
    for r in range(box_row, box_row + BOX_SIZE):
        for c in range(box_col, box_col + BOX_SIZE):
            if grid[r*N+c] == num:
                return True

def solve_sudoku(grid: list[int]) -> bool:
    # Create empty lists of sets for rows x9, columns x9 and boxes x9
    row_sets = []
    column_sets = []
    box_sets = []
    for i in range(N):
        row_sets.append(set())
        column_sets.append(set())
        box_sets.append(set())
    for index, value in enumerate(grid):
        if value != 0:
            row = i // N
            column = i % N
            box = (row // BOX_SIZE) * N_BOXES + column // BOX_SIZE
            row_sets[row].add(value)
            column_sets[column].add(value)
            box_sets[box].add(value)
    return solve_sudoku_internal(grid, row_sets, column_sets, box_sets, 0)

    #  enumerate(grid) -> i, element 
        # Append the element into the correct set
        # rows[row_index].add(element)
        # Call a function/do more on solving sudoku
    """
    Solves a sudoku.

    Input is expected to take the form of an 81 element list that represents
    the Sudoku. If a square is initally blank it should contain a value of
    zero.

    Returns True if the sudoku is solved, False otherwise.
    """
    return True


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
