import streamlit as st
import requests
import base64
from PIL import Image
import io
import os
from mistralai import Mistral

api_key = os.getenv("MISTRAL_API_KEY")
model = "pixtral-12b-2409"  
client = Mistral(api_key=api_key)


# Streamlit App UI
st.title("DermaCare AI: Skin Disease Diagnosis Assistant")
st.write("Upload an image of a skin condition, and the AI will generate a detailed medical report.")

# File uploader for skin disease image
uploaded_file = st.file_uploader("Upload an image (PNG or JPEG):", type=["png", "jpeg", "jpg"])

if uploaded_file:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    # Convert image to Base64
    buffer = io.BytesIO()
    image_format = "PNG" if uploaded_file.type == "image/png" else "JPEG"
    image.save(buffer, format=image_format)
    base64_image = base64.b64encode(buffer.getvalue()).decode("utf-8")

    # Submit button
    if st.button("Analyze Image"):
        with st.spinner("Analyzing..."):
            try:

                # Define messages payload
                messages = [
                    {
                        "role": "system",
                        "content": f"""You are a Medical AI Assistant specializing in analyzing and diagnosing skin diseases. 

                    Your goal is to:
                    1. Accurately identify the skin condition depicted in the provided image.
                    2. Assess the severity or stage of the condition, if possible.
                    3. Analyze visible skin features such as color, texture, and irregular patterns.
                    4. Provide medically relevant observations and recommendations for further diagnosis or treatment.
                    5. Use the contextual information to provide an even more in-depth report about the disease.

                    **Medical Report Requirements**:
                    - Include **Disease Identification**: Clearly state the suspected disease(s) and provide reasoning, citing relevant medical characteristics.
                    - Detail the **Stage/Severity** of the disease: Include clear explanations about why this stage/severity is suggested based on visible patterns and retrieved information.
                    - Describe **Skin Characteristics**: Offer detailed descriptions of color, texture, shape, visible patterns, and any noteworthy features.
                    - Highlight **Patterns of Concern**: Discuss irregularities, such as asymmetry, abnormal texture, or discoloration, and their implications.
                    - Provide **Treatment Recommendations**: Include a detailed overview of potential treatments, next steps for diagnosis, and preventive measures, where relevant.

                    **Report Format**:
                    - Use headings and subheadings for each section.
                    - Provide a detailed explanation of observations in a structured and reader-friendly format.
                    - Ensure the report reflects a high level of precision, depth, and clinical relevance.
                    """
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": """You are provided with a skin disease image for analysis. Please generate a detailed medical report with all the outlined requirements.

                                **Image Details**:
                                - **Type**: Skin disease image
                                - **Format**: Base64-encoded image
                                - **Source**: Uploaded by a user for medical assistance

                                Please analyze the image and generate a comprehensive report."""
                            },
                            {
                                "type": "image_url",
                                "image_url": f"data:image/{image_format.lower()};base64,{base64_image}"
                            },
                        ],
                    },
                ]

                chat_response = client.chat.complete(
                model=model,
                messages=messages,
                temperature=0.7,
                top_p=1.0
                )

                response = chat_response.choices[0].message.content

                # Send request to the API
                st.subheader("Analysis Result")
                st.markdown(response)
                
            except:
                st.error("There was an issue processing the image. Please try again.")
