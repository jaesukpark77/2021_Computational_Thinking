#달력
import calendar


print("당신이 태어난 달의 달력을 보여줍니다~")

year = int(input("몇년도? "))
month = int(input("몇 월? "))
calendar.prmonth(year, month)
