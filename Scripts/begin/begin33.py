# Begin33 Прохоренков ИСП-211
someWeight = float(input())
costOfSomeWeight = float(input())
costOfOneKilo = costOfSomeWeight / someWeight
weight = float(input())
print(f'Стоимость одного килограмма: {costOfOneKilo}\nСтоимость {weight} кг конфет: {weight * costOfOneKilo}')