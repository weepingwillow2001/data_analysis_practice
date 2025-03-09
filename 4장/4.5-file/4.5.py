import numpy as np
arr1 = np.arange(10)
np.save("some_array", arr1) #파일 저장
#arr을 some_array 파일로 저장
print(np.load("some_array.npy")) #확장자는 npy를 사용함
# [0 1 2 3 4 5 6 7 8 9]

#savez: save zip, "여러개" 배열을 압축된 형식으로 저장
arr2 = np.arange(20)
np.savez("array_archive.npz", a=arr1, b=arr2)
# a는 첫 번째 배열의 이름
# b는 두 번째 배열의 이름
archive = np.load("array_archive.npz")
print(archive["b"])  # 'b'라는 이름으로 저장된 배열에 접근
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]