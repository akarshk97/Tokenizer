import matplotlib.pyplot as plt 
  
# x axis values 
x = [10, 20, 40, 80, 100, 200, 300, 400, 500]
# corresponding y axis values 
y = [0.40627599999999997, 0.8712909999999999, 2.5278669999999996, 5.477261, 6.884777, 12.283196, 18.417088, 22.479330999999995, 29.002139999999997]
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('# of documents') 
# naming the y axis 
plt.ylabel('CPU time in seconds') 
  
# giving a title to my graph 
plt.title('Term Weights') 
  
# function to show the plot 
plt.show() 