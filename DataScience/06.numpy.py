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
