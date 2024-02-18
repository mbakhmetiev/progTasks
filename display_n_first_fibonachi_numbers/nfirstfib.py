#/usr/bin/python
'''
    Пользователь вводит число n
    Необходимо вывести n первых членов последовательности Фибоначчи

    The sequence commonly starts from 0 and 1,
    although some authors start the sequence from 1 and 1 or sometimes (as did Fibonacci) from 1 and 2.
    Starting from 0 and 1, the sequence begins
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
'''

def fib(n):
    if n<= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n_terms = 10
print("Fibonacci sequence:")

for i in range(1, n_terms + 1):
    print(fib(i), end = " ")
