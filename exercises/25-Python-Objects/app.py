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
    

# STEP 1 Change the fourth lucky number of John Doe to 33  

Person.lucky_numbers[3] = 33

# STEP 2 Create Little Jimmy's object
 
class Person_3:
    name = "Jimmy"
    lastname = "Doe"
    age = 13
    gender = "female"
    lucky_numbers = [ 1, 2, 3, 4]
    significant_other = None

class Family:
    lastname = "Doe"
    members = [Person, Person_2]       #Array of objects, don't forget to add Jimmy

# STEP 3 Add Jimmy to Family object

Family.members.append(Person_3)

def add_allFamilyLuckyNumbers(an_array):
    sum_ofAllLuckyNumbers = 0 # sum_ofAllLuckyNumbers is a number, the sum of all lucky numbers.
    temp = 0
    for i in Family.members:
        for x in i.lucky_numbers:
            sum_ofAllLuckyNumbers += x 
    
    return sum_ofAllLuckyNumbers 

print(add_allFamilyLuckyNumbers(Family.members)) #Step 3



