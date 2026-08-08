# Student Record Management System

students = [
    ["Ali", "101", "85"],
    ["Ahmed", "102", "90"],
    ["Asad", "103", "95"]
]

while True:
    print("\n===== Student Record Management System =====")
    print("Available Roll Numbers")
    print("101")
    print("102")
    print("103")
    print("0. Exit")

    roll = input("\nEnter Roll Number: ")

    if roll == "101":
        print("\nStudent Record")
        print("Name:", students[0][0])
        print("Roll Number:", students[0][1])
        print("Marks:", students[0][2])

    elif roll == "102":
        print("\nStudent Record")
        print("Name:", students[1][0])
        print("Roll Number:", students[1][1])
        print("Marks:", students[1][2])

    elif roll == "103":
        print("\nStudent Record")
        print("Name:", students[2][0])
        print("Roll Number:", students[2][1])
        print("Marks:", students[2][2])

    elif roll == "104":
        print("invalid roll number.")
        break

    else:
        print("program ended")