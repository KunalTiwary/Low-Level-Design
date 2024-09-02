from .Director import Director
from .EngineeringDesignBuilder import EngineeringStudentBuilder
from .MBAStudentBuilder import MBAStudentBuilder



director_obj1 = Director(EngineeringStudentBuilder())
director_obj2 = Director(MBAStudentBuilder())

engineer_student = director_obj1.create_student()
mba_student = director_obj2.create_student()

print(engineer_student)
print(mba_student)
