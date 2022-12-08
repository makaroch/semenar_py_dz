# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def Task_1():
    a = "1.txt"
    with open(a,'r',encoding='utf-8') as file:
        text_list = file.readline().split()
    print(text_list)
    tex_l = list(filter(lambda item: not('а' in item) and not('б' in item) and not('в' in item), text_list))
    print(tex_l)
#Task_1()
def Task_2():
    def Compress(file_name : str):
        with open(file_name,'r', encoding='utf-8') as file:
            string = file.readline()
        i = 0
        compress = ''
        print(string)
        while i < len(string):
            count = 1
            while (i+1 < len(string)) and (string[i] == string[i+1]):
                count += 1
                i += 1
            compress += str(count) + string[i]
            i += 1
        with open("compress_rle.txt", 'w+', encoding="utf-8") as file:
            file.writelines(compress)
    # Compress("decompress_rle.txt")
    def Decompress(file_name : str):
        with open(file_name,'r', encoding='utf-8') as file:
            text = file.read()
        i = 0
        quantity = ''
        result = ''
        while i < len(text):
            while text[i].isdigit():
                quantity += text[i]
                i += 1
            result += text[i] * int(quantity)
            quantity = ''
            i+=1
        with open('decompress_rle.txt','w+', encoding="utf-8") as file:
            file.writelines(result)
    # Decompress("compress_rle.txt")
