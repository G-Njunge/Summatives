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
import sys

class Assignments:
    #initializing these variables because I will use them  across methods
    def __init__(self):
        self.name = None
        self.category = None
        self.weight = None
        self.grade = None
        self.form_choice = None
        self.form_weight = 0
        self.sum_weight = 0
        self.choice = None
        self.form_limit = 60
        self.sum_limit = 40
    
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
        
        if input_type == "category" or input_type == "form_choice" or input_type == "choice":
            if value in ["1","2"]:
                return True
            else:
                print("Invalid input please input a number that is either 1 or 2\n")
            
        return True
        
    def get_name(self):
           while True: 
            self.name = input("Please input the assignment name: ").strip() #removes any trailing white spaces
            if self.InputValidation(self.name,"name"):
                break
        
    def get_category(self):
        while True:
            self.category= input(f"Which category is the {self.name} assignment? Choose either 1 or 2\n1.Formative\n2.Summative\n")  
            if self.InputValidation(self.category,"category"):
                break   
    
    
    def get_form_weight(self):
        if self.form_weight == self.form_limit:
            print("Your weight is at a maximum, you cannot add any more formative assignments")
            self.user_choice()
        
       #input validation for the formative weight     
        while True:
            
            self.weight= input(f"input {self.name}'s weight: ").strip()
            if not self.weight.isdigit():
                print("invalid input, please input a whole number")
            elif not self.weight:
                print("field is empty, please input a valid number")
            elif not 0< int(self.weight) <= 60 :
                print("Weight for a formative assignment should range from 0 to 60 please try again")
            else :
                form_range = (self.form_limit-self.form_weight)
                self.form_weight += int(self.weight)
                if self.form_weight > self.form_limit:
                    print(f"Your total formative weight is more than 60, please input a value ranging from 0 to {form_range}")
                    self.form_weight -= int(self.weight)
                    self.get_form_weight()
                elif self.form_weight == self.form_limit:
                    print("Your assignment has been recorded, but you have already gotten to the max weight of 60.\nThis means you cannot add any more formative assignments")
                    break
                else:
                    print("Your assignment has been recorded!")
                break
    def get_sum_weight(self): 
        if self.sum_weight == self.sum_limit:
            print("Your weight is at a maximum, you cannot add any more summative assignments")
            self.user_choice()


        #Input validation for the summative weight
        while True:
            self.weight= input(f"input {self.name}'s weight: ").strip()
            if not self.weight.isdigit():
                print("invalid input, please input a whole number")
            elif not self.weight:
                print("field is empty, please input a valid number")
            elif not 0< int(self.weight) <= 40 :
                    print(f"Weight for a summative assignment should range from 0 to {self.sum_limit} please try again")
            else :
                    sum_range = (self.sum_limit-self.sum_weight)
                    self.sum_weight += int(self.weight)
                    if self.sum_weight > self.sum_limit:
                        print(f"Your total summative weight is more than {self.sum_limit}, please input a value ranging from 0 to {sum_range}")
                        self.sum_weight -= int(self.weight)
                        self.get_sum_weight()
                    elif self.sum_weight == self.sum_limit:
                        print(f"Your assignment has been recorded, but you have already gotten to the max weight of {self.sum_limit}.\nThis means you cannot add any more summative assignments")
                        break
                    else:
                        print("Your assignment has been recorded!")
                        break
                
    def user_choice(self):
        while True:
            self.choice = input("Would you like to input another assignment? Choose either 1 or 2\n1.Yes\n2.No(exit)\n")
            self.InputValidation(self.choice, "choice")
            if self.choice == "1":
                self.assignment_details()
            else:
                print("Thank you for using assignment checker!")
                sys.exit()


    def assignment_details(self):
        self.assign_name = self.get_name()
        self.assign_cat = self.get_category()
        if self.category == "1":
            self.get_form_weight()    
        else:
            self.get_sum_weight()
        self.grade = int(input(f"Enter the grade/100: "))
        self.user_choice()
        
 

Assignments1=Assignments()
Assignments1.assignment_details()