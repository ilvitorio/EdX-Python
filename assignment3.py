import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
data = pd.read_csv('Datasets/wheat.data')


fig = plt.figure()
#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the area,
# perimeter and asymmetry features. Be sure to use the
# optional display parameter c='red', and also label your
# axes
# 
# .. your code here ..
plot1 = fig.add_subplot(111,projection='3d')
plot1.set_xlabel('area')
plot1.set_ylabel('perimeter')
plot1.set_zlabel('asymmetry')
plot1.scatter(data['area'],data['perimeter'],data['asymmetry'],c='red',marker='.')


fig = plt.figure()
#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the width,
# groove and length features. Be sure to use the
# optional display parameter c='green', and also label your
# axes
# 
# .. your code here ..

plot1 = fig.add_subplot(111,projection='3d')
plot1.set_xlabel('width')
plot1.set_ylabel('groove')
plot1.set_zlabel('length')
plot1.scatter(data['width'],data['groove'],data['length'],c='green',marker='.')

plt.show()


