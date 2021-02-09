#!/pxrpythonsubst
#
# Copyright 2020 Pixar
#
# Licensed under the Apache License, Version 2.0 (the "Apache License")
# with the following modification; you may not use this file except in
# compliance with the Apache License and the following modification to it:
# Section 6. Trademarks. is deleted and replaced with:
#
# 6. Trademarks. This License does not grant permission to use the trade
#    names, trademarks, service marks, or product names of the Licensor
#    and its affiliates, except as required to comply with Section 4(c) of
#    the License and to reproduce the content of the NOTICE file.
#
# You may obtain a copy of the Apache License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the Apache License with the above modification is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the Apache License for the specific
# language governing permissions and limitations under the Apache License.
#

from pxr.Usdviewq.qt import QtWidgets
from pxr.Usdviewq.common import SelectionHighlightModes

def _waitForRefresh():
    import time
    time.sleep(0.5)
    QtWidgets.QApplication.processEvents()

# Remove any unwanted visuals from the view.
def _modifySettings(appController):
    appController._dataModel.viewSettings.showBBoxes = False
    appController._dataModel.viewSettings.showHUD = False
    appController._dataModel.viewSettings.selHighlightMode = (
        SelectionHighlightModes.NEVER)


#
# Test a case where we move an instanced root that contains strictly
# non-instancable-by-Hydra prims (i.e., no rprims).
#
def _testInstancingEdits6146(appController):
    from pxr import Sdf, Usd

    testALayer = Sdf.Layer.FindOrOpen("usd-6146/testA.usda")
    appController._dataModel.stage.GetRootLayer().TransferContent(testALayer)
    _waitForRefresh()

    testBLayer = Sdf.Layer.FindOrOpen("usd-6146/testB.usda")
    appController._dataModel.stage.GetRootLayer().TransferContent(testBLayer)
    _waitForRefresh()

    # If we get this far without crashing, we're good for now.


def testUsdviewInputFunction(appController):
    _modifySettings(appController)
    _testInstancingEdits6146(appController)
