def hello(**Kwargs):
    print('hello',end='') 
    for key,value in Kwargs.items():
        print(value,end='')
hello(title ='Mr.',first='Bro', middle='Dude' , last='Code')
        
        
        