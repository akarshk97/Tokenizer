import matplotlib.pyplot as plt 
  
# x axis values 
x = [10, 20, 40, 80, 100, 200, 300, 400, 500]
# corresponding y axis values 
y = [0.447445, 0.965844, 2.4082930000000005, 5.411306, 6.829598999999998, 12.785421, 19.344015, 23.402112000000002, 29.808220000000006]
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('# of documents') 
# naming the y axis 
plt.ylabel('CPU time elapsed') 
  
# giving a title to my graph 
plt.title('Term Weights') 
  
# function to show the plot 
plt.show() 