temp = int(input("What is the temparature outside : "))

if not(temp >= 0 and temp <= 30) :
    print('The temperature is good today ') 
    print('Go out side ')
    
elif not(temp < 0 or temp  > 30) :
    print("The temperature is bad today")
    print("Stay Home")
    