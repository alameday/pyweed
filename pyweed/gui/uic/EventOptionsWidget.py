# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/uic/EventOptionsWidget.ui'
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

class Ui_EventOptionsWidget(object):
    def setupUi(self, EventOptionsWidget):
        EventOptionsWidget.setObjectName(_fromUtf8("EventOptionsWidget"))
        EventOptionsWidget.resize(307, 747)
        EventOptionsWidget.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    width: 5em;\n"
"}\n"
""))
        self.verticalLayout = QtGui.QVBoxLayout(EventOptionsWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.timeGroupBox = QtGui.QGroupBox(EventOptionsWidget)
        self.timeGroupBox.setObjectName(_fromUtf8("timeGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.timeGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.timeBetweenRadioButton = QtGui.QRadioButton(self.timeGroupBox)
        self.timeBetweenRadioButton.setEnabled(True)
        self.timeBetweenRadioButton.setChecked(True)
        self.timeBetweenRadioButton.setObjectName(_fromUtf8("timeBetweenRadioButton"))
        self.verticalLayout_2.addWidget(self.timeBetweenRadioButton)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(24, -1, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setHorizontalSpacing(4)
        self.formLayout_3.setVerticalSpacing(1)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.starttimeLabel = QtGui.QLabel(self.timeGroupBox)
        self.starttimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.starttimeLabel.setObjectName(_fromUtf8("starttimeLabel"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.starttimeLabel)
        self.starttimeDateTimeEdit = QtGui.QDateTimeEdit(self.timeGroupBox)
        self.starttimeDateTimeEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.starttimeDateTimeEdit.setCalendarPopup(True)
        self.starttimeDateTimeEdit.setTimeSpec(QtCore.Qt.UTC)
        self.starttimeDateTimeEdit.setObjectName(_fromUtf8("starttimeDateTimeEdit"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.starttimeDateTimeEdit)
        self.endtimeLabel = QtGui.QLabel(self.timeGroupBox)
        self.endtimeLabel.setObjectName(_fromUtf8("endtimeLabel"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.endtimeLabel)
        self.endtimeDateTimeEdit = QtGui.QDateTimeEdit(self.timeGroupBox)
        self.endtimeDateTimeEdit.setCalendarPopup(True)
        self.endtimeDateTimeEdit.setTimeSpec(QtCore.Qt.UTC)
        self.endtimeDateTimeEdit.setObjectName(_fromUtf8("endtimeDateTimeEdit"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.endtimeDateTimeEdit)
        self.horizontalLayout.addLayout(self.formLayout_3)
        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.timeDuringStationsRadioButton = QtGui.QRadioButton(self.timeGroupBox)
        self.timeDuringStationsRadioButton.setObjectName(_fromUtf8("timeDuringStationsRadioButton"))
        self.verticalLayout_2.addWidget(self.timeDuringStationsRadioButton)
        self.verticalLayout.addWidget(self.timeGroupBox)
        self.magnitudeGroupBox = QtGui.QGroupBox(EventOptionsWidget)
        self.magnitudeGroupBox.setObjectName(_fromUtf8("magnitudeGroupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.magnitudeGroupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setHorizontalSpacing(4)
        self.formLayout.setVerticalSpacing(1)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.magnitudeGroupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.minmagLineEdit = QtGui.QDoubleSpinBox(self.magnitudeGroupBox)
        self.minmagLineEdit.setObjectName(_fromUtf8("minmagLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.minmagLineEdit)
        self.label_4 = QtGui.QLabel(self.magnitudeGroupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.maxmagLineEdit = QtGui.QLineEdit(self.magnitudeGroupBox)
        self.maxmagLineEdit.setObjectName(_fromUtf8("maxmagLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.maxmagLineEdit)
        self.label_7 = QtGui.QLabel(self.magnitudeGroupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_7)
        self.magtypeComboBox = QtGui.QComboBox(self.magnitudeGroupBox)
        self.magtypeComboBox.setEnabled(True)
        self.magtypeComboBox.setObjectName(_fromUtf8("magtypeComboBox"))
        self.magtypeComboBox.addItem(_fromUtf8(""))
        self.magtypeComboBox.addItem(_fromUtf8(""))
        self.magtypeComboBox.addItem(_fromUtf8(""))
        self.magtypeComboBox.addItem(_fromUtf8(""))
        self.magtypeComboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.magtypeComboBox)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.magnitudeGroupBox)
        self.depthGroupBox = QtGui.QGroupBox(EventOptionsWidget)
        self.depthGroupBox.setObjectName(_fromUtf8("depthGroupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.depthGroupBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setHorizontalSpacing(4)
        self.formLayout_2.setVerticalSpacing(1)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_2 = QtGui.QLabel(self.depthGroupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.mindepthLineEdit = QtGui.QLineEdit(self.depthGroupBox)
        self.mindepthLineEdit.setObjectName(_fromUtf8("mindepthLineEdit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.mindepthLineEdit)
        self.maxdepthLineEdit = QtGui.QLineEdit(self.depthGroupBox)
        self.maxdepthLineEdit.setObjectName(_fromUtf8("maxdepthLineEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.maxdepthLineEdit)
        self.label_12 = QtGui.QLabel(self.depthGroupBox)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_12)
        self.horizontalLayout_3.addLayout(self.formLayout_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.depthGroupBox)
        self.locationGroupBox = QtGui.QGroupBox(EventOptionsWidget)
        self.locationGroupBox.setObjectName(_fromUtf8("locationGroupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.locationGroupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.locationRangeRadioButton = QtGui.QRadioButton(self.locationGroupBox)
        self.locationRangeRadioButton.setChecked(True)
        self.locationRangeRadioButton.setObjectName(_fromUtf8("locationRangeRadioButton"))
        self.verticalLayout_4.addWidget(self.locationRangeRadioButton)
        self.locationRangeLayout_2 = QtGui.QHBoxLayout()
        self.locationRangeLayout_2.setContentsMargins(24, -1, -1, -1)
        self.locationRangeLayout_2.setSpacing(0)
        self.locationRangeLayout_2.setObjectName(_fromUtf8("locationRangeLayout_2"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem3)
        self.locationRangeNorthLineEdit = QtGui.QLineEdit(self.locationGroupBox)
        self.locationRangeNorthLineEdit.setObjectName(_fromUtf8("locationRangeNorthLineEdit"))
        self.horizontalLayout_23.addWidget(self.locationRangeNorthLineEdit)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.locationRangeEastLineEdit = QtGui.QLineEdit(self.locationGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.locationRangeEastLineEdit.sizePolicy().hasHeightForWidth())
        self.locationRangeEastLineEdit.setSizePolicy(sizePolicy)
        self.locationRangeEastLineEdit.setObjectName(_fromUtf8("locationRangeEastLineEdit"))
        self.horizontalLayout_24.addWidget(self.locationRangeEastLineEdit)
        self.locationRangeWestLineEdit = QtGui.QLineEdit(self.locationGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.locationRangeWestLineEdit.sizePolicy().hasHeightForWidth())
        self.locationRangeWestLineEdit.setSizePolicy(sizePolicy)
        self.locationRangeWestLineEdit.setObjectName(_fromUtf8("locationRangeWestLineEdit"))
        self.horizontalLayout_24.addWidget(self.locationRangeWestLineEdit)
        self.verticalLayout_8.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem5)
        self.locationRangeSouthLineEdit = QtGui.QLineEdit(self.locationGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.locationRangeSouthLineEdit.sizePolicy().hasHeightForWidth())
        self.locationRangeSouthLineEdit.setSizePolicy(sizePolicy)
        self.locationRangeSouthLineEdit.setObjectName(_fromUtf8("locationRangeSouthLineEdit"))
        self.horizontalLayout_25.addWidget(self.locationRangeSouthLineEdit)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_25)
        self.locationRangeLayout_2.addLayout(self.verticalLayout_8)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.locationRangeLayout_2.addItem(spacerItem7)
        self.locationRangeLayout_2.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.locationRangeLayout_2)
        self.locationDistanceFromPointRadioButton = QtGui.QRadioButton(self.locationGroupBox)
        self.locationDistanceFromPointRadioButton.setEnabled(True)
        self.locationDistanceFromPointRadioButton.setObjectName(_fromUtf8("locationDistanceFromPointRadioButton"))
        self.verticalLayout_4.addWidget(self.locationDistanceFromPointRadioButton)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(24, -1, -1, -1)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.formLayout_7 = QtGui.QFormLayout()
        self.formLayout_7.setHorizontalSpacing(4)
        self.formLayout_7.setVerticalSpacing(1)
        self.formLayout_7.setObjectName(_fromUtf8("formLayout_7"))
        self.label_29 = QtGui.QLabel(self.locationGroupBox)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_29)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.distanceFromPointMinRadiusLineEdit = QtGui.QLineEdit(self.locationGroupBox)
        self.distanceFromPointMinRadiusLineEdit.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distanceFromPointMinRadiusLineEdit.sizePolicy().hasHeightForWidth())
        self.distanceFromPointMinRadiusLineEdit.setSizePolicy(sizePolicy)
        self.distanceFromPointMinRadiusLineEdit.setObjectName(_fromUtf8("distanceFromPointMinRadiusLineEdit"))
        self.horizontalLayout_19.addWidget(self.distanceFromPointMinRadiusLineEdit)
        self.label_30 = QtGui.QLabel(self.locationGroupBox)
        self.label_30.setEnabled(True)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.horizontalLayout_19.addWidget(self.label_30)
        self.formLayout_7.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_19)
        self.label_31 = QtGui.QLabel(self.locationGroupBox)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.formLayout_7.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_31)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.distanceFromPointMaxRadiusLineEdit = QtGui.QLineEdit(self.locationGroupBox)
        self.distanceFromPointMaxRadiusLineEdit.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distanceFromPointMaxRadiusLineEdit.sizePolicy().hasHeightForWidth())
        self.distanceFromPointMaxRadiusLineEdit.setSizePolicy(sizePolicy)
        self.distanceFromPointMaxRadiusLineEdit.setObjectName(_fromUtf8("distanceFromPointMaxRadiusLineEdit"))
        self.horizontalLayout_20.addWidget(self.distanceFromPointMaxRadiusLineEdit)
        self.label_32 = QtGui.QLabel(self.locationGroupBox)
        self.label_32.setEnabled(True)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.horizontalLayout_20.addWidget(self.label_32)
        self.formLayout_7.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_20)
        self.label_33 = QtGui.QLabel(self.locationGroupBox)
        self.label_33.setEnabled(True)
        self.label_33.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.formLayout_7.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_33)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.distanceFromPointEastLineEdit = QtGui.QLineEdit(self.locationGroupBox)
        self.distanceFromPointEastLineEdit.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distanceFromPointEastLineEdit.sizePolicy().hasHeightForWidth())
        self.distanceFromPointEastLineEdit.setSizePolicy(sizePolicy)
        self.distanceFromPointEastLineEdit.setObjectName(_fromUtf8("distanceFromPointEastLineEdit"))
        self.horizontalLayout_21.addWidget(self.distanceFromPointEastLineEdit)
        self.label_34 = QtGui.QLabel(self.locationGroupBox)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.horizontalLayout_21.addWidget(self.label_34)
        self.formLayout_7.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_21)
        self.label_35 = QtGui.QLabel(self.locationGroupBox)
        self.label_35.setEnabled(True)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.formLayout_7.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_35)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.distanceFromPointNorthLineEdit = QtGui.QLineEdit(self.locationGroupBox)
        self.distanceFromPointNorthLineEdit.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distanceFromPointNorthLineEdit.sizePolicy().hasHeightForWidth())
        self.distanceFromPointNorthLineEdit.setSizePolicy(sizePolicy)
        self.distanceFromPointNorthLineEdit.setObjectName(_fromUtf8("distanceFromPointNorthLineEdit"))
        self.horizontalLayout_22.addWidget(self.distanceFromPointNorthLineEdit)
        self.label_36 = QtGui.QLabel(self.locationGroupBox)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.horizontalLayout_22.addWidget(self.label_36)
        self.formLayout_7.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_22)
        self.horizontalLayout_18.addLayout(self.formLayout_7)
        spacerItem8 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.locationDistanceFromEventsRadioButton = QtGui.QRadioButton(self.locationGroupBox)
        self.locationDistanceFromEventsRadioButton.setEnabled(False)
        self.locationDistanceFromEventsRadioButton.setObjectName(_fromUtf8("locationDistanceFromEventsRadioButton"))
        self.verticalLayout_4.addWidget(self.locationDistanceFromEventsRadioButton)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(24, -1, -1, -1)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setHorizontalSpacing(4)
        self.formLayout_6.setVerticalSpacing(1)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.label_25 = QtGui.QLabel(self.locationGroupBox)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_25)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.distanceFromEventsMinradiusLineEdit = QtGui.QLineEdit(self.locationGroupBox)
        self.distanceFromEventsMinradiusLineEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distanceFromEventsMinradiusLineEdit.sizePolicy().hasHeightForWidth())
        self.distanceFromEventsMinradiusLineEdit.setSizePolicy(sizePolicy)
        self.distanceFromEventsMinradiusLineEdit.setObjectName(_fromUtf8("distanceFromEventsMinradiusLineEdit"))
        self.horizontalLayout_16.addWidget(self.distanceFromEventsMinradiusLineEdit)
        self.label_26 = QtGui.QLabel(self.locationGroupBox)
        self.label_26.setEnabled(True)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.horizontalLayout_16.addWidget(self.label_26)
        self.formLayout_6.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_16)
        self.label_27 = QtGui.QLabel(self.locationGroupBox)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_27)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.distanceFromEventsMaxradiusLineEdit = QtGui.QLineEdit(self.locationGroupBox)
        self.distanceFromEventsMaxradiusLineEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distanceFromEventsMaxradiusLineEdit.sizePolicy().hasHeightForWidth())
        self.distanceFromEventsMaxradiusLineEdit.setSizePolicy(sizePolicy)
        self.distanceFromEventsMaxradiusLineEdit.setObjectName(_fromUtf8("distanceFromEventsMaxradiusLineEdit"))
        self.horizontalLayout_17.addWidget(self.distanceFromEventsMaxradiusLineEdit)
        self.label_28 = QtGui.QLabel(self.locationGroupBox)
        self.label_28.setEnabled(True)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.horizontalLayout_17.addWidget(self.label_28)
        self.formLayout_6.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_17)
        self.horizontalLayout_15.addLayout(self.formLayout_6)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.verticalLayout.addWidget(self.locationGroupBox)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)

        self.retranslateUi(EventOptionsWidget)
        QtCore.QMetaObject.connectSlotsByName(EventOptionsWidget)

    def retranslateUi(self, EventOptionsWidget):
        self.timeGroupBox.setTitle(_translate("EventOptionsWidget", "Time", None))
        self.timeBetweenRadioButton.setText(_translate("EventOptionsWidget", "Between start and end times", None))
        self.starttimeLabel.setText(_translate("EventOptionsWidget", "Start", None))
        self.starttimeDateTimeEdit.setDisplayFormat(_translate("EventOptionsWidget", "yyyy-MM-dd hh:mm:ss", None))
        self.endtimeLabel.setText(_translate("EventOptionsWidget", "End", None))
        self.endtimeDateTimeEdit.setDisplayFormat(_translate("EventOptionsWidget", "yyyy-MM-dd hh:mm:ss", None))
        self.timeDuringStationsRadioButton.setText(_translate("EventOptionsWidget", "During operation of selected stations", None))
        self.magnitudeGroupBox.setTitle(_translate("EventOptionsWidget", "Magnitude", None))
        self.label.setText(_translate("EventOptionsWidget", "Min", None))
        self.label_4.setText(_translate("EventOptionsWidget", "Max", None))
        self.maxmagLineEdit.setText(_translate("EventOptionsWidget", "10", None))
        self.label_7.setText(_translate("EventOptionsWidget", "Type", None))
        self.magtypeComboBox.setItemText(0, _translate("EventOptionsWidget", "All Types", None))
        self.magtypeComboBox.setItemText(1, _translate("EventOptionsWidget", "TB", None))
        self.magtypeComboBox.setItemText(2, _translate("EventOptionsWidget", "ML", None))
        self.magtypeComboBox.setItemText(3, _translate("EventOptionsWidget", "MS", None))
        self.magtypeComboBox.setItemText(4, _translate("EventOptionsWidget", "MW", None))
        self.depthGroupBox.setTitle(_translate("EventOptionsWidget", "Depth (km)", None))
        self.label_2.setText(_translate("EventOptionsWidget", "Max", None))
        self.mindepthLineEdit.setText(_translate("EventOptionsWidget", "0", None))
        self.maxdepthLineEdit.setText(_translate("EventOptionsWidget", "6000", None))
        self.label_12.setText(_translate("EventOptionsWidget", "Min", None))
        self.locationGroupBox.setTitle(_translate("EventOptionsWidget", "Location", None))
        self.locationRangeRadioButton.setText(_translate("EventOptionsWidget", "Within lat/lon box", None))
        self.locationDistanceFromPointRadioButton.setText(_translate("EventOptionsWidget", "Distance from point", None))
        self.label_29.setText(_translate("EventOptionsWidget", "between", None))
        self.label_30.setText(_translate("EventOptionsWidget", "degrees", None))
        self.label_31.setText(_translate("EventOptionsWidget", "and", None))
        self.label_32.setText(_translate("EventOptionsWidget", "degrees", None))
        self.label_33.setText(_translate("EventOptionsWidget", "from", None))
        self.label_34.setText(_translate("EventOptionsWidget", "E", None))
        self.label_35.setText(_translate("EventOptionsWidget", "and", None))
        self.label_36.setText(_translate("EventOptionsWidget", "N", None))
        self.locationDistanceFromEventsRadioButton.setText(_translate("EventOptionsWidget", "Distance from selected events", None))
        self.label_25.setText(_translate("EventOptionsWidget", "between", None))
        self.label_26.setText(_translate("EventOptionsWidget", "degrees", None))
        self.label_27.setText(_translate("EventOptionsWidget", "and", None))
        self.label_28.setText(_translate("EventOptionsWidget", "degrees", None))

