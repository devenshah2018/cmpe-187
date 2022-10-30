# An instance of a Child class contains the variables age and gender.
class Child:
    def __init__(self, age, gender):
        self.age = age  # The age of the child in integer form
        self.gender = gender  # The gender of the child ("boy" or "girl")


# A function that takes a Child class as its input parameters and returns a ticket containing the list of competitions that the child can participate in
def issue_ticket(Child):
    competitions = "No valid competitions."  # Initialize competition.
    if (Child.gender == "boy" and Child.age > 7 and Child.age < 10):  # First scenario
        competitions = "Storytelling"

    if (Child.gender == "girl" and Child.age > 7 and Child.age < 10):  # Second scenario
        competitions = "Drawing"

    if (Child.gender == "boy" and Child.age > 11 and Child.age < 15):  # Third scenario
        competitions = "Quiz"

    if (Child.gender == "girl" and Child.age > 10 and Child.age < 15):  # Fourth scenario
        competitions = "Essay Writing"

    if ((Child.gender == "girl" or Child.gender == "boy") and Child.age < 6):  # Fifth scenario
        competitions = "Rhyming"

    if ((Child.gender == "girl" or Child.gender == "boy") and Child.age > 20):  # Sixth scenario
        competitions = "Poetry"
    print(competitions)


def main():
    child_1 = Child(9, "boy")
    child_2 = Child(9, "girl")
    child_3 = Child(12, "boy")
    child_4 = Child(11, "girl")
    child_5 = Child(5, "boy")
    child_6 = Child(5, "girl")
    child_7 = Child(21, "boy")
    child_8 = Child(21, "girl")
    issue_ticket(child_1)
    issue_ticket(child_2)
    issue_ticket(child_3)
    issue_ticket(child_4)
    issue_ticket(child_5)
    issue_ticket(child_6)
    issue_ticket(child_7)
    issue_ticket(child_8)


if __name__ == "__main__":
    main()
