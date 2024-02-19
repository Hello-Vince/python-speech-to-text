from pydub import AudioSegment

m4a_file = "./records/AUDIO-2024-02-17-10-20-24.m4a"
wav_filename = "output.wav"

sound = AudioSegment.from_file(m4a_file, format="m4a")
file_handle = sound.export(wav_filename, format="wav")
