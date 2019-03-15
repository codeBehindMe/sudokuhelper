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
Manages the program configuration.

All objects in this module should be static.
"""

import yaml

from src.utilities.constants import APP_CONFIG_PATH


class ConfigurationManager:
    """
    Configuration manager for the application.

    Gives dot access to the attributes in the configuration.
    """

    def __init__(self):
        with open(APP_CONFIG_PATH, 'r') as f:
            self.app_config = yaml.load(f)
        super().__init__()

    def __getattr__(self, item: str):
        return self.app_config[item]

    def __getitem__(self, item: str) -> object:
        return self.app_config[item]


app_config = ConfigurationManager()
