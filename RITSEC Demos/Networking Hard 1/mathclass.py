from hashlib import new
from pwn import *
import sys
import statistics

conn = remote('192.168.74.133', 10000)


def parse(problem):
    op = (((problem.split(' '))[0]).split(':'))[1]
    size = (((problem.split(' '))[1]).split(':'))[1]

    numbers = get_num(int(size))

    print(str(numbers))
    if op == 'mean':
        ans = round(statistics.mean(numbers))
        print('ans = ' + str(ans))
        conn.sendline(bytes(str(ans), 'ascii'))
    elif op == 'median':
        ans = round(statistics.median(numbers))
        print('ans = ' + str(ans))
        conn.sendline(bytes(str(ans), 'ascii'))
    elif op == 'range':
        ans = max(numbers) - min(numbers)
        print('ans = ' + str(ans))
        conn.sendline(bytes(str(ans), 'ascii'))
    elif op == 'minimum':
        ans = min(numbers)
        print('ans = ' + str(ans))
        conn.sendline(bytes(str(ans), 'ascii'))
    elif op == 'maximum':
        ans = max(numbers)
        print('ans = ' + str(ans))
        conn.sendline(bytes(str(ans), 'ascii'))
    else:
        print("???Shouldn't be here???")


def get_num(size):
    numbers = []
    for i in range(size):
        numbers.append(int(str(conn.recvline())[2:-3]))
    return numbers


def main():
    flag = False
    line = 0
    while flag == False:
        line += 1
        string = str(conn.recvline())[2:-3]
        if 'problem:' in string:
            print('FOUND IT: ' + string + ', line: ' + str(line))
            flag = True
    for i in range(100):
        parse(string)
        print(conn.recvline())
        string = str(conn.recvline())[2:-3]
        print(string)


if __name__ == '__main__':
    main()
