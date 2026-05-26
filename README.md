# 🌿 AgriLeaf Doctor - Smart Crop Disease Detection System

## Overview
AgriLeaf Doctor is a comprehensive AI-powered agricultural application designed to help farmers identify and treat crop leaf diseases effectively using the mango leaf disease dataset from Kaggle.

## 🚀 Features
- **🦠 Disease Detection**: AI-powered leaf disease classification using deep learning
- **💊 Treatment Recommendations**: Detailed treatment plans with medicines and organic alternatives
- **🌱 Care Tips**: Expert guidance for maintaining healthy plants
- **🌦️ Weather Alerts**: Disease risk alerts based on weather conditions
- **🌐 Multi-language Support**: Available in multiple Indian languages
-I have created the core files for the Streamlit app, disease info, treatment recommendations, weather alerts, multilingual support, leaf care tips, and the model training script.

Plan:
- The app.py is the main Streamlit app that loads the model and provides UI for disease detection, care tips, weather alerts, and about page.
- disease_info.py contains detailed disease info for mango leaf diseases.
- treatment_recommender.py provides treatment plans, medicines, organic options, and prevention tips.
- weather_alerts.py fetches weather data and calculates disease risk based on weather.
- multilingual_support.py provides basic translation support for multiple Indian languages.
- leaf_care_tips.py provides healthy leaf care tips categorized by topics.
- train_model.py is a script to train a MobileNetV2-based classifier on the mango leaf disease dataset.

Next steps:
- You need to download the mango leaf disease dataset from the provided Kaggle link and place it in the 'dataset' folder.
- You need to obtain an OpenWeatherMap API key and update it in weather_alerts.py.
- Run train_model.py to train the model and generate models/mango_disease_model.h5.
- Run the Streamlit app with `streamlit run app.py`.
- Test the app by uploading leaf images and exploring features.

Please confirm if you want me to assist with any of these next steps or if you want me to help with anything else related to this project.
