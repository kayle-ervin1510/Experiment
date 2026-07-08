class Animatronic:
	my_id = 1
	def __init__(self, name: str, serial_number: int, species: str, location: str, last_maintinence: int):
		self.name = name
		self.serial_number = serial_number
		self.species = species
		self.location = location
		self.last_maintinence = last_maintinence
		self.id = Animatronic.my_code
	
	@classmethod
	def access_code(cls):
		new_code = cls.my_code
		cls.my_code += 1
		return new_code