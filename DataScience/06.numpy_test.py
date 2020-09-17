import numpy as np

print(np.__version__)

a = np.array([1,2,3,4])
print(a) # 리스트와 구분하기 위해 쉼표가 없이 출력된다 
print("a.dtype : {}".format(a.dtype))
print("a.ndim : {}".format(a.ndim))
print("a.shape : {}".format(a.shape))
print("a.itemsize : {}".format(a.itemsize))
print("a.strides : {}".format(a.strides))
print("a.data : {}".format(a.data))         # 메모리 주소값
print("a.data.obj : {}".format(a.data.obj))  # 헤당 매모리 주소값의 참조값
print("a.tolist() : {}".format(a.tolist()))  # 리스트로 변환 
print("dir(a) : {}".format(dir(a)))

b = np.array([[1,2,3,4],[5,6,7,8]])
print(b)
print("b.dtype : {}".format(b.dtype))
print("b.ndim : {}".format(b.ndim))
print("b.shape : {}".format(b.shape))
print("b.itemsize : {}".format(b.itemsize))
print("b.strides : {}".format(b.strides))
print("b.data : {}".format(b.data))         # 메모리 주소값
print("b.data.obj : {}".format(b.data.obj))  # 헤당 매모리 주소값의 참조값
print("b.tolist() : {}".format(b.tolist()))  # 리스트로 변환 

print("row : {}".format(b.shape[0]))
print("coumn : {}".format(b.shape[1]))

c = b.copy()


a  = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

# row를 1차원 배열로 반환
print("a[0] \n {}".format(a[0]))

# row를 2차원 배열로 반환
print("a[[0]] \n {}".format(a[[0]]))

# np.array[row, column]
print("a[0,2] \n {}".format(a[0,2]))

# np.array[[row, row]]
print("a[[0,2]] \n {}".format(a[[0,2]]) )

# np.array[:,[0,2]] 이면 0, 2번째 행의 모든 열을 출력
print("a[:, [0,2]] \n {}".format(a[:,  [0,2]]))

# 열과 행에 모두 리스트를 적용하는 것은 제대로 되지 않는다. 이 경우는 열의 조건과 행의 조건을 만족하는 [1 9]가 출력
print("a[[0,2], [0,2]] \n {}".format(a[[0,2],  [0,2]]))

# 열과 행에 모두 리스트를 적용하려면 np.ix_를 사용해야 한다.
print("a[np.ix_([0,2],[0,2])] \n {}".format(a[np.ix_([0,2],[0,2])]))

# 논리 검색시 and, or를 사용할 수 없다. &, |를 사용해야 한다.
print("a[a>5] \n {}".format(a[a>5]))


print("a[(a>5) & (a<8)] \n {}".format(a[(a>5) & (a<8) ]))

# array간의 결합
A = np.arange(1,10).reshape(3,3)
print(A)

B = np.arange(11,14).reshape(1,3)
print(B)

# vertical 결합 : axis=0
print(np.append(A,B, axis=0))

# horizontal 결합 : axis=1
print(np.append(A,B.T, axis=1))

y = np.linspace(1,10,10)
print(y)


print(y+y)
print(y.__add__(y))
print(np.add(y,y))

# sum
print(y.sum())

# cumulative sum
print(y.cumsum())

# 다차원배열일 경우
a = np.arange(1,11).reshape(2,5)
print(a)
# axis=0 : column별 sum
print(np.sum(a, axis=0))
# axis=1 : row별 sum
print(np.sum(a, axis=1))

# axis=0 : column별 max
print(np.max(a, axis=0))
# axis=1 : row별 max
print(np.max(a, axis=1))


# product (factorial)
print(y.prod())

# cumulative product
print(y.cumprod())

# power
print(np.power(y, 2))

# exponential
print(np.exp(y))

# log (natural)
print(np.log(y))

# log 10
print(np.log10(y))


a = np.array([[1,2,3],[3,2,1]])
# unique 값 
print(np.unique(a))
# inld(a, b) : a에서 b가 있는지 여부의 1차원 배열
print(np.in1d(a, 2))
# isin(a, b) : a에서 b가 있는지 여부의 a의 차원 배열
print(np.isin(a, 2))

# 차집합 a-b
b = np.array([[1,2,7],[4,5,6]])
print(a.shape == b.shape)
print(np.setdiff1d(a, b))

# 교집합 
print(np.intersect1d(a, b))

# 합집합 
print(np.union1d(a, b))

# 대칭차집합 = 합집합 - 교집합
print(np.setxor1d(a, b))

import matplotlib.pyplot as plt

# random normal distribution
mu = 0
sigma =  0.1
number = 1000000
rd = np.random.normal(mu, sigma, number)
print(rd)
plt.hist(rd)
plt.xlabel("number")
plt.ylabel("frequency")
plt.savefig('normal_dist.png')
# plt.show()
plt.close()

# random uniform distribution
# uniform(low, high, size)
ud = np.random.uniform(0, 2, 1000000)
print(ud)
plt.hist(ud)
plt.xlabel("number")
plt.ylabel("frequency")
plt.savefig('uniform_dist.png')
plt.close()

a = np.arange(1,10)
b = np.arange(3,12)
print(dir(a))
print(type(a))
# a의 type이 numpy인지 여부 
print(type(a).__module__ == np.__name__)
# a와 b의 size가 같은지 여부
print(a.shape==b.shape)
print(a)
print(b)

# element add
try :
    print(a+b)
except Exception as e:
    print(e)

# element subtract
try :
    print(a-b)
except Exception as e:
    print(e)

# element mutiply
try :
    print(a*b)
except Exception as e:
    print(e)

# inner product
try :
    print(np.inner(a, b))
except Exception as e:
    print(e)

# dot product
try :
    print(np.dot(a, b))
except Exception as e:
    print(e)

# dot product
try :
    print(a.dot(b))
except Exception as e:
    print(e)

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[9,8,7],[6,5,4],[3,2,1]])
try :
    print(np.dot(A, B))
except Exception as e:
    print(e)

# [[ 30  24  18]
#  [ 84  69  54]
#  [138 114  90]]

C = np.array([[9,8,7]])
try :
    print(np.dot(A, C.T))
except Exception as e:
    print(e)

from numpy import linalg as la 
# determinant
print(la.det(B))

# ivnerse matrix
print(la.inv(B))

# identity matrix (단위행렬)
print(np.eye(3))

# eigen value, eigen vector
v, w = la.eig(B)
print(v)
print(w)

# 0으로 이루어진 행렬
print(np.zeros((3,7)))