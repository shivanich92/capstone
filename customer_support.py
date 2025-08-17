import streamlit as st

# ------------------- Streamlit Page Config -------------------
st.set_page_config(page_title="Customer Support System", page_icon="🛠️", layout="centered")

# Custom CSS for colors + animation effects
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #ffecd2, #fcb69f);
        color: black;
    }
    .stButton>button {
        background: linear-gradient(90deg, #667eea, #764ba2);
        color: white;
        border-radius: 12px;
        font-size: 16px;
        padding: 8px 16px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg, #ff758c, #ff7eb3);
    }
    .css-10trblm { text-align: center; }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("✨ Customer Support System ✨")
st.markdown("Choose a category to get personalized **support & recommendations** 🚀")

# ------------------- Tabs -------------------
tab1, tab2, tab3 = st.tabs(["🍎 Food", "🔌 Electronics", "👗 Clothes"])

# ---------------- FOOD PAGE ----------------
with tab1:
    st.header("🥗 Food Support")
    st.image("https://media.giphy.com/media/3o7TKsQWMrHf1cAAuc/giphy.gif", width=200)

    st.subheader("⚖️ Weight Check (Loss / Gain)")
    protein = st.number_input("Protein (g)", min_value=0, step=1, key="protein")
    carbs = st.number_input("Carbohydrates (g)", min_value=0, step=1, key="carbs")
    fat = st.number_input("Fat (g)", min_value=0, step=1, key="fat")
    
    if st.button("Check Weight Recommendation", key="weight_btn"):
        if protein >= 20 and carbs <= 50 and fat <= 15:
            st.success("✅ This food is suitable for **Weight Loss.**")
        elif protein >= 15 and carbs >= 60:
            st.warning("⚡ This food is more suitable for **Weight Gain.**")
        else:
            st.info("ℹ️ This food is better for **Maintenance.**")

    st.subheader("💊 Health Check (Healthy / Unhealthy)")
    sugar = st.number_input("Sugar (g)", min_value=0, step=1, key="sugar")
    sodium = st.number_input("Sodium (mg)", min_value=0, step=10, key="sodium")
    
    if st.button("Check Healthiness", key="health_btn"):
        if sugar < 10 and sodium < 400:
            st.success("✅ Healthy Choice. 🥦")
        elif sugar > 20 or sodium > 800:
            st.error("⚠️ Unhealthy Choice. 🍔")
        else:
            st.info("😐 Moderately Healthy. 🍽️")

# ---------------- ELECTRONICS PAGE ----------------
with tab2:
    st.header("🔋 Electronics Support")
    st.image("https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", width=200)
    
    issue_type = st.radio("Select Issue Type:", ["Manual Issue", "Technical Issue"], key="issue_type")
    product = st.selectbox("Select Product:", ["Laptop", "Smartphone", "Washing Machine", "TV", "Refrigerator"], key="product")
    
    if st.button("Get Support", key="support_btn"):
        if issue_type == "Manual Issue":
            if product in ["Laptop", "Smartphone"]:
                st.info(f"📘 {product}: Please check **Quick Start Guide** in the box.")
            else:
                st.info(f"📘 {product}: Refer to the **User Manual** provided.")
        else:
            messages = {
                "Laptop": "🛠️ Run diagnostics or contact service center.",
                "Smartphone": "📱 Restart the phone. If issue persists, visit service center.",
                "Washing Machine": "⚡ Check power & water. Contact support if unresolved.",
                "TV": "📺 Restart & check cables. Contact technician if needed.",
                "Refrigerator": "❄️ Check cooling & power. Call service if still faulty."
            }
            st.warning(messages[product])

# ---------------- CLOTHES PAGE ----------------
with tab3:
    st.header("👗 Clothing Support")
    st.image("https://media.giphy.com/media/3o7TKtnuHOHHUjR38Y/giphy.gif", width=200)
    
    skin_type = st.selectbox("Select Skin Type:", ["Fair", "Medium", "Dark"], key="skin")
    color_pref = st.selectbox("Choose Preferred Color:", ["Red", "Blue", "Green", "Black", "White", "Yellow"], key="color")
    
    if st.button("Get Recommendation", key="clothes_btn"):
        if skin_type == "Fair":
            if color_pref in ["Blue", "Black", "Red"]:
                st.success(f"👕 {color_pref} looks **elegant** on Fair skin. 🌟")
            else:
                st.info(f"👗 {color_pref} is okay, but **darker shades** may suit better.")
        elif skin_type == "Medium":
            if color_pref in ["Green", "White", "Yellow"]:
                st.success(f"👕 {color_pref} complements **Medium skin tone** very well. 🌼")
            else:
                st.info(f"👚 {color_pref} is fine, but **earthy tones** usually suit Medium skin.")
        else:
            if color_pref in ["Red", "Yellow", "White"]:
                st.success(f"👕 {color_pref} pops beautifully on **Dark skin.** 🔥")
            else:
                st.info(f"👔 {color_pref} works, but **brighter colors** stand out better.")

