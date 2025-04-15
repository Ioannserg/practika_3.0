def count_vowels(string):
    az = ['a', 'e', 'i', 'o', 'u']
    sum = 0
    for i in string:
        if i in az:
            sum += 1
    print(sum)

count_vowels('aeiouffffa')