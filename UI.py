# # streamlit_app.py
# import streamlit as st
# import requests

# st.title("Sentiment Analysis")
# st.write("Enter a review below and get the sentiment:")

# review = st.text_area("Review")

# if st.button("Predict Sentiment"):
#     if review.strip() == "":
#         st.warning("Please enter a review.")
#     else:
#         with st.spinner("Predicting..."):
#             response = requests.post(
#                 "http://127.0.0.1:5000/predict",
#                 json={"review": review}
#             )

#             if response.status_code == 200:
#                 result = response.json()
#                 sentiment = result["prediction"]
#                 sentiment = "Postive" if sentiment == 1 else "Negative"  
#                 st.success(f"Sentiment: **{sentiment}**")
#             else:
#                 st.error("Failed to get a response from the Flask API.")


import streamlit as st
import requests

# Set RTL CSS for Arabic text
st.markdown("""
    <style>
    body {
        direction: rtl;
        text-align: right;
        font-family: 'Arial', sans-serif;
    }
    .stTextArea, .stButton, .stAlert {
        direction: rtl;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("تحليل المراجعات")
st.write("أدخل رأيك هنا للحصول على التحليل")

review = st.text_area("الرأي")

if st.button("توقع المشاعر"):
    if review.strip() == "":
        st.warning("يرجى إدخال رأيك.")
    else:
        with st.spinner("جارٍ التحليل..."):
            response = requests.post(
                "http://127.0.0.1:5000/predict",
                json={"review": review}
            )

            if response.status_code == 200:
                result = response.json()
                sentiment = result["prediction"]
                st.success(f"المشاعر: **{sentiment}**")
            else:
                st.error("فشل في الحصول على استجابة")