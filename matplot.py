import matplotlib.pyplot as plt

data = [[1,2],[2,3]]

# plt.plot(data)
x=[1,2,3]
y=[2,4,6]
x2=[3,5,7]
y2=[1,7,0]
plt.plot(x,y,linewidth=3,label='first')
plt.hist(x2,linewidth=2, label='DECOND')
plt.hist(y2, label='second')
plt.title('data of my life')
plt.xlabel("age")
plt.ylabel("up and down")
plt.legend()
plt.show()

