# This file is part of sudokuhelper.

# sudokuhelper is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# sudokuhelper is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with sudokuhelper.  If not, see <https://www.gnu.org/licenses/>.

"""
Contains utilities around images.
"""

from functools import wraps

import cv2
import numpy as np


def convert_to_grayscale(img: object) -> object:
    """
    Casts and image to gray.
    Args:
        img:  Image object.

    Returns:
        Image in grayscale.

    """
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


def detect_grid(img: object, k_size: (int, int), t_low: int, t_high: int,
                aperture_size: int) -> object:
    """
    Detects a grid in an image.
    Args:
        aperture_size:
        t_high:
        t_low:
        img: Greyscale image object.
        k_size: Kernel size for smoothing.

    Returns:

    """
    blur = cv2.blur(src=img, ksize=k_size)

    edges = cv2.Canny(image=blur, threshold1=t_low, threshold2=t_high,
                      apertureSize=aperture_size)


