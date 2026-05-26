# Disease information database
DISEASE_DATABASE = {
    'Anthracnose': {
        'name': 'Anthracnose',
        'scientific_name': 'Colletotrichum gloeosporioides',
        'severity': 'High',
        'spread_rate': 'Rapid',
        'causes': [
            'Fungal infection caused by Colletotrichum gloeosporioides',
            'Spread through rain splash and wind',
            'Favored by warm, humid conditions',
            'Infected plant debris and seeds'
        ],
        'symptoms': [
            'Dark brown to black spots on leaves',
            'Sunken lesions with concentric rings',
            'Leaf curling and distortion',
            'Premature leaf drop',
            'Fruit spots with pink spore masses'
        ],
        'image_path': 'images/anthracnose.jpg'
    },
    
    'Bacterial Canker': {
        'name': 'Bacterial Canker',
        'scientific_name': 'Xanthomonas campestris pv. mangiferaeindicae',
        'severity': 'Very High',
        'spread_rate': 'Moderate to Rapid',
        'causes': [
            'Bacterial infection by Xanthomonas campestris',
            'Spread through rain splash and infected tools',
            'Entry through wounds or natural openings',
            'Favored by warm, wet conditions'
        ],
        'symptoms': [
            'Water-soaked lesions on leaves',
            'Dark brown to black cankers on stems',
            'Gummy exudation from cankers',
            'Leaf wilting and dieback',
            'Fruit drop and black spots'
        ],
        'image_path': 'images/bacterial_canker.jpg'
    },
    
    'Cutting Weevil': {
        'name': 'Cutting Weevil',
        'scientific_name': 'Sternochetus mangiferae',
        'severity': 'Moderate',
        'spread_rate': 'Slow to Moderate',
        'causes': [
            'Insect pest - mango seed weevil',
            'Adult weevils lay eggs in fruits',
            'Larvae feed on seeds and pulp',
            'Spread through infested fruits'
        ],
        'symptoms': [
            'Small holes in fruits',
            'Premature fruit drop',
            'Damaged seeds inside fruits',
            'Dark streaks on fruit surface',
            'Reduced fruit quality'
        ],
        'image_path': 'images/cutting_weevil.jpg'
    },
    
    'Die Back': {
        'name': 'Die Back',
        'scientific_name': 'Botryosphaeria spp.',
        'severity': 'High',
        'spread_rate': 'Moderate',
        'causes': [
            'Fungal infection by Botryosphaeria species',
            'Stress factors like drought or wounds',
            'Spread through infected pruning tools',
            'Favored by warm, dry conditions'
        ],
        'symptoms': [
            'Progressive death of twigs and branches',
            'Dark brown to black lesions on bark',
            'Gummy exudation from affected parts',
            'Leaf wilting and yellowing',
            'Cankers on stems and branches'
        ],
        'image_path': 'images/die_back.jpg'
    },
    
    'Gall Midge': {
        'name': 'Gall Midge',
        'scientific_name': 'Procontarinia mangiferae',
        'severity': 'Moderate',
        'spread_rate': 'Moderate',
        'causes': [
            'Insect pest - mango gall midge',
            'Adult flies lay eggs in leaf tissue',
            'Larvae induce gall formation',
            'Multiple generations per year'
        ],
        'symptoms': [
            'Small galls or bumps on leaves',
            'Leaf curling and distortion',
            'Premature leaf drop',
            'Reduced photosynthesis',
            'Stunted plant growth'
        ],
        'image_path': 'images/gall_midge.jpg'
    },
    
    'Healthy': {
        'name': 'Healthy Leaf',
        'scientific_name': 'Normal plant condition',
        'severity': 'None',
        'spread_rate': 'None',
        'causes': [
            'Proper plant care and maintenance',
            'Balanced nutrition',
            'Adequate water management',
            'Regular monitoring'
        ],
        'symptoms': [
            'Uniform green color',
            'Normal leaf shape and size',
            'No spots or lesions',
            'Proper growth and development',
            'Good fruit production'
        ],
        'image_path': 'images/healthy.jpg'
    },
    
    'Powdery Mildew': {
        'name': 'Powdery Mildew',
        'scientific_name': 'Oidium mangiferae',
        'severity': 'Moderate to High',
        'spread_rate': 'Rapid',
        'causes': [
            'Fungal infection by Oidium mangiferae',
            'Spread through wind-borne spores',
            'Favored by warm, dry conditions',
            'High humidity and poor air circulation'
        ],
        'symptoms': [
            'White powdery coating on leaves',
            'Leaf curling and distortion',
            'Stunted growth of new shoots',
            'Reduced fruit set',
            'Premature leaf drop'
        ],
        'image_path': 'images/powdery_mildew.jpg'
    },
    
    'Sooty Mould': {
        'name': 'Sooty Mould',
        'scientific_name': 'Capnodium mangiferae',
        'severity': 'Low to Moderate',
        'spread_rate': 'Slow',
        'causes': [
            'Fungal growth on honeydew excreted by insects',
            'Associated with sap-sucking insects',
            'Favored by high humidity',
            'Poor air circulation'
        ],
        'symptoms': [
            'Black sooty coating on leaves',
            'Reduced photosynthesis',
            'Sticky honeydew on leaf surface',
            'Presence of ants on plants',
            'Yellowing of leaves'
        ],
        'image_path': 'images/sooty_mould.jpg'
    }
}

from multilingual_support import translate_text

def get_disease_info(disease_name, language_code='en'):
    """Get comprehensive disease information"""
    if disease_name in DISEASE_DATABASE:
        disease_info = DISEASE_DATABASE[disease_name].copy()
        
        # Translate the content based on language
        disease_info['name'] = translate_text(disease_name, language_code)  # Translate the disease name
        disease_info['scientific_name'] = translate_text(disease_info['scientific_name'], language_code)
        disease_info['severity'] = translate_text(disease_info['severity'], language_code)
        disease_info['spread_rate'] = translate_text(disease_info['spread_rate'], language_code)
        
        # Translate causes
        disease_info['causes'] = [translate_text(cause, language_code) for cause in disease_info['causes']]
        
        # Translate symptoms
        disease_info['symptoms'] = [translate_text(symptom, language_code) for symptom in disease_info['symptoms']]
        
        return disease_info
    else:
        return {
            'name': translate_text(disease_name, language_code),
            'scientific_name': translate_text('Unknown', language_code),
            'severity': translate_text('Unknown', language_code),
            'spread_rate': translate_text('Unknown', language_code),
            'causes': [translate_text('Information not available', language_code)],
            'symptoms': [translate_text('Information not available', language_code)],
            'image_path': 'images/unknown.jpg'
        }

def get_all_diseases():
    """Get list of all diseases"""
    return list(DISEASE_DATABASE.keys())

def search_disease_by_symptom(symptom):
    """Search diseases by symptom"""
    matching_diseases = []
    for disease, info in DISEASE_DATABASE.items():
        for disease_symptom in info['symptoms']:
            if symptom.lower() in disease_symptom.lower():
                matching_diseases.append(disease)
                break
    return matching_diseases
