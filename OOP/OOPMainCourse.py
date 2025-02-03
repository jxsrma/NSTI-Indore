class Phone():
    def __init__(self):
        print("Phone is created")

    def call(self):
        print('Calling')


class TouchScreen(Phone):
    def __init__(self, company, color, imei, phoneNumber):
        self.company = company
        self.color = color
        self.__imei = imei
        self._phoneNumber = phoneNumber
        print("Touch Screen Phone Created")

    def call(self):
        print('Calling via Touch Screen')

    def insertSim(self, Sim1, Sim2=None, Sim3=None, Sim4=None):
        print(Sim1, Sim2, Sim3, Sim4)


samsung = TouchScreen('Samsung', 'Blue', 123981238, 8945375629)
# samsung.call()
# print(samsung._phoneNumber)
# print(samsung.__imei)
samsung.insertSim('Airtel', 'Jio','BSNL')
