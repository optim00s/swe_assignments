class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Ad yalnız string olmalıdır.")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not (16 <= value <= 30):
            raise ValueError("Yaş 16 ilə 30 arasında olmalıdır.")
        self.__age = value

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, value):
        if not isinstance(value, list):
            raise TypeError("Qiymətlər list olmalıdır.")
        for g in value:
            if not (0 <= g <= 100):
                raise ValueError(f"Hər qiymət 0 ilə 100 arasında olmalıdır. Xətalı dəyər: {g}")
        self.__grades = value

    @property
    def average(self):
        return sum(self.__grades) / len(self.__grades)

    @property
    def status(self):
        if self.average >= 90:
            return "Excellent"
        elif self.average >= 75:
            return "Good"
        elif self.average >= 60:
            return "Normal"
        else:
            return "Fail"

    def info(self):
        print(f"{self.__name}, {self.__age}, {self.average:.1f}, {self.status}")


s = Student("Sharaf", 20, [95, 88, 92])
s.info()

s.grades = [70, 65, 68]
s.info()

s.grades = [50, 55, 48]
s.info()

