#Name : Leon Kobia
#Date : 13/02/26
#Program to calculate arithmetic progression

#Calculating nth term

a = int(input("Enter the first number :"))
n = int(input("Enter the number of terms :"))
d = int(input("Enter the common difference :"))

nth_term = a + (n -1) * d
print(f"The nth term is : {nth_term}")

sn = (n / 2) * (2 * a + (n-1) * d)
print(f"The sum of the first 10 terms is {sn}")


