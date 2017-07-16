# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_coordtransform.ui'
#
# Created: Sun Jul 16 17:09:58 2017
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_Coordtransform(object):
    def setupUi(self, Coordtransform):
        Coordtransform.setObjectName(_fromUtf8("Coordtransform"))
        Coordtransform.resize(527, 543)
        self.OK = QtGui.QDialogButtonBox(Coordtransform)
        self.OK.setGeometry(QtCore.QRect(350, 510, 171, 32))
        self.OK.setOrientation(QtCore.Qt.Horizontal)
        self.OK.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.OK.setObjectName(_fromUtf8("OK"))
        self.X = QtGui.QLineEdit(Coordtransform)
        self.X.setGeometry(QtCore.QRect(10, 110, 113, 27))
        self.X.setObjectName(_fromUtf8("X"))
        self.Y = QtGui.QLineEdit(Coordtransform)
        self.Y.setGeometry(QtCore.QRect(140, 110, 113, 27))
        self.Y.setObjectName(_fromUtf8("Y"))
        self.inputcrs = QtGui.QLineEdit(Coordtransform)
        self.inputcrs.setGeometry(QtCore.QRect(270, 110, 113, 27))
        self.inputcrs.setObjectName(_fromUtf8("inputcrs"))
        self.results = QtGui.QTextBrowser(Coordtransform)
        self.results.setGeometry(QtCore.QRect(10, 350, 501, 101))
        self.results.setObjectName(_fromUtf8("results"))
        self.label = QtGui.QLabel(Coordtransform)
        self.label.setGeometry(QtCore.QRect(10, 70, 241, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.outputcrs = QtGui.QLineEdit(Coordtransform)
        self.outputcrs.setGeometry(QtCore.QRect(400, 110, 113, 27))
        self.outputcrs.setObjectName(_fromUtf8("outputcrs"))
        self.label_2 = QtGui.QLabel(Coordtransform)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 21, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Coordtransform)
        self.label_3.setGeometry(QtCore.QRect(190, 90, 21, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Coordtransform)
        self.label_4.setGeometry(QtCore.QRect(275, 90, 101, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Coordtransform)
        self.label_5.setGeometry(QtCore.QRect(401, 90, 111, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.transform = QtGui.QPushButton(Coordtransform)
        self.transform.setGeometry(QtCore.QRect(400, 150, 97, 27))
        self.transform.setObjectName(_fromUtf8("transform"))
        self.label_6 = QtGui.QLabel(Coordtransform)
        self.label_6.setGeometry(QtCore.QRect(20, 330, 51, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.clear = QtGui.QPushButton(Coordtransform)
        self.clear.setGeometry(QtCore.QRect(290, 150, 97, 27))
        self.clear.setObjectName(_fromUtf8("clear"))
        self.label_8 = QtGui.QLabel(Coordtransform)
        self.label_8.setGeometry(QtCore.QRect(290, 10, 221, 51))
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.line = QtGui.QFrame(Coordtransform)
        self.line.setGeometry(QtCore.QRect(6, 60, 511, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_9 = QtGui.QLabel(Coordtransform)
        self.label_9.setGeometry(QtCore.QRect(30, 0, 221, 61))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/coordtransform/logo.png")))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_7 = QtGui.QLabel(Coordtransform)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 151, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_10 = QtGui.QLabel(Coordtransform)
        self.label_10.setGeometry(QtCore.QRect(10, 260, 161, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Coordtransform)
        self.label_11.setGeometry(QtCore.QRect(80, 480, 21, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Coordtransform)
        self.label_12.setGeometry(QtCore.QRect(230, 480, 21, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(Coordtransform)
        self.label_13.setGeometry(QtCore.QRect(80, 460, 151, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.inputproj4 = QtGui.QTextBrowser(Coordtransform)
        self.inputproj4.setGeometry(QtCore.QRect(10, 210, 501, 41))
        self.inputproj4.setObjectName(_fromUtf8("inputproj4"))
        self.outputproj4 = QtGui.QTextBrowser(Coordtransform)
        self.outputproj4.setGeometry(QtCore.QRect(10, 280, 501, 41))
        self.outputproj4.setObjectName(_fromUtf8("outputproj4"))
        self.trfX = QtGui.QTextBrowser(Coordtransform)
        self.trfX.setGeometry(QtCore.QRect(20, 500, 131, 31))
        self.trfX.setObjectName(_fromUtf8("trfX"))
        self.trfY = QtGui.QTextBrowser(Coordtransform)
        self.trfY.setGeometry(QtCore.QRect(170, 500, 131, 31))
        self.trfY.setObjectName(_fromUtf8("trfY"))

        self.retranslateUi(Coordtransform)
        QtCore.QObject.connect(self.OK, QtCore.SIGNAL(_fromUtf8("accepted()")), Coordtransform.accept)
        QtCore.QObject.connect(self.OK, QtCore.SIGNAL(_fromUtf8("rejected()")), Coordtransform.reject)
        QtCore.QMetaObject.connectSlotsByName(Coordtransform)

    def retranslateUi(self, Coordtransform):
        Coordtransform.setWindowTitle(_translate("Coordtransform", "Coordtransform", None))
        self.label.setText(_translate("Coordtransform", "USAGE: Input x, y and epsg/user defined values", None))
        self.label_2.setText(_translate("Coordtransform", "X", None))
        self.label_3.setText(_translate("Coordtransform", "Y", None))
        self.label_4.setText(_translate("Coordtransform", "INPUT EPSG/USER", None))
        self.label_5.setText(_translate("Coordtransform", "OUTPUT EPSG/USER", None))
        self.transform.setText(_translate("Coordtransform", "Transform", None))
        self.label_6.setText(_translate("Coordtransform", "RESULTS", None))
        self.clear.setText(_translate("Coordtransform", "Clear", None))
        self.label_8.setText(_translate("Coordtransform", "X,Y point coordtransform\n"
" Copyright (C) 2017 Giuseppe De Marco\n"
"www.d2gis.com", None))
        self.label_7.setText(_translate("Coordtransform", "INPUT EPSG/USER To PROJ4", None))
        self.label_10.setText(_translate("Coordtransform", "OUTPUT EPSG/USER To PROJ4", None))
        self.label_11.setText(_translate("Coordtransform", "X", None))
        self.label_12.setText(_translate("Coordtransform", "Y", None))
        self.label_13.setText(_translate("Coordtransform", "TRANSFORMED COORDINATES", None))

##import resources_rc
##
