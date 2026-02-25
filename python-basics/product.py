import tkinter as tk
from tkinter import ttk, messagebox

# --- Main Window ---
root = tk.Tk()
root.title("School Management System")
root.geometry("750x400")

# --- Storage ---
students = []

# --- Input Fields ---
tk.Label(root, text="Student ID").grid(row=0, column=0, padx=10, pady=5)
student_id_entry = tk.Entry(root)
student_id_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="First Name").grid(row=1, column=0, padx=10, pady=5)
first_name_entry = tk.Entry(root)
first_name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Last Name").grid(row=2, column=0, padx=10, pady=5)
last_name_entry = tk.Entry(root)
last_name_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Courses").grid(row=3, column=0, padx=10, pady=5)
courses_entry = tk.Entry(root)
courses_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Phone Number").grid(row=4, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=4, column=1, padx=10, pady=5)

# --- Treeview Table ---
columns = ("ID", "First Name", "Last Name", "Courses", "Phone")
student_table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    student_table.heading(col, text=col)
    student_table.column(col, width=120)

student_table.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

# --- Functions ---
def add_student():
    student = {
        "ID": student_id_entry.get(),
        "First Name": first_name_entry.get(),
        "Last Name": last_name_entry.get(),
        "Courses": courses_entry.get(),
        "Phone": phone_entry.get()
    }
    
    if not all(student.values()):
        messagebox.showwarning("Input Error", "Please fill all fields")
        return
    
    students.append(student)
    student_table.insert("", tk.END, values=(student["ID"], student["First Name"], student["Last Name"], student["Courses"], student["Phone"]))
    
    # Clear fields
    student_id_entry.delete(0, tk.END)
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    courses_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

def export_students():
    if not students:
        messagebox.showwarning("No Data", "No students to export")
        return
    
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"ID: {s['ID']}, Name: {s['First Name']} {s['Last Name']}, Courses: {s['Courses']}, Phone: {s['Phone']}\n")
    
    messagebox.showinfo("Exported", "Students exported to students.txt")

def delete_student():
    selected_item = student_table.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a student to delete")
        return
    
    values = student_table.item(selected_item, "values")
    student_id = values[0]
    
    # Remove from list
    for s in students:
        if s["ID"] == student_id:
            students.remove(s)
            break
    
    # Remove from table
    student_table.delete(selected_item)
    messagebox.showinfo("Deleted", f"Student {student_id} removed successfully")

# --- Buttons ---
add_button = tk.Button(root, text="Add Student", command=add_student)
add_button.grid(row=5, column=0, padx=10, pady=10)

export_button = tk.Button(root, text="Export Students", command=export_students)
export_button.grid(row=5, column=1, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Student", command=delete_student)
delete_button.grid(row=5, column=2, padx=10, pady=10)

# --- Run App ---
root.mainloop()