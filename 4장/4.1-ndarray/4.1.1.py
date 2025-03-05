import numpy as np 
data = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])
print(data)
print(data*10)
print(data+data)
#ndarray의 모든 데이터는 같은 자료형이어야함
#바깥 대괄호: 전체 배열
#안쪽 대괄호: 행
#안쪽 대괄호 안 쉼표: 열 구분
#[             ] ← 가장 바깥쪽 대괄호: 전체 배열
#   [xx, yy]      ← 첫 번째 행
#   [zz, hh]      ← 두 번째 행
#       ↑
#      안쪽 콤마: 열 구분
print(data.shape) #2행 3열
print(data.dtype) #실수
print(data.ndim) #2차원
#1차원: 벡터 (단일 행/열)
#2차원: 표
#3차원: 2차원 배열이 여러개 쌓임
#  [[[1, 2], [3, 4]],
#  [[5, 6], [7, 8]]]