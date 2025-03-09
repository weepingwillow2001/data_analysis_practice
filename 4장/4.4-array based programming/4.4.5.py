import numpy as np
#np.unique: 중복된 값을 제거 + "정렬"된 배열 반환
names = np.array(["Bob", "Will", "Joe", "Bob", "Will", "Joe", "Joe"])
print(np.unique(names))
#['Bob' 'Joe' 'Will']
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))
#[1 2 3 4]

#np.in1d
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))
# [ True False False  True  True False  True]
#values 배열의 각 원소가 [2, 3, 6] 중 하나인지 검사