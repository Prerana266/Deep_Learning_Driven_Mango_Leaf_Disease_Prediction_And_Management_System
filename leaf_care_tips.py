# Healthy leaf care tips database
CARE_TIPS = {
    'Watering': [
        'Water plants early in the morning or late in the evening to reduce evaporation.',
        'Avoid overwatering to prevent root rot.',
        'Use drip irrigation for efficient water use.',
        'Check soil moisture before watering - stick finger 2 inches into soil.',
        'Water deeply but less frequently to encourage deep root growth.'
    ],
    'Nutrition': [
        'Apply balanced fertilizers based on soil test results.',
        'Use organic compost to improve soil health.',
        'Avoid excessive use of nitrogen fertilizers.',
        'Apply micronutrients like zinc and boron as needed.',
        'Use slow-release fertilizers for sustained nutrition.'
    ],
    'Pruning': [
        'Prune diseased and dead branches regularly.',
        'Maintain proper plant spacing for air circulation.',
        'Use sterilized tools to prevent disease spread.',
        'Prune during dry weather to reduce infection risk.',
        'Make clean cuts at 45-degree angle away from buds.'
    ],
    'Pest Management': [
        'Monitor plants regularly for pest infestation.',
        'Use integrated pest management (IPM) techniques.',
        'Encourage natural predators like ladybugs and spiders.',
        'Use yellow sticky traps for monitoring flying insects.',
        'Apply neem oil as preventive measure every 15 days.'
    ],
    'General Care': [
        'Mulch around plants to retain moisture and suppress weeds.',
        'Rotate crops to prevent soil-borne diseases.',
        'Keep the orchard clean and free from plant debris.',
        'Provide adequate sunlight exposure.',
        'Maintain proper drainage to prevent waterlogging.'
    ],
    'Seasonal Care': {
        'Summer': [
            'Increase watering frequency during hot weather.',
            'Provide shade for young plants.',
            'Apply mulch to retain soil moisture.',
            'Monitor for heat stress symptoms.'
        ],
        'Monsoon': [
            'Improve drainage to prevent waterlogging.',
            'Increase fungicide applications.',
            'Remove fallen leaves promptly.',
            'Check for fungal infections regularly.'
        ],
        'Winter': [
            'Reduce watering frequency.',
            'Protect young plants from frost.',
            'Apply winter fertilizers.',
            'Prune during dormant season.'
        ]
    },
    'Soil Health': [
        'Test soil pH and adjust if needed (6.0-7.0 ideal for most crops).',
        'Add organic matter annually to improve soil structure.',
        'Avoid soil compaction by using proper equipment.',
        'Use cover crops to prevent erosion.',
        'Maintain beneficial microbial activity.'
    ],
    'Disease Prevention': [
        'Use disease-resistant varieties when available.',
        'Practice crop rotation every 2-3 years.',
        'Remove and destroy infected plant material.',
        'Disinfect tools between plants.',
        'Maintain plant vigor through proper nutrition.'
    ]
}

from multilingual_support import translate_text

def get_care_tips(language_code='en'):
    """Return healthy leaf care tips"""
    translated_tips = {}
    for category, tips in CARE_TIPS.items():
        translated_category = translate_text(category, language_code)
        if isinstance(tips, list):
            translated_tips[translated_category] = [translate_text(tip, language_code) for tip in tips]
        else:
            # For seasonal care, translate both the category and season names
            translated_seasons = {}
            for season, season_tips in tips.items():
                translated_season = translate_text(season, language_code)
                translated_seasons[translated_season] = [translate_text(tip, language_code) for tip in season_tips]
            translated_tips[translated_category] = translated_seasons
    return translated_tips

def get_seasonal_care_tips(season):
    """Get care tips for specific season"""
    return CARE_TIPS.get('Seasonal Care', {}).get(season, [])

def get_tip_by_category(category):
    """Get tips for specific category"""
    return CARE_TIPS.get(category, [])
