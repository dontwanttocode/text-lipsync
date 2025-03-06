import sys
import os
from gtts import gTTS  
from pydub import AudioSegment

# Add 'Wav2Lip' folder to Python path
sys.path.append(os.path.abspath("Wav2Lip"))

# Define the text for speech synthesis
text = '''Namaste Mathangi! My name is Anika, and I’m here to guide you through managing your credit
card dues. Mathangi, as of today, your credit card bill shows an amount due of INR 5,053 which
needs to be paid by 31st December 2024. Missing this payment could lead to two significant consequences:
First, a late fee will be added to your outstanding balance.
Second, your credit score will be negatively impacted, which may affect your future borrowing
ability. Make your payment by clicking the link here... Pay through UPI or bank transfer. Thank you!
'''  

language = "en"

# Generate TTS audio
tts = gTTS(
    text=text, 
    lang=language, 
    tld="co.in", 
    slow=False
)

# Save audio as MP3 and convert to WAV
tts.save("Wav2Lip/output.mp3")
audio = AudioSegment.from_mp3("Wav2Lip/output.mp3")
audio.export("Wav2Lip/output.wav", format="wav")

print("✅ Audio generated: output.wav")

