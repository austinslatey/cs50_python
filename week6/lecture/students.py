# from csv import DictReader

# students = []


#with open("students.csv") as file:
    #reader = DictReader(file)
    #for row in reader:
        #students.append({"name": row["name"], "home"})


#for students in sorted(students, key=lambda student: student["name"]):
    #print(f"{student['name']} is in {student['house']}")

from csv import DictWriter

name = input("Your name what? ")
home = input("Your home where? ")

with open("students.csv", "a") as file:
    writer = DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name": name, "home": home})
