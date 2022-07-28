
try:
    from serial import Serial

    modelo = 'Real'

    class Sensor:
        def __init__(self):
            self.serial = Serial(port='/dev/serial0', baudrate=9600, timeout=0.05)


        def getLeitura(self):
            try:
                self.serial.write(b'1')
                self.leitura = [int(x) for x in self.serial.readline().split()]

            except:
                self.leitura = (0, 0)

except:

    modelo = 'Fake'

    class Sensor:
        def __init__(self):
            self.range = iter(range(400, 40000, 1))

        def getLeitura(self):
            #x = y = next(self.range)
            #self.leitura = (x, y)
            self.leitura = (688, 688)

