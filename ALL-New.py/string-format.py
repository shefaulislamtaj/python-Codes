""""
animel = "cow" 
item = "moon"
#print("The "+animel+ "jump over the "+item)
#print("The {0}jump over the {1}".format(animel,item))
#print("The {animel}jump over the {item}".format(animel="cow",item="moon"))
text = "The {} jump over the {}"  
print(text.format(animel,item))

name = "Bro" 
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}.Nice to meet you".format(name))
print("Hello, my name is {:<10}.Nice to meet you".format(name))
print("Hello, my name is {:>10}.Nice to meet you".format(name))
print("Hello, my name is {:^10}.Nice to meet you".format(name))
"""
number = 1000
print("The number pi is {:.3f}".format(number))
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number)) 
print("The number pi is {:o}".format(number)) 
print("The number pi is {:x}".format(number)) 
#2:33:24