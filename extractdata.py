import matplotlib.pyplot as plt
x=[9,3,4,2,5,7,9,0]
y=[3,5,3,6,3,7,4,8]

plt.plot(x,y,c='red')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('graph between x and y')

plt.savefig(r'C:\Users\Dell\OneDrive\Desktop\aiMl Notes\xygraph.png')

plt.show()
