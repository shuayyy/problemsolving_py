
#!/bin/python3


def weirdorot(n):
    if n % 2 != 0:  # Odd numbers
        result = 'Weird'
    elif n % 2 == 0 and 2 <= n <= 5:  # Even numbers in range 2-5
        result = 'Not Weird'
    elif n % 2 == 0 and 6 <= n <= 20:  # Even numbers in range 6-20
        result = 'Weird'
    elif n % 2 == 0 and n > 20:  # Even numbers greater than 20
        result = 'Not Weird'
    return result


if __name__ == '__main__':
    n = int(input().strip())
    print(weirdorot(n))
