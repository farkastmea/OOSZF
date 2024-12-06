from abc import ABC,abstractmethod

class Vehicle(ABC):

	@abstractmethod
	def __init__(self, licence_plate, brand, model, price):
		self._licence_plate = licence_plate
		self._brand = brand
		self._model = model
		self._price = price
		self._is_rented = False
		
		
	@abstractmethod
	def rented_vehicle(self):
		pass

	@abstractmethod
	def unrented_vehicle(self):
		pass







