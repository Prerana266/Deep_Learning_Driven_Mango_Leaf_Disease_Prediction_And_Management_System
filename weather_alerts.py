import requests
import streamlit as st
import json
from datetime import datetime, timedelta
from multilingual_support import translate_text

# Weather API configuration
WEATHER_API_KEY = st.secrets["WEATHER_API_KEY"] # Replace with actual API key
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_API_URL = "http://api.openweathermap.org/data/2.5/forecast"

# Disease risk thresholds based on weather conditions
DISEASE_RISK_THRESHOLDS = {
    'Anthracnose': {
        'temperature_range': (20, 30),
        'humidity_min': 80,
        'rainfall_min': 5,
        'risk_level': 'High'
    },
    'Bacterial Canker': {
        'temperature_range': (25, 35),
        'humidity_min': 70,
        'rainfall_min': 10,
        'risk_level': 'Very High'
    },
    'Powdery Mildew': {
        'temperature_range': (20, 25),
        'humidity_min': 40,
        'humidity_max': 70,
        'risk_level': 'Moderate'
    },
    'Cutting Weevil': {
        'temperature_range': (25, 30),
        'humidity_min': 60,
        'risk_level': 'Moderate'
    }
}

def get_weather_data(location):
    """Get current weather data for a location"""
    try:
        params = {
            'q': location,
            'appid': WEATHER_API_KEY,
            'units': 'metric'
        }
        
        response = requests.get(WEATHER_API_URL, params=params)
        data = response.json()
        
        if response.status_code == 200:
            return {
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'weather_description': data['weather'][0]['description'],
                'rainfall': data.get('rain', {}).get('1h', 0),
                'wind_speed': data['wind']['speed']
            }
        else:
            return None
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def calculate_disease_risk(weather_data, disease_name, language_code='en'):
    """Calculate disease risk based on weather conditions"""
    if not weather_data or disease_name not in DISEASE_RISK_THRESHOLDS:
        return {
            'risk_level': translate_text('Unknown', language_code), 
            'recommendation': translate_text('Unable to assess risk', language_code)
        }
    
    thresholds = DISEASE_RISK_THRESHOLDS.get(disease_name, {})
    
    risk_factors = []
    
    # Check temperature
    if 'temperature_range' in thresholds:
        temp_min, temp_max = thresholds['temperature_range']
        if temp_min <= weather_data['temperature'] <= temp_max:
            risk_factors.append(translate_text('Temperature favorable', language_code))
    
    # Check humidity
    if 'humidity_min' in thresholds:
        if weather_data['humidity'] >= thresholds['humidity_min']:
            risk_factors.append(translate_text('High humidity', language_code))
    
    # Check rainfall
    if 'rainfall_min' in thresholds:
        if weather_data['rainfall'] >= thresholds['rainfall_min']:
            risk_factors.append(translate_text('Recent rainfall', language_code))
    
    # Determine risk level
    risk_level = translate_text(thresholds.get('risk_level', 'Low'), language_code)
    
    # Generate recommendations
    if len(risk_factors) >= 2:
        recommendation = translate_text('High risk conditions detected. Consider preventive fungicide application.', language_code)
    elif len(risk_factors) == 1:
        recommendation = translate_text('Moderate risk. Monitor plants closely and take preventive measures.', language_code)
    else:
        recommendation = translate_text('Low risk conditions. Continue regular monitoring.', language_code)
    
    return {
        'risk_level': risk_level,
        'temperature': weather_data['temperature'],
        'humidity': weather_data['humidity'],
        'rainfall': weather_data['rainfall'],
        'recommendation': recommendation,
        'risk_factors': risk_factors
    }

def get_weather_risk(location, language_code='en'):
    """Get weather-based disease risk for a location"""
    weather_data = get_weather_data(location)
    
    if weather_data:
        # Get risk for common diseases
        risks = {}
        for disease in ['Anthracnose', 'Bacterial Canker', 'Powdery Mildew', 'Cutting Weevil']:
            risks[disease] = calculate_disease_risk(weather_data, disease, language_code)
        
        # Find highest risk
        highest_risk = max(risks.items(), key=lambda x: len(x[1].get('risk_factors', [])))
        
        return {
            'temperature': weather_data['temperature'],
            'humidity': weather_data['humidity'],
            'rainfall': weather_data['rainfall'],
            'risk_level': highest_risk[1]['risk_level'],
            'recommendation': highest_risk[1]['recommendation'],
            'all_risks': risks
        }
    
    return None

def get_forecast_data(location, days=3):
    """Get weather forecast for disease risk prediction"""
    try:
        params = {
            'q': location,
            'appid': WEATHER_API_KEY,
            'units': 'metric'
        }
        
        response = requests.get(FORECAST_API_URL, params=params)
        data = response.json()
        
        if response.status_code == 200:
            forecast = []
            for item in data['list'][:days*8]:  # 8 forecasts per day
                forecast.append({
                    'date': datetime.fromtimestamp(item['dt']),
                    'temperature': item['main']['temp'],
                    'humidity': item['main']['humidity'],
                    'rainfall': item.get('rain', {}).get('3h', 0),
                    'weather': item['weather'][0]['description']
                })
            return forecast
        else:
            return None
    except Exception as e:
        print(f"Error fetching forecast data: {e}")
        return None
