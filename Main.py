from Office import Office
from Car import Car
from Truck import Truck

class Autokolcsonzo:
   
	def __init__(self):
		self._office = Office("Car Rent")
		self._init_data()
		
	def _init_data(self):
		self._office.vehicles = Car("ABC123", "Fiat", "Punto", 9000)
		self._office.vehicles = Car("ABC321", "Volvo", "XC90", 10000)
		self._office.vehicles = Truck("ABC432", "vOLVO", "FH", 10000)
		
	def user_interact(self):
		while True:
			print("1. Járművek listázása")
			print("2. Járművek bérlése")
			print("3. Járművek bérlésének lemondása")
			print("4. Kilépés")
			
			menu = input("Válasszon az alábbi menüpontokból: ")
			
			if menu == "1":
				self._office.vehicles
			elif menu == "2":
				licence_plate = input("Add meg a gépjármű rendszámát:")
				self._office.rented_by_vehicle(licence_plate)
			elif menu == "3":
				licence_plate = input("Add meg a gépjármű rendszámát")
				self._office.rented_by_vehicle(licence_plate)
			elif menu == "4":
				break;

auto_kolcsonzo = Autokolcsonzo()
auto_kolcsonzo.user_interact()
