import matplotlib.pyplot as plt 
  
# x axis values 
#x = [10, 20, 40, 80, 100, 200, 300, 400, 500]
y =[48, 69, 162, 279, 323, 491, 622, 799, 923]
# corresponding y axis values 
#y = [0.40627599999999997, 0.8712909999999999, 2.5278669999999996, 5.477261, 6.884777, 12.283196, 18.417088, 22.479330999999995, 29.002139999999997]
#y =[0.6593760000000001, 1.3277500000000002, 3.901822, 9.405406, 12.490525, 25.212403000000002, 37.449824, 53.431297000000015, 70.36403100000001] 
x = [147, 238, 479, 913, 1024, 2048, 3788, 7680, 13004]
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('file size of input documents') 
# naming the y axis 
plt.ylabel('file size of dictinaryFile and postingsFile') 
  
# giving a title to my graph 
plt.title('size efficiency') 
  
# function to show the plot 
plt.show() 

#0.733292, 1.6937799999999998, 6.705661, 20.264395, 29.847214, 87.55227200000002, 188.706194, 383.326, 614.727929