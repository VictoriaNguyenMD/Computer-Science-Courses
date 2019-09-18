class AgeTracker():

    def __init__(self):
        self.ages = {}

    def add_person(self, name, age):
        self.ages[name] = age

    def remove_person(self, name):
        del self.ages[name]

    def have_birthday(self, name):
        self.ages[name] += 1

    def get_birthday(self, name):
        if name in self.ages:
            return self.ages[name]
        else:
            return -1

    
