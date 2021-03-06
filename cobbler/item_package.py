"""
Copyright 2006-2009, MadHatter
Kelsey Hightower <kelsey.hightower@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301  USA
"""

import resource

from cobbler.cexceptions import CX
from cobbler.utils import _


# this datastructure is described in great detail in item_distro.py -- read the comments there.
FIELDS = [
    ["uid", "", 0, "", False, "", 0, "str"],
    ["depth", 2, 0, "", False, "", 0, "float"],
    ["comment", "", 0, "Comment", True, "Free form text description", 0, "str"],
    ["ctime", 0, 0, "", False, "", 0, "float"],
    ["mtime", 0, 0, "", False, "", 0, "float"],
    ["owners", "SETTINGS:default_ownership", 0, "Owners", True, "Owners list for authz_ownership (space delimited)", [], "list"],
    ["name", "", 0, "Name", True, "Name of file resource", 0, "str"],
    ["action", "create", 0, "Action", True, "Install or remove package resource", 0, "str"],
    ["installer", "yum", 0, "Installer", True, "Package Manager", 0, "str"],
    ["version", "", 0, "Version", True, "Package Version", 0, "str"],
]


class Package(resource.Resource):

    TYPE_NAME = _("package")
    COLLECTION_TYPE = "package"

    #
    # override some base class methods first (item.Item)
    #

    def make_clone(self):
        _dict = self.to_dict()
        cloned = Package(self.collection_mgr)
        cloned.from_dict(_dict)
        return cloned


    def get_fields(self):
        return FIELDS


    def check_if_valid(self):
        if self.name is None or self.name == "":
            raise CX("name is required")


    #
    # specific methods for item.Package
    #

    def set_installer(self, installer):
        self.installer = installer.lower()

    def set_version(self, version):
        self.version = version

# EOF
