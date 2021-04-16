n = int(input())

box = {
    1 : 1,
    2 : 1,
    3 : 1,
    4 : 2,
    5 : 3,
    6 : 2,
    7 : 3,
    8 : 3,
    9 : 2,
    10 : 3
}

for i in range(11, n+1):
     # 경우의 수 1. 2와 3으로 나누어 떨어질 때
    if i % 3 == 0 and i % 2 == 0:
        list = [box[int(i / 2)], box[int(i / 3)], box[i - 1]]
        box[i] = min(list) + 1
    elif i % 3 ==0 and i % 2 != 0:
        list = [box[int(i / 3)], box[i - 1]]
        box[i] = min(list) + 1
    elif i % 3 != 0 and i % 2 == 0:
        list = [box[int(i / 2)], box[i - 1]]
        box[i] = min(list) + 1
    else:
        box[i] = box[i-1] + 1

print(box[n])