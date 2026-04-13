# ECE 454: Signal Interpolation

This project demonstrates **Runge's phenomenon** through audio synthesis. It compares different polynomial interpolation methods by generating and comparing audio waveforms created using:

- **True Signal**: The exact mathematical function
- **Linear Interpolation**: Piecewise linear approximation (stable but less smooth)
- **Polynomial Interpolation**: High-degree polynomial fit (exhibits Runge's phenomenon with oscillations)

## Overview

The project interpolates the Runge function `1/(1 + 25x²)` using only 11 sample points, then generates 2-second audio files at 441 Hz to highlight the artifacts that occur with polynomial interpolation. You can listen to the files to hear how polynomial interpolation introduces unwanted oscillations compared to linear interpolation.

## Files

- `main.py` - Main script that generates the audio files
- `runge_true.wav` - Reference signal (ground truth)
- `runge_linear.wav` - Linear interpolation result
- `runge_poly.wav` - Polynomial interpolation result (exhibits Runge's phenomenon)

## Usage

```bash
python main.py
```

This will generate three WAV files demonstrating the differences between interpolation methods.
