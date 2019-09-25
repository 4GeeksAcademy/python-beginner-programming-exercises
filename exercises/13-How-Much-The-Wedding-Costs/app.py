user_input = int(input('How many people are coming to your wedding?'))
# user_input = 99
price = 0
if( user_input < 51):
    price = 4000
elif (51 < user_input and user_input < 101):
    price = 10000
elif (101 < user_input and user_input < 201):
    price = 15000
else:
    price = 20000


# Your code above here 
print('Your wedding will cost '+str(price)+' dollars');