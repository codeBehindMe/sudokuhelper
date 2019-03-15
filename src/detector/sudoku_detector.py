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
Detect's the Sudoku matrix on images.
"""

import cv2

from src.utilities.imagery import KernelFactory
from src.utilities.imagery import convert_to_grayscale


class SudokuDetector:

    def __init__(self, k_size: (int, int), sigma_x: float, l_threshold: int,
                 u_threshold: int, aperture_size: int):
        self.aperture_size = aperture_size
        self.l_threshold = l_threshold
        self.u_threshold = u_threshold
        self.k_size = k_size
        self.sigma_x = sigma_x
        self.kernel_factory = KernelFactory()

    def get_sudoku_contours_from_image(self, img: object):
        """
        Get's the sudoku grid lines from the image.
        Args:
            img: Image to be processed

        Returns:

        """
        img = convert_to_grayscale(img)
        blur = cv2.GaussianBlur(img, self.k_size, self.sigma_x)
        edges = cv2.Canny(blur, self.l_threshold, self.u_threshold,
                          apertureSize=self.aperture_size)
