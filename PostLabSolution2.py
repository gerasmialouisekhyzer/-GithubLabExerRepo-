"""
File: student.py
Based on Programming Exercise 1: Student class with comparison operators.
This script places several Student objects into a list, shuffles it,
then sorts it (relies on Student.__lt__) and displays information.
"""

import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        self.name = name
        self.scores = [0] * number

    def getName(self):
        return self.name

    def setScore(self, i, score):
        self.scores[i - 1] = score

    def getScore(self, i):
        return self.scores[i - 1]

    def getAverage(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

    def getHighScore(self):
        return max(self.scores) if self.scores else 0

    def __str__(self):
        return f"Name: {self.name} Scores: {' '.join(map(str, self.scores))}"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.name == other.name

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.name < other.name

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.name >= other.name


def main():
    students = [
        Student("Alice", 3),
        Student("Zoe", 2),
        Student("Bob", 4),
        Student("Charlie", 1),
        Student("Eve", 2)
    ]

    students[0].setScore(1, 85)
    students[0].setScore(2, 90)
    students[1].setScore(1, 75)
    students[2].setScore(1, 92)
    students[3].setScore(1, 60)
    students[4].setScore(1, 88)

    print("Before shuffle:")
    for s in students:
        print(s)
    print()

    random.shuffle(students)
    print("After shuffle:")
    for s in students:
        print(s)
    print()

    students.sort()
    print("After sort:")
    for s in students:
        print(s)


if __name__ == "__main__":
    main()