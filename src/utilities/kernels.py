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
Factory for creating kernels.
"""
import numpy as np

_default_dtype = np.uint8
_kernel_dtype = np.uint8


def square_kernel(size: int):
    """
    Returns a square kernel.
    Args:
        size: Size of the kernel

    Returns:

    """
    return np.ones(shape=(size, size), dtype=_kernel_dtype)


