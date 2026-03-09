print('나의 이름은 :', '홍길동')
print('나의 나이는 :', 27)
print('나의 키는', 179, 'cm 입니다.')
print('10 + 20 =', 10 +20)
print('10 * 20 =', 10 * 20)

name = '전우치'
print('나의 이름은 :', name)
age = 27
print('나의 나이는 :', age)
height = 179
print('나의 키는', height, 'cm 입니다.')
sum = 10 + 20
print('10 + 20 =', sum)
mult = 10 * 20
print('10 * 20 =', mult)

#LAB 2-6 : 변수 값의 재지정
width = 20
height = 40
width = 30
area = width * height
print('사각형의 면적', area)


#LAB 2-7 : 파이썬 연산자의 사용
print('123*456 =', 123 * 456)
print('1357 * 2468 =', 1357 * 2468)
print('5 ** 4 =', 5 ** 4)
print('10 / 4 =', 10 / 4)
print('10 // 5 =', 10 // 5)
print('10 % 5 =', 10 % 5)

print('5 // 2 =', 5 // 2)
print('2 ** 0.5 =', 2 ** 0.5)
print('3 ** 0.5 =', 3 ** 0.5)

#LAB 2-8 : 복소수의 연산
a = 8+2j
b = 4+3j
print('a+b =', a+b)
print('a-b =', a-b)
print('a*b =', a*b)
print('a/b =', a/b)

#LAB 2-9 : 비트 연산 활용
a = 1024
a = 1024
print(a >> 1)   
print(a >> 2)   
a = a >> 1
print(a)      

a = a >> 1
print(a)        

a = 1
print(a << 1)   

a = a << 1
print(a)       

a = a << 1
print(a)       

a = a << 1
print(a)       

a = a << 1
print(a)        

#LAB 2-10 : 사용자 입력 받기
name = input('이름을 입력하세요 :')
print(name, '님이 입장하였습니다.')

m = int(input('숫자 m을 입력하세요 : '))
n = int(input('숫자 n을 입력하세요 : '))
print('m + n =', m + n)
print('m - n =', m - n)

r = int(input("반지름 입력: "))
area = 3.14 * r * r
print("원의 면적:", area)

