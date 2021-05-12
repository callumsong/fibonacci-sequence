def get_fibonacci_sequence(number):
    previous = 0
    latest = 1
    for x in range(number - 1):
        temp = latest
        latest = previous + latest
        previous = temp
    return {"value": previous}
