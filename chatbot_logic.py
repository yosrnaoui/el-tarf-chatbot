import pandas as pd
from langdetect import detect, DetectorFactory
import re

# For consistent language detection
DetectorFactory.seed = 0

# Load the dataset (CSV must be in same folder)
df = pd.read_csv('algeria_tourist_places_all_cities.csv')
el_tarf_df = df[df['City'] == 'El Tarf']
categories = el_tarf_df['Type'].unique().tolist()

# Mappings (same as dans ton fichier original)
category_map = {
    'en': {cat.lower(): cat for cat in categories},
    'fr': {
        'hôtel': 'Hotel', 'hôtels': 'Hotel', 'montagne': 'Mountain', 'montagnes': 'Mountain',
        'plage': 'Beach', 'plages': 'Beach', 'restaurant': 'Restaurant', 'restaurants': 'Restaurant',
        'site archéologique': 'Archaeological Site', 'sites archéologiques': 'Archaeological Site',
        'musée': 'Museum', 'musées': 'Museum', 'bibliothèque': 'Library', 'bibliothèques': 'Library',
        'stade': 'Stadium', 'stades': 'Stadium', 'parc': 'Park', 'parcs': 'Park',
        'centre commercial': 'Shopping Mall', 'centres commerciaux': 'Shopping Mall',
        'attraction touristique': 'Tourist Attraction', 'attractions touristiques': 'Tourist Attraction',
        'camping': 'Campground', 'campings': 'Campground'
    },
    'ar': {
        'فندق': 'Hotel', 'فنادق': 'Hotel', 'جبل': 'Mountain', 'جبال': 'Mountain',
        'شاطئ': 'Beach', 'شواطئ': 'Beach', 'ساحل': 'Beach', 'مطعم': 'Restaurant', 'مطاعم': 'Restaurant',
        'موقع أثري': 'Archaeological Site', 'مواقع أثرية': 'Archaeological Site',
        'متحف': 'Museum', 'متاحف': 'Museum', 'مكتبة': 'Library', 'مكتبات': 'Library',
        'ملعب': 'Stadium', 'ملاعب': 'Stadium', 'حديقة': 'Park', 'حدائق': 'Park',
        'مركز تجاري': 'Shopping Mall', 'مراكز تجارية': 'Shopping Mall',
        'معلم سياحي': 'Tourist Attraction', 'معالم سياحية': 'Tourist Attraction',
        'مخيم': 'Campground', 'مخيمات': 'Campground'
    }
}

# Protection messages
protection_instructions = {
    'Hotel': {
        'en': 'Respect hotel property and dispose of waste...',
        'fr': 'Respectez la propriété de l’hôtel...',
        'ar': 'احترم ممتلكات الفندق...'
    },
    'Mountain': {
        'en': 'Stay on marked trails to prevent soil erosion...',
        'fr': 'Restez sur les sentiers balisés...',
        'ar': 'ابق على المسارات المحددة...'
    },
    # ✂️ ajoute les autres comme dans ton fichier si besoin
}

def detect_language(text):
    try:
        lang = detect(text)
        return lang if lang in ['ar', 'fr', 'en'] else 'en'
    except:
        return 'en'

def get_category_spots(category, lang):
    category = category.lower()
    category_key = next((k for k in category_map[lang] if k in category), None)
    if not category_key:
        return "Category not recognized."

    matches = el_tarf_df[el_tarf_df['Type'] == category_map[lang][category_key]]
    if matches.empty:
        return "No places found."

    response = ""
    for _, row in matches.iterrows():
        response += f"- {row['Name']} at ({row['Latitude']}, {row['Longitude']})\n"
    response += f"\nProtection Instructions: {protection_instructions.get(category_map[lang][category_key], {'en': 'Follow local guidelines.', 'fr': 'Suivez les directives locales.', 'ar': 'اتبع الإرشادات المحلية.'})[lang]}"
    return response

def process_query(query):
    lang = detect_language(query)
    query = query.lower().strip()

    # Détection mots-clés
    for lang_cat, keywords in category_map[lang].items():
        if lang_cat in query:
            return get_category_spots(lang_cat, lang)

    return {
        'en': "Sorry, I couldn't understand your request.",
        'fr': "Désolé, je n'ai pas compris votre demande.",
        'ar': "عذرًا، لم أفهم طلبك."
    }[lang]
