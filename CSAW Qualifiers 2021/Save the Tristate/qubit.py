from hashlib import new
from pwn import *
import sys

conn = remote('misc.chal.csaw.io', 5001)

flag1 = False
bases = 256
combo = []
for i in range(bases):
    combo.append('+')

#print(combo)

#How many bases would you like to check?
print(conn.recvline())
conn.sendline(bytes(str(bases), 'ascii'))
print(bytes(str(bases), 'ascii'))
#Please enter your 5 bases:
print(conn.recvline())
conn.sendline(bytes((''.join(combo)), 'ascii'))
print(bytes((''.join(combo)), 'ascii'))
#Errors: 2
cur_errors = int(conn.recvline().split(b':')[1])
print('ERRORS: ' + str(cur_errors))
for i in range(bases):
    if cur_errors > 0:
        combo[i] = 'x'
        #How many bases would you like to check?
        #print(conn.recvline())
        conn.recvline()
        conn.sendline(bytes(str(bases), 'ascii'))
        #Please enter your 5 bases:
        #print(conn.recvline())
        conn.recvline()
        conn.sendline(bytes((''.join(combo)), 'ascii'))
        new_errors = int(conn.recvline().split(b':')[1])
        #print('COMBO: ' + (''.join(combo)) + ', NEW ERRORS: ' + str(new_errors) + ', CUR ERRORS: ' + str(cur_errors))
        print('', end = '.')
        if new_errors >= cur_errors:
            combo[i] = '+'
        else:
            cur_errors = new_errors

print('COMBO: ' + (''.join(combo)) + ', NEW ERRORS: ' + str(new_errors) + ', CUR ERRORS: ' + str(cur_errors))

key = []

for i in range(256):
    #print(conn.recvline())
    r = float(conn.recvline().split(b'+')[0])
    if r == 0:
        key.append('1')
    elif r == 1:
        key.append('0')
    elif r == -0.707:
        key.append('1')
    else:
        key.append('0')

print(conn.recvline())
print(''.join(key))
#conn.sendline(bytes((''.join(key)), 'ascii'))
conn.sendline(bytes('a semi-aquatic mammal of action!', 'ascii'))
print(conn.recvline())
