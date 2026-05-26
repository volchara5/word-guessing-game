import random
words_list = ["яблоко", "дерево", "мышка", "небо", "огонь", "вода", "лист", "волк", "здание", "дом", "море", "земля"]
word = random.choice(words_list)
secret_chr = len(word) * '-'
secret_chr_list = [i for i in secret_chr]
symbols_list = [i for i in word]
print('Добро пожаловать в игру "Виселица"!')
print('''         ________
         ()    !
               !
               !
               !
               !
       -----------''')
print('Начнём! Угадайте слово:', *secret_chr_list)
cnt = 6
while cnt != 0:
    char = input('Введите букву').lower()
    if char in symbols_list:
        cnt_chr = symbols_list.count(char)
        for i in range(cnt_chr):
            char_index = symbols_list.index(char)
            secret_one_char = secret_chr_list.pop(char_index)
            symbol = symbols_list.pop(char_index)
            secret_chr_list.insert(char_index, symbol)
            symbols_list.insert(char_index, secret_one_char)
        print(*secret_chr_list)
    elif char in secret_chr_list:
        print('Вы уже вводили эту букву! Попробуйте другую!')
    else:
        cnt -= 1
        if cnt == 5:
            print('''         ________
         (O)   !
               !
               !
               !
               !
       -----------''')
        elif cnt == 4:
            print('''         ________
         (O)   !
          !    !
               !
               !
               !
       -----------''')
        elif cnt == 3:
            print('''         ________
         (O)   !
         /!    !
               !
               !
               !
       -----------''')
        elif cnt == 2:
            print('''         ________
         (O)   !
         /!\   !
               !
               !
               !
       -----------''')
        elif cnt == 1:
            print('''         ________
         (O)   !
         /!\   !
         /     !
               !
               !
       -----------''')
        elif cnt == 0:
            print('''         ________
         (O)   !
         /!\   !
         / \   !
               !
               !
       -----------
       GAME OVER''')
    if '-' not in secret_chr_list:
            print('Поздравляю! Вы подбедили! И это слово:')
            print(*secret_chr_list)
            break
        