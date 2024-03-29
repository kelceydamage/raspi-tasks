#!/usr/bin/env python3
# ------------------------------------------------------------------------ 79->
# Author: ${name=Kelcey Damage}
# Python: 3.5+
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Doc
# ------------------------------------------------------------------------ 79->
#
# Imports
# ------------------------------------------------------------------------ 79->
import numpy as np
from rtl.common.task import Task
from rtl.common.regression import Models

# Globals
# ------------------------------------------------------------------------ 79->

# Classes
# ------------------------------------------------------------------------ 79->
class ColumnSpace(Task):

    def __init__(self, kwargs, contents):
        super(ColumnSpace, self).__init__(kwargs, contents)
        self.newColumns = [('{0}Space'.format(self.column.decode()), '<i8')]
        self.addColumns()

    def columnSpace(self):
        self.getLSpace(
            self.space,
            self.ndata[self.column.decode()]
        )
        self.setColumn(
            0,
            self.lSpace.reshape(-1, )
        )
        return self


# Functions
# ----------------------------------------------------------------------- 79->
def columnSpace(kwargs, contents):
    return ColumnSpace(kwargs, contents).columnSpace().getContents()

# Main
# ------------------------------------------------------------------------ 79->
