import tkinter as tk
from tkinter import ttk

"""
class Budget:
    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses

    def __str__(self):
        return f"Monthly Income: {self.income}\nMonthly Expenses: {self.expenses}"

    def getIncome(self):
        return self.income
    def setIncome(self, i):
        self.income = i

    def getExpenses(self):
        return self.expenses
    def setExpenses(self, e):
        self.expenses = e
    
    def annual(self):
        return (int(self.income)*12 - int(self.expenses)*12)
"""
def gui():
    window = tk.Tk()
    window.title("BankForTheFuture")
    window.geometry("700x300")

    frame = tk.Frame(window, padx=20, pady=20)
    frame.pack()

    income_label = tk.Label(frame, text="Monthly Income:", anchor="center", font=("Arial", 15), justify="center")
    income_label.grid(row=0, column=0)

    income_entry = tk.Entry(frame, font=("Arial", 15))
    income_entry.grid(row=0, column=1)

    expenses_label = tk.Label(frame, text="Monthly Expenses:", font=("Arial", 15))
    expenses_label.grid(row=1, column=0)

    expenses_entry = tk.Entry(frame, font=("Arial", 15))
    expenses_entry.grid(row=1, column=1)

    enter_button = tk.Button(frame, text="Enter", font=("Arial", 15), command=enter)
    enter_button.grid(row=2, column=0, columnspan=2)

    result_label = tk.Label(frame, text="")
    result_label.grid(row=3, column=0, columnspan=2)

    window.mainloop()
    
    return
    
def enter():
    try:
        income = int(income_entry.get())
        expenses = int(expenses_entry.get())
        result_label.config(text="")

        b1 = Budget(income, expenses)

        print("Income: " + str(income) + "\nExpenses: " + str(expenses))
        print("Net Annual Income: $" + str(b1.annual()))
    except ValueError:
        income_entry.delete(0, tk.END)
        expenses_entry.delete(0, tk.END)
        result_label.config(text="Invalid credentials", fg="red")


