class Course:
    def __init__(self, name, grade, updateDate, assignments) -> None:
        self.name = name
        self.grade = grade
        self.updateDate = updateDate
        self.assignments = assignments

    def __str__(self) -> str:
        return f"Name: {self.name} Grade: {self.grade} Weight: {self.weight} Credits: {self.credits}"

    def getAssignments(self):
        return self.assignments