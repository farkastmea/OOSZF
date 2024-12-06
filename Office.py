class Office:
    def __init__(self, name):
        self._name = name
        self._vehicles = []
        
        
    @property
    def name(self):
        return self._name
    
    @property
    def vehicles(self):
        for vehicle in self._vehicles:
            print(f" licence_plate: {vehicle.licence_plate}, brand: {vehicle.brand}, model: {vehicle.model}, price: {vehicle.price}, status: {vehicle.is_rented}")
        
    @vehicles.setter
    def vehicles(self, new_vehicle):
        self._vehicles.append(new_vehicle)
        
    def rented_by_vehicle(self, licence_plate):
        for vehicle in self._vehicles:
            if vehicle.licence_plate == licence_plate:
               (vehicle.rented_vehicle())
               
    def unrented_by_vehicle(self, licence_plate):
        for vehicle in self._vehicles:
             if vehicle.licence_plate == licence_plate:
                (vehicle.unrented_vehicle())
                
        
    
    
  
