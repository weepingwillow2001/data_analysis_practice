#불리언
import numpy as np
names = np.array(["Bob", "Joe", "Ed", "Bob", "Ed", "Joe", "Joe"])
data = np.array([[4, 7], [0, 2], [-5, 6], [0, 0], [1, 2], [-12, -4], [3, 4]])
print(names =="Ed") 
#[False False  True False  True False False]
print(data[names == "Ed", 1: ]) #True만: 3번째 & 5번째 행 // 2번째 열
# [[6]
#  [2]]
print(data[names == "Ed", 1]) #정수 인덱스와 슬라이싱 함께 사용
#[6 2] 

#Ed가 아닌 항목을 선택하려면: !=  //  ~() 사용
print(names != "Ed")
print(~(names == "Ed"))
#[ True  True False  True False  True  True]
a = names == "Ed"
print(data[~a, 1:])
# [[ 7]
#  [ 2]
#  [ 0]
#  [-4]
#  [ 4]]

#and(&) or(|)
c = (names == "Ed") | (names == "Bob")
print(c)
print(data[c])
# [[ 4  7]
#  [-5  6]
#  [ 0  0]
#  [ 1  2]]

data[data < 0] = 0
print(data)
#[[4 7]
# [0 2]
# [0 6]
# [0 0]
# [1 2]
# [0 0]
# [3 4]]
data[names != "Ed", :1 ] = 7
print(data)
# [[7 7]
#  [7 2]
#  [0 6]
#  [7 0]
#  [1 2]
#  [7 0]
#  [7 4]]