# Bandpass Signal Interpolation Audio Demonstration

This project demonstrates **bandpass signal interpolation** through audio synthesis. It compares different interpolation methods by generating and comparing audio waveforms created using:

- **True Signal**: The exact high-resolution signal (44.1 kHz)
- **Linear Interpolation**: Piecewise linear reconstruction (choppy, produces sharp edges)
- **Ideal (FFT) Interpolation**: Bandlimited interpolation (smooth, perfect reconstruction)

## Overview

The project demonstrates how different interpolation methods recover a high-resolution signal from low-resolution samples (8 kHz). It uses a bandpass signal composed of a 3000 Hz carrier modulated by a 5 Hz envelope, then generates 2-second audio files at 44.1 kHz to highlight the differences in interpolation quality. You can listen to the files to hear how ideal bandlimited interpolation produces a smooth reconstruction compared to linear interpolation's artifacts.

## Files

- `main.py` - Main script that generates the audio files and comparison plot
- `bandpass_true.wav` - Reference signal (ground truth at 44.1 kHz)
- `bandpass_linear.wav` - Linear interpolation result
- `bandpass_ideal.wav` - Ideal (FFT) bandlimited interpolation result
- `bandpass_comparison.png` - Visual comparison of the three methods

## Parameters

- **Sample Rate (High)**: 44.1 kHz (true signal)
- **Sample Rate (Low)**: 8 kHz (downsampled signal)
- **Duration**: 2.0 seconds
- **Carrier Frequency**: 3000 Hz
- **Modulator Frequency**: 5 Hz

## Usage

```bash
python main.py
```

This will generate three WAV files and a PNG visualization demonstrating the differences between interpolation methods.
