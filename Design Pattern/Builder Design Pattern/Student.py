
class Student:
    def __init__(self, builder):
        self.roll_number = builder.roll_number
        self.age = builder.age
        self.name = builder.name
        self.father_name = builder.father_name
        self.mother_name = builder.mother_name
        self.subjects = builder.subjects

    def __str__(self):
        return f"roll number: {self.roll_number} age: {self.age} name: {self.name} father name: {self.father_name} mother name: {self.mother_name} subjects: {', '.join(self.subjects)}"