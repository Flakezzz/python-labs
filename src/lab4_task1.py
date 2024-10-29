class Stadium:

    def __init__(self, match="None vs None", totalGoals=0, numOfSpectators=0, name="Name", lightInLx=0):
        self.match = match
        self.totalGoals = totalGoals
        self.__numOfSpectators = numOfSpectators
        self.__name = name
        self.__lightInLx = lightInLx

    # Геттери і сеттери
    def getNumOfSpectators(self):
        return self.__numOfSpectators
    
    def setNumOfSpectators(self, num):
        self.__numOfSpectators = num

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getLightInLx(self):
        return self.__lightInLx
    
    def setLightInLx(self, light):
        self.__lightInLx = light

    # Перевизначення методів
    def __str__(self):
        return f"Match: {self.match},\nTotal Goals: {self.totalGoals},\nSpectators: {self.__numOfSpectators},\nName: {self.__name},\nLight: {self.__lightInLx}"
    
    def __repr__(self):
        return f"Stadium: {Stadium}"

    # Деструктор
    def __del__(self):
        print(f"Destructing obj: {self.__name}")


def main():
        # Ініціалізація 3 об'єктів
        std1 = Stadium()
        std2 = Stadium("", 0, 10000, "Arsenal", 5)
        std3 = Stadium("Dynamo Kyiv vs Shakhtar Donetsk", 3, 5400, "Arena Lviv", 4)

        std2.match = "Real Madrid vs Barcelona"
        std2.totalGoals = 4

        std3.__lightInLx = 11

        # Виводимо значення різними способами
        print(f"{std1}\n")
        print(f"{repr(std2)}\n")
        # Вивід публічних та приватних полів
        print(std3.match)
        print(std3.totalGoals)
        print(std3.getNumOfSpectators())
        print(std3.getName())
        print(std3.getLightInLx())


main()
