from .StudentBuilder import StudentBuilder

class EngineeringStudentBuilder(StudentBuilder):
    def set_subjects(self):
        self.subjects = ["DSA", "OS", "CN"]
        return self
