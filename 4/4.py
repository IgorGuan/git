class Student:
    def __init__(self, name, age, class_id, average_score):
        self.name = name
        self.age = age
        self.class_id = class_id
        self.average_score = average_score

    def display_info(self):
        """Output personal information: name and age."""
        return f"Name: {self.name}, Age: {self.age}"

    def scholarship_amount(self):
        """Calculate scholarship amount based on average score."""
        if self.average_score == 5:
            return 6000
        elif self.average_score < 5:
            return 4000
        else:
            return 0

    def compare_scholarship(self, other):
        """Compare scholarship amount with another student."""
        return "greater than" if self.scholarship_amount() > other.scholarship_amount() else "less than"

class GraduateStudent(Student):
    def __init__(self, name, age, class_id, average_score, research_work):
        super().__init__(name, age, class_id, average_score)
        self.research_work = research_work

    def scholarship_amount(self):
        """Calculate scholarship amount based on average score for graduate students."""
        if self.average_score == 5:
            return 8000
        elif self.average_score < 5:
            return 6000
        else:
            return 0

# Example usage
if __name__ == "__main__":
    student1 = Student("Alice", 20, "CS101", 4.5)
    grad_student1 = GraduateStudent("Bob", 24, "CS102", 5, "AI Research")

    print(student1.display_info())
    print(f"Student Scholarship: {student1.scholarship_amount()}")

    print(grad_student1.display_info())
    print(f"Graduate Student Scholarship: {grad_student1.scholarship_amount()}")

    comparison = student1.compare_scholarship(grad_student1)
    print(f"Student's scholarship is {comparison} Graduate Student's scholarship.")
