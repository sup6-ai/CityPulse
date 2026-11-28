#dictionary inside dictionary

students = {
    "student1": {
        "name": "Supriya",
        "age": 19
    },
    "student2": {
        "name": "Shiva",
        "age": 20
    }
}
print(students)
print(students["student1"]["name"]) 

#lists
hobbies = ["Reading", "Dancing", "Singing", "Painting"]
hobbies.append("Photography")
hobbies.remove("Dancing")
print("My hobbies:", hobbies)


#tuples
student = ("Supriya", 19, "Engineering")
print(student)
print("Index:", student.index(19))
print("Count:", student.count("Supriya"))

#set
skills = {"Python", "Java", "SQL", "Python"}
skills.add("HTML")
print("My skills:", skills)
