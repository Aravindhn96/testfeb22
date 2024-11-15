

# print("python batch 4")     #this line of code prints out python batch 4
# print("hello World")
# print("good morning")

# 1. Python runs the code line by line
# 2. python is case sensitive


# comments
# variable     - container for storing data values

# test = [1, 2, 3, 4, 5]
# test2 = "this is monday"
# test3 = (1, 2, 3, 4, 5)
# test4 = {"name" : "Ram", "age": 21, "DOB": 12}
# test5 = {1, 2, 4, 5, 6}
# test6 = frozenset([1,2, 4, 5, 6])
#
# A = 11j
# print("The value present inside the variable is : ", test)
# print(type(test))
# print(type(test2))
# print(type(test3))
# print(type(test6))

# type

# a-z , A-Z , underscore
# it cannot start with a number
# cannot be a inbuilt keyword of python

# DATA types
# 1. Numberic - int , float , complex
# 2. Sequence - strings [str], list, tuple
# 3. mapping - dict
# 4. set type  -  set , frozen set
# 5. boolean type -  True, False
# 6. None type - None

#operators
# 1. arithemetic operators - +, - , /, *
# 2. comparison operator -  ==
# 3. Assignment operator - =
# 4. Logical operator
# 5. identity operator
# 6. Membership operator

# if else
# if condition:
#     #block of code
# else:
#     #block of code


# for loop
# syntax
#
# for [item] in iterable:
#     #block of code
#             [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# while loop

# while condition:
#     # block of code

# i = 0
# while i <= 5:
#     print(i)
#     i += 1
#

# control statements
# break, continue

# i = 0
# while i< 4:
#     print(i)
#     i += 1

# string:
# methods:
test = "hello world"
# input = "hello world"
# output = "hello python"

# test = test.replace('w','p')
# print(test)

# # upper
# test = test.upper()
# print(test)
#
# test = test.lower()
# print(test)
#
#

# list
# # creating a list
# list = [1, 2, 3, 4, 5, 'r', 'word']
#
# # Accessing the elements
# print(list[0:3])
#
# #modify list
# # adding elements to a list
# # append
# list.append('hello')
# print(list)
#
# list.append('python')
# print(list)
# # extend
#
# list_1 = [1, 2, 3, 4, 5]
# list_2 = [6, 7, 8, 9, 10]
# print(list_1)
# print(list_2)
# list_1.extend(list_2)
# print(list_1)
#
# list_1.extend(['monday', 'tuesday'])
# print(list_1)
#
# # insert
# list_1.insert(10, 'day')
# print(list_1)
#
# # remove
# list_1.remove('day')
# list_1.remove('tuesday')
# print(list_1)
# # pop
# list_1.pop(10)
# print(list_1)
#
# list_1.pop()
# print(list_1)
# # del
# del list_1[2]
# print(list_1)
#
# # dictionaries
# # creating a dictionary
# test_1 = {'name' : 'ram', 'age':25, 'dob': 'december'}
#
# # access values
# value = test_1['age']
# print(value)
#
# # modify dictionary
# # adding
# test_1['place'] = 'bangalore'
# print(test_1)
#
# # remove
# del test_1['dob']
#
# print(test_1)
#
# value = test_1.pop('place')
# print(value)

# for loop
# test_1 = {'name': 'ram', 'age': 25, 'dob': 'december'}
#
# for i in test_1:
#     print(test_1[i])
# print('.................................')
# for k, v in test_1.items():
#     print(k, v)

# funtion


selenium

# selenium IDE
# Selenium RC
# Selenium webdriver
# selenium GRID

# Limitations of selenium
# 1. Selenium webdriver has no support to REST and SOAP platforms
# 2. No reporting capability
# 3. Imaging testing

# locator strategies
# locating a single element
# 1. id
# 2. name
# 3. class name
# 4. xpath
# 5.link_text
# 6.tag name
# 7.css selector
#
#
# driver.find_element(BY.ID, "fromCity").click()
# driver.find_element(BY.Name, "text")
# driver.find_element(BY.XPATH, "text")
#
#
# xpath
# absolute  : "/html/body/div/div/div.../input"
# relative  :   //tagname[@attribute="text/value"]

//input[@id = "username"]



#
#
#
# (//span[@class = "lbl_input appendBottom10"])[3]
#
# contains
#
# //*[contains(@attribute, "text/value")]
#
# //*[conatins(@@id, "fromCity")]
#
# //*[text()= "value"]
#
# //*[text()= "Departure"]
# //*[text()= "Departure"]
#
#
# //tagname[@attribute="text/value"] - attribute
# //*[contains(@attribute, "text/value")] - contains
# //*[text()= "Departure"] - text
#
#
# //input[@id, "fromCity"]
#
# css selector
#
# syntax
# tag name [attributr="text/value"]
#
# # - id
# . - class
#
#
#  input[@id ="fromCity"]
#
#  #fromCity
#
#  .fromCity
#
#
#  browser interactions
#
#  1. maximize_window()
#  2. driver.get("https://www.makemytrip.com/")
#  3. driver.title
#  4. driver.current_url
#  5. driver.refresh()
#  6. driver.back()
#  7. driver.forward()
#  8. driver.close()
#  9. driver.quit()



Drivers
Base
Logs
Screenshots
reports
source
 -> Login_page.py
 -> Flights.py
 -> Hotels.py

Tests
 ->test_login.py
 ->test_flights.py
 ->tests_hotels.py

Confest.py
utilities


Pytest
Naming convention

File name - test
Class name - Test



























