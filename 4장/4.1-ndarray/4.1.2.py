import numpy as np

data1 = [6, 7.5, 8, 0, 1]
arr_1 = np.array(data1)
print(arr_1)
#정수와 소수가 혼합된 경우 float로 출력(모든 데이터는 같은 자료형이어야하므로)

#zeross/ones/empty
print(np.zeros(10)) #또는 ((10,))
#10열 짜리 0
print(np.empty((2, 3, 2))) #초기화되지 않은 배열 생성
#깊이/축, 행, 열
#가장 바깥 대괄호: 전체 배열
#중간 대괄호: 깊이/축 2개
#가장 안쪽 대괄호: 행 3행
#가장 안쪽 대괄호 안 쉼표: 열 2열

print(np.arange(15))
#array_range: range함수 배열 버전

#astype: dtype 변환(~as type)
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)
string_arr = arr.astype(np.string_)
string_arr_1 = arr.astype(np.str_) #b (byte)접두사 없이 출력
print(string_arr)
print(string_arr_1) 

arr_1 = np.array(["1.25", "-9.6", "42"])  # dtype 명시하지 않아도 ok
print(arr_1.astype(float))
#타 배열의 dtype 참조
int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
#dtype을 실수로 명시
print(int_array.astype(calibers.dtype)) #calibers의 dtype 참조
