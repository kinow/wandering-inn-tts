from TTS.api import TTS
from pathlib import Path

next_file = "0000_3.20_t.txt"

print(next_file)

output_file = Path(next_file).name + ".wav"

model_name = "tts_models/en/ek1/tacotron2"
tts = TTS(model_name)

with open(next_file) as f:
  tts.tts_to_file(f.read(), speaker=None, file_path=output_file)

# Text to speech to a file
