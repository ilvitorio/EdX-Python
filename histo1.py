import pandas as pd
import matplotlib
matplotlib.style.use('ggplot') # Look Pretty
# If the above line throws an error, use plt.style.use('ggplot') instead

student_dataset = pd.read_csv("students.data", index_col=0)

my_series = student_dataset.G3
my_dataframe = student_dataset[['G3', 'G2', 'G1']] 

my_series.plot.hist(alpha=0.5)
my_dataframe.plot.hist(alpha=0.5)