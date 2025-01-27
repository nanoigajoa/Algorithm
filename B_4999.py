import sys
input = sys.stdin.readline

jaehwan = input()
doctor = input()

if len(jaehwan) >= len(doctor):
    print('go')
else:
    print('no')