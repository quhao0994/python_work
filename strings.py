print("I'm gonna skip to another line\nlike this ")
print("the backslash let the dubble quete\"stays here")
phrase = "quhao"
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())#连续调用函数，只显示最后一个函数的结果

print("the length of \"quhao\"is",len(phrase))#逗号隔开str和len()
print("I want the first letter in phrase which is "+phrase[0])
print(phrase.index("h"))
print(phrase.replace("o","i"))
