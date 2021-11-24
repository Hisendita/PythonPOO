from invoice import Invoice
from controller import Controller

c = Controller()
invoices_data_list = []

while True:
    print("1.- Add invoice.")
    print("2.- List unpaid invoices.")
    print("3.- List paid invoices.")
    print("4.- Pay invoice")
    print("5.- Exit")
    
    opc = int(input("Select option:"))
    
    if opc == 5:
        break
    
    if opc == 1:
        while True:
            nif = input("Input NIF: ")
            if c.check_nif(nif) == True:
                break
        
        base = float(input("Input price: "))
        if c.add_invoice(nif, base) == True:
            c.add_invoice(nif, base)
        
    if opc == 2:
        c.add_invoice("20868740N", 100)
        print(c.list_unpaid_invoices("20868740N"))




