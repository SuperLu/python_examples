import serial

ser = serial.Serial("com2",115200,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE,0.100)
ser.write("hello pyserial")
while True:
    str = ser.read(100)
    if str == "EXIT":
        ser.close()
        print "close com2"
        break
    if len(str) > 0:
        print "%d %s" % (len(str),str)