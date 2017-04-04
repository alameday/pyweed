# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/uic/MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1037, 594)
        MainWindow.setStyleSheet(_fromUtf8("QTableView { gridline-color: gray }"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.mapFrame = QtGui.QFrame(self.splitter)
        self.mapFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mapFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mapFrame.setObjectName(_fromUtf8("mapFrame"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.mapFrame)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.mapCanvas = MyQt4MplCanvas(self.mapFrame)
        self.mapCanvas.setObjectName(_fromUtf8("mapCanvas"))
        self.verticalLayout_4.addWidget(self.mapCanvas)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.mapZoomInButton = QtGui.QToolButton(self.mapFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapZoomInButton.sizePolicy().hasHeightForWidth())
        self.mapZoomInButton.setSizePolicy(sizePolicy)
        self.mapZoomInButton.setObjectName(_fromUtf8("mapZoomInButton"))
        self.horizontalLayout_3.addWidget(self.mapZoomInButton)
        self.mapZoomOutButton = QtGui.QToolButton(self.mapFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapZoomOutButton.sizePolicy().hasHeightForWidth())
        self.mapZoomOutButton.setSizePolicy(sizePolicy)
        self.mapZoomOutButton.setObjectName(_fromUtf8("mapZoomOutButton"))
        self.horizontalLayout_3.addWidget(self.mapZoomOutButton)
        self.mapResetButton = QtGui.QToolButton(self.mapFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapResetButton.sizePolicy().hasHeightForWidth())
        self.mapResetButton.setSizePolicy(sizePolicy)
        self.mapResetButton.setObjectName(_fromUtf8("mapResetButton"))
        self.horizontalLayout_3.addWidget(self.mapResetButton)
        spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.eventAndStationWidget = QtGui.QWidget(self.splitter)
        self.eventAndStationWidget.setObjectName(_fromUtf8("eventAndStationWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.eventAndStationWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter_2 = QtGui.QSplitter(self.eventAndStationWidget)
        self.splitter_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setChildrenCollapsible(False)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.eventsWidget = QtGui.QWidget(self.splitter_2)
        self.eventsWidget.setObjectName(_fromUtf8("eventsWidget"))
        self.eventsLayout = QtGui.QVBoxLayout(self.eventsWidget)
        self.eventsLayout.setMargin(0)
        self.eventsLayout.setSpacing(0)
        self.eventsLayout.setObjectName(_fromUtf8("eventsLayout"))
        self.eventsButtonLayout = QtGui.QHBoxLayout()
        self.eventsButtonLayout.setSpacing(12)
        self.eventsButtonLayout.setObjectName(_fromUtf8("eventsButtonLayout"))
        self.toggleEventOptions = QtGui.QToolButton(self.eventsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleEventOptions.sizePolicy().hasHeightForWidth())
        self.toggleEventOptions.setSizePolicy(sizePolicy)
        self.toggleEventOptions.setCheckable(True)
        self.toggleEventOptions.setChecked(True)
        self.toggleEventOptions.setObjectName(_fromUtf8("toggleEventOptions"))
        self.eventsButtonLayout.addWidget(self.toggleEventOptions)
        self.getEventsButton = QtGui.QPushButton(self.eventsWidget)
        self.getEventsButton.setObjectName(_fromUtf8("getEventsButton"))
        self.eventsButtonLayout.addWidget(self.getEventsButton)
        self.eventsLayout.addLayout(self.eventsButtonLayout)
        self.eventsTable = QtGui.QTableWidget(self.eventsWidget)
        self.eventsTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.eventsTable.setAlternatingRowColors(True)
        self.eventsTable.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.eventsTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.eventsTable.setShowGrid(False)
        self.eventsTable.setWordWrap(False)
        self.eventsTable.setObjectName(_fromUtf8("eventsTable"))
        self.eventsTable.setColumnCount(0)
        self.eventsTable.setRowCount(0)
        self.eventsTable.verticalHeader().setVisible(False)
        self.eventsLayout.addWidget(self.eventsTable)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.eventSelectionLabel = QtGui.QLabel(self.eventsWidget)
        self.eventSelectionLabel.setText(_fromUtf8(""))
        self.eventSelectionLabel.setObjectName(_fromUtf8("eventSelectionLabel"))
        self.horizontalLayout.addWidget(self.eventSelectionLabel)
        self.clearEventSelectionButton = QtGui.QToolButton(self.eventsWidget)
        self.clearEventSelectionButton.setObjectName(_fromUtf8("clearEventSelectionButton"))
        self.horizontalLayout.addWidget(self.clearEventSelectionButton)
        self.eventsLayout.addLayout(self.horizontalLayout)
        self.stationsWidget = QtGui.QWidget(self.splitter_2)
        self.stationsWidget.setObjectName(_fromUtf8("stationsWidget"))
        self.stationsLayout = QtGui.QVBoxLayout(self.stationsWidget)
        self.stationsLayout.setMargin(0)
        self.stationsLayout.setSpacing(0)
        self.stationsLayout.setObjectName(_fromUtf8("stationsLayout"))
        self.stationsButtonLayout = QtGui.QHBoxLayout()
        self.stationsButtonLayout.setSpacing(12)
        self.stationsButtonLayout.setObjectName(_fromUtf8("stationsButtonLayout"))
        self.getStationsButton = QtGui.QPushButton(self.stationsWidget)
        self.getStationsButton.setObjectName(_fromUtf8("getStationsButton"))
        self.stationsButtonLayout.addWidget(self.getStationsButton)
        self.toggleStationOptions = QtGui.QToolButton(self.stationsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleStationOptions.sizePolicy().hasHeightForWidth())
        self.toggleStationOptions.setSizePolicy(sizePolicy)
        self.toggleStationOptions.setCheckable(True)
        self.toggleStationOptions.setChecked(True)
        self.toggleStationOptions.setObjectName(_fromUtf8("toggleStationOptions"))
        self.stationsButtonLayout.addWidget(self.toggleStationOptions)
        self.stationsLayout.addLayout(self.stationsButtonLayout)
        self.stationsTable = QtGui.QTableWidget(self.stationsWidget)
        self.stationsTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.stationsTable.setAlternatingRowColors(True)
        self.stationsTable.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.stationsTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.stationsTable.setShowGrid(False)
        self.stationsTable.setWordWrap(False)
        self.stationsTable.setObjectName(_fromUtf8("stationsTable"))
        self.stationsTable.setColumnCount(0)
        self.stationsTable.setRowCount(0)
        self.stationsTable.verticalHeader().setVisible(False)
        self.stationsLayout.addWidget(self.stationsTable)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.stationSelectionLabel = QtGui.QLabel(self.stationsWidget)
        self.stationSelectionLabel.setText(_fromUtf8(""))
        self.stationSelectionLabel.setObjectName(_fromUtf8("stationSelectionLabel"))
        self.horizontalLayout_2.addWidget(self.stationSelectionLabel)
        self.clearStationSelectionButton = QtGui.QToolButton(self.stationsWidget)
        self.clearStationSelectionButton.setObjectName(_fromUtf8("clearStationSelectionButton"))
        self.horizontalLayout_2.addWidget(self.clearStationSelectionButton)
        self.stationsLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.splitter_2)
        self.waveformButtonLayout = QtGui.QHBoxLayout()
        self.waveformButtonLayout.setObjectName(_fromUtf8("waveformButtonLayout"))
        self.getWaveformsButton = QtGui.QPushButton(self.eventAndStationWidget)
        self.getWaveformsButton.setObjectName(_fromUtf8("getWaveformsButton"))
        self.waveformButtonLayout.addWidget(self.getWaveformsButton)
        self.verticalLayout_3.addLayout(self.waveformButtonLayout)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.eventOptionsDockWidget = QtGui.QDockWidget(MainWindow)
        self.eventOptionsDockWidget.setFloating(False)
        self.eventOptionsDockWidget.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.eventOptionsDockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.eventOptionsDockWidget.setObjectName(_fromUtf8("eventOptionsDockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.eventOptionsDockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.eventOptionsDockWidget)
        self.stationOptionsDockWidget = QtGui.QDockWidget(MainWindow)
        self.stationOptionsDockWidget.setFloating(False)
        self.stationOptionsDockWidget.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.stationOptionsDockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.stationOptionsDockWidget.setObjectName(_fromUtf8("stationOptionsDockWidget"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.stationOptionsDockWidget.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.stationOptionsDockWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.getEventsButton, self.getStationsButton)
        MainWindow.setTabOrder(self.getStationsButton, self.eventsTable)
        MainWindow.setTabOrder(self.eventsTable, self.stationsTable)
        MainWindow.setTabOrder(self.stationsTable, self.getWaveformsButton)
        MainWindow.setTabOrder(self.getWaveformsButton, self.clearEventSelectionButton)
        MainWindow.setTabOrder(self.clearEventSelectionButton, self.clearStationSelectionButton)
        MainWindow.setTabOrder(self.clearStationSelectionButton, self.toggleEventOptions)
        MainWindow.setTabOrder(self.toggleEventOptions, self.toggleStationOptions)
        MainWindow.setTabOrder(self.toggleStationOptions, self.mapZoomInButton)
        MainWindow.setTabOrder(self.mapZoomInButton, self.mapZoomOutButton)
        MainWindow.setTabOrder(self.mapZoomOutButton, self.mapResetButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.mapZoomInButton.setText(_translate("MainWindow", "Zoom In", None))
        self.mapZoomOutButton.setText(_translate("MainWindow", "Zoom Out", None))
        self.mapResetButton.setText(_translate("MainWindow", "Reset", None))
        self.toggleEventOptions.setText(_translate("MainWindow", "< Options", None))
        self.getEventsButton.setText(_translate("MainWindow", "Get Events", None))
        self.eventsTable.setSortingEnabled(True)
        self.clearEventSelectionButton.setText(_translate("MainWindow", "Clear Selection", None))
        self.getStationsButton.setText(_translate("MainWindow", "Get Stations", None))
        self.toggleStationOptions.setText(_translate("MainWindow", "Options >", None))
        self.stationsTable.setSortingEnabled(True)
        self.clearStationSelectionButton.setText(_translate("MainWindow", "Clear Selection", None))
        self.getWaveformsButton.setText(_translate("MainWindow", "Get Waveforms", None))
        self.eventOptionsDockWidget.setWindowTitle(_translate("MainWindow", "Event Options", None))
        self.stationOptionsDockWidget.setWindowTitle(_translate("MainWindow", "Station Options", None))

from gui.uic.MyQt4MplCanvas import MyQt4MplCanvas
