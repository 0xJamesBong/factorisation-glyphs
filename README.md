# Polygons in a circle

This is a python script that generates images of polygons inscribed in circles, by utilizing the `svg` format.

## Requirements

- Python 3.5 or higher
- sympy module

## Usage

The script provides the following functions:

- `makeCircle()`: Generates a circle with a random fill color.
- `rotate(degrees, image)`: Rotates the image (in degrees) with respect to the center of the circle.
- `scaleDown(scale, image)`: Scales down the image according to the specified scale and shifts it to the center of the circle.
- `reflect(image)`: Reflects the image about the vertical axis of symmetry.
- `makePolygon(prime)`: Generates a polygon with `prime` sides inscribed in the circle.
- `composeShape(prime, image)`: Generates a composed shape with `prime` sub-images and an input `image`.
- `wrapCanvas(stuffInside)`: Wraps the `stuffInside` inside an svg canvas with background color black.

To use the script, simply call the desired functions within the script or create a separate python file and import the functions.

## Example

An example use of the script is to generate an image of a hexagon and a square inscribed in a circle:

```python
from sympy.ntheory import factorint

# define primes
hexagon = 6
square = 4

# make the shapes
hexShape = makePolygon(hexagon)
sqShape = makePolygon(square)

# compose the shapes
composed = composeShape(hexagon, sqShape)

# wrap the image
finalImage = wrapCanvas(composed)

# write the image to file
with open('hexagon_and_square_in_circle.svg', 'w') as f:
    f.write(finalImage)
```

## Notes

The script is an implementation of [inscribing polygons in circles](https://en.wikipedia.org/wiki/Regular_polygon#Circumscribed_and_inscribed_polygons) and is inspired by the following [stackoverflow post](https://stackoverflow.com/questions/4643647/fast-prime-factorization-module). The script is scalable to generate polygons with a high number of sides, but note that generating an image of a polygon with a very large number of sides may result in long processing times.
