# Task 1

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

if __name__ == "__main__":
    vehicle1 = Vehicle("4ELL01", "Car", "Travis Kelce")
    vehicle2 = Vehicle("G0D8Y3", "Truck", "Steph Curry")

    print(f"The first vehicle is owner was: {vehicle1.owner}")
    print(f"The second vehicle is owner was: {vehicle2.owner}")

    vehicle1.update_owner("Aarron Rodgers")
    vehicle2.update_owner("Koby Bryant")

    print(f"\nThe first vehicle is now owned by: {vehicle1.owner}")
    print(f"The second vehicle is now owned by: {vehicle2.owner}")


# Task 2

class Event:
    def __init__(self, name, date ):
        self.name = name
        self.date = date
        self.participants = [] 

    def add_participants(self, participants_name):
            self.participants.append(participants_name)

    def get_participant_count(self):
        count = len(self.participants)
        print(f"Participant Count: {count}")

event1 = Event("Family Cookout", "January, 5, 2025")


event1.add_participants("Jeffrey")
event1.add_participants("Jason")
event1.get_participant_count()


