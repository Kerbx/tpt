# Begin21 Прохоренков ИСП-211
point1 = (float(input()), float(input()))
point2 = (float(input()), float(input()))
point3 = (float(input()), float(input()))

len1to2 = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
len1to3 = ((point3[0] - point1[0]) ** 2 + (point3[1] - point1[1]) ** 2) ** 0.5
len2to3 = ((point3[0] - point2[0]) ** 2 + (point3[1] - point2[1]) ** 2) ** 0.5

perimetr = len1to2 + len1to3 + len2to3
poluPerimetr = perimetr / 2
s = (poluPerimetr * (poluPerimetr - len1to2) * (poluPerimetr - len1to3) * (poluPerimetr - len2to3)) ** 0.5

print(f'Периметр равен: {perimetr}\nПлощадь равна: {s}')