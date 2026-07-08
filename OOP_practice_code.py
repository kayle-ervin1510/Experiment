# Add a charge commponent to instance.
class Animatronic:
    my_code = 83

    def __init__(
        self,
        name: str,
        serial_number: int,
        type: str,
        species: str,
        #location: str,
        charged: int,
    ):
        self.name = name
        self.serial_number = serial_number
        self.type = type
        self.species = species
        #self.location = location
        self.need_charge = charged
        # assign unique id using class access_code
        self.id = Animatronic.access_code()

    @property
    def check_number(self):
        return self.serial_number

    @check_number.setter
    def check_number(self, number_is):
        if not isinstance(number_is, int):
            return f"Invalid. Must have numerical data."
        if number_is < 0:
            return f"Invalid. No negative integers are allowed within the serial numbers"
        if number_is < 10 or number_is > 15:
            return f"Invalid. Must be between 10 and 15 characters."
        self._number = number_is


    
    @property
    def what_species(self):
        return self.what_species
    
    @what_species.setter
    def species(self, check_species):
        if not (isinstance(check_species, str)):
            return f"I'm sorry, that is an invalid species type. Must be in stirng format."
        self._species = check_species
    @property
    def what_type(self):
        return self.what_type

    @what_type.setter
    def type(self, check_type):
        if not (isinstance(check_type, str)):
            return f"I'm sorry, that is an invalid animatronic type. We accept string values only."
        self._type = check_type

    @property
    def is_charged(self):
        return self.is_charged
    
    @is_charged.setter
    def charged(self, what_charge):
        if not (isinstance(what_charge, int)):
            return f"Invalid. Must be numerical format."
        elif (95 < what_charge < 100):
            return f"Looks like you're good to go!"
        elif (85 < what_charge < 95):
            return f"You have enough charge to keep going for a while yet."
        elif (75 < what_charge < 85):
            return f"Your power is running low. It's reccomended you recharge before a long journey."
        elif (50 < what_charge < 75):
            return f"It's reccomended you find a recharge station soon. You power will run out within the hour."
        elif (10 < what_charge < 50):
            return f"Insificient power for high maintience tasks. Find a recharge station now."
        elif (0 < what_charge < 10):
            return f"Insufficient power. Recharge now."
        elif (what_charge > 100):
            return f"Error - cannot have more than 100% power."
    
    # I would like to make a list of locations
    
    @classmethod
    def access_code(cls):
        new_code = cls.my_code
        cls.my_code += 1
        return new_code

