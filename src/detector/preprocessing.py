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
This module provides image pre-processing for the detector. It is responsible
for carrying out image adjustments prior to detection happens.
"""

from src.utilities.imagery import convert_to_grayscale

import cv2

class ImagePreprocessor:

    def __init__(self, image: object):
        self.image = image
        self.output = image

    def initial_pass(self):
        """
        Takes an initial pass of processing the image for line detection.

        Returns:

        """

        self.output = convert_to_grayscale(self.output)
        self.output = cv2.GaussianBlur(self.output)

    def get_output(self):
        """
        Returns processed image.
        Returns:

        """

        return self.output
