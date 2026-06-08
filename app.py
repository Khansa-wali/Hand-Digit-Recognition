import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
from streamlit_drawable_canvas import st_canvas

# Load Model
model=tf.keras.models.load_model("model.h5")

st.title("✍️ Handwritten Digit Recognizer")
st.write("Draw a digit (0–9) in the box below")


# Drawing canvas
canvas = st_canvas(
    fill_color="black",
    stroke_width=20,
    stroke_color="white",
    background_color="black",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas"
)

if canvas.image_data is not None:

    img = Image.fromarray(canvas.image_data.astype("uint8"))
    img = img.convert("L")
    img = img.resize((28, 28))

    img_array = np.array(img)
    img_array = img_array.reshape(1, 28, 28, 1)
    img_array = img_array / 255.0

    if st.button("Predict Digit"):
        prediction = model.predict(img_array)
        result = np.argmax(prediction)

        st.success(f"Predicted Digit: {result}")
        st.bar_chart(prediction[0])


