"""
--- Day 2: Red-Nosed Reports ---
Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?

Your puzzle answer was 472.

--- Part Two ---
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?

Your puzzle answer was 520.

Both parts of this puzzle are complete! They provide two gold stars: **

"""
from typing import List

class Day2:
    def __init__(self, input_file: str):
        self.input_file = input_file

    def read_input(self) -> List[List[int]]:
        """
        Reads input data and parses into a list of lists of integers.
        """
        try:
            with open(self.input_file) as file:
                return [list(map(int, line.strip().split())) for line in file]
        except FileNotFoundError:
            raise Exception(f"File {self.input_file} not found.")
        except ValueError:
            raise Exception(f"File {self.input_file} contains invalid data.")


    def is_safe_report(self, report: List[int]) -> bool:
        """
        Checks if a report satisfies the safety conditions:
        1. All levels are either increasing or decreasing.
        2. All adjacent levels are either increasing or decreasing.
        """
        # Compute differences between adjacent levels
        differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

        # Check if all differences are within the allowed range
        if not all(1 <= abs(diff) <= 3 for diff in differences):
            return False

        # Check if all differences are positive (increasing) or all negative (decreasing)
        all_increasing = all(diff > 0 for diff in differences)
        all_decreasing = all(diff < 0 for diff in differences)

        return all_increasing or all_decreasing

    def problem_dampener(self, report):
        """
        Check if the report satisfies the safety conditions,
        allowing the removal of a single level if needed
        """
        # If the report is already safe
        if self.is_safe_report(report):
            return True

        # Check by removing a level... The bruteforce way!
        for i in range(len(report)):
            if self.is_safe_report(report[:i] + report[i + 1:]):
                return True

        return False

    def problem1(self) -> int:
        """
        Counts the number of safe reports in the input data.
        """
        reports = self.read_input()
        safe_count = sum(1 for report in reports if self.is_safe_report(report))

        return safe_count

    def problem2(self) -> int:
        """
        Counts the number of safe reports, considering the ability to remove one level.
        """
        reports = self.read_input()
        safe_count = sum(1 for report in reports if self.problem_dampener(report))

        return safe_count

    def run(self):
        """
        Runs both problems sequentially.
        """
        print("Solving Problem 1...")
        print(f"Number of safe reports: {self.problem1()}")

        print("\nSolving Problem 2...")
        print(f"Number of safe reports: {self.problem2()}")

if __name__ == '__main__':
    app = Day2("input_day2.txt")
    app.run()
