import numpy as np

# jutyper notebook에 출력하려면
# %matplotlib inline

from matplotlib import pyplot as plt


x = np.arange(1,5)
print(x)
y = np.arange(2,6)
print(y)
y2 = np.array([2,4,6,9])
print(y2)


# canvas size 지정 
fig = plt.figure(figsize=(8,4))

# title
plt.title('Income and Life Expectancy')

# fmt [color][marker][line style]: 
#    color : black: k
#            cyan : c
#    line style :
#            - : solid line
#            -- : dashed line
#            -. : dash-dot line
#            :  : dotted line style
# plt.plot(x, y, 'ko')

plt.plot(x, y, 'yo:' )
# # graph를 겹쳐 그릴 수 있다.
plt.plot(x,y2, 'ks--')
# plt.plot(x,y,y2)

plt.xlabel("Income")
plt.ylabel("Life")

plt.xticks(x)
plt.yticks(y2)

plt.grid(True)

plt.show()

