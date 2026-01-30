![Lemon Classifier](static/banner.jpeg)
<div align="center">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Mahotas-2E7D32?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Haralick_Features-4CAF50?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Pillow-4A7382?style=for-the-badge&logo=python&logoColor=white" />
</div>

## 🍋 Lemon Quality Classifier 

The Lemon Classifier is a lightweight web application designed to automatically classify images of lemons. Utilizing a pre-trained deep learning model, it provides a user-friendly interface for uploading images and receiving instant classification results. This project serves as a practical example of deploying a machine learning model for image recognition within a Flask-based web environment, ideal for quality control, educational purposes, or simply demonstrating ML inference.

## ✨ Features

- **Machine Learning–Based Predictions**  
  Implements a supervised ML pipeline with **Haralick texture features** and a **Scikit-learn      classifier**.
- **Computer Vision Feature Extraction**  
  Extracts texture and intensity-based features using **Mahotas** before classification.
- **Real-Time Inference**  
  Provides instant predictions immediately after image upload.
- **Simple & Interactive Web Interface**  
  Clean, minimal UI designed for demonstrations and easy use.
- **Modular & Reusable ML Pipeline**  
  Enables easy retraining, feature tuning, or classifier replacement.


## 📌 Prerequisites

Before running the Lemon Quality Classifier, ensure the following requirements are met:

- **Python 3.13.x or higher**
- **Conda or Miniconda** (recommended for environment management)
- **Mahotas** (for Haralick texture feature extraction)
- Familiarity with **Scikit-learn**, **NumPy**, and **Pandas**

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/alanfrancis765/lemon_Classifier_IBM
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ensure Model is Present**
    Make sure your pre-trained model file (e.g., `QDA_lemon.pkl`) is located in the `Model/` directory.
   
4.  **Start development server**
    ```bash
    python -m streamlit app.py
    ```
## 🧠 Model Overview

The model uses a **classical machine learning approach combined with texture-based computer vision techniques** for lemon quality classification. Instead of deep learning, it relies on **Haralick texture features** extracted from grayscale images using the **Mahotas** library.

Multiple classifiers were evaluated, and **Quadratic Discriminant Analysis (QDA)** was selected as the final model due to its superior class separation and generalization performance. This approach offers **high accuracy, low computational cost, and strong interpretability**, making it well-suited for automated visual inspection in agriculture.

## 📁 Project Structure

```
lemon_Classifier_IBM/
├── Model/              
├── static/             
│   └── images      
├── app.py                
├── requirements.txt    
├── LICENSE             
└── README.md            
```

## 📸 Screenshots
[🍋click here](https://lemonclassifieribm-ctrxazhlfcecxhvzxcrrgb.streamlit.app/)

![before](static/image001.png)
![after](static/image002.png)

## 📝 Author and details:

-Hi this is Alan Francis I am an AIML student at Marian College of Engineering. This project is licensed under the [MIT License]. If you have any questions or suggestions, feel free to contact me at [alanfrancis347@gmail.com](mailto:alanfrancis347@gmail.com). Thank you for checking out the NASA Exoplanet Detection System! I hope this tool is helpful for your exoplanet research and exploration.
We welcome contributions to improve the **Lemon Quality Classifier**!  
If you have suggestions, bug fixes, or feature improvements, feel free to contribute.

---

<div align="center">

Made with IBM® by [alanfrancis765](https://github.com/alanfrancis765)

</div>














