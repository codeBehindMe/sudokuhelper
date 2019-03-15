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
Tests the validity of the configuration manager.
"""

from src.configuration_manager.configuration_manager import app_config


class TestConfigurationManager:

    def test_config_is_not_none(self):
        """
        Test that the configuration is loaded correctly.
        Returns:

        """

        assert app_config is not None

    def test_can_access_attributes_with_dot(self):
        """
        Check's that the configuration can be accessed with the dot operator.
        Returns:

        """

        assert app_config.name is not None

    def test_can_access_attributes_with_brackets(self):
        """
        Check's to see that the configuration values can be accessed via the
        square brackets.
        Returns:

        """

        assert app_config['name'] is not None
