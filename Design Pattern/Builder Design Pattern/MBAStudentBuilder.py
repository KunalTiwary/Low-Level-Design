from .StudentBuilder import StudentBuilder

class MBAStudentBuilder(StudentBuilder):
    def set_subjects(self):
        self.subjects = ["Micro Economics", "Business Studies", "Operations Management"]
        return self
