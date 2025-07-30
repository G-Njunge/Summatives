"""
This program uses object-oriented programming to manage and evaluate student assignment perfomance.

it includes:
An Assignmets record class - represents individual assignment s and their details in a clean organized way

An input validator class - contains input validation methods which are modified according to the user_input required

An Assignments class(Base class) - collects assignment details from the user, each instance is a unigue assignment with its details

A Calculations class (Derived Class) - Inherits from Assignments and performs the outlined calculations

A decision() function - Determines whether a student passes or fails.

main() function - Arranges the methods and functions in a logical manner so that the program is executed succesfully

"""

class Assignments:
    #initializing these variables because I will use them  across methods
    def __init__(self):
        self.name = None
        self.category = None
        self.weight = None
        self.grade = None
        self.form_choice = None
        self.form_weight = None
        self.sum_weight = None
    
    def InputValidation(self, value,input_type):
        value = value.strip()
        if not value:
            print("The field is empty, please type a valid input")
            return False
        
        
        if input_type == "name":
            if not any (char.isalpha() for char in value):
                print("Your input should contain at least one alphabetic character, please try again")
                return False
            return True
        
        if input_type == "category" or input_type == "form_choice":
            if value in ["1","2"]:
                return True
            else:
                print("Invalid input please input a number that is either 1 or 2\n")
                return False
                
        if input_type == "weight":
            try: 
                weight = int(value)
            except ValueError:
                print(" Your input should be an integer or float value")
                return False
            self.weight = int(self.weight)
            if self.category == "1":
                if 0 <= self.weight <= 60 - self.form_weight:
                    return True
            elif self.category == "2":
                if 0 <= self.weight <= 40 - self.sum_weight:
                    return True
            else:
                print("Your weight is out of allowed range")
                return False
            
        return True
        
    def get_name(self):
           while True: 
            self.name = input("Please input the assignment name:").strip() #re,oves any trailing white spaces
            if self.InputValidation(self.name,"name"):
                break
        
    def get_category(self):
        while True:
            self.category= input(f"Which category is the {self.name} assignment? Choose either 1 or 2\n1.Formative\n2.Summative\n")  
            if self.InputValidation(self.category,"category"):
                break   

    def get_weight(self):
        self.form_weight = 0
        self.sum_weight = 0
        while True:
            if self.category == "1":
                form_range = (60-self.form_weight)
                print(f"Total Formative weight: {self.form_weight}\nYour input should range between 0 and {form_range}")
            else:
                if self.category == "2":
                    sum_range = (40 - self.sum_weight)
                    print(f"Total Summative weight: {self.sum_weight}\nYour input should range between 0 and {sum_range}")
            
            self.weight = input(f"Please input {self.name}'s weight: ")
            if self.InputValidation(self.weight,"weight"):      
                self.weight = int(self.weight)
                self.form_weight = (self.form_weight + self.weight)
            # if self.form_weight == 60:
            #     print("You have reached the maximum weight of your formative assignments, you can no longer input any more assignmrnts in this category") 
            #     self.form_choice = input(" Would you like to add another assignment in the summative category?\nChoose either 1 or 2\n1.Yes\n2.No")
                    
            #         if self.InputValidation(self.form_choice):
            #             break 
            #         if self.form_choice == "1":
            #             self.assignment_details()
            #         else:
            #             break


    def assignment_details(self):
        self.assign_name = self.get_name()
        self.assign_cat = self.get_category()
        self.assign_weight = self.get_weight()
        self.grade = int(input(f"Enter the grade/100: "))
        
 

Assignments1=Assignments()
Assignments1.assignment_details()