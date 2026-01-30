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


### Prerequisites
-   Python 3.8+
-   `pip` package manager

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/alanfrancis765/lemon_Classifier_IBM.git
    cd lemon_Classifier_IBM
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ensure Model is Present**
    Make sure your pre-trained model file (e.g., `lemon_classifier_model.h5`) is located in the `Model/` directory.
    <!-- TODO: Specify exact model file name if known, or provide instructions on how to obtain/train it. -->

4.  **Start development server**
    ```bash
    python app.py
    ```

5.  **Open your browser**
    Visit `http://localhost:5000`

## 📁 Project Structure

```
lemon_Classifier_IBM/
├── Model/               # Directory for the pre-trained deep learning model (.h5 file)
├── static/              # Contains static web assets (HTML, CSS, JS for the frontend)
│   └── index.html       # Main web interface for image upload
│   └── style.css        # Stylesheet for the web interface
│   └── script.js        # Frontend JavaScript logic
├── app.py               # Main Flask application file; handles web routes, model loading, and prediction logic
├── requirements.txt     # Lists all Python dependencies
├── LICENSE              # Project license (MIT)
└── README.md            # This README file
```

## ⚙️ Configuration

### Environment Variables
The Flask application can be configured via environment variables.

| Variable | Description                                    | Default | Required |

|----------|------------------------------------------------|---------|----------|

| `PORT`   | Port on which the Flask application will run.  | `5000`  | No       |

### Example: Running on a different port
```bash
export PORT=8000
python app.py
```

## 📚 API Reference

The application provides a web interface and a dedicated API endpoint for image classification.

### Web Interface
-   **URL**: `/`
-   **Method**: `GET`
-   **Description**: Serves the main HTML page for uploading lemon images.

### Prediction Endpoint
-   **URL**: `/predict`
-   **Method**: `POST`
-   **Content-Type**: `multipart/form-data`
-   **Description**: Accepts an image file and returns its classification.

**Request Body (multipart/form-data):**

| Field Name | Type | Description             |

|------------|------|-------------------------|

| `file`     | File | The image file to classify |

**Example Response (JSON):**
```json
{
  "prediction": "Fresh Lemon",
  "confidence": "98.75%"
}
```

**Error Response (JSON):**
```json
{
  "error": "No file part"
}
```

## 🚀 Deployment

To deploy this application in a production environment, it is recommended to use a WSGI server like Gunicorn and a reverse proxy like Nginx.

1.  **Install Gunicorn (if not already in `requirements.txt`):**
    ```bash
    pip install gunicorn
    ```
2.  **Run with Gunicorn:**
    ```bash
    gunicorn -w 4 app:app
    ```
    (This runs the Flask `app` object from `app.py` with 4 worker processes.)

## 🤝 Contributing

We welcome contributions to improve the Lemon Classifier! If you have suggestions or want to contribute, please feel free to fork the repository and submit a pull request.

### Development Setup for Contributors
1.  Fork the repository.
2.  Clone your forked repository: `git clone https://github.com/YOUR_USERNAME/lemon_Classifier_IBM.git`
3.  Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature-name`
4.  Make your changes and commit them.
5.  Push your changes to your fork: `git push origin feature/your-feature-name`
6.  Open a Pull Request to the `main` branch of this repository.

## 📄 License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

## 🙏 Acknowledgments

-   Built as part of an IBM project/course.
-   Thanks to the developers of Flask, TensorFlow, Keras, NumPy, and Pillow for their excellent libraries.

## 📞 Support & Contact

-   🐛 Issues: [GitHub Issues](https://github.com/alanfrancis765/lemon_Classifier_IBM/issues)

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by [alanfrancis765](https://github.com/alanfrancis765)

</div>
```






