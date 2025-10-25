def get_number_of_steps_to_zero(num: int) -> int:
    count = 0
    while num > 0:
        if num % 2 == 0:
            num /= 2
            count += 1
        else:
            num -= 1
            count += 1
    return count


num = int(input())
print(get_number_of_steps_to_zero(num))
