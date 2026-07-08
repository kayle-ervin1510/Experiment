class Animatronic:
	my_id = 83
	
	def __init__(self, name: str, serial_number: int, type: str, species: str, location: str, last_maintinence: int):
		self.name = name
		self.serial_number = serial_number
		self.type = type
		self.species = species
		self.location = location
		self.last_maintinence = last_maintinence
		self.id = Animatronic.my_code
	@property
	def check_number(self):
	    return self.check_number

@classmethod
def access_code(cls):
	new_code = cls.my_Code
	cls.my_code += 1
	return new_code
	
	
