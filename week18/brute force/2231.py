n = input()
a = min(int(n), len(n) * 9) # 각 자릿수 합 최대

n = int(n)

while True:
    sum = 0
    for i in str(n-a):
        sum += int(i)

    if sum == a:
        print(n-a)
        break

    a -= 1

    if a == 0:
        print(0)
        break




