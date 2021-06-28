#4번

import numpy as np

score = []
for i in range(5):
    grade = int(input("성적 입력 : "))
    score.append(grade)
    
합 = np.sum(score)    
avg = np.mean(score)

print("합계 : ", 합)
print("평균 : ", avg)