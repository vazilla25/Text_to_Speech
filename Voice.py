from gtts import gTTS
import os
def generate_voice_from_text(text, filename="MKULIMA_voice.mp3"):
    """Convert text to speech"""
    tts = gTTS(text=text, lang='en-UK', slow=False)
    tts.save(filename)
    print(f"Voice saved as {filename}")
    os.system(f"start {filename}") # Plays the generated file (Windows)
# Example usage:
tweet_text = "The rains have started, and we hope it lasts to get a good maize crop this season."
generate_voice_from_text(tweet_text)