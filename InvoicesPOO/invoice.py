import itertools, datetime
"""
Logic behind the invoice class:

    · The ID will be automatically incrementated when a new invoice is
    created
    
    · The date will be automatically set according to the current timestamp
    in dd-m-yy format
    
    · The vat will be set to a 21%
    
    · The "paid" state will be False because when created it cannot
    be paid at the same moment since we will be using a method to pay
    them
    
"""

class Invoice:
    id_iterator = itertools.count()
    
    def __init__(self, nif, base):
        self.id = next(Invoice.id_iterator)
        self.date = datetime.datetime.today().strftime("%d-%b-%y")
        self.nif = nif
        self.base = base
        self.vat = 0.21
        
        self.status = False
    
    def get_id(self):
        return self.id
    
    def get_date(self):
        return self.date
    
    def get_nif(self):
        return self.nif
    
    def get_base(self):
        return self.base
    
    def get_vat(self):
        return self.vat
    
    def get_status(self):
        return self.status
    
    def get_total(self):
        return self.get_base() * self.get_vat()
    
    def set_status(self, status):
        self.status = status