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
Main entry point to the program.
"""
import cv2 as cv

from src.utilities.imagery import convert_to_grayscale

if __name__ == '__main__':
    im = cv.imread('test/resources/sudoku_1.png')
    imgray = convert_to_grayscale(im)

    ret, thresh = cv.threshold(imgray, 127, 255, 0)


    cv.imshow('img', im)

    k = cv.waitKey()

    if k == 27:
        cv.destroyAllWindows()
