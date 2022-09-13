# 1/1 С клавиатуры вводится 7мизначное число.
# Если четных цифр в нем больше, чем нечетных, то
# найти сумму всех цифр. Если нечетных больше, чем
# четных, то найти произведение 1, 3 и 6 цифр.
# nums = int(input())
# even = 0
# odd = 0
# summ = 0
# first = int(nums[0])
# middle = int(nums[2])
# last = int(nums[5])
# while nums != 0:
#     x = nums % 10
#     if x % 2 == 0:
#         even += 1
#         if even > odd:
#             summ += x
#         elif odd> even:
#             w = first * middle * last
#
#     else:
#         odd += 1
#     nums = nums // 10
# print(summ)
# print(w)

# 1.2 C клавиатуры вводится строка. Если количество согласных и
# гласных в ней одинаково, то выведите на экран все гласные буквы
# st = input().lower()
# lst_vowels = 'aeiouy'
# vowels = 0
# cons = 0
# for letter in st:
#     if letter in lst_vowels:
#         vowels += 1
#     elif letter not in lst_vowels:
#         cons += 1
#         if vowels == cons:
#             z = st()
#             # z = st
#             # i in lst_vowels:
#             print(st if st in lst_vowels)
            # if st in lst_vowels:
            #     print(st, end=' ')