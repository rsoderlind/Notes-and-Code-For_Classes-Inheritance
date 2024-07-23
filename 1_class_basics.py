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


#create two dog objects from our class
dog_1 = Dog('Spot', "male", 3)
dog_2 =Dog('Katy', "Female", 2)
           
#now you can get attributes that are linked
print(dog_1.name)
print(dog_2.gender)

#also can override attributes
dog_1.name = "Spooty Dog"
print(dog_1.name)

#we can call methods on the class
dog_1.eat()
dog_2.eat()
print()

dog_1.bark(True)
dog_2.bark(False)

dog_1.compute_age()
dog_2.compute_age()






        