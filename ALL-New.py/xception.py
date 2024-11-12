try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero!! idiot!!!!")
except ValueError as e :
    print(e)
    print("Enter only number plz")
except Exception as e:
    print(e)
    print("Something went wrong:(")  
else:
    print(result)
finally:
    print("The will always execute")  
    #2:43:41