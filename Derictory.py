def average(numbers: list):
    summary = 0
    count = 0

    for number in numbers:
        summary += number
        count += 1

    result = summary / count
    if result == round(result):
        return round(result)
    return result


def median(numbers: list):

    some_list = sorted(numbers)
    if len(some_list) % 2 == 1:
        result = some_list[len(some_list) // 2]
    else:
        result = (some_list[len(some_list) // 2 - 1] + some_list[len(some_list) // 2]) / 2
    if result == round(result):
        return round(result)
    return result

def find_max(numbers: list):
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number

    if max_number == round(max_number):
        return round(max_number)
    return max_number


def find_min(numbers: list):
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number

    if min_number == round(min_number):
        return round(min_number)
    return min_number


def amount(numbers: list):
    summary = 0

    for number in numbers:
        summary += number

    result = summary
    if result == round(result):
        return round(result)
    return result


def multiplication(numbers: list):
    multiply = 1

    for number in numbers:
        multiply *= number

    result = multiply
    if result == round(result):
        return round(result)
    return result



