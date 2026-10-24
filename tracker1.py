import tkinter as tk
from tkinter import messagebox

# Store expense details in lists
expense_names = []
expense_amounts = []


# Function to add an expense
def add_expense():
    name = name_entry.get().strip()
    amount = amount_entry.get().strip()

    # Validate input
    if not name or not amount:
        messagebox.showerror(
            "Input Error",
            "Please enter both expense name and amount."
        )
        return

    try:
        amount = float(amount)

        if amount <= 0:
            messagebox.showerror(
                "Input Error",
                "Amount must be greater than zero."
            )
            return

        # Store data in lists
        expense_names.append(name)
        expense_amounts.append(amount)

        # Display expense in Listbox
        expense_listbox.insert(
            tk.END,
            f"{name} - Rs. {amount:.2f}"
        )

        # Update total
        update_total()

        # Clear input fields
        name_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter a valid numeric amount."
        )


# Function to calculate total expenses
def update_total():
    total = sum(expense_amounts)
    total_label.config(
        text=f"Total Expenses: Rs. {total:.2f}"
    )


# Function to delete selected expense
def delete_expense():
    try:
        selected_index = expense_listbox.curselection()

        if not selected_index:
            messagebox.showwarning(
                "Selection Error",
                "Please select an expense to delete."
            )
            return

        index = selected_index[0]

        # Remove from lists and Listbox
        expense_names.pop(index)
        expense_amounts.pop(index)
        expense_listbox.delete(index)

        # Update total
        update_total()

    except (IndexError, tk.TclError):
        messagebox.showerror(
            "Error",
            "Unable to delete the selected expense."
        )


# Function to clear all expenses
def clear_expenses():
    if not expense_names:
        messagebox.showinfo(
            "Information",
            "There are no expenses to clear."
        )
        return

    confirm = messagebox.askyesno(
        "Confirm",
        "Are you sure you want to clear all expenses?"
    )

    if confirm:
        expense_names.clear()
        expense_amounts.clear()
        expense_listbox.delete(0, tk.END)
        update_total()


# Main window
root = tk.Tk()
root.title("Daily Expense Tracker")
root.geometry("450x520")
root.resizable(False, False)

# Heading
heading = tk.Label(
    root,
    text="DAILY EXPENSE TRACKER",
    font=("Arial", 18, "bold")
)
heading.pack(pady=15)

# Expense name
tk.Label(
    root,
    text="Expense Name:",
    font=("Arial", 11)
).pack()

name_entry = tk.Entry(root, width=35, font=("Arial", 11))
name_entry.pack(pady=5)

# Expense amount
tk.Label(
    root,
    text="Amount (Rs.):",
    font=("Arial", 11)
).pack()

amount_entry = tk.Entry(root, width=35, font=("Arial", 11))
amount_entry.pack(pady=5)

# Add button
add_button = tk.Button(
    root,
    text="Add Expense",
    command=add_expense,
    width=18,
    bg="green",
    fg="white"
)
add_button.pack(pady=10)

# Expense list
tk.Label(
    root,
    text="Your Expenses:",
    font=("Arial", 12, "bold")
).pack(pady=5)

expense_listbox = tk.Listbox(
    root,
    width=42,
    height=10,
    font=("Arial", 10)
)
expense_listbox.pack(pady=5)

# Total expense
total_label = tk.Label(
    root,
    text="Total Expenses: Rs. 0.00",
    font=("Arial", 13, "bold"),
    fg="blue"
)
total_label.pack(pady=10)

# Delete button
delete_button = tk.Button(
    root,
    text="Delete Selected",
    command=delete_expense,
    width=18
)
delete_button.pack(pady=3)

# Clear all button
clear_button = tk.Button(
    root,
    text="Clear All Expenses",
    command=clear_expenses,
    width=18
)
clear_button.pack(pady=3)

# Run the application
root.mainloop()