class Student:
    def __init__(self, dni, name, surnames, age, city, province, email):
        self.dni = dni
        self.name = name
        self.surnames = surnames
        self.age = age
        self.city = city
        self.province = province
        self.email = email
    
    # get methods --> query method
    # set methods --> actualization method
    
    def get_dni(self):
        return self.dni
    
    def set_dni(self, dni):
        self.dni = dni
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def get_surnames(self):
        return self.surnames
    
    def set_surnames(self, surnames):
        self.surnames = surnames
        
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
        
    def get_city(self):
        return self.city
    
    def set_city(self, city):
        self.city = city
        
    def get_province(self):
        return self.province
    
    def set_province(self, province):
        self.province = province
    
    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email