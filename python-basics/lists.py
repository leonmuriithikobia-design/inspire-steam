#Leon Kobia
#18/02/26
#Program to show lists in python

friends = [ "Rachel", "Phoebe","Ross","Joey","Monica","Chandler",]

print(friends)
friends.sort()
print(friends)
friends.reverse()
print(friends)
friends.append("Jack")
print(friends)
new_friends = ["Tracy","James","Faith","Ernest","Benedict"]
print(len(new_friends))
#New list of students
students = friends + new_friends

print(students)
students.pop()
print(students)
students.insert(5,"Jenny")
print(students)
students.insert(9,"Valerie")
print(students)
students.extend("Dan")
print(students)
students.remove("Rachel")
print(students)
new_students = students.copy()
print(new_students)
