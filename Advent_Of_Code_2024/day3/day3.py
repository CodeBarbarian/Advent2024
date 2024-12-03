"""
--- Day 3: Mull It Over ---
"Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The Historians head out to take a look.

The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"

The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!

It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?

Your puzzle answer was 173731097.

--- Part Two ---
As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?

Your puzzle answer was 93729253.
"""

import re


class Day3:
    def __init__(self, input_file):
        self.input_file = input_file

    def load(self):
        """Loads the file content as a list of lines."""
        with open(self.input_file) as file:
            lines = file.readlines()
        return lines

    def problem1(self):
        """Finds and processes `mul(number, number)` patterns."""
        pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

        # Load data from the file
        data = self.load()

        # Collect all matches from all lines
        matches = []
        for line in data:
            matches.extend(re.findall(pattern, line))

        # Convert matches into a list of lists of integers
        params = [[int(num1), int(num2)] for num1, num2 in matches]

        total = 0
        for item in params:
            total += item[0] * item[1]

        print(total)

    def problem2(self):
        """Handles `do()` and `don't()` instructions to enable or disable `mul()`."""
        # Regex patterns
        mul_pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
        dont_pattern = r"don't\(\)"
        do_pattern = r"do\(\)"
        combined_pattern = f"{dont_pattern}|{do_pattern}|{mul_pattern}"

        # Load data from the file
        data = self.load()

        # Initialize state
        calculate = True
        total = 0

        for line in data:
            # Find all matches for the combined pattern
            matches = re.finditer(combined_pattern, line)

            for match in matches:
                if match.group().startswith("don't()"):
                    calculate = False
                elif match.group().startswith("do()"):
                    calculate = True
                elif match.group().startswith("mul"):
                    if calculate:
                        num1, num2 = map(int, match.groups()[:2])
                        total += num1 * num2

        print(f"Total for Problem 2: {total}")

    def run(self):
        """Runs the problem solutions."""
        self.problem1()
        self.problem2()


if __name__ == '__main__':
    app = Day3("input_day3.txt")
    app.run()
