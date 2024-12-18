# import numpy as np
# import matplotlib.pyplot as plt
# from PIL import Image

# def rgb_to_grayscale(image):
#     """
#     Преобразует цветное изображение в оттенки серого.
#     """
#     return np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])

# def apply_filter(image, kernel):
#     """
#     Применяет свёртку с заданным фильтром (ядром) к изображению.
#     """
#     kernel_height, kernel_width = kernel.shape
    
#     pad_height = kernel_height // 2
#     pad_width = kernel_width // 2
    
#     output = np.zeros_like(image)

#     padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)
    
#     # Выполняем свёртку
#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             region = padded_image[i:i + kernel_height, j:j + kernel_width]
#             output[i, j] = np.sum(region * kernel)
    
#     return output

# image_path = 'forest.jpg'  
# image = Image.open(image_path)

# image = np.array(image)

# gray_image = rgb_to_grayscale(image)

# sobel_x = np.array([
#     [1, 0, -1],
#     [2, 0, -2],
#     [1, 0, -1]
# ])

# sobel_y = np.array([
#     [1, 2, 1],
#     [0, 0, 0],
#     [-1, -2, -1]
# ])

# gradient_x = apply_filter(gray_image, sobel_x)
# gradient_y = apply_filter(gray_image, sobel_y)

# gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

# gradient_magnitude = np.clip(gradient_magnitude, 0, 255)

# plt.imshow(gradient_magnitude, cmap='gray')
# plt.axis('off')
# plt.show()


# num1 = int(input("Введите число "))

# if num1 < 18:
#     print("Вы ребенок")
# elif num1 >= 18 and num1 < 50:
#     print("Вы взрослый")
# elif num1 >= 50 and num1 < 99:
#     print("Вы старый")
# else:
#     print("Вы умерли или живете больше века")


# num1 = input("Игрок 1, ваш выбор (Камень, Ножницы или Бумага): ").capitalize()
# num2 = input("Игрок 2, ваш выбор (Камень, Ножницы или Бумага): ").capitalize()

# valid_choices = ("Камень", "Ножницы", "Бумага")

# if num1 == num2:
#     print("Ничья!")
# elif (num1 == "Камень" and num2 == "Ножницы") or (num1 == "Ножницы" and num2 == "Бумага") or (num1 == "Бумага" and num2 == "Камень"):
#         print("Игрок 1 победил!")
# else:
#     print("Игрок 2 победил!")



# 1 задание
# for i in range( 1,21):
#     if i % 2 == 0:
#         print(i)


# 2 задание 

# n = int(input("Введите число "))
# sum = 0
# for i in range (1 , n + 1):
#     sum += i
# print(sum)


# 3 задание 

# n = int(input("Введите число "))

# for i in range ( 1, 11):
#     print(f"{n} * {i} = {n * i}")


# 4 задание 
# for i in range ( 50,100):
#     if i % 2 != 0:
#         print(i)


# vowels = "аеёиоуыэюя"

# n = input("Введите строку: ")
# count = 0
# for i in n.lower():  
#     if i in vowels:
#         count += 1

# print(f" гласных букв в строке: {count}")




# import random


# c =[]
# i =0
# while i < 10:
#     c.append(random.randint(0,100))
#     i+=1
# print(c)


# dog = {
#     "name": "Бобик",
#     "age": 15,
#     "poroda": "Овчарка"
# }
# dog["name"] = "Vova"
# print(dog)


# 1 задание - создать массив и вывести на экран 4 индекс

# 2 задание - создать пустой массив и заполнить 10 рандомными числами

# 3 задание - создать пустой массив и заполнить 10 числами, где пользователь 
# сам вводит числа  Подсказка -  переменную ввода нужно создать внутри цикла


# 4 задание = создайте массив и  удалите элемент из массива с помощью pop

# 5 задача - создайте массив где нужно вставить элемент между 1 и 2 индексом (insert)




# 1 Задание 

# list = [1,2,45,5,6]

# for i in list:
#     if i %2 ==0:
#         print(i) 
    
# 2 Задание 

# list = [1,2,45,5,6]
# sum = 0
# for i in list:
#     sum +=i
# print(sum)

# 3 задание 

# list = []
# sum = 0
# for i in range(10):
#     num = int(input(f"Введите число {i+1} "))
#     list.append(num)

# for i in list:
#     sum+=i
# print(list)
# print(sum)

# 4 задание

# list = [22,3,5,6,7,4,4,8]
# print(max(list))

# list = [22,3,5,6,7,4,4,8]

# list.reverse()

# print(list)


# def countFood():
#     a = int(input())
#     b = int(input())
#     print("Всего", a+b,"шт.")

# countFood()


# def cylinder():
#     r = float(input())
#     h = float(input())

#     side = 2*3.14 * r * h

#     circle = 3.14 * r**2

#     full = side + 2 * circle
#     return full

# square = cylinder()
# print(square)



# 1 задание 


# def countFood():
#     a = input()
#     b = input()
#     print( a + " " + b)

# countFood()

# 2 задание -

# def list(lst):
#     a = []
#     for i in lst:
#         if i not in a:
#             a.append(i)
#     return a

# print(list([1, 2, 2, 3])) 

# # 3 задание 
# def square(a):
#     S = a**2
#     P = 4 *a
#     return S,P
# print(square(2))

# list = {
#     "name": "Daniil",
#     "age": 18,
#     "address " : "Lescovo"
# }
# print(list)

