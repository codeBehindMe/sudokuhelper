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

import cv2 as cv


class SudokuDetector:

    def __init__(self, k_size: (int, int), sigma_x: float):
        self.k_size = k_size
        self.sigma_x = sigma_x

    def get_sudoku_contours_from_image(self, img: object):
        """
        Get's the sudoku contours from the image.
        Args:
            img: Image to be processed

        Returns:

        """
        blur = cv.GaussianBlur(img, self.k_size, self.sigma_x)
        ret_val, thresh = cv.threshold(blur, 0, 255,
                                       cv.THRESH_BINARY + cv.THRESH_OTSU)

