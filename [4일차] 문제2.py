#문제2

midterm = int(input("중간고사: "))
final = int(input("기말고사: "))
ave = (midterm + final) / 2

if ave > 70:
    print("Pass")
else:
    print("Fail")
