#! /usr/bin/env python
# -*- coding: utf-8 -*-
############################################
#
# UI class for admin the plugins
#
############################################

from PyQt4.QtCore import *
from PyQt4.QtGui import *

# for chinese text to convert
try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
# real class for ui
class Ui_PluginsMgr(QDialog):
    def __init__(self, parent=None):
        super(Ui_PluginsMgr, self).__init__(parent)
        self.setFixedSize(500, 380)
        # add some button
        self.btnRefresh = QToolButton(self)
        self.btnRefresh.setFixedSize(80, 25)
        self.btnInstall = QToolButton(self)
        self.btnInstall.setFixedSize(80, 25)
        self.btnUninstall = QToolButton(self)
        self.btnUninstall.setFixedSize(80, 25)
        self.btnClose = QToolButton(self)
        self.btnClose.setFixedSize(80, 25)
        self.btnmialBug = QToolButton(self)
        self.btnmialBug.setFixedSize(80, 25)
        # layout h
        layoutbtn = QHBoxLayout()
        layoutbtn.addWidget(self.btnRefresh)
        layoutbtn.addWidget(self.btnInstall)
        layoutbtn.addWidget(self.btnUninstall)
        layoutbtn.addWidget(self.btnmialBug)
        layoutbtn.addWidget(self.btnClose)
        # listview
        self.listplugins = QTreeWidget(self)
        self.listplugins.setColumnCount(4)
        strlist = QStringList()
        strlist.append(QString("PluginName"))
        strlist.append(QString("Version"))
        strlist.append(QString("Author"))
        strlist.append(QString("Path"))
        self.listplugins.setHeaderLabels(strlist)
        self.listplugins.setColumnWidth(0, 150)
        self.inittree()
        layoutui = QVBoxLayout()
        layoutui.addWidget(self.listplugins)
        layoutui.addLayout(layoutbtn)
        # set layout
        self.setLayout(layoutui)
        # use lang
        self._tanslateLang()

    def _tanslateLang(self):
        self.setWindowTitle(_fromUtf8("插件管理"))
        self.btnRefresh.setText(_fromUtf8("刷新插件"))
        self.btnInstall.setText(_fromUtf8("安装插件"))
        self.btnUninstall.setText(_fromUtf8("卸载插件"))
        self.btnmialBug.setText(_fromUtf8("提交Bug"))
        self.btnClose.setText(_fromUtf8("关闭"))
    # 模块管理
    def adduiplugin(self, **kwargs):
        strlist = QStringList()
        strlist.append(_fromUtf8(kwargs.get("name", "")))
        strlist.append(_fromUtf8(kwargs.get("version", "")))
        strlist.append(_fromUtf8(kwargs.get("author", "")))
        strlist.append(_fromUtf8(kwargs.get("path", "")))
        if kwargs.get("type") == "Search":
            self.treesearch.addChild(QTreeWidgetItem(strlist))
        if kwargs.get("type") == "Download":
            self.treedownload.addChild(QTreeWidgetItem(strlist))
    def inittree(self):
        # delete all
        self.listplugins.clear()
        # add parent
        self.treesearch = QTreeWidgetItem(QStringList(QString("SearchPlugins")))
        self.treedownload = QTreeWidgetItem(QStringList(QString("DownloadPlugins")))
        self.listplugins.addTopLevelItem(self.treesearch)
        self.listplugins.addTopLevelItem(self.treedownload)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    fm = Ui_PluginsMgr()
    fm.show()
    app.exec_()

