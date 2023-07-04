#Sara Umer 1999495
import math 
import datetime

#This is for the current date of user 


print("Birthday Calculator")
print("Current Day")


print("Month:")
current_month = int(input())
    

print("Day:")
current_day = int(input())

print("Year")
current_year = int(input())



#This is for user's birthday
print("Birthday")

print("Month:")
user_month = int(input())

print("Day:")
user_day = int(input())
print("Year:")
user_year = int(input())

#make separate block for current date and user birthday

#date_current = {
    #current_month:int(input()),
    #current_day:int(input()),
    #current_year:int(input()),
    
#}

#user_birthday = { 
    #user_month:int(input()),
    #user_day:int(input()),
    #user_year:int(input()),

#}

#Calculate Age of User
print("You are",current_year-user_year,"years old.") 
