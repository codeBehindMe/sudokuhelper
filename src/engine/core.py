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
Sudoku solver core.

The core is the primary way to extract functionality out of the sudoku helper.
It is designed with the intention that the way that the sudoku helper will
be utilised differently depending on how it is hosted.

For example, if it's hosted over the internet, it will likely not have a
stream of images coming in, instead perhaps a single image may come in. A lot
of processing on the single image may be done to try to work out the puzzle.

On the other hand, if it's part of a bigger application or maybe works on a
micro-services architecture, it may be used in a video stream. In this case,
it should statefully process the video to get the best one and then return
a result once a good frame is found.
"""


class SingleShotSolver:

    def __init__(self):
        raise NotImplementedError()


