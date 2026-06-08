Handwritten Digit Recognition App

An interactive Machine Learning web application that recognizes handwritten digits (0–9) using a trained deep learning model. The user draws a digit on a canvas, and the model predicts it in real time.

 Live Demo

👉 Add Streamlit link here after deployment

About the Project

This project demonstrates a complete end-to-end machine learning workflow:

--Data preprocessing
--Model training
--Model saving (model.h5)
--Web deployment using Streamlit

It bridges the gap between machine learning and real-world applications.

Features are:
--Draw digits on interactive canvas
--Real-time prediction using CNN model
--Instant response
--Predicts digits from 0 to 9
--Simple and clean UI

Tech Stack
--Python 
--TensorFlow / Keras 
--Streamlit 
--NumPy 
--Pillow 
--Streamlit Drawable Canvas 

Project Structure

Streamlit_Project/
│
├── app.py                # Main Streamlit application
├── model.h5              # Trained CNN model
├── requirements.txt      # Dependencies
├── .gitignore            # Ignored files
└── README.md             # Documentation


How to Run Locally?
git clone https://github.com/your-username/your-repo.git
cd your-repo
pip install -r requirements.txt
streamlit run app.py


Model Details
--Dataset: MNIST Handwritten Digits
--Model: Convolutional Neural Network (CNN)
--Output Classes: 10 (0–9)
--Framework: TensorFlow / Keras


Deployment

--This app is deployed using Streamlit Cloud for real-time web access.

Future Improvements
--Add handwriting smoothing
--Show confidence score
--Improve UI/UX design

Author

--Built with passion for Machine Learning and real-world AI deployment.

