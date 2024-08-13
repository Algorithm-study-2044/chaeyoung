# 왜 안 돼? 왜 시간초과?

def is_Prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def Prime_num_list(n):
    result = []
    for i in range(2, n+1):
        if is_Prime_num(i):
            result.append(i)
    return result

def main():
    n = int(input())
    pnums = Prime_num_list(n)
    #print(pnums)

    cnt = 0

    l, r = 0, 0
    tmpSum = pnums[0]

    while l < len(pnums):
        print(f"{pnums[l]}부터 {pnums[r]}의 합은 {tmpSum}이다")
        if tmpSum == n:
            cnt += 1
            tmpSum -= pnums[l]
            l += 1

        elif tmpSum < n:
            if r == len(pnums) - 1:
                break
            else:
                r += 1
                tmpSum += pnums[r]
        elif tmpSum > n:
            tmpSum -= pnums[l]
            l += 1

    print(cnt)
    return

main()