import pandas as pd
import matplotlib

matplotlib.style.use('ggplot') # Look Pretty
# If the above line throws an error, use plt.style.use('ggplot') instead

student_dataset = pd.read_csv("students.data", index_col=0) 
student_dataset.plot.scatter(x='G1', y='G3')