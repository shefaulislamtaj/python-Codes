""""
n = input("Enter a text of numbe :  ")

list = n.split() 
sum = 0 
for num in list:
    sum =sum + int (num)
    print(sum)
    """  
""""  
numofwords = 0
numofletters = 0
numofdigits = 0 
n = input("Enter a text of numbe :  ")
for x in n:
 if x >='a' and  <=  'z':
    numofletters = numofletters +1
    
    elif x >= '0' and x <= '9':
    numofdigits = numofdigits + 1
    
print(numofdigits)
print(numofletters)

 = input("Enter a text of numbe :  ")
numofwords = 0
numofletters = 0
numofdigits =0 

n = input("Enter a text or number:  ")

for x in n:
    if 'a' <= x <= 'z' or 'A' <= x <= 'Z':  # Check for both lowercase and uppercase letters
        numofletters += 1
    elif '0' <= x <= '9':  # Check for digits
        numofdigits += 1

print("Number of digits:", numofdigits)
print("Number of letters:", numofletters)

"""
numofletters = 0  # Initialize the counter for letters
numofdigits = 0  # Initialize the counter for digits

n = input("Enter a text or number:  ")

for x in n:
    if 'a' <= x <= 'z' or 'A' <= x <= 'Z':  # Check for both lowercase and uppercase letters
        numofletters += 1
    elif '0' <= x <= '9':  # Check for digits
        numofdigits += 1

print("Number of digits:", numofdigits)
print("Number of letters:", numofletters)  # Fixed typo in 'numofletters'
