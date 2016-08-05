import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import parallel_coordinates

# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..

data = pd.read_csv('Datasets/wheat.data')

#
# TODO: Drop the 'id', 'area', and 'perimeter' feature
# 
# .. your code here ..

data.drop(['id','area','perimeter'],1,inplace=1)

#
# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
# 
# .. your code here ..
parallel_coordinates(data,'wheat_type',alpha=0.4)


plt.show()


