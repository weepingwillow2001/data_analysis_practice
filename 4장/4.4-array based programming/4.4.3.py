import numpy as np
rng = np.random.default_rng(seed=12345)
arr = rng.standard_normal(100)

print((arr > 0).sum()) #양수인 값의 "개수" (true = 1, flase = 0)
print((arr <= 0).sum()) # 0이하 값의 "개수"
#NumPy에서 배열에 비교 연산자를 적용하면 무조건 불리언 배열이 생성!!

#any: 배열에 True 값이 하나라도 있으면 True를 반환합니다
#all: 배열의 모든 값이 True인 경우에만 True를 반환합니다.

bools = np.array([False, False, True, False])
print(bools.any())  # 결과: True
print(bools.all()) # 결과: False

#숫자 배열: 0이 아닌 모든 값은 True로, 0은 False로 간주.
bools = np.array([0, 0, 0, 0])
print(bools.any()) # 결과: False
bools = np.array([12, 44, 57, 6])
print(bools.all()) # 결과: True