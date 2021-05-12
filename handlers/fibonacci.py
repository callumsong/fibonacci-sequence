import logging


def get_fibonacci_sequence(number):
    previous = 0
    latest = 1
    for x in range(number - 1):
        temp = latest
        latest = previous + latest
        previous = temp
    logging.info("Fibonacci Number is " + str(previous))
    return {"value": previous}
