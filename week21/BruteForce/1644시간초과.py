def is_Prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def Prime_num_list(n):
    result = []
    for i in range(2, n + 1):
        if is_Prime_num(i):
            result.append(i)
    return result


def main():
    n = int(input())
    pnums = Prime_num_list(n)
    cnt = 0

    for i in range(len(pnums)):
        tmp = pnums[i]
        if tmp == n:
            cnt += 1
            break

        addnums = pnums[i + 1:]
        for a in addnums:
            tmp += a

            if tmp == n:
                cnt += 1
                break
            elif tmp > n:
                break
    print(cnt)
    return


main()