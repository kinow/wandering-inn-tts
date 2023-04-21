from pathlib import Path

import subprocess

next_file = '0000_3.19_t.txt'

print(next_file)

output_file = Path(next_file).name + ".wav"

with open(next_file) as f:
  r = subprocess.run(
    [
      'pico2wave', '-l', '"en-US"', '-w', output_file, f'"{f.read()}"'
    ]
  )
  r.check_returncode()

# Text to speech to a file
