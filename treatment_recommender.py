from multilingual_support import translate_text

# Treatment recommendations database
TREATMENT_DATABASE = {
    'Anthracnose': {
        'treatment': 'Apply fungicide treatment combined with cultural practices',
        'medicines': [
            {'name': 'Copper Oxychloride', 'dosage': '2.5g per liter of water'},
            {'name': 'Carbendazim', 'dosage': '1g per liter of water'},
            {'name': 'Mancozeb', 'dosage': '2g per liter of water'}
        ],
        'organic_options': [
            'Neem oil spray (5ml per liter of water)',
            'Trichoderma harzianum application',
            'Garlic extract spray',
            'Baking soda solution (1 teaspoon per liter)'
        ],
        'prevention': [
            'Remove and destroy infected plant parts',
            'Improve air circulation around plants',
            'Avoid overhead irrigation',
            'Apply balanced fertilizers',
            'Use disease-free planting material'
        ],
        'application_schedule': 'Spray every 7-10 days during favorable conditions',
        'waiting_period': '7 days before harvest'
    },
    
    'Bacterial Canker': {
        'treatment': 'Use copper-based bactericides and cultural practices',
        'medicines': [
            {'name': 'Streptomycin + Tetracycline', 'dosage': '100ppm solution'},
            {'name': 'Copper Hydroxide', 'dosage': '2g per liter of water'},
            {'name': 'Kasugamycin', 'dosage': '1ml per liter of water'}
        ],
        'organic_options': [
            'Copper soap spray',
            'Neem oil with baking soda',
            'Garlic and chili extract',
            'Beneficial bacteria (Bacillus subtilis)'
        ],
        'prevention': [
            'Use disease-free planting material',
            'Disinfect pruning tools between cuts',
            'Avoid working in wet conditions',
            'Improve drainage around plants',
            'Apply copper sprays preventively'
        ],
        'application_schedule': 'Spray every 5-7 days during wet weather',
        'waiting_period': '14 days before harvest'
    },
    
    'Cutting Weevil': {
        'treatment': 'Integrated pest management approach',
        'medicines': [
            {'name': 'Imidacloprid', 'dosage': '0.5ml per liter of water'},
            {'name': 'Thiamethoxam', 'dosage': '0.3g per liter of water'},
            {'name': 'Fipronil', 'dosage': '1ml per liter of water'}
        ],
        'organic_options': [
            'Neem cake application in soil',
            'Pheromone traps for monitoring',
            'Beneficial nematodes',
            'Beauveria bassiana spray'
        ],
        'prevention': [
            'Remove and destroy infested fruits',
            'Use pheromone traps for monitoring',
            'Maintain orchard sanitation',
            'Collect and destroy fallen fruits',
            'Use resistant varieties'
        ],
        'application_schedule': 'Spray at fruit set and repeat every 15 days',
        'waiting_period': '21 days before harvest'
    },
    
    'Die Back': {
        'treatment': 'Fungicide application and pruning management',
        'medicines': [
            {'name': 'Carbendazim', 'dosage': '1g per liter of water'},
            {'name': 'Thiophanate-methyl', 'dosage': '1g per liter of water'},
            {'name': 'Propiconazole', 'dosage': '1ml per liter of water'}
        ],
        'organic_options': [
            'Prune affected branches 6 inches below infection',
            'Apply Trichoderma to cut surfaces',
            'Use copper-based fungicides',
            'Improve plant nutrition'
        ],
        'prevention': [
            'Prune during dry weather',
            'Disinfect pruning tools between cuts',
            'Avoid mechanical injuries',
            'Maintain plant vigor',
            'Improve air circulation'
        ],
        'application_schedule': 'Spray after pruning and repeat every 14 days',
        'waiting_period': '7 days before harvest'
    },
    
    'Gall Midge': {
        'treatment': 'Insecticide application and cultural control',
        'medicines': [
            {'name': 'Dimethoate', 'dosage': '1.5ml per liter of water'},
            {'name': 'Methyl demeton', 'dosage': '1ml per liter of water'},
            {'name': 'Acephate', 'dosage': '1.5g per liter of water'}
        ],
        'organic_options': [
            'Neem oil spray (5ml per liter)',
            'Beneficial fungi (Metarhizium)',
            'Sticky traps for adults',
            'Remove and destroy galled leaves'
        ],
        'prevention': [
            'Monitor for adult flies',
            'Remove affected leaves promptly',
            'Maintain orchard hygiene',
            'Encourage natural predators',
            'Use resistant varieties'
        ],
        'application_schedule': 'Spray at first sign of infestation, repeat weekly',
        'waiting_period': '14 days before harvest'
    },
    
    'Healthy': {
        'treatment': 'Continue good agricultural practices',
        'medicines': [],
        'organic_options': [
            'Regular neem oil spray as preventive',
            'Balanced organic nutrition',
            'Compost tea application',
            'Beneficial microbe application'
        ],
        'prevention': [
            'Maintain regular monitoring',
            'Provide balanced nutrition',
            'Ensure proper irrigation',
            'Practice crop rotation',
            'Maintain orchard hygiene'
        ],
        'application_schedule': 'Regular preventive sprays every 15-20 days',
        'waiting_period': 'Not applicable'
    },
    
    'Powdery Mildew': {
        'treatment': 'Fungicide application with sulfur-based products',
        'medicines': [
            {'name': 'Wettable sulfur', 'dosage': '2g per liter of water'},
            {'name': 'Dinocap', 'dosage': '1ml per liter of water'},
            {'name': 'Hexaconazole', 'dosage': '0.5ml per liter of water'}
        ],
        'organic_options': [
            'Potassium bicarbonate spray (3g per liter)',
            'Milk spray (1:10 ratio with water)',
            'Neem oil with baking soda',
            'Sulfur dust application'
        ],
        'prevention': [
            'Improve air circulation',
            'Avoid overhead irrigation',
            'Remove affected plant parts',
            'Maintain proper plant spacing',
            'Apply preventive fungicides'
        ],
        'application_schedule': 'Spray every 7-10 days during favorable conditions',
        'waiting_period': '7 days before harvest'
    },
    
    'Sooty Mould': {
        'treatment': 'Control sap-sucking insects and wash plants',
        'medicines': [
            {'name': 'Imidacloprid', 'dosage': '0.5ml per liter of water'},
            {'name': 'Acephate', 'dosage': '1g per liter of water'},
            {'name': 'Thiamethoxam', 'dosage': '0.3g per liter of water'}
        ],
        'organic_options': [
            'Insecticidal soap spray',
            'Neem oil application',
            'Release beneficial insects',
            'Horticultural oil spray'
        ],
        'prevention': [
            'Control ant populations',
            'Monitor for sap-sucking insects',
            'Maintain plant hygiene',
            'Encourage beneficial insects',
            'Regular washing of leaves'
        ],
        'application_schedule': 'Spray insecticides as needed, wash plants regularly',
        'waiting_period': '7 days before harvest'
    }
}

