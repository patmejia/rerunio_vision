import numpy as np
import rerun as rr
from scipy.special import jn

def init_rerun(data_name):
    rr.init(data_name, spawn=True)

def create_positions(x, y, z):
    return np.column_stack([x.flatten(), y.flatten(), z.flatten()])

def log_points(name, x, y, z, radii=0.1):
    positions = create_positions(x, y, z)
    colors = np.full_like(positions, [0, 76, 153], dtype=np.uint8)
    rr.log_points(name, positions=positions, colors=colors, radii=radii)

def create_bessel_wave(x, y, t, frequency, amplitude, phase_shift):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    wave = amplitude * jn(0, frequency * r + t) * np.cos(frequency * theta + phase_shift)
    return wave

def animate_bessel_wave(total_duration, dt):
    width, height, xmin, xmax, ymin, ymax = 100, 100, -5, 5, -5, 5
    x, y = np.meshgrid(np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height))

    for t in np.arange(0, total_duration + dt/2, dt):
        frequency = 1
        amplitude = 6
        phase_shift = 0
        wave = create_bessel_wave(x, y, t, frequency, amplitude, phase_shift)
        log_points("BesselWave", x.flatten(), y.flatten(), wave.flatten())

def main():
    init_rerun("Animated Bessel Wave")
    animate_bessel_wave(total_duration=20, dt=0.02)

if __name__ == "__main__":
    main()
