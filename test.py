# 입출력과 사칙연산_곱셈
num1 = int(input())
num2 = int(input())
a,b,c = map(int, str(num1))
d,e,f = map(int, str(num2))


print(num1 * f)
print(num1 * e)
print(num1 * d)
print(num1 * num2)

# 두 수 비교하기(백준_1330)
A, B = map(int, input().split())

if 10000 >= A >=-10000 and 10000 >= B >= -10000 :
    if A > B :
        print('>')
    elif A < B :
        print('<')
    else :
        print('==')

# 시험 성적
A =int(input())

if 100 >= A >= 0:
    if 100 >= A >= 90 :
        print('A')
    elif 89 >= A >= 80:
        print('B')
    elif 79 >= A >= 70:
        print('C')
    elif 69 >= A >= 60:
        print('D')
    else :
        print('F')

# 윤년
A =int(input())

if 4000 >= A >= 1 :
    if A % 4 == 0 and A % 100 != 0 or A%100 == 0 and A % 400 == 0 :
        print(1)
    else :
        print(0)

# 사분면 고르기
A = int(input())
B = int(input())

if 1000 >= A >= -1000 and 1000 >= B >= -1000 :
    if A > 0 and B > 0 :
        print(1)
    elif A > 0 and B < 0 :
        print(4)
    elif A < 0 and B > 0 :
        print(2)
    else :
        print(3)
    

