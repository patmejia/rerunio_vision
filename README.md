# vision_rerun
Brief Installation and setup of Rerun.io, focusing on 2D and 3D computer vision and robotics data visualization
![Design 6](https://github.com/patmejia/vision_rerun/assets/92187562/97a9ac47-ecf2-43cf-9875-9b54461f4ac5)
![Design 6 (2)](https://github.com/patmejia/vision_rerun/assets/92187562/6c4cf0f2-0377-4a05-82e6-60b143f8f53b)
![Design 6 (1)](https://github.com/patmejia/vision_rerun/assets/92187562/f841e66b-a7b3-41eb-9ca5-526b815b9cba)
![Design 6 (3)](https://github.com/patmejia/vision_rerun/assets/92187562/8ace177d-7ae8-4ea6-a07e-a4649494021c)
![Design 6 (2)](https://github.com/patmejia/vision_rerun/assets/92187562/d6fb33d7-7c1a-4913-aa1d-0cb9e3ea5546)
![Design 6 (4)](https://github.com/patmejia/vision_rerun/assets/92187562/04f43f4e-2c29-4b1f-b900-bfa05b4eda9c)


---


# Rerun-Visualization-Deployment

## About
This repository facilitates the streamlined installation and setup of Rerun.io, focusing on 2D and 3D computer vision and robotics data visualization. It includes:

- **Python and Rust SDK Integration**: Quick installation and setup guides.
- **Viewer Interaction**: Instructions for interacting with the Rerun Viewer.
- **Data Logging**: Examples for logging your own data.
- **Community Support**: Links to troubleshooting guides and community channels.

## Installation

### Python Installation
Install the Rerun SDK for Python (requires Python-3.8+):
```bash
pip install rerun-sdk
```

### Rust Installation
Add Rerun to your Rust project:
```bash
cargo add rerun
```

### Rerun Viewer Binary Installation
Install the Rerun binary for streaming log data or loading .rrd files:
```bash
pip install rerun-sdk
rerun --help
```
or
```bash
cargo install rerun-cli
rerun --help
```

## Trying Out the Viewer
Launch the Rerun demo:
```bash
python3 -m rerun_demo
```

## Logging Your Own Data
Create a Python script to log data. Example:
```python
import rerun as rr
import numpy as np

rr.init("my data", spawn=True)
positions = np.zeros((10, 3))
positions[:,0] = np.linspace(-10,10,10)
colors = np.zeros((10,3), dtype=np.uint8)
colors[:,0] = np.linspace(0,255,10)
rr.log_points("my_points", positions=positions, colors=colors, radii=0.5)
```

## Advanced Topics
Explore the [Viewer Walkthrough](link) or [Logging Data in Python](link) guide for more advanced topics.

## Support and Community
- Troubleshooting guide: [link]
- Open an issue: [link]
- Join the Discord server: [link]

## License
This project is licensed under the terms of the MIT license. See the LICENSE file for details.

---

**Note**: Rerun.io is in early beta, and changes may occur. Always refer to the official documentation for the most accurate information.
