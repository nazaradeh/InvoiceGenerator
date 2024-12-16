import tkinter as tk

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

root = tk.Tk()
root.geometry("600x500")
root.title("Invoice Generator")

tk.Label(root, text="Invoice Number").grid(row=0, column=0, pady=5)
tk.Entry(root, width=15).grid(row=1, column=0, pady=5)

tk.Label(root, text="Client Information").grid(row=0, column=1, pady=5)
tk.Text(root, width=15, height=5).grid(row=1, column=1, pady=5)

tk.Label(root, text="Item").grid(row=2, column=0, pady=5)
tk.Entry(root, width=30).grid(row=3, column=0, pady=5)

tk.Label(root, text="Rate").grid(row=2, column=1, pady=5)
tk.Entry(root, width=15).grid(row=3, column=1, pady=5)

tk.Label(root, text="Quantity").grid(row=2, column=2, pady=5)
tk.Entry(root, width=10).grid(row=3, column=2, pady=5)

tk.Label(root, text="Amount").grid(row=2, column=3, pady=5)
tk.Entry(root, width=20).grid(row=3, column=3, pady=5)

confirmation_button = tk.Button(root, text="Generate", command=lambda: None)
confirmation_button.grid(row=4, column=0, columnspan=2, pady=20)


root.mainloop()
