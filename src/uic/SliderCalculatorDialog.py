# Form implementation generated from reading ui file 'ui/SliderCalculatorDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SliderCalculator(object):
    def setupUi(self, SliderCalculator):
        SliderCalculator.setObjectName("SliderCalculator")
        SliderCalculator.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        SliderCalculator.resize(423, 227)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SliderCalculator.sizePolicy().hasHeightForWidth())
        SliderCalculator.setSizePolicy(sizePolicy)
        SliderCalculator.setWindowTitle("Slider Calculator")
        SliderCalculator.setToolTip("")
        SliderCalculator.setAccessibleDescription("")
        SliderCalculator.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(SliderCalculator)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_SliderValue = QtWidgets.QLabel(SliderCalculator)
        self.label_SliderValue.setToolTip("")
        self.label_SliderValue.setAccessibleDescription("")
        self.label_SliderValue.setText("SliderValue")
        self.label_SliderValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_SliderValue.setObjectName("label_SliderValue")
        self.gridLayout.addWidget(self.label_SliderValue, 1, 0, 1, 1)
        self.lineEdit_TargetValue_max = QtWidgets.QLineEdit(SliderCalculator)
        self.lineEdit_TargetValue_max.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_TargetValue_max.setObjectName("lineEdit_TargetValue_max")
        self.gridLayout.addWidget(self.lineEdit_TargetValue_max, 2, 2, 1, 1)
        self.lineEdit_TargetValue_min = QtWidgets.QLineEdit(SliderCalculator)
        self.lineEdit_TargetValue_min.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_TargetValue_min.setObjectName("lineEdit_TargetValue_min")
        self.gridLayout.addWidget(self.lineEdit_TargetValue_min, 2, 1, 1, 1)
        self.label_TargetValue = QtWidgets.QLabel(SliderCalculator)
        self.label_TargetValue.setToolTip("")
        self.label_TargetValue.setAccessibleDescription("")
        self.label_TargetValue.setText("Target Value")
        self.label_TargetValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_TargetValue.setObjectName("label_TargetValue")
        self.gridLayout.addWidget(self.label_TargetValue, 2, 0, 1, 1)
        self.label_min = QtWidgets.QLabel(SliderCalculator)
        self.label_min.setToolTip("")
        self.label_min.setAccessibleDescription("")
        self.label_min.setText("min")
        self.label_min.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_min.setObjectName("label_min")
        self.gridLayout.addWidget(self.label_min, 0, 1, 1, 1)
        self.lineEdit_SliderValue_min = QtWidgets.QLineEdit(SliderCalculator)
        self.lineEdit_SliderValue_min.setEnabled(True)
        self.lineEdit_SliderValue_min.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lineEdit_SliderValue_min.setToolTip("")
        self.lineEdit_SliderValue_min.setAccessibleDescription("")
        self.lineEdit_SliderValue_min.setText("")
        self.lineEdit_SliderValue_min.setFrame(False)
        self.lineEdit_SliderValue_min.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_SliderValue_min.setReadOnly(True)
        self.lineEdit_SliderValue_min.setPlaceholderText("")
        self.lineEdit_SliderValue_min.setObjectName("lineEdit_SliderValue_min")
        self.gridLayout.addWidget(self.lineEdit_SliderValue_min, 1, 1, 1, 1)
        self.lineEdit_SliderValue_max = QtWidgets.QLineEdit(SliderCalculator)
        self.lineEdit_SliderValue_max.setEnabled(True)
        self.lineEdit_SliderValue_max.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lineEdit_SliderValue_max.setToolTip("")
        self.lineEdit_SliderValue_max.setAccessibleDescription("")
        self.lineEdit_SliderValue_max.setInputMask("")
        self.lineEdit_SliderValue_max.setText("")
        self.lineEdit_SliderValue_max.setFrame(False)
        self.lineEdit_SliderValue_max.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_SliderValue_max.setReadOnly(True)
        self.lineEdit_SliderValue_max.setPlaceholderText("")
        self.lineEdit_SliderValue_max.setClearButtonEnabled(False)
        self.lineEdit_SliderValue_max.setObjectName("lineEdit_SliderValue_max")
        self.gridLayout.addWidget(self.lineEdit_SliderValue_max, 1, 2, 1, 1)
        self.label_max = QtWidgets.QLabel(SliderCalculator)
        self.label_max.setToolTip("")
        self.label_max.setAccessibleDescription("")
        self.label_max.setText("max")
        self.label_max.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_max.setObjectName("label_max")
        self.gridLayout.addWidget(self.label_max, 0, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_Factor = QtWidgets.QLabel(SliderCalculator)
        self.label_Factor.setToolTip("")
        self.label_Factor.setAccessibleDescription("")
        self.label_Factor.setText("Factor")
        self.label_Factor.setObjectName("label_Factor")
        self.gridLayout_2.addWidget(self.label_Factor, 0, 0, 1, 1)
        self.label_Offset = QtWidgets.QLabel(SliderCalculator)
        self.label_Offset.setToolTip("")
        self.label_Offset.setAccessibleDescription("")
        self.label_Offset.setText("Offset")
        self.label_Offset.setObjectName("label_Offset")
        self.gridLayout_2.addWidget(self.label_Offset, 1, 0, 1, 1)
        self.lineEdit_Factor = QtWidgets.QLineEdit(SliderCalculator)
        self.lineEdit_Factor.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lineEdit_Factor.setToolTip("")
        self.lineEdit_Factor.setAccessibleDescription("")
        self.lineEdit_Factor.setText("")
        self.lineEdit_Factor.setFrame(False)
        self.lineEdit_Factor.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_Factor.setReadOnly(True)
        self.lineEdit_Factor.setPlaceholderText("")
        self.lineEdit_Factor.setObjectName("lineEdit_Factor")
        self.gridLayout_2.addWidget(self.lineEdit_Factor, 0, 1, 1, 1)
        self.lineEdit_Offset = QtWidgets.QLineEdit(SliderCalculator)
        self.lineEdit_Offset.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lineEdit_Offset.setToolTip("")
        self.lineEdit_Offset.setAccessibleDescription("")
        self.lineEdit_Offset.setText("")
        self.lineEdit_Offset.setFrame(False)
        self.lineEdit_Offset.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_Offset.setReadOnly(True)
        self.lineEdit_Offset.setPlaceholderText("")
        self.lineEdit_Offset.setObjectName("lineEdit_Offset")
        self.gridLayout_2.addWidget(self.lineEdit_Offset, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(SliderCalculator)
        self.buttonBox.setToolTip("")
        self.buttonBox.setAccessibleDescription("")
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SliderCalculator)
        self.buttonBox.accepted.connect(SliderCalculator.accept) # type: ignore
        self.buttonBox.rejected.connect(SliderCalculator.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SliderCalculator)
        SliderCalculator.setTabOrder(self.lineEdit_TargetValue_min, self.lineEdit_TargetValue_max)
        SliderCalculator.setTabOrder(self.lineEdit_TargetValue_max, self.lineEdit_SliderValue_min)
        SliderCalculator.setTabOrder(self.lineEdit_SliderValue_min, self.lineEdit_SliderValue_max)
        SliderCalculator.setTabOrder(self.lineEdit_SliderValue_max, self.lineEdit_Factor)
        SliderCalculator.setTabOrder(self.lineEdit_Factor, self.lineEdit_Offset)

    def retranslateUi(self, SliderCalculator):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SliderCalculator = QtWidgets.QDialog()
    ui = Ui_SliderCalculator()
    ui.setupUi(SliderCalculator)
    SliderCalculator.show()
    sys.exit(app.exec())
