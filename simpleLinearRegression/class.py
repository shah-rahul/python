import numpy as np  
import matplotlib.pyplot as plt
  
# random is a function, doing random sampling in numpy.
array = np.random.binomial(1, 0.5, 20)

fig = plt.figure(figsize =(10, 7))
 
plt.hist(array, bins = [0, 0.1,0.2,0.3,0.4, 0.5, 0.6, 0.7,0.8 ,0.9 ,1],),
 
plt.title("Numpy Histogram")
 
# show plot
plt.show()
# the array will be having 20 elements.
print(array)