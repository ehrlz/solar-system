# Solar System
This project utilizes Python and the OpenGL library to showcase a simple animation of the solar system, demonstrating the rotation of the Earth around the Sun along with the Moon's orbit around the Earth. Textures are incorporated to represent the Earth, the Sun, and the Moon.

![solar-system](https://github.com/ehrlz/solar-system/assets/62675568/8625d90d-dc59-4157-b3db-cc2050b8f2de)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![OpenGL](https://img.shields.io/badge/OpenGL-%23FFFFFF.svg?style=for-the-badge&logo=opengl)

## Requirements
- Python3
- OpenGL
- PIL (Python Imaging Library)

You can install the dependencies using the following command:
```
pip install PyOpenGL Pillow
```

## How to run
1. Download the source code or clone the repository:
```
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```
2. Run the script in your terminal.
```
python3 solar_system.py
```

## Functionality
- `LoadTextures(image)` handles loading the necessary textures for the Earth, the Sun, and the Moon. Make sure to have the corresponding images in the "textures" folder within the project directory.

- The `earth()`, `sun()`, and `moon()` functions create the respective lists for each celestial body, configuring the appearance and texture of the spheres.

- The `init()` function initializes the OpenGL window, sets the background color, and enables depth testing.

- The `dibujo()` function defines the position and rotations of the Earth, the Sun, and the Moon. It also uses the previously created lists to render the celestial bodies.

- The `idle()` function manages the updates of rotation angles to simulate movement over time.

- The `setangle(alpha)` function ensures that angles stay within the appropriate range.

- The `reshape(newwidth, newheight)` function adjusts the projection matrix when the window size changes.

The animation represents in real scale (not the Sun) the rotation of the Earth around the Sun, the Moon's orbit around the Earth, and the rotation of the Sun. Angles and speeds are configured to make the animation perceptible and enjoyable. Experiment with parameters according to your preferences.

## Configurable Parameters
You can experiment with the following parameters in the script to customize the animation according to your preferences:

- Rotation Speed (**k**):
Multiplication factor affecting the rotation speeds of the Earth, the Moon's orbit, and the Sun's rotation. Adjust the value for faster or slower rotations.
- **Texture Paths**:
Ensure the images for Earth, Sun, and Moon are placed in the "textures" folder. You can replace the file paths in `LoadTextures(image)` with your own texture paths.
- Window Size:
Modify **xw** and **yw** variables to change the initial size of the OpenGL window.
- Initial Camera Position:
Adjust the values in `glTranslatef(0, 0, -100)` in `dibujo()` to change the initial camera position.
- Aspect Ratio and Perspective:
Tune the angle and aspect variables in `init()` to modify the field of view and aspect ratio.
- Scaling Factors:
Experiment with the scaling factors `glScalef()` calls to change the size of the Earth, Moon, and Sun in the animation.
