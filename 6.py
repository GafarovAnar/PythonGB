# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no
n= int (input("Введите шестизначное385 число"))
if 99999<n and n<1000000:
    n1=int(n%1000)
    n=int(n/1000)
    sum=int(n1/100)
    n2=int((n1%100)/10)
    sum=sum+(n1%100)
    sum=sum+n2
    sum1=int(n/100)
    n3=int((n%100)/10)
    sum1=sum1+(n%100)
    if sum==sum1:
        print(" счастливый билет!")
    else:
        print("Несчастливый билет!")
else:
    print("Это не шестизначное число!")