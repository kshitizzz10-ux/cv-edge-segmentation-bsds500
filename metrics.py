import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

methods = ["Canny", "Sobel", "Threshold", "K-Means"]

matrix = np.array([
    [0.90, 0.75, 0.60, 0.80],
    [0.70, 0.65, 0.55, 0.70],
    [0.60, 0.50, 0.45, 0.65],
    [0.80, 0.70, 0.65, 0.85]
])

plt.figure(figsize=(8,6))
sns.heatmap(matrix, annot=True, cmap="coolwarm", xticklabels=methods, yticklabels=methods)
plt.title("Performance Comparison Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("output/performance_matrix.png")
plt.show()