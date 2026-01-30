import streamlit as st
import numpy as np
import joblib
from PIL import Image
import mahotas as mh

# -------------------------------------------------
# LOAD MODEL
# -------------------------------------------------
model = joblib.load("Model/QDA_lemon.pkl")

# -------------------------------------------------
# FEATURE EXTRACTION (FIXED)
# -------------------------------------------------
def extract_features_from_image(image: Image.Image):
    image_np = np.array(image)
    gray = mh.colors.rgb2grey(image_np, dtype=np.uint8)
    features = mh.features.haralick(gray).ravel()
    return features.reshape(1, -1)

# -------------------------------------------------
# GRADE CONFIG
# -------------------------------------------------
GRADE_CONFIG = {
    0: {
        "title": "Excellent",
        "emoji": "✨",
        "color": "#06D6A0",
        "description": (
            "Premium quality lemon with uniform color, smooth texture, "
            "and no visible surface defects. Indicates optimal freshness "
            "and high market value."
        ),
        "recommendation": (
            "Ideal for export, premium retail, and long-distance distribution."
        )
    },
    1: {
        "title": "Good",
        "emoji": "👍",
        "color": "#FFD166",
        "description": (
            "High-quality lemon with minor natural variations in texture or color. "
            "Free from major defects and suitable for most commercial purposes."
        ),
        "recommendation": (
            "Recommended for standard retail sale and local markets."
        )
    },
    2: {
        "title": "Fair",
        "emoji": "⚠️",
        "color": "#118AB2",
        "description": (
            "Acceptable quality lemon showing noticeable surface irregularities "
            "or texture variations. Freshness may be slightly reduced."
        ),
        "recommendation": (
            "Best used for juice extraction, processing, or short-term consumption."
        )
    },
    3: {
        "title": "Rejected",
        "emoji": "❌",
        "color": "#EF476F",
        "description": (
            "Poor quality lemon with significant defects, discoloration, "
            "or signs of spoilage. Does not meet commercial quality standards."
        ),
        "recommendation": (
            "Not suitable for sale. Recommended for disposal or non-food use."
        )
    }
}


# -------------------------------------------------
# CSS (SAFE & CONTROLLED)
# -------------------------------------------------
def load_css():
    st.markdown(
        """
        <style>
        .stApp {
            background: radial-gradient(circle at top, #7DD3FC, #020617 65%);
            color: #E5F3F8;
        }

        .hero {
            background: linear-gradient(135deg, #7DD3FC, #020617);
            padding: 42px 22px;
            border-radius: 0 0 26px 26px;
            margin-bottom: 32px;
            box-shadow: 0 16px 32px rgba(0,0,0,0.45);
        }

        .hero h1 {
            text-align: center;
            font-size: 3rem;
            margin-bottom: 12px;
            color: #0F172A;
        }

        .hero p {
            text-align: center;
            font-size: 1.05rem;
            color: #1E293B;
            opacity: 0.9;
        }

        .block-container {
            padding-top: 0rem;
            padding-bottom: 3rem;
            max-width: 1000px;
        }

        section[data-testid="stFileUploader"] {
            background-color: #020617;
            padding: 20px;
            border-radius: 14px;
            border: 1px solid #1E293B;
        }

        .grade-card {
            padding: 24px;
            border-radius: 18px;
            margin-top: 24px;
            box-shadow: 0 14px 30px rgba(0,0,0,0.4);
        }
        .footer {
            text-align: center;
            margin-top: 60px;
            color: #CBD5E1;
            font-size: 0.9rem;
            opacity: 0.7;
            padding : 20px 0;
        }

        img {
            border-radius: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# -------------------------------------------------
# STREAMLIT UI
# -------------------------------------------------
st.set_page_config(
    page_title="Lemon Quality Classifier",
    page_icon="🍋"
)

load_css()

# HERO BANNER
st.markdown(
    """
    <div class="hero">
        <h1>🍋 Lemon Quality Classifier</h1>
        <p>Upload a lemon image to evaluate its quality using texture-based ML.</p>
    </div>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Upload lemon image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", width=300)

    with st.spinner("Analyzing texture..."):
        features = extract_features_from_image(image)
        prediction = model.predict(features)[0]

    grade = GRADE_CONFIG[prediction]

    confidence = None
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(features)[0]
        confidence = probs[prediction] * 100
        
    confidence_html = ""
    if confidence is not None:
        confidence_html = f"""
        <p style="color:#0F172A; margin-top:12px;">
            <b>Confidence:</b> {confidence:.1f}%
        </p>
        """

    # THEME-MATCHED GRADE CARD
    st.markdown(
        f"""
        <div class="grade-card"
             style="
                background: rgba(230, 244, 247, 0.45);
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                border-left: 8px solid {grade['color']};
             ">
            <h2 style="margin-top:0; color:#0F172A;">
                {grade['emoji']} {grade['title']}
            </h2>
            <p style="color:#0F172A;"><b>Description:</b> {grade['description']}</p>
            <p style="color:#0F172A;"><b>Recommendation:</b> {grade['recommendation']}</p>
            </p>{confidence_html}
    </div>
        """,
        unsafe_allow_html=True
    )
    #footer 
    st.markdown(
        """
        <div class="footer">
            © 2026 Alan Francis · <a href="mailto:alanfrancis11ah@gmail.com"
            style="color:#7DD3FC; text-decoration:none;">
            alanfrancis11ah@gmail.com</a>
        </div>
        """,
        unsafe_allow_html=True
    )