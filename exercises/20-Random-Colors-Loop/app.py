import random

def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(color_number,"Invalid Color Number")


def get_allStudentColors():

    #your loop here
    example_color = 1
    students_array = []

    for i in range(11):
        example_color = get_color(random.randint(0,4))
        students_array.append(example_color)
    return students_array



print(get_allStudentColors())