def get_treatment_recommendation(disease_name, language_code='en'):
    """Get treatment recommendations for a specific disease"""
    if disease_name in TREATMENT_DATABASE:
        treatment_info = TREATMENT_DATABASE[disease_name].copy()
        
        # Translate treatment information
        treatment_info['treatment'] = translate_text(treatment_info['treatment'], language_code)
        treatment_info['name'] = translate_text(disease_name, language_code)  # Translate the disease name
        
        # Translate medicines
        for medicine in treatment_info['medicines']:
            medicine['name'] = translate_text(medicine['name'], language_code)
        
        # Translate organic options
        treatment_info['organic_options'] = [translate_text(option, language_code) for option in treatment_info['organic_options']]
        
        # Translate prevention tips
        treatment_info['prevention'] = [translate_text(tip, language_code) for tip in treatment_info['prevention']]
        
        return treatment_info
    else:
        return {
            'treatment': 'Consult local agricultural expert',
            'medicines': [],
            'organic_options': ['Contact agricultural extension service'],
            'prevention': ['Monitor plant regularly', 'Maintain good hygiene'],
            'application_schedule': 'As recommended by expert',
            'waiting_period': 'Follow expert advice'
        }

def get_cost_estimate(disease_name, area_size):
    """Estimate treatment cost based on disease and area"""
    base_costs = {
        'Anthracnose': 1500,
        'Bacterial Canker': 2000,
        'Cutting Weevil': 1800,
        'Die Back': 2200,
        'Gall Midge': 1600,
        'Powdery Mildew': 1200,
        'Sooty Mould': 1000,
        'Healthy': 0
    }
    
    if disease_name in base_costs:
        return base_costs[disease_name] * (area_size / 1000)  # Cost per 1000 sq ft
    else:
        return 1500 * (area_size / 1000)

def get_organic_alternatives(disease_name):
    """Get organic treatment alternatives"""
    treatment = get_treatment_recommendation(disease_name)
    return treatment.get('organic_options', [])

def get_prevention_schedule(disease_name):
    """Get prevention schedule for disease"""
    treatment = get_treatment_recommendation(disease_name)
    return treatment.get('prevention', [])

def compare_treatments(disease_name):
    """Compare chemical vs organic treatments"""
    treatment = get_treatment_recommendation(disease_name)
    
    comparison = {
        'chemical': {
            'effectiveness': 'High (immediate results)',
            'cost': 'Medium to High',
            'environmental_impact': 'Higher',
            'waiting_period': treatment.get('waiting_period', '7-14 days')
        },
        'organic': {
            'effectiveness': 'Medium to High (gradual results)',
            'cost': 'Low to Medium',
            'environmental_impact': 'Lower',
            'waiting_period': '0-3 days'
        }
    }
    
    return comparison
