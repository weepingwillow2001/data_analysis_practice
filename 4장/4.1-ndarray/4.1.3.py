#배열의 산술연산: 반복문(for) 사용하지 않고 벡터화( 전체 배열에 대해 한 번에 연산을 수행하는 것을 의미)함
import numpy as np
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr)
print(arr * arr)
# array([[ 1.,  4.,  9.],
#        [16., 25., 36.]])
print(arr - arr)
# array([[0., 0., 0.],
#        [0., 0., 0.]])

#스칼라 인수(단일 값: 1, 2, -10..)
arr_s = np.array([[1., 2., 3.], [4., 5., 6.]])

print(1 / arr_s) #1이 스칼라 인수
# 결과:
# array([[1.    , 0.5   , 0.3333],
#        [0.25  , 0.2   , 0.1667]])

print(arr_s ** 2)
# 결과:
# array([[ 1.,  4.,  9.],
#        [16., 25., 36.]])

#비교 연산: 불리언 값 도출
arr_b = np.array([[0., 4., 1.], [7., 2., 12.]])

print(arr_b)
# 결과:
# array([[ 0.,  4.,  1.],
#       [ 7.,  2., 12.]])

print(arr_b > arr)
# 결과:
# array([[False,  True, False],
#       [ True, False,  True]])