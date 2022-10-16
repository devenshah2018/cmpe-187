class Child:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender


def issue_ticket(Child):
    competitions = []
    if (Child.gender == "boy" and Child.age > 7 and Child.age < 10):
        competitions.append("Storytelling")

    if (Child.gender == "girl" and Child.age > 7 and Child.age < 10):
        competitions.append("Drawing")

    if (Child.gender == "boy" and Child.age > 11 and Child.age < 15):
        competitions.append("Quiz")

    if (Child.gender == "girl" and Child.age > 10 and Child.age < 15):
        competitions.append("Essay Writing")

    if ((Child.gender == "girl" or Child.gender == "boy") and Child.age < 6):
        competitions.append("Rhyming")

    if ((Child.gender == "girl" or Child.gender == "boy") and Child.age > 20):
        competitions.append("Poetry")
    print(competitions)


def main():
    student_1 = Child(8, "boy")
    student_2 = Child(9, "girl")
    student_3 = Child(13, "boy")
    student_4 = Child(11, "girl")
    student_5 = Child(5, "boy")
    student_6 = Child(23, "boy")
    issue_ticket(student_1)
    issue_ticket(student_2)
    issue_ticket(student_3)
    issue_ticket(student_4)
    issue_ticket(student_5)
    issue_ticket(student_6)


if __name__ == "__main__":
    main()
