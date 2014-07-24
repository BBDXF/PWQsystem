#! /usr/bin/env python
# -*- coding: utf-8 -*-
############################################
#
# UI class for admin the plugins
#
############################################
import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_pluginsmgr

class PluginsMgr(ui_pluginsmgr.Ui_PluginsMgr):
    def __init__(self, parent=None):
        super(PluginsMgr, self).__init__(parent)
        self.pluginsdir = "../plugins"
        self.plginsSearch = []
        self.plginsDownload = []
        self.connect(self.btnRefresh, SIGNAL("clicked()"), self.reflash)
        self.connect(self.btnClose, SIGNAL("clicked()"), self.close)
    def reflash(self):
        print "Reflash"
        self.inittree()
        for p in self.plginsSearch:
            self.adduiplugin(type="Search", name=p.PluginName, version=p.PluginVersion, author=p.PluginAuthor, path=self.pluginsdir)
        for p in self.plginsDownload:
            self.adduiplugin(type="Download", name=p.PluginName, version=p.PluginVersion, author=p.PluginAuthor, path=self.pluginsdir)
        self.listplugins.expandAll()
    def install(self, pluginfile):
        # 先判断是否注册
        (pluginmodle, pluginend) = os.path.splitext(pluginfile)
        if pluginend != ".py":
            return
        try:
            runmodle = __import__(pluginmodle)
            if runmodle is not None:
                if hasattr(runmodle, "MusicsearchAPI"):
                    namedclass = getattr(runmodle, "MusicsearchAPI")
                    self.plginsSearch.append(namedclass())
                    #print namedclass
                else:
                    if hasattr(runmodle, "DownloadAPI"):
                        namedclass = getattr(runmodle, "DownloadAPI")
                        self.plginsDownload.append(namedclass())
                        #print namedclass
        except:
            print("error in load plugins")

    def uninstall(self, plugin):
        pass
    def sendbug(self):
        pass
    def searchplugins(self):
        self.listplugins.clear()
        #earch the plugins dir
        self.pluginsdir = os.path.abspath(self.pluginsdir)
        # add plugins dir to sys.path
        sys.path.append(self.pluginsdir)
        for pluginfile in os.listdir(self.pluginsdir):
            if os.path.isfile(os.path.join(self.pluginsdir, pluginfile)):
                try:
                    #print pluginfile
                    self.install(pluginfile)
                except:
                    print "Install plugin {} failed".format(pluginfile)
        self.reflash()
    def search(self, txt, ty=0):
        psearch = self.plginsSearch[ty]
        txts = " ".join(txt.split()).split()
        if len(txts) == 1:
            psearch.searchaduioinfo(title=txts[0])
        else:
            if len(txts) > 1:
                psearch.searchaduioinfo(title=txts[0], artist=txts[1])
        return psearch.audioinfo
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    p = PluginsMgr()
    p.searchplugins()
    p.show()
    app.exec_()








