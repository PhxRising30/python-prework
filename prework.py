#Question One
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below:
#def hello_name(user_name):

#This one was a combination of Chapter 8 and Chapter 2 - I just figured out the plug in function of the 2nd chapter to the 8th chapter format.

def greet_user(user_name):
    user_name = "username"
    print("hello_ " + user_name.title().upper() + "!")

greet_user('username')



#Question Two
#Write a Python function, first_odds that prints the odd numbers from 1-100 and returns nothing. The first line of code has been defined as below:
#def first_odds():

def first_odds(current_number):
    current_number = 0
    while current_number < 100:
        current_number += 1
        if current_number % 2 == 0:
            continue

        print(current_number)

first_odds(0)

#Question Three
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of code has been defined as below:
#def max_num_in_list(a_list):

def max_num_in_list(a_list, a_number):
    print("\nI have a list of numbers consisting of " + a_list + ".")
    print("My max number is " + a_number + ".")

max_num_in_list('10,20,45,90' , '90')

#Question Four
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean type (true/false). Also the first line of code is defined below:
#def is_leap_year(a_year):

def is_leap_year(a_year) :
    a_year = 2020
    if((a_year % 400 == 0) or  
     (a_year % 100 != 0) and  
     (a_year % 4 == 0)):   
        print("True");  
    else:
        print("False")

is_leap_year(2020)

#Question Five
#Write a function to check to see if all numbers in list are consecutive numbers. For example [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean type. 

def is_consecutive(a_list):
    a_list = [11, 12, 13, 14, 15, 16, 17]
    sorted_list = sorted(a_list)

    range_list=list(range(min(a_list), max(a_list)+1))
    if sorted_list == range_list:
        print("True")
    else:
        print("False")


is_consecutive(a_list = [11, 12, 13, 14, 15, 16, 17])
