#ufunc: 배열의 모든 요소에 한 번에 연산을 적용
#ufunc 목록
# 수학 연산 ufunc>

# np.add(x, y): 두 배열의 요소별 덧셈 (x + y)
# np.subtract(x, y): 두 배열의 요소별 뺄셈 (x - y)
# np.multiply(x, y): 두 배열의 요소별 곱셈 (x * y)
# np.divide(x, y): 두 배열의 요소별 나눗셈 (x / y)
# np.power(x, y): x의 y제곱 (x ** y)
# np.sqrt(x): 제곱근
# np.exp(x): 지수 함수 (e^x)
# np.log(x), np.log10(x): 자연로그, 상용로그

# 삼각함수 ufunc>

# np.sin(x), np.cos(x), np.tan(x): 삼각함수
# np.arcsin(x), np.arccos(x), np.arctan(x): 역삼각함수

# 비교 연산 ufunc>

# np.greater(x, y): x > y
# np.less(x, y): x < y
# np.equal(x, y): x == y
# np.maximum(x, y): 두 배열에서 각 위치별 최댓값
# np.minimum(x, y): 두 배열에서 각 위치별 최솟값

# 기타 유용한 ufunc>

# np.abs(x): 절댓값
# np.floor(x): 내림
# np.ceil(x): 올림
# np.round(x): 반올림
import numpy as np

arr = np.arange(10)
print(arr) #[0 1 2 3 4 5 6 7 8 9]
print(np.sqrt(arr)) #[0.         1.         1.41421356 1.73205081 2.         2.23606798  2.44948974 2.64575131 2.82842712 3.        ]
print(np.exp(arr)) #[1.00000000e+00 2.71828183e+00 7.38905610e+00 2.00855369e+01  5.45981500e+01 1.48413159e+02 4.03428793e+02 1.09663316e+03  2.98095799e+03 8.10308393e+03]

rng = np.random.default_rng(seed = 12345)
x = rng.standard_normal(8)
y = rng.standard_normal(8)
print(x) #[-1.42382504  1.26372846 -0.87066174 -0.25917323 -0.07534331 -0.74088465  -1.3677927   0.6488928 ]
print(y) #[ 0.36105811 -1.95286306  2.34740965  0.96849691 -0.75938718  0.90219827  -0.46695317 -0.06068952]
print(np.maximum(x, y)) #[ 0.36105811  1.26372846  2.34740965  0.96849691 -0.07534331  0.90219827  -0.46695317  0.6488928 ]
#짝을 이루어 비교

#np.modf: 소수부(remainder)와 정수부(whole_part)로 분리
arr = rng.standard_normal(7) * 5  # 표준정규분포에서 7개 표본 추출 후 5를 곱함
print(arr)  # [4.5146, -8.1079, -0.7909, 2.2474, -6.718, -0.4084, 8.6237]

remainder, whole_part = np.modf(arr)  # 소수부와 정수부 분리

print(remainder)  # [0.5146, -0.1079, -0.7909, 0.2474, -0.718, -0.4084, 0.6237]
print(whole_part)  # [4., -8., -0., 2., -6., -0., 8.]

arr = np.array([4.5146, -8.1079, -0.7909, 2.2474, -6.718, -0.4084, 8.6237])

# arr과 같은(like) 크기의 0으로 채워진 배열 생성
out = np.zeros_like(arr)

# arr + 1 계산
print(np.add(arr, 1))  # [5.5146, -7.1079, 0.2091, 3.2474, -5.718, 0.5916, 9.6237]

# arr + 1 계산 결과를 out에 저장
np.add(arr, 1, out=out)
#arr + 1 계산 결과를 새 배열을 생성하지 않고 
#미리 준비한 out 배열에 직접 저장->메모리 효율적

print(out)  # [5.5146, -7.1079, 0.2091, 3.2474, -5.718, 0.5916, 9.6237]