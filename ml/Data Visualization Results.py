import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

values = np.array([9534092, 50541, 98755, 120705])
cnf_mat = values.reshape(2, 2)
print(cnf_mat)

#Code to generate heatmap given a confusion matrix

def heatMap(cnf_mat):
    heat_map = sns.heatmap(cnf_mat, annot=True, cmap="YlGnBu", fmt='g')
    plt.title('Confusion matrix')
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')
    plt.show()
    return heat_map

heatMap(cnf_mat)
