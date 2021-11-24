from invoice import Invoice

class Controller:
    def __init__(self):
        self.invoices = []
        self.hidden_invoice_data = []
        
    def add_invoice(self, nif, base):
        inv = Invoice(nif, base)
        
        for e in self.invoices:
            if inv.get_nif() == e:
                return False

        temp_tuple = (inv.get_id(), inv.get_nif(), inv.get_date(), inv.get_total())
        hidden_temp_tuple = (inv.get_id(), inv.get_nif(), inv.get_base(), inv.get_vat(), inv.get_total(), inv.get_date(), inv.get_status())
        
        self.invoices.append(temp_tuple)
        self.hidden_invoice_data.append(hidden_temp_tuple)
        return True
    
    def list_unpaid_invoices(self, nif):
        f = False
        f2 = False
        list_unpaid_invoices = []
        for elements in self.hidden_invoice_data:
            for e in elements:
                if e == nif:
                    f = True
                if e == False:
                    f2 = True
                    
        if f == True and f2 == True:
            for elements in self.invoices:
                for e in elements:
                    list_unpaid_invoices.append(e)
            return list_unpaid_invoices
        
        return False
    
    def list_paid_invoices(self, nif):
        f = False
        f2 = False
        list_unpaid_invoices = []
        for elements in self.hidden_invoice_data:
            for e in elements:
                if e == nif:
                    f = True
                if e == True:
                    f2 = True
                    
        if f == True and f2 == True:
            for elements in self.invoices:
                for e in elements:
                    list_unpaid_invoices.append(e)
            return list_unpaid_invoices
        
        return False
    """
    def pay_invoice(self, nif):
        f = False
        f2 = False
        for elements in self.hidden_invoice_data:
            for e in elements:
                if e == nif:
                    f = True
                if e == False:
                    f2 = True
                    
        if f == True and f2 == True:
    """        

    def check_nif(self, nif):
        letters = "TRWAGMYFPDXBNJZSQVHLCKE"
        numbers = "1234567890"
        
        if len(nif) == 9:
            letter = nif[8].upper()
            l = nif[:8]
            if len(l) == len([n for n in l if n in numbers]):
                if letters[int(l)%23] == letter:
                    return True
        return False