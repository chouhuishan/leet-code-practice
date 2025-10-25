def max_num(num: int) -> int:
    num = list(str(num))

    for i, char in enumerate(num):
        if char == "6":
            num[i] = "9"
            break
    res = "".join(num)
    return int(res)


num = int(input())
print(max_num(num))
