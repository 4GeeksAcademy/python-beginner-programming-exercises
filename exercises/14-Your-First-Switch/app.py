def get_color(color_name):

    switcher = {
        0:'Red',
        1:'red',
        2:'blue',
        3:'Blue',
        4:'green',
        5:'Green'
    }
    return switcher.get(color_name,"Invalid day of week")


color_input= str(input('What color do you want?\n'))
#print("$$$",get_color(color_input)
is_available = get_color(color_input)
if(is_available):
    print('Good news! That color is available')
else:
    print('We are sorry, that color is not available')