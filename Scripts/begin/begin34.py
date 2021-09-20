# Begin34 Прохоренков ИСП-211
someWeightCandy = float(input())
someWeightIris = float(input())
costOfSomeWeightCandy = float(input())
costOfSomeWeightIris = float(input())
costOfOneKiloCandy = costOfSomeWeightCandy / someWeightCandy
costOfOneKiloIris = costOfSomeWeightIris / someWeightIris
print(f'Стоимость одного килограмма конфет: {costOfOneKiloCandy}\
        Стоимость одного килограмма ириса: {costOfOneKiloIris}\
        Конфеты дороже ириса в {costOfOneKiloCandy / costOfOneKiloIris} раз.')