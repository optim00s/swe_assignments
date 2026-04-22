from datetime import date

class Person:
    def __init__(self, name, surname, age, address):
        self.name = name
        self.surname = surname
        self.__age = age
        self.__address = address
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
    
    def info(self):
        birthyear = date.today().year - self.__age
        print(f"{self.name}, {self.surname}, {self.__age}, {birthyear}, {self.__address}")

person_1 = Person("Sharaf", "Feyzullayev", 23, "Hazi Aslanov")
person_1.info()

print("-" * 50)

class Employee:
    def __init__(self, salary, mkr_score, name):
        self.salary = salary
        self.__mkr_score = mkr_score
        self.name = name
    
    @property
    def mkr_score(self):
        return self.mkr_score
    
    @mkr_score.setter
    def mkr_score(self, value):
        if 1000 <= value <= 2000:
            self.salary -= self.salary * 0.4
        elif 2000 <= value <= 5000:
            self.salary -= self.salary * 0.25
        elif 5000 <= value:
            self.salary -= self.salary * 0.15
    
    def info(self):
        print(f"{self.name}, {self.__mkr_score}, {self.salary}")
    
employee_1 = Employee(30000, 2780, "Teor")
employee_1.mkr_score = 5000
employee_1.info()
        
      
        
        
        
        
        
        