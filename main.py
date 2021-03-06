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
import cv2
import numpy as np

from src.utilities.kernels import square_kernel


def image_lines():
    img = cv2.imread("test/resources/sudoku_newspaper.jpeg")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    edges = cv2.Canny(gray, 90, 150, apertureSize=3)
    kernel = square_kernel(3)
    edges = cv2.dilate(edges, kernel, iterations=1)
    kernel = square_kernel(2)
    edges = cv2.erode(edges, kernel, iterations=1)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)

    for line in lines:
        for rho, theta in line:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imshow('img', img)
    cv2.imshow('edges', edges)

    k = cv2.waitKey()

    if k == 27:
        cv2.destroyAllWindows()


def blob_detection():
    # Read image
    im = cv2.imread("test/resources/sudoku_newspaper.jpeg")
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # Set up the detector with default parameters.
    params = cv2.SimpleBlobDetector_Params()
    params.filterByCircularity = True
    params.minCircularity = 0.73
    detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs.
    keypoints = detector.detect(im)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    # im_with_keypoints = cv2.drawMatches(im, keypoints, np.array([]),
    #                                     (0, 0, 255),
    #                                     cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    im_with_keypoints = cv2.drawKeypoints(im, keypoints, None,
                                          flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Show keypoints
    cv2.imshow("Keypoints", im_with_keypoints)
    cv2.waitKey(0)


if __name__ == '__main__':
    # image_lines()
    blob_detection()
