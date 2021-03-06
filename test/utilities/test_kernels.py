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
Contains the test for kernels
"""

import numpy as np

from src.utilities.kernels import square_kernel


class TestKernels:

    def test_square_kernel(self):
        """
        Check's to see that the square kernel's behaviour is as expected.
        Returns:

        """
        k = square_kernel(4)

        assert k.shape == (4, 4)
        assert k.dtype == np.uint8
