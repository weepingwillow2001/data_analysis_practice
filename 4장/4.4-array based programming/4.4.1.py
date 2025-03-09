#numpy.where
#np.where(조건, 조건이_참일_때_값, 조건이_거짓일_때_값)
import numpy as np

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

result = np.where(cond, xarr, yarr)
print(result)
# [1.1 2.2 1.3 1.4 2.5]

rng = np.random.default_rng(seed=12345)  # 시드값으로 난수 생성기 초기화
arr = rng.standard_normal((4, 4))  # 4x4 크기의 표준 정규 분포 난수배열 생성
print(arr)
print(arr > 0) #0보다 큰지 비교하여 불리언 배열 생성
np.where(arr > 0, 2, -2) #조건, 참 값, 거짓 값
np.where(arr > 0, 2, arr)  # 양수인 경우에만 값을 2로 변경

#NumPy에서 배열에 비교 연산자를 적용하면 무조건 불리언 배열이 생성!!!!