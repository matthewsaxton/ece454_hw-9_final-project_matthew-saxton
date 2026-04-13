import numpy as np
from scipy.interpolate import BarycentricInterpolator
from scipy.io import wavfile

# --- Audio Settings ---
sample_rate = 44100
freq = 441          # 441 Hz gives us exactly 100 samples per cycle
duration = 2.0      # Length of the audio in seconds
samples_per_cycle = int(sample_rate / freq) 
num_cycles = int(freq * duration) 

# 1. Define the base x interval for one single cycle of the soundwave
x_cycle = np.linspace(-1, 1, samples_per_cycle)

# 2. Generate the True Signal Cycle
y_true_cycle = 1 / (1 + 25 * x_cycle**2)

# 3. Create low-resolution samples (11 points) to simulate a poorly sampled wave
x_low = np.linspace(-1, 1, 11)
y_low = 1 / (1 + 25 * x_low**2)

# 4. Interpolate the cycles
# Linear Interpolation (Choppy but stable)
y_lin_cycle = np.interp(x_cycle, x_low, y_low)

# Polynomial Interpolation (Produces Runge's Phenomenon)
poly_interpolator = BarycentricInterpolator(x_low, y_low)
y_poly_cycle = poly_interpolator(x_cycle)

# 5. Build full 2-second audio waves by repeating the single cycles
wave_true = np.tile(y_true_cycle, num_cycles)
wave_lin = np.tile(y_lin_cycle, num_cycles)
wave_poly = np.tile(y_poly_cycle, num_cycles)

# 6. Helper function to normalize and save as 16-bit PCM WAV
def save_wav(filename, wave_data):
    # Remove DC offset (center the wave)
    wave_data = wave_data - np.mean(wave_data) 
    
    # Normalize volume to prevent speakers from blowing out, 
    # especially needed for the massive spikes in wave_poly
    max_val = np.max(np.abs(wave_data))
    if max_val > 0:
        wave_data = wave_data / max_val
        
    # Convert to 16-bit audio format
    wave_data_int16 = np.int16(wave_data * 32767)
    
    # Save the file
    wavfile.write(filename, sample_rate, wave_data_int16)
    print(f"Saved: {filename}")

# --- Generate the Files ---
print("Generating audio files...")
save_wav("runge_true.wav", wave_true)
save_wav("runge_linear.wav", wave_lin)
save_wav("runge_poly.wav", wave_poly)
print("Done!")