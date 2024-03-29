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

# Globals
# ------------------------------------------------------------------------ 79->

# Classes
# ------------------------------------------------------------------------ 79->
class CrossAverage(Task):

    def __init__(self, kwargs, content):
        super(CrossAverage, self).__init__(kwargs, content)
        self.newColumns = [
            ('{0}'.format(o['column']), '<f8')
            for o in self.operations
        ]
        self.addColumns()

    def crossAverage(self):
        for i in range(len(self.operations)):
            o = self.operations[i]
            dtypes = [x for x in self.dtypes.descr if x[0] in o['columns']]
            tempData = np.zeros(self.ndata.shape, dtypes)
            for j in range(len(dtypes)):
                tempData[dtypes[j][0]] = self.ndata[dtypes[j][0]]
            
            self.setColumn(
                i,
                np.mean(np.array(tempData.tolist()), axis=1)
            )
        return self


# Functions
# ------------------------------------------------------------------------ 79->
def crossAverage(kwargs, contents):
    return CrossAverage(kwargs, contents).crossAverage().getContents()

# Main
# ------------------------------------------------------------------------ 79->
