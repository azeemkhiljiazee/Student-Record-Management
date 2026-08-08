from tkinter import *

students = {
    "101": ["Ali", "85"],
    "102": ["Ahmed", "90"],
    "103": ["Asad", "95"]
}

def search():
    roll = entry.get()

    if roll in students:
        name, marks = students[roll]
        output.config(
            text=f"Name : {name}\n\nRoll Number : {roll}\n\nMarks : {marks}",
            fg="green"
        )
    else:
        output.config(text="Student Record Not Found!", fg="red")

root = Tk()
root.title("Student Record Management System")
root.geometry("650x450")
root.configure(bg="#D6EAF8")

frame = Frame(root, bg="white", bd=3, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center", width=420, height=320)

Label(frame,
      text="Student Record Management System",
      font=("Arial", 18, "bold"),
      bg="white",
      fg="#0B5394").pack(pady=15)

Label(frame,
      text="Enter Roll Number",
      font=("Arial", 12),
      bg="white").pack()

entry = Entry(frame, font=("Arial", 13), width=22, justify="center")
entry.pack(pady=10)

Button(frame,
       text="Search",
       font=("Arial", 11, "bold"),
       bg="#0078D7",
       fg="white",
       width=15,
       command=search).pack(pady=10)

output = Label(frame,
               text="",
               font=("Arial", 12),
               bg="#F8F9F9",
               width=28,
               height=6,
               relief="solid",
               justify="left")
output.pack(pady=15)

root.mainloop()