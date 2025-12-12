import random

def get_color(color_number=4):
    # Making sure is a number and not a string
    color_number = int(color_number)   

    switcher = {
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    
    return switcher.get(color_number,"Invalid Color Number")

#  ⬆ DON'T CHANGE THE CODE ABOVE ⬆ 

def get_allStudentColors():
    example_color = get_color(1)
    students_array = []

    for i in range(10):
        color_number = random.randint(0,3)
        student_color = get_color(color_number)
        students_array.append(student_color)   
             
    return students_array

    #  ↓ your loop here ↓   

print(get_allStudentColors())
