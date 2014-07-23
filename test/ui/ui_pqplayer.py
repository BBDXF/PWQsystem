# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pqplayer.ui'
#
# Created: Wed Jul 23 09:32:50 2014
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(586, 308)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(9, 9, 570, 292))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.layout_up = QtGui.QHBoxLayout(self.widget)
        self.layout_up.setMargin(0)
        self.layout_up.setObjectName(_fromUtf8("layout_up"))
        self.layout_left = QtGui.QVBoxLayout()
        self.layout_left.setObjectName(_fromUtf8("layout_left"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_main_title = QtGui.QLabel(self.widget)
        self.label_main_title.setObjectName(_fromUtf8("label_main_title"))
        self.horizontalLayout_2.addWidget(self.label_main_title)
        self.label_main_ver = QtGui.QLabel(self.widget)
        self.label_main_ver.setObjectName(_fromUtf8("label_main_ver"))
        self.horizontalLayout_2.addWidget(self.label_main_ver)
        self.layout_left.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_title = QtGui.QLabel(self.widget)
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.verticalLayout.addWidget(self.label_title)
        self.slider_ctr_progree = phonon.Phonon.SeekSlider(self.widget)
        self.slider_ctr_progree.setMaximumSize(QtCore.QSize(16777215, 15))
        self.slider_ctr_progree.setObjectName(_fromUtf8("slider_ctr_progree"))
        self.verticalLayout.addWidget(self.slider_ctr_progree)
        self.label_time = QtGui.QLabel(self.widget)
        self.label_time.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_time.setObjectName(_fromUtf8("label_time"))
        self.verticalLayout.addWidget(self.label_time)
        self.layout_left.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkBox_lrc = QtGui.QCheckBox(self.widget)
        self.checkBox_lrc.setObjectName(_fromUtf8("checkBox_lrc"))
        self.horizontalLayout.addWidget(self.checkBox_lrc)
        self.toolButton_left = QtGui.QToolButton(self.widget)
        self.toolButton_left.setObjectName(_fromUtf8("toolButton_left"))
        self.horizontalLayout.addWidget(self.toolButton_left)
        self.toolButton_play = QtGui.QToolButton(self.widget)
        self.toolButton_play.setObjectName(_fromUtf8("toolButton_play"))
        self.horizontalLayout.addWidget(self.toolButton_play)
        self.toolButton_right = QtGui.QToolButton(self.widget)
        self.toolButton_right.setObjectName(_fromUtf8("toolButton_right"))
        self.horizontalLayout.addWidget(self.toolButton_right)
        self.slider_volume = phonon.Phonon.VolumeSlider(self.widget)
        self.slider_volume.setMaximumSize(QtCore.QSize(16777215, 15))
        self.slider_volume.setIconSize(QtCore.QSize(15, 15))
        self.slider_volume.setObjectName(_fromUtf8("slider_volume"))
        self.horizontalLayout.addWidget(self.slider_volume)
        self.layout_left.addLayout(self.horizontalLayout)
        self.listView = QtGui.QListView(self.widget)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.layout_left.addWidget(self.listView)
        self.layout_up.addLayout(self.layout_left)
        self.layout_right = QtGui.QVBoxLayout()
        self.layout_right.setObjectName(_fromUtf8("layout_right"))
        self.layout_search = QtGui.QHBoxLayout()
        self.layout_search.setObjectName(_fromUtf8("layout_search"))
        self.lineEdit_search = QtGui.QLineEdit(self.widget)
        self.lineEdit_search.setObjectName(_fromUtf8("lineEdit_search"))
        self.layout_search.addWidget(self.lineEdit_search)
        self.toolButton_baidu = QtGui.QToolButton(self.widget)
        self.toolButton_baidu.setObjectName(_fromUtf8("toolButton_baidu"))
        self.layout_search.addWidget(self.toolButton_baidu)
        self.toolButton_163 = QtGui.QToolButton(self.widget)
        self.toolButton_163.setObjectName(_fromUtf8("toolButton_163"))
        self.layout_search.addWidget(self.toolButton_163)
        self.layout_right.addLayout(self.layout_search)
        self.listView_2 = QtGui.QListView(self.widget)
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.layout_right.addWidget(self.listView_2)
        self.layout_up.addLayout(self.layout_right)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_main_title.setText(_translate("MainWindow", "PQ音乐播放器", None))
        self.label_main_ver.setText(_translate("MainWindow", "V 1.0", None))
        self.label_title.setText(_translate("MainWindow", "刘德华", None))
        self.label_time.setText(_translate("MainWindow", "00:00/00:00", None))
        self.checkBox_lrc.setText(_translate("MainWindow", "歌词", None))
        self.toolButton_left.setText(_translate("MainWindow", "<", None))
        self.toolButton_play.setText(_translate("MainWindow", "||", None))
        self.toolButton_right.setText(_translate("MainWindow", ">", None))
        self.toolButton_baidu.setText(_translate("MainWindow", "百度音乐", None))
        self.toolButton_163.setText(_translate("MainWindow", "网易云音乐", None))

from PyQt4 import phonon

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

