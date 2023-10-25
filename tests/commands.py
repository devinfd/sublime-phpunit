# Copyright (C) 2023 Gerard Roche
#
# This file is part of PHPUnitKit.
#
# PHPUnitKit is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PHPUnitKit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PHPUnitKit.  If not, see <https://www.gnu.org/licenses/>.

from sublime_plugin import TextCommand


class PhpunitTestSetupFixtureCommand(TextCommand):

    def run(self, edit, text):

        # This fixes an issue where an exception is thrown when  reloading the
        # test commands. I don't know why this is  needed, but it works. It's
        # most likely a bug in ST. The exception:
        #     Traceback (most recent call last):
        #       File "/home/code/sublime_text_3/sublime_plugin.py", line 933, in run_
        #         return self.run(edit, **args)
        #       File "/home/code/.config/sublime-text-3/Packages/PHPUnitKit/tests/commands.py", line 11, in run
        #         self.view.replace(edit, Region(0, self.view.size()), text)
        #     TypeError: 'NoneType' object is not callable
        from sublime import Region  # noqa: F401

        self.view.replace(edit, Region(0, self.view.size()), text)

        if '|' in text:
            cursor_placeholders = self.view.find_all('\\|')
            if cursor_placeholders:
                self.view.sel().clear()
                for i, cursor_placeholder in enumerate(cursor_placeholders):
                    self.view.sel().add(cursor_placeholder.begin() - i)
                    self.view.replace(
                        edit,
                        Region(cursor_placeholder.begin() - i, cursor_placeholder.end() - i),
                        ''
                    )


class PhpunitTestEraseCommand(TextCommand):
    def run(self, edit):
        # See comments above about why this import is inline.
        from sublime import Region  # noqa: F401
        self.view.erase(edit, Region(0, self.view.size()))
