import numpy as np
x = np.array([[1., 2., 3.], [4., 5., 6.]])
# [[1. 2. 3.]
#  [4. 5. 6.]]
y = np.array([[6., 23.], [-1, 7], [8, 9]])
# [[ 6. 23.]
#  [-1.  7.]
#  [ 8.  9.]]
print(x.dot(y)) #는 np.dot(x, y)와 동일(내적구하기)
# [[ 28.  64.]
#  [ 67. 181.]]

#행렬곱셈연산자 @
result = x @ np.ones(3) #x.dot(np.ones(3))와 동일
#[1, 1, 1]과 x의 내적 구하기
print(result)
# [ 6. 15.]



#numpy.linalg
import numpy as np
from numpy.linalg import inv # 역행렬과 QR분해 함수 임포트

# 랜덤 행렬 생성
rng = np.random.default_rng(seed=12345)
X = rng.standard_normal((5, 5))

# X의 전치행렬과 X의 곱 (X^T * X)
matrix = X.T @ X #X.T.dot(X)와 동일

# 역행렬 계산
print(inv(matrix))
# 결과: 역행렬 출력 (5x5 행렬)

# 원래 행렬과 역행렬의 곱 (단위행렬이 나와야 함)
print(matrix @ inv(matrix))
# 결과: 단위행렬에 가까운 값 출력 (소수점 오차 있음)


# numpy.linalg의 중요한 함수들:
# inv(a): 행렬 a의 역행렬을 계산합니다.
# 예: inv(mat)는 mat의 역행렬을 반환


# solve(a, b): 선형 방정식 ax = b의 해를 계산합니다.
# inv보다 수치적으로 안정적이므로 역행렬을 구하는 대신 이 함수를 사용하는 것이 좋습니다.


# det(a): 행렬 a의 행렬식(determinant)을 계산합니다.
# 행렬이 특이행렬인지 확인하는 데 유용합니다.


# eig(a): 정방행렬 a의 고유값과 고윳값을 계산합니다.
# eigenvalues, eigenvectors = np.linalg.eig(a)


# qr(a): QR 분해를 수행합니다 (직교행렬 Q와 상삼각행렬 R).
# q, r = np.linalg.qr(a)


# svd(a): 특이값 분해(Singular Value Decomposition)를 수행합니다.
# u, s, vh = np.linalg.svd(a)
# 주성분 분석(PCA)이나 데이터 압축에 유용합니다.


# norm(x): 벡터나 행렬의 노름(norm)을 계산합니다.
# 기본적으로 프로베니우스 노름(Frobenius norm)을 계산합니다.