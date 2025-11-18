# separate_audio.py
# Διαχωρίζει φωνή και μουσική από ένα αρχείο ήχου (.mp3, .wav, κλπ)
# Αποθηκεύει δύο αρχεία: vocals.wav και instrumental.wav

import os
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"
from spleeter.separator import Separator

def separate_audio(input_file):
    # Έλεγχος αν υπάρχει το αρχείο
    if not os.path.exists(input_file):
        print(f" The file '{input_file}' doesnt found.")
        return

    # Δημιουργία διαχωριστή (2stems = φωνή + μουσική)
    separator = Separator('spleeter:2stems')

    # Εκτέλεση διαχωρισμού
    print(" Spliting the file... (this may need some time)")
    separator.separate_to_file(input_file, 'output')

    print("\nThe splitting is completed!")
    print("Files saved at 'output' folder ")
    print("   - vocals.wav (only voice)")
    print("   - accompaniment.wav (only music)")

if __name__ == "__main__":
    # Παράδειγμα χρήσης:
    # Αν το αρχείο είναι στο ίδιο φάκελο με αυτό το script
    input_path = "ston_lefko_ton_purgo.mp3"
    separate_audio(input_path)
