# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pluginsmgr.ui'
#
# Created: Tue Jul 22 18:27:10 2014
#      by: PyQt4 UI code generator 4.11.1
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(481, 430)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 461, 411))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.treeView = QtGui.QTreeView(self.widget)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.verticalLayout.addWidget(self.treeView)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.toolButton = QtGui.QToolButton(self.widget)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.toolButton_2 = QtGui.QToolButton(self.widget)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout.addWidget(self.toolButton_2)
        self.toolButton_3 = QtGui.QToolButton(self.widget)
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.horizontalLayout.addWidget(self.toolButton_3)
        self.toolButton_5 = QtGui.QToolButton(self.widget)
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        self.horizontalLayout.addWidget(self.toolButton_5)
        self.toolButton_4 = QtGui.QToolButton(self.widget)
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.horizontalLayout.addWidget(self.toolButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.toolButton.setText(_translate("Form", "刷新插件", None))
        self.toolButton_2.setText(_translate("Form", "安装插件", None))
        self.toolButton_3.setText(_translate("Form", "卸载插件", None))
        self.toolButton_5.setText(_translate("Form", "提交BUG", None))
        self.toolButton_4.setText(_translate("Form", "关闭", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

