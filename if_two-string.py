
def two_string(str1, str2):
    print("----")
    if type(str1) == str and type(str2) == str:
        print("Все ОК!")
        if str1 == str2:
            return 1
        elif str1 != str2 and len(str1) > len(str2):
            return 2
        elif str1 != str2 and str2 == "learn":
            return 3
        else:
            return "Что делать - неизвестно!"
    else:
        return 0
        


print(two_string(1,"fgfg"))
print(two_string("fgfg","fgfg"))
print(two_string('asdfg','fgfg'))
print(two_string('fgfg','learn'))
print(two_string('fgfg','asdfggh'))