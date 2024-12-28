from bms.bms_controller import BMSController

com_port = 'COM8'
# com_port = '/dev/ttyUSB0'

bms = BMSController(com_port)
print(bms.power())
print("------------------------------------------------")
print (bms.batteries())
