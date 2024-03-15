class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all=[]

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.owner = owner
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise ValueError("Invalid pet type")
        type(self).all.append(self)

class Owner:
    
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise TypeError("pet must be an instance of Pet class")
        
    def get_sorted_pets(self):
        # lambda function takes a pet object as input("pet") and returns the value of it's "name" attribute 
        return sorted(Pet.all, key=lambda pet: pet.name)