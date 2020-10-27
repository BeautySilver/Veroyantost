from random import randint



def r():
    result = []
    while len(result) != 7:
        x = randint(0, 7)
        if x not in result:
            result.append(x)

    return result


def put():
    boxes = [0, 0, 0, 0, 0, 0, 0, 0]
    if randint(0, 1) == 1:
        box = randint(0, 7)
        boxes[box] = 1

    return boxes


def choose():
    boxes = put()
    choice = r()
    for i in choice:
        if boxes[i] == 1:
            return -1

    for i in range(8):
        if i not in choice:
            if boxes[i] == 1:
                return 1
            else:
                return 0


result = 0
iterations = 0

for i in range(1000000):
    res = choose()
    if res != -1:
        iterations += 1
        result += res



print(result/iterations)