#Sara Umer 1999495

#A variable like user_num can store a value like an integer. Extend the given program as indicated.

#Get a second user input into user_num1.
#Output the user's input. (2 pts)
#Output the input squared and cubed. Hint: Compute squared as user_num * user_num. (2 pts)
#Get a second user input into user_num2, and output the sum and product. (1 pt)

print("Enter integer:")

user_num = int(input())


print("You entered:",user_num)

print(user_num,"squared is",user_num*user_num)

print("And",user_num,"cubed is",user_num*user_num*user_num,"!!")

print("Enter another integer:")

user_num2 = int(input())

  
print(user_num,"+",user_num2,"is",user_num+user_num2)
print(user_num,"*",user_num2,"is",user_num*user_num2)


