class CarRecord:
    def __init__(self, VehicleID, Registration, DateOfRegistration, EngineSize, PurchasePrice):
        self.VehicleID = VehicleID
        self.Registration = Registration
        self.DateOfRegistration = DateOfRegistration
        self.EngineSize = EngineSize
        self.PurchasePrice = PurchasePrice
        
arr = []
for i in range (5):
    car = CarRecord(i,i,i,i,i) #generic values
    arr.append(car)
    
print(arr) #prints memory locations of objects to show they are in the array
