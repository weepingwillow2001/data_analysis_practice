#1차원 색인(indexing)
import numpy as np
arr = np.arange(10) # 0부터 10 제외
print(arr)
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[0]) # 0
print(arr[5:8]) # array([5, 6, 7])

#1차원 슬라이싱(slicing)
arr[5:8] = 12
print(arr)
arr_slice = arr[5:8] #12 12 12
print(arr_slice)

arr_slice[0] = 99
print(arr)
arr_slice[:] = 777 # 슬라이싱된 값의 모든 값에 할당
print(arr)

#다차원 색인
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[0])
print(arr_2d[2][0]) # 7
print(arr_2d[0,1]) # 2
#아래 둘은 같은 표현: 행/열

arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr_3d)
print(arr_3d[0]) #[[1, 2, 3], [4, 5, 6]]
print(arr_3d[1, 0, 2]) #축/행/열 순서 9

#다차원 슬라이싱
print(arr_2d[0:2]) #2차원의 경우 행을 기준으로 판단
#[[1 2 3]
# [4 5 6]]
print(arr_2d[:2, 1:]) #행/열
#[[2 3]
# [5 6]] !!!

lower_dim_arr = arr_2d[1, :2]
print(lower_dim_arr) #두 번째 행의 처음 두 열만 선택
#[4 5]  
print(lower_dim_arr.ndim) #1 차원

lower_dim_arr_2 = arr_2d[:2, 2]
print(lower_dim_arr_2) #처음 두 행의 세번째 열만 선택
#[3 6]
print(lower_dim_arr_2.ndim) #1 차원
#이처럼 정수! index와 slicing을 함께 사용하면 한차원 낮은 슬라이스를 얻게됨!!

print(arr_2d[ : , :1]) #모든 행의 첫번째 열만 선택(1 미만이므로)
# [[1]
#  [4]
#  [7]]

arr_2d[:2, 1:] = 0 #처음 두 행의 두번째 열부터 선택
print(arr_2d)
#array([[1, 0, 0],
#       [4, 0, 0],
#       [7, 8, 9]])