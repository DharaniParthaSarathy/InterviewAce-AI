import speech_recognition as sr
import tempfile
import os

def speech_to_text(audio_bytes):

    recognizer = sr.Recognizer()

    try:

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        )

        temp_file.write(audio_bytes)

        temp_file.close()

        with sr.AudioFile(
            temp_file.name
        ) as source:

            audio = recognizer.record(
                source
            )

        text = recognizer.recognize_google(
            audio
        )

        os.unlink(
            temp_file.name
        )

        return text

    except Exception as e:

        return f"Error: {str(e)}"