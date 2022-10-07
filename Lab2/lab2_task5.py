class Student:

    def __init__(self, name: str, surname: str, recordbook_num: int, **kwargs):
        self.name = name
        self.surname = surname
        self.recordbook_num = recordbook_num
        self.grades = kwargs

    def __str__(self):
        return f"\n{self.name} {self.surname}:\
                \nRecord book number: {self.recordbook_num}\
                \nSubjects: {'; '.join(map(str, self.grades))}\
                \nGrades: {'; '.join(map(str, self.grades.values()))}\
                \nAverage score: {self.average} \n"

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.surname == other.surname

    def __lt__(self, other) -> bool:
        return self.average < other.average

    def __gt__(self, other) -> bool:
        return self.average > other.average

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Not String")
        if not name:
            raise ValueError("Empty name")
        self.__name = name

    @property
    def recordbook_num(self):
        return self.__recordbook_num

    @recordbook_num.setter
    def recordbook_num(self, recordbook_num):
        if not isinstance(recordbook_num, int):
            raise TypeError("Not String")
        if not recordbook_num:
            raise ValueError("No record book number")
        self.__recordbook_num = recordbook_num

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        if not all(isinstance(v, int) for v in grades.values()) or not all(2 <= v <= 5 for v in grades.values()):
            raise TypeError("Wrong grade type")
        self.__grades = grades

    @property
    def average(self):
        return sum(self.grades.values())/len(self.grades)


class Group:

    def __init__(self, *args: Student):
        self.__students = []
        for student in args:
            self.add_student(student)

    @property
    def students(self):
        return self.__students

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Not Student")
        if self.__exists(student) or not len(self.__students) < 20:
            raise ValueError("Value Error")
        self.__students += [student]

    def __exists(self, student: Student) -> bool:
        if student in self.__students:
            return True
        return False

    def best_five(self) -> list:
        return sorted(self.__students, reverse=True)[:5]


st1 = Student("Oleksandr", "Kalenskyi", 100, Math=5, History=2)
st2 = Student("Nazar", "Dom", 99, Math=3, History=2)
group1 = Group(st1, st2)
st3 = Student("Egor", "Ohtyrka", 101, Math=2, History=5)
group1.add_student(st3)
print("".join(map(str, group1.best_five())))
