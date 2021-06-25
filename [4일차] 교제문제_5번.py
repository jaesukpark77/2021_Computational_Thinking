#5번

n = int(input("정수 입력?"))

if n<0 or n==0:
    print("잘못된 입력")
elif n%3==0:
    print("3의 배수")
    
else:
    print("3의 배수 아님")