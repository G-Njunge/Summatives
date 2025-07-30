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
        self.grade = None
    
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
    def get_grade(self):
        while True:
            self.grade = input(f"Enter the grade/100: ")

            if not self.grade:
                print("The field is empty, please input a valid grade")
            elif not self.grade.isdigit():
                print("Invalid input, your grade should be a whole number")
            elif not 0 <= int(self.grade) <= 100 :
                print("Invalid input, Your grade should range between 0 and 100")
            else:
                break
        

    # def assignment_details(self):
    #     self.assign_name = self.get_name()
    #     self.assign_cat = self.get_category()
    #     if self.category == "1":
    #         self.get_form_weight()    
    #     else:
    #         self.get_sum_weight()
    #     self.assign_grade = self.get_grade()
    #     self.user_choice()
        

class grading(Assignments) :
    def __init__ (self):
        super().__init__()
        self.weighted_grade= 0 
        self.total_weighted_grade = 0
        self.total_weight = 0
        self.form_overall_grade = 0
        self.sum_overall_grade = 0

    def calc_weighted_grade(self):
        self.weighted_grade = (int(self.grade)/100 * int(self.weight))
        self.total_weighted_grade += self.weighted_grade
        self.total_weight += int(self.weight)
        print(f"Your weighted grade for {self.name} assignment is {self.weighted_grade} ")
    
    def get_form_final_grade(self):
        if self.total_weight == 0:
            return 0
        self.form_overall_grade = round((self.total_weighted_grade/self.total_weight)*100,2)
    def get_sum_final_grade(self):
        if self.total_weight == 0:
            return 0
        self.sum_overall_grade = round((self.total_weighted_grade/self.total_weight)*100,2)
    def decision(self):
        if self.form_overall_grade >= 30 and self.sum_overall_grade >= 20:
            print("You have passed")
            print(f"You have a toal formative grade of {self.form_overall_grade}")
            print(f"You have a total summative grade of {self.sum_overall_grade}")
        else:
            if self.form_overall_grade < 30:
                print("You have failed because your total formative grade is below 50% of 60") 
            else:
                print("You have failed because your total summative grade is below 50% of 40") 

            print(f"You have a toal formative grade of {self.form_overall_grade}")
            print(f"You have a total summative grade of {self.sum_overall_grade}")

def main():
    grader = grading()

    while True:
        grader.get_name()
        grader.get_category()

        if grader.category == "1":
            grader.get_form_weight()
            grader.get_grade()
            grader.calc_weighted_grade()
            grader.get_form_final_grade()
        else:
            grader.get_sum_weight()
            grader.get_grade()
            grader.calc_weighted_grade()
            grader.get_sum_final_grade()
    
        while True:
            choice = input("Would you like to input another assignment? Choose either 1 or 2\n1.Yes\n2.No(exit)\n")
            if choice == "1":
                break
            elif choice == "2":
                grader.decision()
                print("Thank you for using assignment checker!")
                sys.exit()
            else:
                print(" Invalid input. please enter either 1 0r 2 ")

main()
        