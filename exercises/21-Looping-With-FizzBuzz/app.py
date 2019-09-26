
# print('\n'.join("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i) for i in range(1,101)))
def fizz_buzz():
    # your code here
    for i in range(1,101):
        if(i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif(i % 3 == 0):
            print("Fizz") 
        elif(i % 5 == 0):
            print("Buzz")
        else:
            print(i)    
    
fizz_buzz(); 