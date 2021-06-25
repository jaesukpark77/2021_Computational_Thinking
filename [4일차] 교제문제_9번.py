#9번

출생년도 = int(input("출생년도 ? "))

나이 = 2021 - 출생년도 + 1

print("올해 %d살이겠군요." %나이)

if 1<= 나이 <=7:
    print("어린이")
elif 나이 <= 13:
    print("초등학생")
elif 나이 <= 16:
    print("중학생")
elif 나이 <= 19:
    print("고등학생")
elif 나이 <= 26:
    print("대학생")
else:
    print("직장인")