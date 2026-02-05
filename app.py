import streamlit as st
import joblib

# Load trained pipeline
model = joblib.load("sentiment_model.pkl")

st.title("🎬 Sentiment Analysis App")
st.write("Enter a review to predict sentiment")

user_input = st.text_area("Your Review")

if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text")
    else:
        prediction = model.predict([user_input])[0]
        sentiment = "Positive" if prediction == 1 else "Negative"

        result_text = f"""
Review:
{user_input}

Predicted Sentiment:
{sentiment}
"""

        st.success(f"Sentiment: {sentiment}")

        # ⬇️ DOWNLOAD BUTTON
        st.download_button(
            label="⬇️ Download Result",
            data=result_text,
            file_name="sentiment_result.txt",
            mime="text/plain"
        )
