# Begin35 Прохоренков ИСП-211
velocitySelf = float(input())
velocityRiver = float(input())
timeLake = float(input())
timeRiver = float(input())
sLake = timeLake * velocitySelf
sRiver = timeRiver * (velocitySelf - velocityRiver)
print(sLake + sRiver)