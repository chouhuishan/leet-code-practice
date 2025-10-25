def get_two_integers(n: int) -> list[int]:
    def no_zero_int(num: int) -> bool:
        return "0" not in str(num)  # return False if there is a 0 in the num

    if n < 2:
        raise ValueError("n must be more than 2")
    for a in range(1, n):
        b = n - a
        if no_zero_int(a) and no_zero_int(
            b
        ):  # if no_zero_int(a) and no_zero_int(b) is True
            return [a, b]


n = int(input())
print(get_two_integers(n))
