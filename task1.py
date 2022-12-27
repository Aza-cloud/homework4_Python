# 1. Вычислить число c заданной точностью
# ________________________________________

num = float(input("Enter a real number:  "))
d = float(input("Enter the required accuracy '0.0001': ")) 
res = 0
while d != 1:
    d = d * 10
    res = res + 1
print(round(num, res))
