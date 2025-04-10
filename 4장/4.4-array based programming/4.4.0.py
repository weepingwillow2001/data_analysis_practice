#numpy.meshgrid
#"두 개"의 1 차원 배열(points)을 받아 
#모든 x, y 짝을 만들 수 있는 2차원 배열(표) "두 개"(xs, ys)를 반환
import numpy as np
points = np.arange(-5, 5, 0.01) #-5부터 4.99까지 0.01 만큼 증가
xs, ys = np.meshgrid(points, points)
print(xs)
# [[-5.   -4.99 -4.98 ...  4.97  4.98  4.99]
#  [-5.   -4.99 -4.98 ...  4.97  4.98  4.99]
#  [-5.   -4.99 -4.98 ...  4.97  4.98  4.99]
#  ...
#  [-5.   -4.99 -4.98 ...  4.97  4.98  4.99]
#  [-5.   -4.99 -4.98 ...  4.97  4.98  4.99]
#  [-5.   -4.99 -4.98 ...  4.97  4.98  4.99]]
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)
# [[7.07106781 7.06400028 7.05693985 ... 7.04988652 7.05693985 7.06400028] 
#  [7.06400028 7.05692568 7.04985815 ... 7.04279774 7.04985815 7.05692568] 
#  [7.05693985 7.04985815 7.04278354 ... 7.03571603 7.04278354 7.04985815] 
#  ...
#  [7.04988652 7.04279774 7.03571603 ... 7.0286414  7.03571603 7.04279774] 
#  [7.05693985 7.04985815 7.04278354 ... 7.03571603 7.04278354 7.04985815] 
#  [7.06400028 7.05692568 7.04985815 ... 7.04279774 7.04985815 7.05692568]]