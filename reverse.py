import time
from langdetect import detect
new = []
haha = {' ':' ' ,'q': 'й', 'w': 'ц',
        'e': 'у', 'r': 'к', 't': 'е',
        'y': 'н', 'u': 'г', 'i': 'ш',
        'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ',
        'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а',
        'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л',
        'l': 'д', ';': 'ж', "'": 'э', 'z': 'я',
        'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и',
        'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю',
        'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К',
         'T': 'Е', 'Y': 'Н', 'U': 'Г', 'I': 'Ш',
         'O': 'Щ', 'P': 'З', '{': 'Х', '}': 'Ъ',
         'A': 'Ф', 'S': 'Ы', 'D': 'В', 'F': 'А',
         'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л',
         'L': 'Д', ':': 'Ж', '"': 'Э', 'Z': 'Я',
         'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И',
         'N': 'Т', 'M': 'Ь', '<': 'Б', '>': 'Ю',
         '/': '.'

        }

def num(nums, lang):
    print("Youre language its a:" + str(lang))
    if lang == 'EN':
        new_dict = {v:k for k, v in haha.items()}
        print(nums)
        my_range = len(nums)
        print(my_range)
        i = 0
        while i < len(nums):
            police = nums[i]
            print(police)
            print(type(police))
            my_dict = new_dict.get(police)
            print(my_dict)
            new.append(my_dict)
            i = i + 1
    else:
        print(nums)
        my_range = len(nums)
        print(my_range)
        i = 0
        while i < len(nums):
            police = nums[i]

            print(type(police))
            my_dict = haha.get(police)
            print(my_dict)
            new.append(my_dict)
            i = i + 1
    return new

def first():
    lang = input("enter your language (RU or EN):")
    my_num = input("enten your number:")
    print(my_num.isupper())
    my_z = []
    a = list(my_num)
    algoritm = num(a, lang)
    print(new)

    myString = ''.join(new)
    print(myString)


    print("ваше предложение это:" + myString)







