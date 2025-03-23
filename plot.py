import matplotlib.pyplot as plt


x=[1,2,3,4,5]
y=[10,15,45,30,50]
plt.plot(x,y)

plt.plot(x,y, marker='o', linestyle='--',color='green',label='My Line')
plt.xlabel('X-Aixs')
plt.ylabel('Y-Axis')
plt.title('Customized Line Plot')
plt.legend()
plt.show()
