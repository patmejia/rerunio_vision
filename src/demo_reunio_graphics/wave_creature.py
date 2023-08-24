import rerun as rr
import numpy as np
import matplotlib.pyplot as plt
import time

def init_rerun(data_name):
    rr.init(data_name, spawn=True)

def create_positions(x, y, z):
    return np.column_stack([x, y, z])

def create_colors(z, colormap):
    gradient_magnitude = np.sqrt(np.gradient(z, axis=1)**2 + np.gradient(z, axis=0)**2)
    epsilon = 1e-6
    gradient_magnitude = (gradient_magnitude - gradient_magnitude.min()) / (gradient_magnitude.max() - gradient_magnitude.min() + epsilon)
    return (colormap(gradient_magnitude.flatten())[:, :3] * 255).astype(np.uint8)

def log_points(name, x, y, z, color=None, radii=0.1):
    positions = create_positions(x, y, z)
    colors = color if color is not None else np.full_like(positions, [0, 76, 153], dtype=np.uint8)
    rr.log_points(name, positions=positions, colors=colors, radii=radii)

def animate_WaterMesh(t, bg_x, bg_y):
    wave_speed = 15
    bg_z = 0.4 * (np.sin(2 * np.pi * (bg_x + t/wave_speed) / 10) + np.sin(2 * np.pi * (bg_y - t/wave_speed) / 10)) - 5
    damping = 0.99
    bg_z *= damping
    log_points("WaterMesh", bg_x.flatten(), bg_y.flatten(), bg_z.flatten())
    return bg_z

def animate_surface(t, total_duration, x, y, colormap):
    z = compute_z_values(x, y, t, total_duration)
    float_height = 1
    z += float_height
    swimming_effect = 0.3 * np.sin(2 * np.pi * t / 5)
    z += swimming_effect
    colors = create_colors(z, colormap)
    log_points("Wiggling_Sine_Wave_Surface", x.flatten(), y.flatten(), z.flatten(), colors)
    return z

def initialize_params():
    return 100, 100, -5, 5, -5, 5, 0.02, plt.get_cmap('Blues'), 20

def create_grid(xmin, xmax, ymin, ymax, width, height):
    x, y = np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height)
    return np.meshgrid(x, y)

def compute_z_values(x, y, t, total_duration):
    z = np.sin(np.sqrt(x**2 + y**2) - t) + 0.2 * np.sin(4 * np.pi * t / total_duration)
    vertical_shift = 0.5 * np.sin(2 * np.pi * t / total_duration)
    return z + vertical_shift if t <= total_duration / 2 else z - vertical_shift

def animate():
    width, height, xmin, xmax, ymin, ymax, dt, colormap, total_duration = initialize_params()
    x, y = create_grid(xmin, xmax, ymin, ymax, width, height)
    
    for t in np.arange(0, total_duration + dt / 2, dt):
        creature_z = animate_surface(t, total_duration, x, y, colormap)
        bg_z = animate_WaterMesh(t, x, y)
        time.sleep(dt)

def main():
    init_rerun("Animated 3D Wiggling Sine Wave Surface")
    animate()

if __name__ == "__main__":
    main()