import cv2
import numpy as np
import os
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

input_folder = r"D:\cv_project\images"
output_folder = r"D:\cv_project\output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def apply_kmeans(image, k=3):
    data = image.reshape((-1, 3))
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(data)
    segmented = kmeans.cluster_centers_[kmeans.labels_]
    segmented = segmented.reshape(image.shape)
    return segmented.astype(np.uint8)

for file in os.listdir(input_folder):
    if file.lower().endswith((".jpg", ".png", ".jpeg")):
        path = os.path.join(input_folder, file)

        img_color = cv2.imread(path)
        if img_color is None:
            continue

        img_color = cv2.resize(img_color, (400, 400))
        img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

        canny = cv2.Canny(img_gray, 100, 200)

        sobel = cv2.Sobel(img_gray, cv2.CV_64F, 1, 1, ksize=5)
        sobel = cv2.convertScaleAbs(sobel)

        kmeans_img = apply_kmeans(img_color, k=3)

        _, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

        cv2.imwrite(os.path.join(output_folder, file + "_canny.jpg"), canny)
        cv2.imwrite(os.path.join(output_folder, file + "_sobel.jpg"), sobel)
        cv2.imwrite(os.path.join(output_folder, file + "_kmeans.jpg"), kmeans_img)
        cv2.imwrite(os.path.join(output_folder, file + "_threshold.jpg"), thresh)

        plt.figure(figsize=(10, 6))

        plt.subplot(2, 3, 1)
        plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))
        plt.title("Original")
        plt.axis("off")

        plt.subplot(2, 3, 2)
        plt.imshow(canny, cmap="gray")
        plt.title("Canny")
        plt.axis("off")

        plt.subplot(2, 3, 3)
        plt.imshow(sobel, cmap="gray")
        plt.title("Sobel")
        plt.axis("off")

        plt.subplot(2, 3, 4)
        plt.imshow(thresh, cmap="gray")
        plt.title("Threshold")
        plt.axis("off")

        plt.subplot(2, 3, 5)
        plt.imshow(cv2.cvtColor(kmeans_img, cv2.COLOR_BGR2RGB))
        plt.title("KMeans")
        plt.axis("off")

        plt.tight_layout()
        plt.savefig(os.path.join(output_folder, file + "_comparison.png"))
        plt.close()

print("Done")