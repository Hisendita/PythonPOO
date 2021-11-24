from student import Student

class Controller:
    def __init__(self):
        self.students = {}
    
    def add_student(self, dni, name, surnames, age, city, province, email):
        s = Student(dni, name, surnames, age, city, province, email)
        
        if s.get_dni() in self.students:
            return False