import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import numpy as np

# jutyper notebook에 출력하려면
# %matplotlib inline

# from matplotlib import pyplot as plt


# x = np.arange(1,5)
# print(x)
# y = np.arange(2,6)
# print(y)
# y2 = np.array([2,4,6,9])
# print(y2)


# # canvas size 지정 
# fig = plt.figure(figsize=(8,4))

# # title
# plt.title('Income and Life Expectancy')

# # fmt [color][marker][line style]: 
# #    color : black: k
# #            cyan : c
# #    line style :
# #            - : solid line
# #            -- : dashed line
# #            -. : dash-dot line
# #            :  : dotted line style
# # plt.plot(x, y, 'ko')

# plt.plot(x, y, 'yo:' )
# # # graph를 겹쳐 그릴 수 있다.
# plt.plot(x,y2, 'ks--')
# # plt.plot(x,y,y2)

# plt.xlabel("Income")
# plt.ylabel("Life")

# plt.xticks(x)
# plt.yticks(y2)

# plt.grid(True)

# plt.show()

import matplotlib.pyplot as plt

labels = ['Samsung Elec', 'SK Hynix', 'LG Elec', 'NHN', 'KAKAO']
ratio = [50, 20, 10, 10, 10]

plt.pie(ratio, labels=labels, startangle=90)
plt.show()


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()