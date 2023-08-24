import rerun as rr
import numpy as np

def init_rerun(data_name):
    rr.init(data_name, spawn=True)

def create_positions(num_positions, start, end):
    positions = np.zeros((num_positions, 3))
    positions[:,0] = np.linspace(start, end, num_positions)
    return positions

def create_colors(num_colors, start, end):
    colors = np.zeros((num_colors, 3), dtype=np.uint8)
    colors[:,0] = np.linspace(start, end, num_colors)
    return colors

def log_points(name, positions, colors, radii):
    rr.log_points(name, positions=positions, colors=colors, radii=radii)

def main():
    init_rerun("my data")
    positions = create_positions(10, -10, 10)
    colors = create_colors(10, 0, 255)
    log_points("my_points", positions, colors, 0.5)

if __name__ == "__main__":
    main()