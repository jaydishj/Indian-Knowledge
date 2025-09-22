# streamlit_medicinal_plants.py

import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os
from pathlib import Path
# ================================
# Custom Background with Ayurvedic Pattern
# ================================
st.set_page_config(page_title="🌿 Indian knowledge system 🌿", layout="centered")

st.title("🌿 Indian knowledge system 🌿")

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://www.transparenttextures.com/patterns/arabesque.png");
    background-size: auto;
    background-color: #FFD700; /* leaf base */
}

[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}

[data-testid="stSidebar"] {
    background-color: #FFF8DC; /* light green for sidebar */
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("medicinal_plant_cnn.h5")

model = load_model()
st.markdown("""
### 🧭 About Indian Knowledge Systems (IKS)  
Indian Knowledge Systems (IKS) represent the holistic and indigenous wisdom of India,  
covering fields such as **Ayurveda, Yoga, Siddha, Unani, and Ethnobotany**.  
In Ayurveda, medicinal plants are not just remedies but part of a **sustainable lifestyle**  
that emphasizes balance between **mind, body, spirit, and environment**.

This application uses **AI + IKS** to recognize medicinal plants and provides:  
- 🌱 **Scientific & Common Names**  
- 🌿 **Medicinal Properties**  
- 💊 **Therapeutic Uses (Traditional & Ayurvedic)**  
- 🧴 **Curing Applications in Indian Systems**  

✨ By blending **modern machine learning** with **traditional Ayurvedic knowledge**,  
this tool aims to support research, education, and preservation of India’s medicinal heritage.
""")
# =============================
# Dataset class names
# =============================
data_dir = r"e:/medicinal plant/Medicinal_Leaf_Dataset/Compressed_dataset"
class_names = sorted(os.listdir(data_dir))

# =============================
# Knowledge Base (English + Tamil)
# =============================
plant_info = {
    "Ashok": {
        "scientific": "Saraca asoca",
        "common_en": "Ashoka Tree",
        "common_ta": "அசோக மரம்",
        "properties_en": "Uterine tonic, anti-inflammatory, analgesic",
        "properties_ta": "கருப்பை நலத்திற்கு, அழற்சி குறைப்பான், வலிநிவாரணி",
        "therapeutic_en": "Used in Ayurveda for menstrual disorders, uterine health",
        "therapeutic_ta": "ஆயுர்வேதத்தில் மாதவிடாய் கோளாறுகள் மற்றும் கருப்பை நலத்திற்குப் பயன்படுத்தப்படுகிறது",
        "curing_en": "Decoction of bark & flowers; given in dysmenorrhea and leucorrhea",
        "curing_ta": "பட்டை மற்றும் பூ சாறு; மாதவிடாய் வலி மற்றும் வெள்ளைச் சிந்தலில் பயன்படும்"
    },
    "Basil": {
        "scientific": "Ocimum tenuiflorum (Tulsi)",
        "common_en": "Holy Basil",
        "common_ta": "துளசி",
        "properties_en": "Antioxidant, antimicrobial, adaptogenic",
        "properties_ta": "ஆக்சிடன்ட் எதிர்ப்பு, கிருமி எதிர்ப்பு, உடல் தழுவும் தன்மை",
        "therapeutic_en": "Boosts immunity, cures cold, cough, and respiratory ailments",
        "therapeutic_ta": "நோய் எதிர்ப்பு சக்தியை அதிகரிக்கும், சளி, இருமல் மற்றும் சுவாச நோய்களை குணப்படுத்தும்",
        "curing_en": "Leaves taken as tea/kadha; paste applied for skin diseases",
        "curing_ta": "இலைகள் கஷாயமாக குடிக்கப்படும்; விழுது தோல் நோய்களுக்கு பயன்படுத்தப்படுகிறது"
    },
    "Neem": {
        "scientific": "Azadirachta indica",
        "common_en": "Neem",
        "common_ta": "வேப்பம்",
        "properties_en": "Antibacterial, antifungal, blood purifier",
        "properties_ta": "பாக்டீரியா எதிர்ப்பு, பூஞ்சை எதிர்ப்பு, இரத்த சுத்திகரிப்பு",
        "therapeutic_en": "Used for skin diseases, fever, diabetes, infections",
        "therapeutic_ta": "தோல் நோய்கள், காய்ச்சல், நீரிழிவு மற்றும் தொற்றுநோய்களுக்கு பயன்படுத்தப்படுகிறது",
        "curing_en": "Neem oil, leaf paste, bark decoction",
        "curing_ta": "வேப்பெண்ணெய், இலை விழுது, பட்டை சாறு"
    },
    "Thankuni": {
        "scientific": "Centella asiatica",
        "common_en": "Gotu Kola / Thankuni",
        "common_ta": "வல்லாரை",
        "properties_en": "Memory enhancer, wound healer, nervine tonic",
        "properties_ta": "நினைவாற்றல் மேம்படுத்தி, காயம் ஆற்றுபவன், நரம்பு சக்தி ஊட்டி",
        "therapeutic_en": "Improves memory, reduces anxiety, heals wounds",
        "therapeutic_ta": "நினைவாற்றலை மேம்படுத்தும், பதட்டத்தை குறைக்கும், காயங்களை ஆற்றும்",
        "curing_en": "Leaf juice or paste; used in mental weakness and skin ulcers",
        "curing_ta": "இலை சாறு அல்லது விழுது; மன பலவீனம் மற்றும் தோல் புண்களில் பயன்படும்"
    },
    "Vasaka": {
        "scientific": "Justicia adhatoda",
        "common_en": "Malabar Nut / Vasaka",
        "common_ta": "அடாதோடை",
        "properties_en": "Expectorant, bronchodilator, antispasmodic",
        "properties_ta": "சளி கரைக்கும், நுரையீரல் திறப்பான், தசை பிடிப்பு குறைப்பான்",
        "therapeutic_en": "Cures cough, asthma, chronic bronchitis",
        "therapeutic_ta": "இருமல், ஆஸ்துமா, நீண்டகால மூச்சுக் குழாய் அழற்சி குணமாகும்",
        "curing_en": "Leaf juice mixed with honey; decoction used as expectorant",
        "curing_ta": "இலை சாறு தேனுடன்; சாறு சளி கரைக்கப் பயன்படும்"
    }
}

# =============================
# Prediction Function
# =============================
def predict_image(img):
    img_size = (224, 224)
    img = image.load_img(img, target_size=img_size)
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions)

    plant_name = class_names[predicted_class]
    return plant_name, confidence

# =============================
# Streamlit UI
# =============================

st.write("Upload a medicinal plant image to get its **prediction, scientific name, medicinal uses, and bilingual details (English + தமிழ்)**")

uploaded_file = st.file_uploader("📤 Upload a Plant Leaf/Photo", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    with st.spinner("🔍 Analyzing..."):
        plant_name, confidence = predict_image(uploaded_file)

    if plant_name in plant_info:
        info = plant_info[plant_name]

        st.success(f"✅ Predicted: **{info['common_en']} / {info['common_ta']}**")
        st.write(f"**🔬 Scientific Name:** {info['scientific']}")
        st.write(f"**🌱 Properties:** {info['properties_en']} \n\n 🪴 {info['properties_ta']}")
        st.write(f"**💊 Therapeutic Uses:** {info['therapeutic_en']} \n\n 💊 {info['therapeutic_ta']}")
        st.write(f"**🧴 Curing Details:** {info['curing_en']} \n\n 🧴 {info['curing_ta']}")
       
    else:
        st.write("⚠️Invalid image file. Please upload a proper image, The uploaded image does not match any recognized herb. Please try another image.")

        
        
