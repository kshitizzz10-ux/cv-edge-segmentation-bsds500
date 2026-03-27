# Comparative Study of Edge Detection and Image Segmentation using BSDS500 Dataset

## 📌 Project Overview

This project presents a comparative analysis of classical computer vision techniques for **edge detection** and **image segmentation** using the BSDS500 dataset.

The goal of this project is to evaluate how different algorithms perform in extracting structural and regional information from images.

---

## 🎯 Objectives

* To implement classical edge detection techniques
* To perform image segmentation using clustering methods
* To compare results visually and analytically
* To evaluate performance using a matrix-based comparison

---

## 🧠 Techniques Used

### Edge Detection

* Canny Edge Detection
* Sobel Operator

### Segmentation

* Thresholding
* K-Means Clustering

---

## 📂 Project Structure

```
cv-edge-segmentation-bsds500/
│── images/                  # Input sample images
│── output/                  # Generated output images
│── main.py                  # Main processing script
│── metrics.py               # Performance matrix generation
│── requirements.txt         # Dependencies
│── README.md                # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/your-username/cv-edge-segmentation-bsds500.git
cd cv-edge-segmentation-bsds500
```

---

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project

### Step 1: Add Input Images

* Place 1–3 images inside the `images/` folder
* Supported formats: `.jpg`, `.png`

---

### Step 2: Run Main Script

```
python main.py
```

👉 This will:

* Apply edge detection (Canny, Sobel)
* Apply segmentation (Threshold, K-Means)
* Save results in the `output/` folder

---

### Step 3: Generate Performance Matrix

```
python metrics.py
```

👉 This will generate:

* `performance_matrix.png` inside the output folder

---

## 📊 Output Explanation

For each input image, the following outputs are generated:

* Canny Edge Image
* Sobel Edge Image
* Threshold Segmentation
* K-Means Segmentation
* Combined Comparison Image

---

## 📈 Results Summary

* **Canny Edge Detection** produces sharp and accurate edges
* **Sobel Operator** detects gradients but introduces noise
* **Thresholding** provides basic binary segmentation
* **K-Means Clustering** effectively segments regions based on color similarity

---

## 🧪 Evaluation Method

The project uses:

* Visual comparison of outputs
* Performance comparison matrix
* Edge density concept (theoretical metric)

---

## 📚 Dataset

The project uses a subset of the **BSDS500 (Berkeley Segmentation Dataset)**, which contains natural images with diverse textures and object boundaries.

---

## ⚠️ Limitations

* Classical methods struggle with complex lighting conditions
* No deep learning models used
* Performance depends on parameter tuning (e.g., K in K-Means)

---

## 🚀 Future Improvements

* Integration of deep learning models (CNN, U-Net)
* Use of ground truth for quantitative evaluation
* Real-time image processing system

---

## 👨‍💻 Author

**Kshitiz Goyal**
VIT Bhopal University

---

## 📌 Note

This project is developed as part of a Computer Vision course to demonstrate fundamental image processing techniques and their comparative performance.
