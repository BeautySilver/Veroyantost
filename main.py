from random import randint



boxs = []
a=0


def generator():
    while len(boxs)<7:
        num = randint(1,9)
        #print("First num", num)
        if num not in boxs:
            print("SEcond num", num)

            boxs.append(num)


def operation():
    if randint(0,2) == 1:
        box = randint(1,9)
        #print("First box", box)
        if box not in boxs:
            print("Second box", box)
            a += 1


for i in range(2):
    generator()
    operation()

print(i)