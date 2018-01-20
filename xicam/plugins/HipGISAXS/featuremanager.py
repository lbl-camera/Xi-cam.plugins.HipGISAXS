from qtpy.uic import loadUi
from qtpy import QtGui
from qtpy import QtCore

from . import customwidgets
from . import display

features = []
functionTree = None


def clearFeatures():
    global features
    features = []


def addSubstrate():
    global features
    if not sum([type(feature) is customwidgets.substrate for feature in features]):
        features.insert(0, customwidgets.substrate())
    update()


def addLayer():
    global features
    features.append(customwidgets.layer())
    update()


def addParticle():
    global features
    features.append(customwidgets.particle())
    update()


def removeFeature(index):
    global features
    del features[index]
    update()


def layercount():
    return sum([type(feature) is customwidgets.layer for feature in features])


def particlecount():
    return sum([type(feature) is customwidgets.particle for feature in features])


def update():
    global functionTree
    assert isinstance(layout, QtGui.QVBoxLayout)

    for i in range(layout.count()):
        layout.itemAt(i).parent = None

    # layout.addItem(QtGui.QSpacerItem(0,0,vData=QtGui.QSizePolicy.Expanding))

    for item in features[::-1]:
        layout.addWidget(item)

    if display.viewWidget:
        display.redraw()


def loadform(path):
    f = QtCore.QFile(path)
    f.open(QtCore.QFile.ReadOnly)
    form = loadUi(f)
    f.close()
    return form


def load():
    global features, functionTree
    layout.setAlignment(QtCore.Qt.AlignBottom)
    addSubstrate()
    addLayer()
    addParticle()
