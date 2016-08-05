import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..

data = pd.read_csv('Datasets/wheat.data')

#
# TODO: Drop the 'id' feature
# 
# .. your code here ..

data.drop('id',1,inplace=True)

#
# TODO: Compute the correlation matrix of your dataframe
# 
# .. your code here ..

correlationMatrix = data.corr(method='pearson')

#
# TODO: Graph the correlation matrix using imshow or matshow
# 
# .. your code here ..

#Create the figure plot
plt.figure()

#Create the Matshow figure to modify
plt.matshow(correlationMatrix, cmap=plt.cm.Blues)
#Add to the figure the range
plt.colorbar()
#Auxiliary variables
tick_marks = [i for i in range(len(correlationMatrix.columns))]
#add the names for each grid in the x axis
plt.xticks(tick_marks, correlationMatrix.columns, rotation='vertical')
#add the names for each grid point in the y axis
plt.yticks(tick_marks, correlationMatrix.columns)
#show the graph
plt.show()
