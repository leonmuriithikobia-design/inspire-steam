#Leon Kobia
#19/02/26
#Program on objects in python

class Human:
    #First we define the attributes of a human being
    type = "Mammal"
    legs = 2
    Brain = True
    Warm_blooded = True
    city = "Nairobi"

    #We then create a constructoe for the class project
    #The constructor will be used to create copies of this 
    def__init__(self, name, age):
        self.human_name = name
        self.human_age = age

    def tell_story(self):
        print(f"Hello, I am {self.human_name}. Here is a story")
        print("I once drove a car to Mombasa")
#Create the humans
Leon = Human("Leon", 19)
Ernest = Human("Ernest", 18)

#Let the humans created do things
Leon.tell_story()
print("Leon's age is:", leon.human_age)

#Modify one of the objects without modifying other objects
leon.city = "Kiambu"

print("leon's location:", leon.city)
print("Amani's location:",amani.city)