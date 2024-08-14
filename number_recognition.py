import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt
import seaborn as sns

digits_img = pd.read_csv("train.csv")
y = digits_img.label
digits_img.drop(columns = ["label"], inplace = True)

digits = digits_img

#scaler = StandardScaler()
#digits = scaler.fit_transform(digits)

pca = PCA(n_components = 400, random_state = 100)
digits = pca.fit_transform(digits)
digits = pd.DataFrame(digits)
model = KMeans(n_clusters = 10, random_state = 100)
model.fit(digits)

y_pred = model.predict(digits)

matrix = pd.DataFrame(confusion_matrix(y, y_pred))

row_ind, col_ind = linear_sum_assignment(-matrix)
label_map = {col:row for row, col in zip(row_ind,col_ind)}

y_rpred = [label_map[y] for y in y_pred]

matrix = matrix[list(label_map.keys())]
matrix.columns = [0,1,2,3,4,5,6,7,8,9]

print(digits)
"""
sns.set(style = "whitegrid")
fig = plt.figure(figsize = (10,8))
ax = fig.add_subplot(111, projection = "3d")
groups = range(10)
colors = ["#E6194B","#3CB44B","#0082C8","#FFE119","#F58231","#911EB4","#46F0F0","#F032E6","#D2F53C","#FABEBE"]
for group, color in zip(groups, colors):
    subset = digits[digits.target == group]
    ax.scatter(xs = subset["pixel0"], ys = subset["pixel1"], zs = subset["pixel2"], c = color , label = group, s = 1, alpha = 0.2)
plt.show()

fig = plt.figure(figsize = (10,10))
for i in range(100):
    sub = fig.add_subplot(10, 10, i + 1, xticks = [], yticks = [])
    sub.set_title("Predicted: " + str(y_rpred[i]))
    sub.imshow(np.array(digits_img.iloc[i]).reshape(-1,28), cmap = "gray")
plt.tight_layout()
plt.show()
"""
correct = 0
for i in range(len(y)):
    if y[i] == y_rpred[i]:
        correct += 1
correct_percent = correct / len(y)
print(correct_percent)
#0.5418809523809524 accuracy without scaling nor PCA
#0.49123809523809525 accuracy with standard scaling not PCA
#0.5845238095238096 accuracy with PCA components set to 400 (approx max)
#Min-Max normalizitaion results in the same accuracy as without scaling