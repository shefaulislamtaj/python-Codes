class student:
    roll = ""
    gpa = ""
    
    def set_value(self,roll,gpa):
        self.roll = roll 
        self.gpa = gpa 
    
    def display(self):
       print(f"Roll : {self.roll}, Gpa : {self.gpa}")
    
rahim = student()  
#print(isinstance(rahim,student))  
#rahim.roll = "1001"  
#rahim.gpa = "2.22" 
rahim.set_value(1001,2.22)
rahim.display()
 


karim = student()  
#print(isinstance(karim,student))  
#karim.roll = "1002"  
#karim.gpa = "2.30"
rahim.set_value(1001,2.22)
karim.display()