# rerun.io

### Computer Vision & Robotics Integration: `rerun_sdk` - Towards Real-Time Data Analytics

---

<p align="center">
<img src="media/rerun_vision_robot.png" alt="Alt text" width="423">
</p>

### **Objective**: Utilizes Rerun.io for precise 3D visualizations in Computer Vision, including animations of Sine Wave Surface, Bessel Wave, and Spheres. Point logging feature of Rerun.io for mapping and displaying 3D coordinates.

---

<p align="center">
<img src="media/dna_abacus/dna_abacus.gif" alt="DNA Abacus animation">
<br>
<sub><i>Figure: DNA Abacus. To run, execute: <code>python src/dna_abacus.py</code></i></sub>
</p>

---

## 1. Setup

```bash
conda create -n rerun python=3.8
conda activate rerun
pip install rerun-sdk matplotlib scipy
```

#### Official Docs: [rerun.io](https://www.rerun.io/docs/getting-started)

---

## 2. Usage

### Example 1. Spheres Visualization (spheres_row.py):

```bash
python src/demo_rerunio_graphics/spheres_row.py
```

* Initialize rerun: `init_rerun(data_name)`.
* Create positions and colors for spheres: `create_positions(num_positions, start, end)` and `create_colors(num_colors, start, end)`.
* Log points of spheres: `log_points(name, positions, colors, radii)`.

---

### Example 2. Bessel Wave Animation (3d_bessel.py):

```bash
python src/demo_rerunio_graphics/3d_bessel.py
```

* Initialize rerun: `init_rerun(data_name)`.
* Create Bessel wave positions and log points: `create_bessel_wave(x, y, t, frequency, amplitude, phase_shift)` and `log_points(name, x, y, z, radii)`.
* Equation: $z = \text{Bessel function}(\text{frequency} \cdot r + t) \cdot \cos(frequency \cdot \theta + \text{phase shift})$.

---

<p align="center">
<img src="media/wave_creature/fast.gif" alt="Wave Creature animation">
<br>
<sub><i>Figure: Wave Creature. To run, execute: <code>python src/demo_rerunio_graphics/wave_creature.py</code></i></sub>
</p>

---

### Example 3. Sine Wave Animation (wave_creature.py):

```bash
python src/demo_rerunio_graphics/wave_creature.py
```

* Initialize rerun: `init_rerun(data_name)`.
* Generate positions and colors: `create_positions(x, y, z)` and `create_colors(z, colormap)`.
* Animate waving flag background: `animate_WaterMesh(t, bg_x, bg_y)`.
* Animate sine wave surface: `animate_surface(t, total_duration, x, y, colormap)`.
* Equation: $z = \sin(\sqrt{x^2 + y^2} - t) + \text{components}$.

---

## License & Acknowledgments

* **License**: MIT license.
* **Note**: Rerun.io in early beta; consult [official guidance](https://www.rerun.io/docs/getting-started).
* **Acknowledgments**: [rerun.io](https://www.rerun.io)
