class student:
    roll = ""
    gpa = ""

    def __init__(self, roll, gpa): 
        self.roll = roll 
        self.gpa = gpa 

    def display(self):
        print(f"ROLL: {self.roll}, GPA: {self.gpa}")  

# Creating objects and passing values directly to the constructor
rahim = student(1001, 2.22)
rahim.display()

karim = student(1002, 2.30)
karim.display()


