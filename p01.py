#이름 : 이돈규
#학과 : 인공지능소프트웨어

#1. if문 
x = 100
if x > 1:
    print("x는 1보다 큽니다.")

#2. if-else문
score = 60
if score >= 60:
    print("합격")
else :
    print("불합격")

#3.
num = int(input("양의 정수를 입력하시오: "))
if num % 2 == 0:
    print("짝수입니다")
else :
    print("홀수입니다")

#4.
num = int(input("수를 입력하세요: "))
if num < 0:
    print("음수입니다")
else :
    print("양수입니다")
    if num % 2 == 0:
        print("짝수입니다")
    else :
        print("홀수입니다")

#5.
age=int(input("나이를 입력하시오: "))
if age >= 15:
    print("본 영화를 보실 수 있습니다.")
else :
    print("본 영화를 보실 수 없습니다.")