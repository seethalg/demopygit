import re
print("hello")
i = 1

while i > 0:
    print(i,":",end="")
    i -=2
    fav = int(input("What is your age:"))
    if fav > 14:
        print("you are older than me!!!")
    else:
        re.sub(" You are a child", " ", "a")
        print("You are a child")

