
import streamlit as st

st.set_page_config(page_title="🌿 Indian Knowledge System 🌿", layout="centered")
st.title("🌿 Scan to Sense:Indian Knowledge System 🌿")

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
plants = [
    {
        "name_en": "Malabar Nut / Vasaka",
        "name_ta": "அடாதோடை",
        "scientific": "Justicia adhatoda",
        "properties_en": "Expectorant, bronchodilator, antispasmodic",
        "properties_ta": "சளி கரைக்கும், நுரையீரல் திறப்பான், தசை பிடிப்பு குறைப்பான்",
        "therapeutic_en": "Cures cough, asthma, chronic bronchitis",
        "therapeutic_ta": "இருமல், ஆஸ்துமா, நீண்டகால மூச்சுக் குழாய் அழற்சி குணமாகும்",
        "curing_en": "Leaf juice mixed with honey; decoction used as expectorant",
        "curing_ta": "இலை சாறு தேனுடன்; சாறு சளி கரைக்கப் பயன்படும்",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/33/Justicia_adhatoda.jpg"
    },
    {
        "name_en": "Holy Basil / Tulsi",
        "name_ta": "துளசி",
        "scientific": "Ocimum tenuiflorum",
        "properties_en": "Antioxidant, antimicrobial, adaptogenic",
        "properties_ta": "ஆக்சிடன்ட் எதிர்ப்பு, கிருமி எதிர்ப்பு, உடல் தழுவும் தன்மை",
        "therapeutic_en": "Boosts immunity, cures cold, cough, and respiratory ailments",
        "therapeutic_ta": "நோய் எதிர்ப்பு சக்தியை அதிகரிக்கும், சளி, இருமல் மற்றும் சுவாச நோய்களை குணப்படுத்தும்",
        "curing_en": "Leaves taken as tea/kadha; paste applied for skin diseases",
        "curing_ta": "இலைகள் கஷாயமாக குடிக்கப்படும்; விழுது தோல் நோய்களுக்கு பயன்படுத்தப்படுகிறது",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/60/Tulsi-plant.jpg"
    },
    {
        "name_en": "Neem",
        "name_ta": "வேப்பம்",
        "scientific": "Azadirachta indica",
        "properties_en": "Antibacterial, antifungal, blood purifier",
        "properties_ta": "பாக்டீரியா எதிர்ப்பு, பூஞ்சை எதிர்ப்பு, இரத்த சுத்திகரிப்பு",
        "therapeutic_en": "Used for skin diseases, fever, diabetes, infections",
        "therapeutic_ta": "தோல் நோய்கள், காய்ச்சல், நீரிழிவு மற்றும் தொற்றுநோய்களுக்கு பயன்படுத்தப்படுகிறது",
        "curing_en": "Neem oil, leaf paste, bark decoction",
        "curing_ta": "வேப்பெண்ணெய், இலை விழுது, பட்டை சாறு",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Azadirachta_indica_Blossoms.jpg"
    },
    {
        "name_en": "Jarul",
        "name_ta": "ஜருள்",
        "scientific": "Lagerstroemia speciosa",
        "properties_en": "Anti-diabetic, antioxidant, blood sugar regulator",
        "properties_ta": "நீரிழிவு நோய் எதிர்ப்பு, ஆக்சிடன்ட் எதிர்ப்பு, ரத்த சர்க்கரை கட்டுப்பாடு",
        "therapeutic_en": "Used for diabetes, obesity, and kidney health",
        "therapeutic_ta": "நீரிழிவு, இடுப்புத்தொற்று மற்றும் சிறுநீரகம் நலத்திற்கு பயன்படும்",
        "curing_en": "Leaf extract and tea; fruit decoction",
        "curing_ta": "இலையின் சாறு மற்றும் தேநீர்; பழச் சாறு",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/09/Lagerstroemia_speciosa_flower.jpg"
    },
    {
        "name_en": "Mastwood",
        "name_ta": "மாஸ்ட்வுட்",
        "scientific": "Calophyllum inophyllum",
        "properties_en": "Anti-inflammatory, wound healing, skin care",
        "properties_ta": "அழற்சி குறைப்பு, காயங்கள் குணப்படுத்துதல், தோல் பராமரிப்பு",
        "therapeutic_en": "Used for skin diseases, joint pain, and hair care",
        "therapeutic_ta": "தோல் நோய்கள், மூட்டு வலி மற்றும் தலைமுடி பராமரிப்பு",
        "curing_en": "Oil from seeds applied externally; leaf paste for wounds",
        "curing_ta": "விதைகளிலிருந்து எண்ணெய் புறக்கூறு; இலை விழுது காயங்களுக்கு",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/73/Calophyllum_inophyllum.jpg"
    },
    {
        "name_en": "Minjiri / Nageshor",
        "name_ta": "மிஞ்சிரி / நாகேஷோர்",
        "scientific": "Vitex negundo",
        "properties_en": "Anti-inflammatory, analgesic, antimicrobial",
        "properties_ta": "அழற்சி குறைப்பு, வலி நிவாரணம், கிருமி எதிர்ப்பு",
        "therapeutic_en": "Used for joint pain, respiratory problems, and skin infections",
        "therapeutic_ta": "மூட்டு வலி, சுவாச பிரச்சினைகள், தோல் தொற்று குணப்படுத்தும்",
        "curing_en": "Leaf juice and decoction; applied on affected areas",
        "curing_ta": "இலை சாறு மற்றும் சாறு; பாதிக்கப்பட்ட பகுதிகளில் பயன்படுத்தப்படுகிறது",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/87/Vitex_negundo.jpg"
    }
]

uploaded_file = st.file_uploader("📤 Upload a Plant Leaf/Photo")
selected_plant_name = None

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    
    # For now, we can **simulate classification** by letting user select from dropdown
    plant_options = [plant['name_en'] for plant in plants]
    selected_plant_name = st.selectbox("Select the Plant (Simulated Classification)", plant_options)

# ================================
# Show Info for the Selected Plant
# ================================
if selected_plant_name:
    # Find the plant info
    info = next((p for p in plants if p["name_en"] == selected_plant_name), None)
    
    if info:
        st.image(info["image_url"], caption=f"{info['name_en']} / {info['name_ta']}", use_container_width=True)
        st.success(f"✅ Plant: **{info['name_en']} / {info['name_ta']}**")
        st.write(f"**🔬 Scientific Name:** {info['scientific']}")
        st.write(f"**🌱 Properties:** {info['properties_en']} \n\n 🪴 {info['properties_ta']}")
        st.write(f"**💊 Therapeutic Uses:** {info['therapeutic_en']} \n\n 💊 {info['therapeutic_ta']}")
        st.write(f"**🧴 Curing Details:** {info['curing_en']} \n\n 🧴 {info['curing_ta']}")

