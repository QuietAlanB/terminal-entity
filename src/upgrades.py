from color import COLOR

class Upgrade:
        def __init__(self, name, level, powerLevels, timeLevels, accessLevels):
                self.name = name
                self.level = level
                self.time = timeLevels[0]
                self.power = powerLevels[0]
                self.access = accessLevels[0]
                self.powerLevels = powerLevels
                self.timeLevels = timeLevels
                self.accessLevels = accessLevels
                self.upgrading = False

        def StartUpgrade(self):
                self.upgrading = True
                self.UpdateValues()

        def UpdateValues(self):
                if (len(self.powerLevels) == self.level - 1):
                        return

                self.power = self.powerLevels[self.level - 1]
                self.time = self.timeLevels[self.level - 1]
                self.access = self.accessLevels[self.level - 1]

        def Update(self):
                if (self.upgrading):
                        self.time -= 1

                        if (self.time == 0):
                                self.level += 1
                                self.upgrading = False
                                self.UpdateValues()
                                print(f"{COLOR.BLUE}{self.name}{COLOR.WHITE} finished upgrading")
