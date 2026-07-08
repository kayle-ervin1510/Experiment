class Plex:
	my_id = 1
	def __init__(self, Daycare, Arcade, El_Chips, Rockstar_Row, Security_Office, Tunnels, Auditorium):
		self.Daycare = Daycare
		self.Arcade = Arcade
		self.El_Chips = El_Chips
		self.Rockstar_Row = Rockstar_Row
		self.Security_Office = Security_Office
		self.Tunnels = Tunnels
		self.Arcade = Arcade
		self.id = Plex.my_id
	
	@classmethod
	def access_area(cls):
		new_id = cls.my_id
		cls.my_id += 1
		return new_id