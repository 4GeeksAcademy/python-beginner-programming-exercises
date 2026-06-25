# ✅↓ Write your code here ↓✅
def number_of_bottles():
    for i in range (99, 2, -1):
        print (f' {i} bottles of milk on the wall, {i} bottles of milk \n Take one down and pass it around, {i-1} bottles of milk on the wall.')

    print (f' 2 bottles of milk on the wall, 2 bottles of milk \n Take one down and pass it around, 1 bottle of milk on the wall.')
    print (f'1 bottle of milk , 1 bottle of milk.\n Take one down and pass it around, no more bottles of milk')
    print (f'No more bottles of milk on the wall, no more bottles of milk.')
    print (f'Go to the store and buy some more, 99 bottles of milk on the wall.')
    return None
number_of_bottles()