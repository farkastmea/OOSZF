from Vehicle import Vehicle

class Car (Vehicle):
	
	def __init__(self, licence_plate, brand, model, price):
		super().__init__(licence_plate,brand, model, price)
		self._is_rented
		
	@property
	def licence_plate(self):
		return self._licence_plate
	
	@property
	def brand(self):
		return self._brand
	
	@property
	def model(self):
		return self._model
	
	@property
	def price(self):
		return self._price
	
	@property
	def is_rented(self):
		return self._is_rented
		
	def rented_vehicle(self):
		if not self._is_rented:
			self._is_rented = True
		else:
			print("Hiba, a gépjármű már bérelt")
   
	def unrented_vehicle(self):
		if self._is_rented:
			self._is_rented = False
		else:
			print("Hiba, a gépjármű nem volt bérelt")