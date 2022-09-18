from random import randint

#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""



#player1= input ('Игрок 1, представтесь, напишите Ваше имя: ')
#player2= input ('Игрок 2, представтесь, напишите Ваше имя: ')
#candies = 2021
#flag = randint(0, 2)
#if flag:
#    print(f"Первый ходит {player1}")
#else:
#    print(f"Первый ходит {player2}")

#def game_step (name):
#    x = int(input(f"{name}, введите количество конфет, сколько возьмете от 1 до 28: "))
#    while x < 1 or x > n:
#        x = int(input(f"{name}, введите корректное число конфет: "))
#    return x

#count1 = 0
#count2 = 0          


#while candies > 28:
#    if flag:
#        c = game_step(player1)
#        count1 += c
#        candies -= c
#        flag = False
#        print(f"{player1} взял {c} конфет. Теперь у него {count1} конфет. Осталоь в игре {candies} конфет")
#    else:
#        c = game_step(player2)  
#        count2 += c
#        candies -= c
#        flag = True
#        print(f"{player2} взял {c} конфет. Теперь у него {count2} конфет. Осталоь в игре {candies} конфет")


#if flag:
#   print(f"Победил: {player1}")
#else:
#    print(f"Победил: {player2}")


# а) Игра против бота

#player1= input ('Игрок 1, представтесь, напишите Ваше имя: ')
#player2= "Компаньон-2022"
#candies = 2021
#n = 28
#flag = randint(0, 2)
#if flag:
#    print(f"Первый ходит {player1}")
#else:
#    print(f"Первый ходит {player2}")


#def game_step (name):
#    x = int(input(f"{name}, введите количество конфет, сколько возьмете от 1 до 28: "))
#    while x < 1 or x > n:
#        x = int(input(f"{name}, введите корректное число конфет: "))
#    return x

#count1 = 0
#count2 = 0          

#while candies > n:
#    if flag:
#        c = game_step(player1)
#        count1 += c
#        candies -= c
#        flag = False
#        print(f"{player1} взял {c} конфет. Теперь у него {count1} конфет. Осталоь в игре {candies} конфет")
#    else:
#        c = randint(1, n+1)
#        count2 += c
#        candies -= c
#        flag = True
#        print(f"{player2} взял {c} конфет. Теперь у него {count2} конфет. Осталоь в игре {candies} конфет")

#if flag:
#    print(f"Победил: {player1}")
#else:
#    print(f"Победил: {player2}")            


#б) Игра против бота с интеллектом



#player1= input ('Игрок 1, представтесь, напишите Ваше имя: ')
#player2= "Компаньон-2022"
#candies = 2021
#n = 28
#flag = randint(0, 2)
#if flag:
#    print(f"Первый ходит {player1}")
#else:
#    print(f"Первый ходит {player2}")


#def game_step (name):
#    x = int(input(f"{name}, введите количество конфет, сколько возьмете от 1 до 28: "))
#    while x < 1 or x > n:
#        x = int(input(f"{name}, введите корректное число конфет: "))
#    return x

#count1 = 0
#count2 = 0         

#while candies > n:
#    if flag:
#        c = game_step(player1)
#        count1 += c
#        candies -= c
#        flag = False
#        print(f"{player1} взял {c} конфет. Теперь у него {count1} конфет. Осталоь в игре {candies} конфет")
#    else:
#        if candies < (2 * n):
#            c = (candies - n - 1)
#            count2 += c
#            candies -= c
#            flag = True
#        else:
#            c = randint(1,28)
#            count2 += c
#            candies -= c
#            flag = True
#        print(f"{player2} взял {c} конфет. Теперь у него {count2} конфет. Осталоь в игре {candies} конфет")

#if flag:
#    print(f"Победил: {player1}")
#else:
#    print(f"Победил: {player2}")      

#____________________________________________________________________________________________________________________________

# 2. Создайте программу для игры в ""Крестики-нолики"".

#board = ([1, 2, 3, 4, 5, 6, 7, 8, 9])

#def draw_board(board):
#     counter = 0
#     for i in range(len(board)):
#         print(board[i], end = '   ')
#         counter += 1
#             print()
#             counter = 0


#def take_pos(letter, board):
#     flag = True
#     while flag:
#         draw_board(board)
#         pos = input("\n На какую позицию поставить " + letter + ' \n')
#         if not pos in '123456789':
#             print('Необходимо ввести число от 1 до 9\n')
#             continue
#         if board[int(pos) - 1] != int(pos):
#             print('Клетка занятата\n')
#             continue
#         board[int(pos) - 1] = letter
#         flag = False
#     return board


#def win(board, letter):
#     if board[0] == letter and board[1] == letter and board[2] == letter: return True
#     elif board[3] == letter and board[4] == letter and board[5] == letter: return True
#     elif board[6] == letter and board[7] == letter and board[8] == letter: return True
#     elif board[0] == letter and board[3] == letter and board[6] == letter: return True
#     elif board[1] == letter and board[4] == letter and board[7] == letter: return True
#     elif board[2] == letter and board[5] == letter and board[8] == letter: return True
#     elif board[0] == letter and board[4] == letter and board[8] == letter: return True
#     elif board[2] == letter and board[4] == letter and board[6] == letter: return True
#     else: False


#def head():
#     print('\nДобро пожаловать в игру "КРЕСТИКИ-НОЛИКИ"\n')
#     while True:
#         for i in range(9):
#             if i > 4:
#                 if win(board, 'x') == True:
#                     print('Победил игрок "x"\n')
#                     break
#                 elif win(board, 'o') == True:
#                     print('Победил игрок "o"\n')
#                     break
#             if i % 2 == 0: take_pos('x', board)
#             else: take_pos('o', board)
#         if i == 8: print("Ничья\n")
#         break
#     print("Игра окончена")

                
#head()

#_______________________________________________________________________________________________________________________

# # 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

#def encode(string):
#     count = 1
#     word = string[0]
#     res = []
#     for i in range(len(string) - 1):
#         if word == string[i + 1]:
#             count += 1
#         else:
#             res.append(f'{string[i]}{count}')
#             word = string[i + 1]
#             count = 1
#     res.append(f'{word}{count}')
#     return ''.join(res)


#def decode(string):
#     res = []
#     tmp = ''
#     for i in range(len(string)-2):
#         d = 0
#         tmp = ''
#         if string[i].isalpha():

#             if string[i+1].isdigit() and string[i+2].isdigit():
#                 tmp += (string[i+1] + string[i+2])
#             elif string[i+1].isdigit():
#                 tmp += string[i+1]

#             d = int(tmp)
#             res.append(string[i]*d)

#         elif string[-2].isalpha() and len(string)-1 == i+2:
#             if string[i+2].isdigit():
#                 tmp += (string[i+2])

#             d = int(tmp)
#             res.append(string[i+1]*d)

#    return ''.join(res)

#with open('C:\Users\evgen\OneDrive\Desktop\Python\Семинар\Python-DZ5\ new1.txt', 'r')as file:
#    s = file.readline()

#print(s)
#encode_file = encode(s)

#print(encode_file)
#with open('C:\Users\evgen\OneDrive\Desktop\Python\Семинар\Python-DZ5\ decode.txt', 'w')as file:
#     file.write(decode(encode_file))

#with open('C:\Users\evgen\OneDrive\Desktop\Python\Семинар\Python-DZ5\ decode.txt', 'r')as file:
#     s = file.readline()
#print(s)

