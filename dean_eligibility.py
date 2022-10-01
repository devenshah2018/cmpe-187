class Student:
    def __init__(self, age, lived_in_ca, work_in_ca, parents_lived_ca, volunteering, household_income):
        self.age = age
        self.lived_in_ca = lived_in_ca
        self.work_in_ca = work_in_ca
        self.parents_lived_ca = parents_lived_ca
        self.volunteering = volunteering
        self.household_income = household_income

    
def check_eligibility():
    student = Student(20, 3, 1, 4, True, 4000)
    if 18 <= student.age <= 24:
        if student.lived_in_ca >= 2 or student.work_in_ca >= 0.5 or student.parents_lived_ca >= 1 or student.volunteering == True:
            dean_eligibility = 1
        elif student.household_income < 5000:
            dean_eligibility = 'Dean for consideration'
    else:
        dean_eligibility = 0
    return(dean_eligibility)


print(check_eligibility())


        
