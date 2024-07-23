class Dog():
    """A class to represent a general dog"""
    #if we want to create a dog object or if we want to 
    #initialize a dog object we have to pass in information
    #to the init method inside of the parenthesis

    #the first thing you always have to pass to a class in the 
    #self keyword
    #self = individual dog object realizes who it is

    #what does the dog need? What does every dog have?
    #every dog has a name, gender and age
    
    #we need at attach parameters to the individual dog like this:
    #my_dog = Dog("Spot", make, 10)

    #take this example:
    #def __init__(self, my_name, my_gender, my_age):
    #    my_dog = Dog("Spot", make, 10)
    #right now in the example above the parameters are not
    #connected to dog object
    #to connect the parameters to the dog object use the self keyword
    # self.name = my_name means the name attached to this dog equals
    # name of whatever we pass in
     
    def __init__(self, my_name, my_gender, my_age):
        self.name = my_name
        self.gender = my_gender
        self.age = my_age

    #now we need to program behavior
    #i.e. eating, barking, computing age in dog years
    #must pass in self parameter into every method
    #by passing the self keyword into the method
    #the dog knows it can eat ... it links the method to itself
    def eat(self):
        if self.gender == "male":
            print("Here " + self.name + "Good boy, eat up!")

        else:
            print("Here " + self.name + "Good girl, eat up!")


    #in this method we pass in an outside variable/parameter
    def bark(self, is_loud):
        if is_loud:
            print("WOOF! WOOF! WOOF!")
        else:
            print("woof!")

    #the dog knows it can compute its own age
    def compute_age(self):
        #inside of methods you can create variables
        #the variable dog_years only exists locally in this method. THerefore,
        #you cannot use the variable dog_years in any other method
        dog_years = self.age*7
        print(self.name + "is " + str(dog_years) + "years old in dog years.")


#a Dog class is broad and there are many types of dogs
#lets say I want a Beagle class? A beagle is a dog. Beagles hunt, but
#not all dogs hunt. We need all the methods of the class Dog and extra methods.
#Dog is a super class and Beagle is a sub class or child...inheritance.
class Beagle(Dog):
    #initialize Beagle class
    #1. always start with self keyword when initializing
    #2. ask yourself what does Beagle need? a name, gender, and age
    #3. we also have added something unique to the Beagle ... is_gun_shy

    #Look at Dog super class and in init method we are attaching parameters, i.e. self.name = my_name etc.
    #We should probably do something similar to the Beagle class
    #We want the Beagle class to inherit from the Dog class and inherit all methods and behaviors
    ##we must do something special, which is call the init method of super class and pass
    #required information. We don't have to pass self but need name, gender and age
    def __init__(self, my_name, my_gender, my_age, is_gun_shy):
        #in the init () pass in basically what is in Dog super class
        super().__init__(my_name, my_gender, my_age)
        #we must now do something to make Beagle class unique, we must do somethng with is_gun_shy
        self.is_gun_shy = is_gun_shy

    #another method for the Beagle class
    def hunt(self):
        #if the dog is not shy then take them hunting
        if not self.is_gun_shy:
            self.bark(True)
            print(self.name + " just brought back a duck")
        else:
            print(self.name + " is not a good hunting dog")    

#first thing that happens is initialization runs and we initialize the super class
#name, gender, and age are now linked to Beagle class
#dog_1 = Beagle("Katie", "Female", 3, True)
#dog_1.eat()
#dog_1.bark(False)

#you can override the bark method in the Dog super class like this:
    def bark(self, is_loud):
        if is_loud:
            print("HOWL! HOWL! HOWL")
        else:
            print("howl")

beagle = Beagle("Katie", "Female", 3, True)
beagle.eat()
beagle.bark(True)
beagle.compute_age()
print()
beagle.hunt()
print()
dog = Dog("spooty", "Male", 10)
dog.bark(True)

#if we make a dog object it will not have access to the method hunt()
#dog.hunt() will not work
#the Dog class can't hunt