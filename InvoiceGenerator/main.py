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
root.geometry("550x310")
root.title("Invoice Generator")
root.resizable(False, False)

container = tk.Frame(root)
container.pack(expand=True, fill="both", padx=20)

row_1 = tk.Frame(container)
row_1.grid(row=0, column=0, pady=10)

tk.Label(row_1, text="Invoice Number").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(row_1, width=15).grid(row=1, column=0, padx=5, pady=5, sticky="n")

tk.Label(row_1, text="Client Information").grid(row=0, column=1, padx=5, pady=5)
tk.Text(row_1, width=15, height=5).grid(row=1, column=1, padx=5, pady=5)

row_2 = tk.Frame(container)
row_2.grid(row=1, column=0, pady=10)


tk.Label(row_2, text="Item").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(row_2, width=30).grid(row=1, column=0, padx=5, pady=5)

tk.Label(row_2, text="Rate").grid(row=0, column=1, padx=5, pady=5)
tk.Entry(row_2, width=15).grid(row=1, column=1, padx=5, pady=5)

tk.Label(row_2, text="Quantity").grid(row=0, column=2, padx=5, pady=5)
tk.Entry(row_2, width=10).grid(row=1, column=2, padx=5, pady=5)

tk.Label(row_2, text="Amount").grid(row=0, column=3, padx=5, pady=5)
tk.Entry(row_2, width=20).grid(row=1, column=3, padx=5, pady=5)

confirmation_button = tk.Button(container, text="Generate", command=lambda: None)
confirmation_button.grid(row=2, column=0, columnspan=2, pady=20)


root.mainloop()
