class Frouit:

    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def orange(self, d):
        return d + 1

    def apple(self):
        print('apple is good for you')

    def welcome_person(self):
        print(f"Weclome: {self.name} to your office")

person = Frouit('yosef')
print(person.get_name())

person.welcome_person()

#name = 'Hey'
#f"hello {name}"
#"hello {1} {0} {2}".format("A", "B", 55)