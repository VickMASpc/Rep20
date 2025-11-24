semana = ("seg", "ter", "qua", "qui", "sex", "sab", "dom")

print(semana[0], semana[-1])

nums = (2, 4, 6, 8, 10, 12)

print(max(nums))
print(min(nums))
print(sum(nums))

cants = ("nom1", "nom2", "nom3", "nom4")

print(type(cants))

cantstList = list(cants)
cants = cantstList

print(type(cants))

print(cantstList)

cantstList.append("nome5")

print(cants)
