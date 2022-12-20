from machine import UART

class RFIDScanner:
    def __init__(self, port, baud=9600):
        self.uart = UART(port, baud)
    def ScanInput():
        read = self.uart.read()
        while(read == None):
            #print("Waiting for scan")
            read = self.uart.read()
        return read
    def getCardID(byteinput):
        read = bytearray(read)
        card = read[3:7]
        return (int.from_bytes(card, "big"))
    def ScanCard():
        return getCardID(ScanInput());
        
        
        
        
    