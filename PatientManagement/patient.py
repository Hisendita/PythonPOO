class Patient:
    def __init__(self, nif, name, surname, yob, telf, mail):
        self.nif = nif
        self.name = name
        self.surname = surname
        self.yob = yob
        self.telf = telf
        self.mail = mail
        self.hov = []
        self.nov = 0
    
    def get_nif(self):
        return self.nif
    
    def get_name(self):
        return self.name
    
    def get_surname(self):
        return self.surname
    
    def get_yob(self):
        return self.yob
    
    def get_telf(self):
        return self.telf
    
    def get_mail(self):
        return self.mail
    
    def get_hov(self):
        return self.hov
    
    def get_nov(self):
        return self.nov
    
    def set_hov(self, hov):
        self.hov = hov
    
    def set_nov(self, nov):
        self.nov = nov
    
    def __repr__(self):
        return "<nif:"+self.get_nif()+">"+"<name:"+self.get_name()+">"+"<surname:"+self.get_surname()+">"+"<year_of_birth:"+str(self.get_yob())+">"+"<phone:"+str(self.get_telf())+">"+"<mail:"+self.get_mail()+">"+"<number_of_visits:"+str(self.get_nov())+">"+"<history_of_visits:"+str(self.get_hov())+">"