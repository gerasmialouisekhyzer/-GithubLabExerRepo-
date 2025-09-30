"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = [0] * number

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score (safe if zero scores)."""
        return sum(self.scores) / len(self.scores) if self.scores else 0

    def getHighScore(self):
        """Returns the highest score (safe if no scores)."""
        return max(self.scores) if self.scores else 0

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.scores))

    def __eq__(self, other):
        """Return True if two students have the same name."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.name == other.name

    def __lt__(self, other):
        """Return True if this student's name is lexicographically less than the other's."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.name < other.name

    def __ge__(self, other):
        """Return True if this student's name is lexicographically greater than or equal to the other's."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.name >= other.name


def main():
    """Test the comparison operators between Student objects."""
    a = Student("Alice", 3)
    b = Student("Bob", 2)
    c = Student("Alice", 1)  

    print(a) 
    print(b) 
    print(c) 
    print()

    print(f"{a.getName()} == {b.getName()} -> {a == b}")
    print(f"{a.getName()} == {c.getName()} -> {a == c}")

    # Test less than
    print(f"{a.getName()} < {b.getName()} -> {a < b}")
    print(f"{b.getName()} < {a.getName()} -> {b < a}")

    # Test greater than or equal
    print(f"{a.getName()} >= {b.getName()} -> {a >= b}")
    print(f"{a.getName()} >= {c.getName()} -> {a >= c}")


if __name__ == "__main__":
    main()