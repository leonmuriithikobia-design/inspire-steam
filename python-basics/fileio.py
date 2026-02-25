#Leon Kobia
#24/02/26
#Program to run file operations

#Create new file
new_file = open("Student_data.txt","r+")

#Write new file
new_file.write("{Student Name : Leon Kobia, ID : 23397143, email : kobialeo@live.com}")
new_file.close()

#Read data from the file
new_file = open("Student_data.txt")
data = new_file.read()

print(data)

new_file.close()

#delete file
#Use OS module
import os
os.remove("remove.txt")
#Delete folder
os.rmdir("folder")