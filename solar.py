import math
import sys

class SpeedCalculation:
    def __init__(self, peakSunTime, panelSurfaceArea, wattage, chargeTimeRemaining, raceTimeRemaining, currentTime, currentDni, currentAmbientTemp, storedPower):
        self.peakSunTime = peakSunTime
        self.panelSurfaceArea = panelSurfaceArea
        self.wattage = wattage
        self.chargetimeRemaining = chargeTimeRemaining  # free time to charge (does not include race time)
        self.raceTimeRemaining = raceTimeRemaining
        self.currentTime = currentTime
        self.currentDni = currentDni
        self.currentAmbientTemp = currentAmbientTemp
        self.storedPower = storedPower
        self.ratioOfPowerBasedOnTime = math.cos(math.radians(90) - math.radians(90 - (15 * abs(currentTime - peakSunTime))))
        # assumes power falls off as the cos of the angle between sun and panels

    def calculatepowerinput(self, dni, watts, powerTimeRatio):
        powerinput = (dni / 1000) * watts * powerTimeRatio
        return powerinput

    def calculatepowerinput(self):
        powerinput = (self.currentDni / 1000) * self.wattage * self.ratioOfPowerBasedOnTime
        return powerinput

    def calculateTargetSpeed(self, storedpower, chargetime, racetime, avgpredictedinput):
        targetpoweroutput = (storedpower + avgpredictedinput * (chargetime+racetime)) / racetime
        targetspeed = self.calculatespeed(targetpoweroutput)
        return targetspeed

    def calculatespeed(self, poweroutput):  # needs to be implemented
        speed = poweroutput + 10
        return speed

    def calculateTargetSpeed(self):
        targetpoweroutput = (self.storedPower + self.calculatepowerinput() * (self.chargetimeRemaining + self.raceTimeRemaining)) / self.raceTimeRemaining
        targetspeed = self.calculatespeed( targetpoweroutput)
        return targetspeed

def main(a, b, c, d, e, f, g, h, i):
    s1 = SpeedCalculation(a, b, c, d, e, f, g, h, i)
    #12, 100, 300, 2, 10, 11, 1000, 70, 0
    result = s1.calculateTargetSpeed()
    print(result)

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    d = int(sys.argv[4])
    e = int(sys.argv[5])
    f = int(sys.argv[6])
    g = int(sys.argv[7])
    h = int(sys.argv[8])
    i = int(sys.argv[9])

    main(a, b, c, d, e, f, g, h, i)


#   arg parse instead of sys
#   calculate predicted total average energy input instead of using current input
#   drag data