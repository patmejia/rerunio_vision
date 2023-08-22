# rerun_sdk:
### Computer Vision & Robotics Integration: Towards Real-Time Vision

---
<p align="center">
<img src="media/rerun_vision_robot.png" alt="Alt text" width="423">
</p>

### **Objective**: This project utilizes Rerun.io to create precise 3D visualizations for Computer Vision, including animations of a Sine Wave Surface, a Bessel Wave, and Spheres. The point logging feature of Rerun.io is used to accurately map and display the 3D coordinates of these objects.


---

<br>

## Setup

```bash
conda create -n rerun python=3.8
conda activate rerun
pip install rerun-sdk matplotlib scipy
```

#### Official Docs: [rerun.io](https://www.rerun.io/docs/getting-started)

---
<br>

## Usage

<br>

### *1.* Spheres Visualization (spheres_row.py):

```bash
python src/spheres_row.py
```

#### *•* Initialize rerun: `init_rerun(data_name)`.

#### *•* Create positions and colors for spheres: `create_positions(num_positions, start, end)` and `create_colors(num_colors, start, end)`.

#### *•* Log points of spheres: `log_points(name, positions, colors, radii)`.

---
<br>

### *2.* Bessel Wave Animation (3d_bessel.py):
  
```bash
python src/3d_bessel.py
```

#### *•* Initialize rerun: `init_rerun(data_name)`.

#### *•* Create Bessel wave positions and log points: `create_bessel_wave(x, y, t, frequency, amplitude, phase_shift)` and `log_points(name, x, y, z, radii)`.

#### *•* Equation: $z = \text{Bessel function}(frequency \cdot r + t) \cdot \cos(frequency \cdot \theta + phase\_shift)$.

---

<br>

### *3.* Sine Wave Animation (wave_creature.py):

```bash
python src/sine_wave/wave_creature.py
```
#### *•* Initialize rerun: `init_rerun(data_name)`.

https://github.com/patmejia/rerun_vision/assets/92187562/b582a6df-a2f3-485e-b6dd-b42fd66dcd92

#### *•* Generate positions and colors: `create_positions(x, y, z)` and `create_colors(z, colormap)`.

#### *•* Animate waving flag background: `animate_WaterMesh(t, bg_x, bg_y)`.

#### *•* Animate sine wave surface: `animate_surface(t, total_duration, x, y, colormap)`.

#### *•* Equation: $z = \sin(\sqrt{x^2 + y^2} - t) + \text{components}$.


---
<br>

## **License & Acknowledgments**
#### *•* **License**: MIT license.
#### *•* **Note**: Rerun.io in early beta; consult [official guidance](https://www.rerun.io/docs/getting-started).
#### *•* **Acknowledgments**: [rerun.io](https://www.rerun.io)
---
