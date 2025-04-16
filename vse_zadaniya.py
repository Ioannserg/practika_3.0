#Задача 1. Анограмма

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    num = 0
    for i in s1:
        if i in s2:
            num += 1

    if len(s1) == len(s2) == num:
        print('Строка является анограмой')

    else:
        print('Строка не является анограммой')

# is_anagram('wwwerty', 'wytwwer')



#Задача 2. Палиндром

def is_palindrome(s):
    s = s.lower().replace(',', '').replace(':', '').replace('!', '').replace(' ', '')
    revers_s = s[::-1]
    if s.lower() == revers_s:
        return True

    else:
        return False

# print(is_palindrome('A man, a plan, a canal: Panama'))



#Задача 3. Самое длинное слово

def longest_word(s):
    words = s.split()
    lond_word = max(words, key=len)
    return lond_word

# print(longest_word("In the middle of a vast desert, an extraordinary adventure awaits"))



#Задача 4. Форматирование номера телефона

def format_phone_number(digits):
    return f'({digits[0:3]}) {digits[3:6]}-{digits[6:]}'

# print(format_phone_number('1234567890'))


#Задача 5: Удаление дублирующих символов

def remove_duplicates(s):
    result = ''
    for i in s:
        if i not in result:
            result += i
    return result

# print(remove_duplicates('programming'))



#Задача 6: Проверка на уникальность символов

def is_unique(s):
    result = ''
    for i in s:
        if i not in result:
            result += i
    if len(s) == len(result):
        return True
    else:
        return False

# print(is_unique('hello'))




#############################################################################


#Задача 1: Удаление дубликатов

def remove_duplicates(lst):
    lst_sort = []
    for i in lst:
        if i not in lst_sort:
            lst_sort.append(i)
    return lst_sort

# print(remove_duplicates([1, 2, 2, 3, 4, 4, 1, 2, 4, 2, 4, 10, 34, 1, 234]))


#Задача 2: Генерация списка квадратов

def generate_squares(n):
    lst = [x**2 for x in range(1, n+1)]
    return lst

# print(generate_squares(5))


# Задача 3: Объединение двух списков

def merge_lists(list1, list2):
    list3 = list1 + list2
    list3.reverse()
    for i in list3:
        count1 = list3.count(i)
        if count1 > 1:
            list3.remove(i)
    list3.reverse()
    return list3



# print(merge_lists([6, 1, 2, 3, 4], [4, 5, 1, 6, 2]))



#Задача 4: Проверка на отсортированность

def is_sorted(lst):
    lst_sort = lst.copy()
    lst_sort.sort()
    if lst == lst_sort:
        return True
    else:
        return False

# print(is_sorted([7, 1, 2, 3, 4, 5]))



#Задача 5: Слияние списков

def merge_lists(list1, list2):
    list3 = []
    for i in range(0, len(list1)):
        list3.append(list1[i] + list2[i])

    return list3

# print(merge_lists([1, 2, 3], [4, 5, 6]))



####################################################

#Задача 1: Частотный анализ строки

def char_frequency(s):
    words = []
    for i in s:
        words.append(i)
    dict1 = {word: words.count(word) for word in words}
    return dict1

# print(char_frequency('hello'))



#Задача 2: Слияние двух словарей

def merge_dicts(dict1, dict2):
    merged = dict1.copy()

    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
# print(merge_dicts(dict1, dict2))



#Задача 3: Обратное преобразование словаря в два списка

def dict_to_lists(my_dict):
    list1 = []
    list2 = []
    for key, value in my_dict.items():
        list1.append(key)
        list2.append(value)
    return list1, list2

# print(dict_to_lists({"a": 1, "b": 2, "c": 3}))


# Задача 4: Группировка элементов по первому символу

def group_by_first_letter(strings):
    dict1 = {}
    for i in strings:
        first_char = i[0].lower()
        if first_char not in dict1:
            dict1[first_char] = []
        dict1[first_char].append(i)

    return dict1

strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
# print(group_by_first_letter(strings))



# Задача 5: Извлечение подсловаря

def extract_subdict(my_dict, keys):
    dict2 = my_dict.copy()
    for key, value in my_dict.items():
        if key not in keys:
            del dict2[key]
    return dict2


my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys = ["a", "c"]
# print(extract_subdict(my_dict, keys))




##################################################################



# Задача 1: Уникальные элементы списка

def get_unique_elements(lst):
    list2 = list(set(lst))
    return list2

# print(get_unique_elements([1, 2, 2, 3, 4, 4, 4, 5]))



# Задача 2: Проверка списка на уникальность элементов

def is_unique_list(lst):
    list2 = list(set(lst))
    if len(list2) == len(lst):
        return True
    else:
        return False

# print(is_unique_list([1, 2, 3, 4]))  # True
# print(is_unique_list([1, 2, 2, 3]))  # False



# Задача 3: Получение уникальных гласных из строки

def get_unique_vowels(s):
    glas = {'e', 'a', 'o', 'u', 'i'}
    my_list = []
    s.lower()
    for i in s:
        if i in glas:
            my_list.append(i)

    list2 = set(my_list)
    return list2
# print(get_unique_vowels("Hello World"))  # {'e', 'o'}
