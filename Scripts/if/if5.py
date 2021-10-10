# if5 Прохоренков Егор ИСП-211
a = int(input())
b = int(input())
c = int(input())

_sumPos = 0
_sumNeg = 0

if a > 0:
    _sumPos += 1
else:
    _sumNeg += 1
if b > 0:
    _sumPos += 1
else:
    _sumNeg += 1
if c > 0:
    _sumPos += 1
else:
    _sumNeg += 1

print(_sumPos, _sumNeg)