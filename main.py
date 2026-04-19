import numpy as np
from scipy.signal import resample
from scipy.io import wavfile
import matplotlib.pyplot as plt

# --- Audio Settings ---
sample_rate_high = 44100  # Target high-resolution sample rate
sample_rate_low = 8000    # Low resolution (Must be > 2 * highest frequency for Nyquist)
duration = 2.0            # Length of the audio in seconds

# --- Bandpass Signal Parameters ---
# Carrier frequency (the high "bandpass" part): 3000 Hz
# Modulator frequency (the low-frequency envelope): 5 Hz
f_carrier = 3000
f_mod = 5

# 1. Generate the Time Arrays
t_high = np.linspace(0, duration, int(sample_rate_high * duration), endpoint=False)
t_low = np.linspace(0, duration, int(sample_rate_low * duration), endpoint=False)

# 2. Generate the True High-Resolution Signal
envelope_high = 1 + np.sin(2 * np.pi * f_mod * t_high)
wave_true = envelope_high * np.sin(2 * np.pi * f_carrier * t_high)

# 3. Generate the Low-Resolution "Sampled" Signal
envelope_low = 1 + np.sin(2 * np.pi * f_mod * t_low)
wave_low = envelope_low * np.sin(2 * np.pi * f_carrier * t_low)

# 4. Interpolate the low-resolution signal back to high-resolution
# Method A: Linear Interpolation (Choppy, straight lines)
wave_lin = np.interp(t_high, t_low, wave_low)

# Method B: Fourier (Ideal Bandlimited) Interpolation
wave_ideal = resample(wave_low, len(t_high))

# 5. Helper function to normalize and save as 16-bit PCM WAV
def save_wav(filename, wave_data):
    wave_data = wave_data - np.mean(wave_data) 
    max_val = np.max(np.abs(wave_data))
    if max_val > 0:
        wave_data = wave_data / max_val
    wave_data_int16 = np.int16(wave_data * 32767)
    wavfile.write(filename, sample_rate_high, wave_data_int16)
    print(f"Saved: {filename}")

# --- Generate the Audio Files ---
print("Generating bandpass audio files...")
save_wav("bandpass_true.wav", wave_true)
save_wav("bandpass_linear.wav", wave_lin)
save_wav("bandpass_ideal.wav", wave_ideal)

# --- Generate the Plot ---
print("Generating visual plot...")
plt.figure(figsize=(12, 8))

# Zoom in on the first 5 milliseconds to actually see the waves
zoom_start = 0.0
zoom_end = 0.005

# Subplot 1: True Signal vs Points
plt.subplot(3, 1, 1)
plt.plot(t_high, wave_true, label='True Signal (44.1 kHz)', color='black', alpha=0.7)
plt.scatter(t_low, wave_low, label='Sampled Points (8 kHz)', color='red', zorder=5)
plt.xlim(zoom_start, zoom_end)
plt.title('True Signal vs Low-Resolution Samples')
plt.legend(loc='upper right')

# Subplot 2: Linear Interpolation
plt.subplot(3, 1, 2)
plt.plot(t_high, wave_true, label='True Signal', color='black', alpha=0.3)
plt.plot(t_high, wave_lin, label='Linear Interpolation', color='orange', linestyle='--')
plt.scatter(t_low, wave_low, color='red', zorder=5)
plt.xlim(zoom_start, zoom_end)
plt.title('Linear Interpolation (Notice the sharp, jagged edges)')
plt.legend(loc='upper right')

# Subplot 3: Ideal Interpolation
plt.subplot(3, 1, 3)
plt.plot(t_high, wave_true, label='True Signal', color='black', alpha=0.3, linewidth=4)
plt.plot(t_high, wave_ideal, label='Ideal (FFT) Interpolation', color='green', linestyle='--')
plt.scatter(t_low, wave_low, color='red', zorder=5)
plt.xlim(zoom_start, zoom_end)
plt.title('Ideal Bandlimited Interpolation (Perfectly tracks the true curve)')
plt.legend(loc='upper right')
plt.xlabel('Time (seconds)')

plt.tight_layout()
plt.savefig("bandpass_comparison.png")
print("Saved: bandpass_comparison.png")
print("Done!")