# list = [2,4,5,6,"hello",True]
# list[0] = 5
# print(list)

# 1 задание
# def count(list):
#     for i in list:
#         if i% 2 == 0:
#             print(i)

# count([1,3,53,2,6,8,2,4])


# 2 Задание 

# def count (a):
#     sum = 0
#     for i in range(1,a+1):
#         sum +=i
#     print(sum)

# n = int(input("Введите число "))
# count(n)


# 3 задание 

# def count(list):
#     print(max(list))
#     print(min(list))

# count([2,45,7,89,22,6,89,2,1])

# 4 Задание 
# def count(n):
#     for i in range(1, 11):
#         print(f"{n} * {i} = {n*i}")

# a = int(input("Введите число "))
# count(a)

# 5 Задание 

# def count(word):
#     vowels = "aeyuio"
#     vowels2 = "аеуыояию"
#     count = 0  
#     word = word.lower()  
#     for i in word:  
#         if i in vowels or i in vowels2:  
#             count += 1
#     print(count) 

# a = input("Введите слово ")
# count(a) 


# def list(lst):
#     a = []
#     for i in lst:
#         if i not in a:
#             a.append(i)
#     print(a) 
# list([1, 2, 2, 3,5,3,4,1,6])


# import random

# c= []
# i = 0
# while i < 10:
#     c.append(random.randint(0,100))
#     i+=1    
# print(c)






# for i in num:
#     if i % 2 ==0:
#         print(i)

# for i in num:
#     if i % 3 ==0:
#         print(i)


# def cylinder():
#     r = int(input())
#     h = int(input())
#     side = 2* 3.14 * r*h
#     circle = 3.14 * r**2
#     full = side + 2 * circle
#     return full, circle

# print(cylinder())


# def count():
#     product = 1 
#     while True:
#         number = int(input("Вводите числа покав не нажмете 0 "))
#         if number == 0:
#             break  
#         product *= number  
#     return product

# print(count())

# def outer():       
#     n = 5    
#     def inner():      
#         nonlocal n
#         n += 1        
#         print(n)
 
#     return inner

# fn = outer()   
# fn()    
# fn()    

# def outFunc():
#     num = 5

#     def inputFunc():
#         nonlocal num
#         num = 10  # Создается новая переменная внутри
#         print("Внутри внутренней функции:", num)

#     inputFunc()
#     print("Внутри внешней функции:", num)

# outFunc()


# def coffe(typeCoffe):
#     def sizeCoffe(size):
#         return f"Ваш заказ: {size} {typeCoffe}"
#     return sizeCoffe

# latte = coffe("Латте")
# capuchino = coffe("Капучино")

# print(latte("Большой"))   # Ваш заказ: Большой Латте
# print(capuchino("Средний")) # Ваш заказ: Средний Капучино


# def passenger_counter():
#     count = 0

#     def increment():
#         nonlocal count
#         count += 1
#         return count

#     return increment

# turnstile = passenger_counter()
# print(turnstile())  # 1
# print(turnstile())  # 2
# print(turnstile())  # 3


# def user(name):
#     def hello():
#         return f"Hello {name}"
#     return hello

# name1 = user("Daniil")
# print(name1())

# name1 = user("Dima")
# print(name1())


# def func(a):
#     def attention():
#         return f"Внимание - ваша задача {a}"
#     return attention

# b = func("Встать в 5 утра")
# print(b())

# b = func("дождатся Нового года")
# print(b())


# word = input("Введите текст ")
# word.lower()
# vowels = 'aeyuio'
# count = 0
# for i in word:
#     if i in vowels:
#         count += 1
# print(count)


# arr = [2,3,5,6,7,1,3,6,6]
# print(max(arr))


# arr = [2,3,5,6,7,1,3,6,6]
# print(sum(arr)/ len(arr))


# arr = [2,3,5,6,7,1,3,6,6]
# arr2 = []
# for i in arr:
#     if i %2 !=0:
#         arr2.append(i)
# print(arr2)



# try:
#     num1 = int(input("Введите 1 число "))
#     num2 = int(input("Введите 2 число "))
#     print(num1 / num2)
# except ValueError:
#     print("Введите число, а не символ")
# except ZeroDivisionError:
#     print("На ноль делить нельзя")

# arr = [2,3,5,6,7,1,3,6,6]

# try:
#     index = int(input("Введите индекс "))
#     print(arr[index])
# except IndexError:
#     print("индекс вне диапазона!")
# except ValueError:
#     print("введите  число, а не символ ")



# def func(n):
#     def inputFunc(x):
#         return n * x
#     return inputFunc

# a = func(2)
# print(a(5))  

# b = func(3)
# print(b(4))  



# word = input("Введите строку ")
# vowels = 'aeyuio'
# vowelsRus = 'аеуоэяиёю'
# count = 0


# for i in word.lower():
#     if i in vowels or i in vowelsRus:
#         count +=1
# print(count)


# arr = [2,5,5,7,8,9,3,11 ]
# print(max(arr))
# print(sum(arr)/len(arr))


# def fff(a,b):
#     return a +b 

# f = fff(2,4)
# def ddd(c,n):
#     return  c+ n

# print(ddd(f, 5))










# arr = [2,5,5,7,8,9,3 ]
# arr2 = []
# for i in arr:
#     if i % 2 !=0:
#         arr2.append(i)
# print(arr2)

# count = 0
# for i in range(0, 101):
#      count +=i
# print(count)


def sum():
    for i in arr:
       print(i)

sum()
