invoice_number = "WXYZ-001"
invoice_file_name = "AryoNazaradeh_Invoice_" + invoice_number
client_name = ""
client_address_line_one = ""
client_address_line_two = ""
client_address_line_three = ""
client_address_line_four = ""
table_of_items = []

def add_row():
    item = input("Enter item 1: ")
    rate = input("Enter rate 1: ")
    quantity = input("Enter quantity 1: ")
    amount = input("Enter amount 1: ")
    table_of_items.append([item, rate, quantity, amount])

input()
