def sum(*nums):
    result = 0
    for num in nums:
        result += num
    return result


def human(**data):
    for keys, values in data.items():
        print(f"{keys}: {values}")


print(sum(1, 2, 5, 6, 45, 34, 6, 76, 2, 23, 4, 46, 34))

human(
    name="jash",
    age=40,
    subject="Python"
)
