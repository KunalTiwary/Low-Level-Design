from .StudentBuilder import StudentBuilder
from .EngineeringDesignBuilder import EngineeringStudentBuilder
from .MBAStudentBuilder import MBAStudentBuilder


class Director:
    def __init__(self, student_builder: StudentBuilder):
        self.student_builder = student_builder

    def create_student(self):
        if isinstance(self.student_builder, EngineeringStudentBuilder):
            return self.create_engineering_student()
        elif isinstance(self.student_builder, MBAStudentBuilder):
            return self.create_mba_student()
        return None

    def create_engineering_student(self):
        return self.student_builder.set_roll_number(1).set_age(22).set_name("sj").set_subjects().build()

    def create_mba_student(self):
        return self.student_builder.set_roll_number(2).set_age(24).set_name("sj").set_father_name("MyFatherName").set_mother_name("MyMotherName").set_subjects().build()