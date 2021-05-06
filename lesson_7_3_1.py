# Exercise #1
#
# Create a class Zoo that keeps track of animals in it:
#
# Zoo class should have a dictionary attribute to keep track of animals.
# In this dictionary keys are animals and values are their quantity

# It should also have a list of zoo employees

# When Zoo is initialized by default there are 3 squirrels in a zoo and 1 employee John

# There should be at least 1 employee per 10 animals

# It should have a method to add animals to it (ex: add_animal).
# If called without parameters it will increase the number of squirrels in a zoo.

# If after adding a new animal there are not enough employees it should print
# Not enough employees for all animals! Hire someone new!"

# If add_animal is called and there are already not enough employees it should print "Not enough employees!
# Can't take care of a new animal!". In this case, the animal will not be added to the zoo

# It should also have the method to remove an animal

# It should have the method to hire a new employee

# It should have the method to fire an employee. If that method is called without an employee's name,
# the most recently hired person will be fired

# It should also print how many animals are in the zoo (by every species) and
# names of all employees (use __str__() for it)

class Zoo:
    """Class that keeps record of employees and animals in a zoo"""

    def __init__(self):
        self.employees = ["John"]
        self.animals = {"squirrel": 3}
        # print()
        # for key, value in self.animals.items():
        #     print(key, ' : ', value)

    def add_animal(self, animal_name):
        number_of_animals = sum(self.animals.values())
        if (len(self.employees) * 10) <= number_of_animals:
            print("Not enough employees! Can't take care of a new animal!")
        else:
            if animal_name in self.animals:
                self.animals[animal_name] += 1
                print("The animal is successfully added.")
            else:
                self.animals[animal_name] = 1
            if (len(self.employees) * 10) == (number_of_animals + 1):
                print("Not enough employees for all animals! Hire someone new!")
        # print()
        # for key, value in self.animals.items():
        #     print(key, ' : ', value)

    def remove_animal(self, animal_name):
        if animal_name in self.animals:
            self.animals[animal_name] -= 1
            print("The animal is successfully removed.")
        else:
            print("There is no such an animal is the zoo.")

    def hire_employee(self, name=None):
        if name is None:
            print("Cannot hire someone without a name")
        else:
            self.employees.append(name)
            print(name + " is welcome to the team!")

    def fire_employee(self, name=None):
        if name is None:
            print(self.employees.pop() + " is fired")
        else:
            print(self.employees.pop(self.employees.index(name)) + " is fired")

    def __str__(self):
        employees_str = "\nEmployees of the zoo: " + ",".join(self.employees)
        animals_str = "There are {} animals in the zoo.\n".format(str(sum(self.animals.values())))
        return employees_str + "\n" + animals_str


# just some tests - you can remove them if you want
Austin_Zoo = Zoo()
print(Austin_Zoo)
Austin_Zoo.add_animal("squirrel")
Austin_Zoo.add_animal("lion")
Austin_Zoo.add_animal("lion")
Austin_Zoo.add_animal("lion")
Austin_Zoo.add_animal("lion")
Austin_Zoo.add_animal("lion")
Austin_Zoo.add_animal("lion")
Austin_Zoo.add_animal("lion")
Austin_Zoo.add_animal("lion")
Austin_Zoo.hire_employee()
Austin_Zoo.hire_employee("Bethany")
Austin_Zoo.add_animal("lion")
Austin_Zoo.add_animal("lion")
Austin_Zoo.hire_employee("Michael")
Austin_Zoo.remove_animal("lion")
Austin_Zoo.remove_animal("goat")
Austin_Zoo.fire_employee()
Austin_Zoo.fire_employee("John")
print(Austin_Zoo)

