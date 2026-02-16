#Leon Kobia
#16/02/26
#Program to calculate factorials of numbers
number= int(input("Enter the number x :"))
factorial = 1 #Initialise factorial as 1
for x in range(1,number + 1):
    factorial = factorial * x
    

print(f"{number}!={factorial}")