# rerun.io

### Computer Vision & Robotics Integration: `rerun_sdk` -Towards Real-Time Data Analytics

---

<p align="center">
<img src="media/rerun_vision_robot.png" alt="Alt text" width="423">
</p>

### **Objective**: This project utilizes Rerun.io to create precise 3D visualizations for Computer Vision, including animations of a Sine Wave Surface, a Bessel Wave, and Spheres. The point logging feature of Rerun.io is used to accurately map and display the 3D coordinates of these objects.

---

<br>

## *1.* Setup

```bash
conda create -n rerun python=3.8
conda activate rerun
pip install rerun-sdk matplotlib scipy
```

#### Official Docs: [rerun.io](https://www.rerun.io/docs/getting-started)

---

<br>

## *2.* Usage

<br>

### *Example 1.* Spheres Visualization (spheres_row.py):

```bash
python src/demo_reunio_graphics/spheres_row.py
```

#### *•* Initialize rerun: `init_rerun(data_name)`.

#### *•* Create positions and colors for spheres: `create_positions(num_positions, start, end)` and `create_colors(num_colors, start, end)`.

#### *•* Log points of spheres: `log_points(name, positions, colors, radii)`.

---

<br>

### *Example 2.* Bessel Wave Animation (3d_bessel.py):

```bash
python src/demo_reunio_graphics/3d_bessel.py
```

#### *•* Initialize rerun: `init_rerun(data_name)`.

#### *•* Create Bessel wave positions and log points: `create_bessel_wave(x, y, t, frequency, amplitude, phase_shift)` and `log_points(name, x, y, z, radii)`.

#### *•* Equation: $z = \text{Bessel function}(\text{frequency} \cdot r + t) \cdot \cos(frequency \cdot \theta + \text{phase shift})$.

---

<br>

### *Example 3.* Sine Wave Animation (wave_creature.py):

```bash
python src/demo_reunio_graphics/wave_creature.py
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
