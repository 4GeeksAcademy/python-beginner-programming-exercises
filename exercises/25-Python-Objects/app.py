class Person:
    name = "John"                       
    lastname = "Doe"
    age = 35                             
    gender = "male"
    lucky_numbers = [ 7, 11, 13, 17]     
  

class Person_2:
    name = "Jane" 
    lastname = "Doe" 
    age = 38
    gender = "female"
    lucky_numbers = [ 2, 4, 6, 8]

class Family:
    lastname = "Doe"
    members = [Person, Person_2]       #Array of objects, don't forget to add Jimmy

    

# STEP 1 Change the fourth lucky number of John Doe to 33  
# Your code here
Person.lucky_numbers[3] = 33

# STEP 2 Create Little Jimmy's object and then add it to the family object
# Your code here
 
class Person_3:
    name = "Jimmy"
    lastname = "Doe"
    age = 13
    gender = "female"
    lucky_numbers = [ 1, 2, 3, 4]
 
Family.members.append(Person_3)

def add_allFamilyLuckyNumbers(an_array):
    sum_ofAllLuckyNumbers = 0 # sum_ofAllLuckyNumbers is a number, the sum of all lucky numbers.
    temp = 0
    for i in Family.members:
        for x in i.lucky_numbers:
            sum_ofAllLuckyNumbers += x 
    
    return sum_ofAllLuckyNumbers 

# STEP 3 Print the sum of all the lucky numbers of the Doe's family
# Your code here

print(add_allFamilyLuckyNumbers(Family.members))  