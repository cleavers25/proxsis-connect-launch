import numpy as np
import wave
import math

sr = 44100
duration = 92.0
total_samples = int(sr * duration)
t = np.linspace(0, duration, total_samples, False)

audio = np.zeros(total_samples, dtype=np.float32)

# Chords progression (frequencies in Hz)
# Cmaj9: C3, G3, B3, D4, E4
# Am9:   A2, E3, G3, B3, C4
# Fmaj7: F2, C3, E3, A3, C4
# Gsus4: G2, D3, G3, C4, D4
chords = [
    [130.81, 196.00, 246.94, 293.66, 329.63], # Cmaj9
    [110.00, 164.81, 196.00, 246.94, 261.63], # Am9
    [87.31, 130.81, 164.81, 220.00, 261.63],  # Fmaj7
    [98.00, 146.83, 196.00, 261.63, 293.66],  # Gsus4
]

chord_len = 8.0 # seconds per chord
n_chords = int(duration / chord_len) + 1

for ci in range(n_chords):
    c_start = ci * chord_len
    c_end = min((ci + 1) * chord_len, duration)
    s_idx = int(c_start * sr)
    e_idx = int(c_end * sr)
    cur_len = e_idx - s_idx
    if cur_len <= 0:
        continue
    
    t_chord = np.linspace(0, c_end - c_start, cur_len, False)
    chord_freqs = chords[ci % len(chords)]
    
    # Warm pad sound with soft attack and decay
    env = np.ones(cur_len, dtype=np.float32)
    att_samples = int(1.2 * sr)
    dec_samples = int(1.2 * sr)
    if cur_len > att_samples:
        env[:att_samples] = np.linspace(0, 1, att_samples)
    if cur_len > dec_samples:
        env[-dec_samples:] = np.linspace(1, 0, dec_samples)
        
    chord_wave = np.zeros(cur_len, dtype=np.float32)
    for idx, f in enumerate(chord_freqs):
        vol = 0.08 if idx == 0 else 0.05
        # fundamental + soft harmonics
        chord_wave += vol * (np.sin(2 * np.pi * f * t_chord) + 
                             0.3 * np.sin(2 * np.pi * f * 2 * t_chord) +
                             0.1 * np.sin(2 * np.pi * f * 3 * t_chord))
    
    audio[s_idx:e_idx] += chord_wave * env

# Add scene transition bell chimes at specific transition times
scene_chimes = [0.2, 6.0, 22.0, 42.0, 74.0, 84.0]
for st in scene_chimes:
    s_idx = int(st * sr)
    chime_dur = 2.5
    c_len = int(chime_dur * sr)
    if s_idx + c_len < total_samples:
        tc = np.linspace(0, chime_dur, c_len, False)
        # exponential decay chime
        chime_env = np.exp(-tc * 2.5)
        # chime chord: C6 (1046 Hz), G6 (1568 Hz), E6 (1318 Hz)
        chime_wave = 0.07 * (np.sin(2 * np.pi * 1046.5 * tc) + 
                             0.05 * np.sin(2 * np.pi * 1318.5 * tc) +
                             0.04 * np.sin(2 * np.pi * 1567.9 * tc)) * chime_env
        audio[s_idx:s_idx + c_len] += chime_wave

# Normalize audio to -3dB peak
max_val = np.max(np.abs(audio))
if max_val > 0:
    audio = (audio / max_val) * 0.75

audio_int16 = (audio * 32767).astype(np.int16)

wav_path = "/home/cleavers/Dokumen/coolify_new/soundtrack.wav"
with wave.open(wav_path, "w") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(sr)
    wf.writeframes(audio_int16.tobytes())

print(f"Audio synthesized successfully: {wav_path}")
