import rerun as rr
from math import tau
import numpy as np
from rerun_demo.data import build_color_spiral
from rerun_demo.util import bounce_lerp, interleave

NUM_POINTS = 100

# Initialize rerun module
def init_rr():
    rr.init("DNA Abacus")
    rr.spawn()
    rr.set_time_seconds("stable_time", 0)

# Log points with given attributes
def log_points(name, points, colors, radii):
    rr.log_points(name, points, colors=colors, radii=radii)

# Log scaffolding structure
def log_scaffolding(points):
    rr.log_line_segments("dna/structure/scaffolding", points, color=[128, 128, 128])

# Generate beads and colors
def generate_beads_and_colors(points1, points2, offsets):
    beads = [bounce_lerp(points1[n], points2[n], offsets[n]) for n in range(NUM_POINTS)]
    colors = [[int(bounce_lerp(80, 230, offsets[n] * 2))] for n in range(NUM_POINTS)]
    return beads, np.repeat(colors, 3, axis=-1)

# Log bead locations and colors
def log_beads(points1, points2, offsets, time):
    beads, colors = generate_beads_and_colors(points1, points2, offsets)
    rr.log_points("dna/structure/scaffolding/beads", beads, radii=0.06, colors=colors)

# Animate bead movement
def animate_beads(points1, points2, time_offsets):
    for i in range(400):
        time = i * 0.01
        times = np.repeat(time, NUM_POINTS) + time_offsets
        log_beads(points1, points2, times, time)
        rr.log_transform3d(
            "dna/structure",
            rr.RotationAxisAngle(axis=[0, 0, 1], radians=time / 4.0 * tau),
        )
        rr.set_time_seconds("stable_time", time) # moved to minimize latency/jitter

# Build and log spiral points
def build_and_log_points():
    points1, colors1 = build_color_spiral(NUM_POINTS)
    points2, colors2 = build_color_spiral(NUM_POINTS, angular_offset=tau*0.5)
    log_points("dna/structure/left", points1, colors1, 0.08)
    log_points("dna/structure/right", points2, colors2, 0.08)
    return points1, points2

# Main execution function
def main():
    try:
        init_rr()
        points1, points2 = build_and_log_points()
        points = interleave(points1, points2)
        log_scaffolding(points)
        offsets = np.random.rand(NUM_POINTS)
        log_beads(points1, points2, offsets, 0)
        animate_beads(points1, points2, np.random.rand(NUM_POINTS))
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
    finally:
        os.kill(os.getpid(), signal.SIGTERM)

if __name__ == "__main__":
    main()