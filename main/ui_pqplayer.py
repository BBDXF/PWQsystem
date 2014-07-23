#! /usr/bin/env python
# -*- coding: utf-8 -*-
############################################
#
# UI class for admin the plugins
#
############################################

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import phonon

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_MainWindow(QDialog):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.resize(586, 308)
        #self.setStyleSheet(_fromUtf8("background-color: rgb(85, 85, 127);color: rgb(255, 255, 255);"))
        self.layout_all = QHBoxLayout()
        # title
        self.layout_title = QHBoxLayout()
        self.label_main_title = QLabel()
        self.label_main_ver = QLabel()
        self.layout_title.addWidget(self.label_main_title)
        self.layout_title.addWidget(self.label_main_ver)
        # show progress
        self.layout_progress = QVBoxLayout()
        self.label_author = QLabel()
        self.label_author.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_time = QLabel()
        self.label_time.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.slider_progree = phonon.Phonon.SeekSlider()
        self.slider_progree.setMaximumSize(QSize(16777215, 15))
        self.layout_progress.addWidget(self.label_author)
        self.layout_progress.addWidget(self.slider_progree)
        self.layout_progress.addWidget(self.label_time)
        # btn control
        self.layout_control = QHBoxLayout()
        self.checkBox_lrc = QCheckBox()
        self.layout_control.addWidget(self.checkBox_lrc)
        self.toolButton_left = QToolButton()
        self.layout_control.addWidget(self.toolButton_left)
        self.toolButton_play = QToolButton()
        self.layout_control.addWidget(self.toolButton_play)
        self.toolButton_right = QToolButton()
        self.layout_control.addWidget(self.toolButton_right)
        self.slider_volume = phonon.Phonon.VolumeSlider()
        self.slider_volume.setMaximumSize(QSize(16777215, 15))
        self.slider_volume.setIconSize(QSize(15, 15))
        self.layout_control.addWidget(self.slider_volume)
        # listshow
        self.listshow = QListWidget()
        # btn local
        self.layout_local = QHBoxLayout()
        self.toolButton_addfile = QToolButton()
        self.toolButton_clear = QToolButton()
        self.toolButton_plugins = QToolButton()
        self.layout_local.addWidget(self.toolButton_addfile)
        self.layout_local.addWidget(self.toolButton_clear)
        self.layout_local.addWidget(self.toolButton_plugins)
        # lef layout
        self.layout_left = QVBoxLayout()
        self.layout_left.addLayout(self.layout_title)
        self.layout_left.addLayout(self.layout_progress)
        self.layout_left.addLayout(self.layout_control)
        self.layout_left.addWidget(self.listshow)
        self.layout_left.addLayout(self.layout_local)
        # right layout
        self.layout_right = QVBoxLayout()
        # top search layout
        self.layout_search = QHBoxLayout()
        self.lineEdit_search = QLineEdit()
        self.toolButton_baidu = QToolButton()
        self.toolButton_163 = QToolButton()
        self.layout_search.addWidget(self.lineEdit_search)
        self.layout_search.addWidget(self.toolButton_baidu)
        self.layout_search.addWidget(self.toolButton_163)
        # search list
        self.listsearch = QListWidget()
        self.layout_right.addLayout(self.layout_search)
        self.layout_right.addWidget(self.listsearch)
        # layout_all
        self.layout_all.addLayout(self.layout_left)
        self.layout_all.addLayout(self.layout_right)
        # set layout
        self.setLayout(self.layout_all)
        # text
        self.setWindowTitle(_fromUtf8("pqplayer"))
        self.label_main_title.setText(_fromUtf8("PQ音乐播放器"))
        self.label_main_ver.setText(_fromUtf8("V1.0.1"))
        self.label_author.setText(_fromUtf8(""))
        self.label_time.setText(_fromUtf8("00:00/00:00"))
        self.checkBox_lrc.setText(_fromUtf8("歌词"))
        self.toolButton_left.setText(_fromUtf8("<"))
        self.toolButton_play.setText(_fromUtf8("||"))
        self.toolButton_right.setText(_fromUtf8(">"))
        self.toolButton_baidu.setText(_fromUtf8("百度音乐"))
        self.toolButton_163.setText(_fromUtf8("网易云音乐"))
        self.toolButton_addfile.setText(_fromUtf8("添加文件"))
        self.toolButton_clear.setText(_fromUtf8("清除列表"))
        self.toolButton_plugins.setText(_fromUtf8("插件管理"))
        # skin
        self.setskin("")
        #QMetaObject.connectSlotsByName(MainWindow)

    def setskin(self, strskin):
        # skin
        self.setStyleSheet(_fromUtf8(strskin))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())

