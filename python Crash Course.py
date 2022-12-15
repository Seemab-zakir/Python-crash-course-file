#!/usr/bin/env python
# coding: utf-8

# # If else statments

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
 print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
 print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
 print("Adding extra cheese.")

print("\nFinished making your pizza!")

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
 if name in friends:
    print(" Hi " + name.title() +
          ", I see your favorite language is " + favorite_languages[name].title() + "!")


# # A List of Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}



alien_list=[alien_0,alien_1,alien_2]
for alien_lists in alien_list:
    print(alien_lists)


aliens=[]
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
 
# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
    print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

    


#example 2

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
 
# Show the first 5 aliens:
for alien in aliens[0:5]:
    print(alien)
    print("...")


# In[21]:


# Store information about a pizza being ordered.
pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese'],
 }

# Summarize the order.
print("You ordered a " + pizza['crust'] + "crust pizza " +
 "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)


# In[ ]:


favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


# # A Dictionary in a Dictionary
# 

# In[20]:


users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


# # User Input and while Loops

# In[20]:


n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    


# # Flag

# In[ ]:


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
 message = input(prompt)
if message == 'quit':
 active = False
else:
 print(message)


# # Using continue in a Loop

# In[19]:


current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
print(current_number)


# # Avoiding Infinite Loops

# In[6]:


x = 1
while x <= 5:
   print(x)
   x += 1


# # Using a while Loop with Lists and Dictionaries 

# In[8]:


# Start with users that need to be verified, 

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    # Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# # Removing All Instances of Specific Values from a List

# In[9]:


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
 
 print(pets)


# # Filling a Dictionary with User Input

# In[30]:


responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
 # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
 
 # Store the response in the dictionary:
    responses[name] = response
 
 # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
 
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")


# # functions

# In[35]:


def greet_user():
    print("Hello!")
greet_user()


# # Passing Information to a Function 

# In[33]:


def greet_user(username):
 """Display a simple greeting."""
 print("Hello, " + username.title() + "!")

greet_user("jessie")


# # Arguments and Parameters

# The variable username in the definition of greet_user() is an example of a 
# parameter, a piece of information the function needs to do its job. The value 
# 'jesse' in greet_user('jesse') is an example of an argument.

# In[37]:


def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
 
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
#Keyword Arguments
describe_pet(animal_type='hamster', pet_name='harry')



# In[39]:


def describe_pet(pet_name, animal_type='dog'):#Default Values
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('willie')
#describe_pet('willie')


# # Avoiding Argument Errors

# In[20]:


def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet()


# # Return Values

# In[21]:


def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# # Making an Argument Optional

# In[41]:


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


# 
# # #Mid Term Exam Solution
# 

# In[32]:


#Q1 
num=6
for i in range(num+1):
    for j in range(i):
        print(i,end=' ')
    print("")


# Q#2

# In[1]:


num = float(input("Input a number: "))
if num > 0:
   print("It is positive number")
elif num == 0:
   print("It is Zero")
else:
   print("It is a negative number")


# In[8]:


#Q3
num = int(input("Input a number: "))
sum_num = (num * (num + 1)) / 2
print("Sum of the first", num ," integers is", sum_num)


# In[18]:


#Q4
dict1 = {1: ["Ahmed", 21, 'BMET'],
         2: ["Ali  ", 20, 'BMET'],
         3: ["Usman", 21, 'BMET'],
         }

# Print the names of the columns.
print('NAME   ', 'AGE   ', 'COURSE   ')

# print each data item.
for key, value in dict1.items():
    name, age, course = value
    print(name,'  ', age,'  ', course)


# In[1]:


#Q5
li=[1,2,3,1,3,1,3,1]
def fifth(li):
  fifth_element=li[5]
  if len(li)==8 and (li.count(fifth_element)>3):
    return True
  else:
    return False
fifth(li)


# # Local and Global Scope

# In[2]:


#Parameters and variables that are assigned in a called function are said to exist in that function’s local scope. Variables 
#that are assigned outside all functions are said to exist in the global scope


# In[41]:


def spam():
    eggs = 31337  
    
    
    
    
    
    
spam()
print(eggs)


# In[53]:


#remive error by using return
def num(n1,n2):
    output=(n1+n2)
    return output
num(1,2)


# In[59]:


def num1():
    n=2 #local variable
    return n
num1()
#print(n)#outside of local scope
    


# In[ ]:





# In[ ]:





# # Global Variables Can Be Read from a Local Scope

# In[66]:


#eggs = 42
def spam():
 print(eggs)

spam()
#print(eggs)


# # Local and Global Variables with the Same Name

# In[73]:


def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'
    
    
def chicken():
    eggs = 'chicken local'
    print(eggs) # prints 'chicken local'
    spam()
    #print(eggs) # prints 'chicken local'
    
    
    
    
    
    
#eggs = 'global'
#chicken()
#print(eggs) # prints 'global


# In[69]:


def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'
    
spam()


# # Global Variable

# In[24]:


msg="what's your name?"






def name():
    print(msg)
    
    
    
    
    
name()



#using global word to meke a global varibale in the local scope
msg="what's your name?"
def name():
    msg="how  r you doing?"
    print(msg)
    
    
    
name()
print(msg)


# In[76]:


#using global word to meke a global varibale in the local scope
msg="what's your name?"
def name():
    global msg
    msg="how you doing?"
    print(msg)
    
    
name()
print(msg)


# In[ ]:


import pandas as pd 


# # Object Oriented Programming

# In[1]:


x=1
print(type(x))


# In[2]:


print(type("hello"))


# In[4]:


def hello():
    print("hello ")
print (type(hello))


# In[5]:


word= "hello"
print(word.upper()) # upper() is a method that operate on the object word


# In[6]:


x= 1
print(x.upper()) # no class for such operation is made


# # Create our own class

# In[13]:


class dog:
    def bark(self): # let define function which is a methods and all method are start by a parameter self
        print("bark")
d=dog()# d is assigned to a instant of the class dog# instantiating
#print(type(d))


# In[14]:


class dog:
    def bark(self): # lets define function which is a methods and all method are start by a parameter self
        print("bark")
d=dog()
d.bark()
print(type(d))


# In[18]:


class dog:
    
    def add(self,x):
        return (x+1)
    def bark(self): # let define function which is a methods and all method are start by a parameter self
        print("bark")
d=dog()
d.bark()
print(d.add(4))
print(type(d))


# In[100]:


class school:
    def __init__(self,m,s):# automatically called when we make an object.
        self.math=m
        self.science=s
obj=school(40,50)
print(obj.math) 
print(obj.science) 


# In[105]:


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")
    
obj=Dog('german shephered',2)
obj.sit()
obj.roll_over()
#print("My dog's name is " + obj.name.title() + ".")
#print("My dog is " + str(obj.age) + " years old.")


# In[106]:


my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

#my_dog.sit()


# In[41]:


class Dog():
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
obj1=Dog('husky')
obj2=Dog('German shephered')
print(obj1.get_name())
print(obj2.get_name())


# # Modify value

# In[107]:


class Dog():
    def __init__(self, name,age):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def update_age(self,age):
        self.age = age
        
    
obj=Dog('husky',3)
obj.update_age(4)
print(obj.get_age())


# In[88]:


doge_name=["husky","beagle","bulldog"]
dog_age=[2,3,4]
#what if we have more then 25 dog it will be difficult to call the name and age on the basis of index 
#to avoid that we made class of name dog and define objects to define the attrivbutes of all types of dog. 


# # multiple classes
# 

# In[98]:


class student:
    def __init__(self,name,age, grade):
        self.name=name
        self.age=age
        self.grade=grade
        
    def get_grade(self):#method
        return self.grade
    
class course:
    def __init__(self,name,max_students,students):
        self.name=name
        self.max_students=max_students
        self.students=students
        
        
    def add_student(self,student):
        if len(self.students)<len(self.max_students):
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value=0
        for student in self.students:
            value+= student.get_grade
        return value/ len(self.students)
        
      
s1=student("ALI",22,"A")
s2=student("Ahmed",20,"C")
s3=student("Afaq",23,"B")

#adding course
course = course("OOP",24,2)
course.add_student.student.get_grade(s1)
course.add_student(s2)
print(course.get_average_grade())




        
    


# # Parent Class

# In[3]:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("ahmed", "Ali")
x.printname()


# # child Class

# In[4]:


class Student(Person):
  pass
x = Student("Salar", "hassan")
x.printname()


# # Add the __init__() Function

# In[11]:


#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#The child's __init__() function overrides the inheritance of the parent's __init__() function.
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:


# # Use the super() Function

# In[5]:


#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)


# # Add Properties

# In[6]:


class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2022


# In[6]:


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("salar", "hassan", 2022)


# # Add Methods

# In[7]:


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    #If you add a method in the child class with the same name as a function in the parent class, 
    #the inheritance of the parent method will be overridden.


# In[8]:


class Class1:
    def m(self):
        print("In Class1")
       
class Class2(Class1):
    def m(self):
        print("In Class2")
 
class Class3(Class1):
    def m(self):
        print("In Class3") 
        
class Class4(Class2, Class3):
    pass  
     
obj = Class4()
obj.m()


# # polymorphism

# In[1]:


print(5+6)


# In[2]:


print("5"+"6")


# In[3]:


print(len("coding"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "ALI", "Address": "Canada"}))


# In[4]:


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()


# In[10]:


class parrot:
    def fly(self):
        print("Parrot can fly")
    def swim(self):
        print("parrot can't fly")
class penguin:
              def fly(self):
                    print("Parrot can't fly")
              def swim(self):
                    print("parrot can fly")
def flying_test(bird):
                    bird.fly()

blu = parrot()
peggy= penguin()

flying_test(blu)
flying_test(peggy)
                          


# # Abstraction 

# In[ ]:


#break in small parts
#e.g mouse is one layer,keyboard is other layer,screen is third layer


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Encapsulation

# In[ ]:


#hide implimentation

