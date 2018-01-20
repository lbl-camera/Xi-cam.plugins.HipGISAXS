from qtpy import QtCore, QtGui
from qtpy.uic import loadUi

particlemenu = None
blankForm = None
leftwidget = None
centerwidget = None
rightwidget = None

from os import path


def load():
    global leftwidget, centerwidget, rightwidget, blankForm
    # Load the gui from file
    f = QtCore.QFile(path.join(path.dirname(__file__), "hipgisaxsleftwidget.ui"))
    f.open(QtCore.QFile.ReadOnly)
    leftwidget = loadUi(f)
    f.close()

    rightwidget = QtGui.QStackedWidget()
    centerwidget = QtGui.QSplitter(QtCore.Qt.Vertical)

    blankForm = QtGui.QLabel('Select a feature on the left panel to edit...')
    blankForm.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
    blankForm.setAlignment(QtCore.Qt.AlignCenter)
    showForm(blankForm)

    # leftmodes = [(leftwidget, QtGui.QFileIconProvider().icon(QtGui.QFileIconProvider.File))]

    return centerwidget, rightwidget, leftwidget


def showForm(form):
    rightwidget.addWidget(form)
    rightwidget.setCurrentWidget(form)
