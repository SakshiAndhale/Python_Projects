# Online Language Translator in Python

from googletrans import Translator

# Create a Translator instance
translator = Translator()

# Language code dictionary
languages = {
    "bn": "Bangla",
    "en": "English",
    "ko": "Korean",
    "fr": "French",
    "de": "German",
    "he": "Hebrew",
    "hi": "Hindi",
    "it": "Italian",
    "ja": "Japanese",
    'la': "Latin",
    "ms": "Malay",
    "ne": "Nepali",
    "ru": "Russian",
    "ar": "Arabic",
    "zh": "Chinese",
    "es": "Spanish"
}

# Function to display language options
def display_language_options():
    print("Code : Language")
    for code, language in languages.items():
        print(f"{code} => {language}")
    print()

# Function to get valid language code from the user
def get_language_code():
    while True:
        user_code = input(
            "Please input desired language code (or type 'options' to see the available languages): "
        ).lower()
        
        if user_code == "options":
            display_language_options()
        elif user_code in languages:
            print(f"You have selected {languages[user_code]}")
            return user_code
        else:
            print("Invalid language code! Please try again.")

# Main translation function
def translate_text():
    user_code = get_language_code()  # Get valid language code from user

    while True:
        text = input("\nEnter the text to translate (or type 'close' to exit): ").strip()

        if text.lower() == "close":
            print("\nThank you for using the translator! Have a nice day!")
            break

        try:
            # Perform the translation
            translated = translator.translate(text, dest=user_code)

            # Display the translation
            print(f"\n{languages[user_code]} translation: {translated.text}")
            print(f"Pronunciation: {translated.pronunciation or 'N/A'}")

            # Display the source language if available in the dictionary
            if translated.src in languages:
                print(f"Translated from: {languages[translated.src]}")
            else:
                print(f"Translated from: {translated.src}")

        except Exception as e:
            print(f"An error occurred during translation: {e}")

# Start the translation process
translate_text()
