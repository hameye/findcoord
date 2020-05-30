# FindCoord 
Time saver tool for multiplatform analysis

Tool computing and extracting the coordinates of analysis on a spectroscopic tool given the coordinates from another tool and some landmarks. 

Overlay of the affine transformation from Scikit-Image : https://scikit-image.org/docs/dev/api/skimage.transform.html?highlight=affine#skimage.transform.AffineTransform

## Install

Just do:
```bash
pip install findcoord
```

## Use in python
```python
import findcoord.transform as fn
TF = fn.transformation(input_filename, output_filename)

TF.calculate_coordinates()
TF.extract_coordinates()
```