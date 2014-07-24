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
from PyQt4.phonon import *
import ui_pqplayer
import pluginsmgr

class PQPlayer(ui_pqplayer.Ui_MainWindow):
    def __init__(self, parent=None):
        super(PQPlayer, self).__init__(parent)
        self.audiooutput = Phonon.AudioOutput(Phonon.MusicCategory)
        self.mediaobj = Phonon.MediaObject()
        Phonon.createPath(self.mediaobj, self.audiooutput)
        self.slider_progree.setMediaObject(self.mediaobj)
        self.slider_volume.setAudioOutput(self.audiooutput)
        self.pluginui = pluginsmgr.PluginsMgr()
        self.pluginui.searchplugins()
        self.audiolist = []
        self.curindex = 0
        self.audiotime_all = 0
        self.audiotime_cur = 0
        self.connect(self.mediaobj, SIGNAL("tick(qint64)"), self.tickInterval)
        self.connect(self.mediaobj, SIGNAL("finished()"), self.finished)
        self.connect(self.mediaobj, SIGNAL("metaDataChanged()"), self.metaDataChanged)
        self.connect(self.toolButton_addfile, SIGNAL("clicked()"), self.addfile)
        self.connect(self.toolButton_play, SIGNAL("clicked()"), self.startplay)
        self.connect(self.toolButton_left, SIGNAL("clicked()"), self.startleft)
        self.connect(self.toolButton_right, SIGNAL("clicked()"), self.startright)
        self.connect(self.listshow, SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.startselect)
        self.connect(self.listsearch, SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.startsearchurl)
        self.connect(self.toolButton_clear, SIGNAL("clicked()"), self.clearlist)
        self.connect(self.toolButton_plugins, SIGNAL("clicked()"), self.pluginsmgr)
        self.connect(self.toolButton_baidu, SIGNAL("clicked()"), self.searchbaidu)
        self.connect(self.toolButton_163, SIGNAL("clicked()"), self.search163)
    def startsearchurl(self, item):
        strvar = item.data(Qt.ToolTipRole)
        txt = strvar.toString()
        if len(txt) > 0:
            self.audiolist.append(txt)
            self.curindex = len(self.audiolist)-1
            self.updatelistui()
            self.mediaobj.setCurrentSource(Phonon.MediaSource(txt))
            self.mediaobj.play()
            self.listshow.setCurrentRow(self.curindex)
    def clearlist(self):
        self.audiolist = []
        self.curindex = 0
        self.listshow.clear()
    def startselect(self, item):
        #strvar = item.data(Qt.ToolTipRole)
        #print strvar.toString()
        #print self.audiolist[self.listshow.currentRow()]
        self.curindex = self.listshow.currentRow()
        self.mediaobj.stop()
        if self.curindex < len(self.audiolist):
            self.mediaobj.setCurrentSource(Phonon.MediaSource(self.audiolist[self.curindex]))
            self.mediaobj.play()
            self.listshow.setCurrentRow(self.curindex)
        else:
            self.curindex = 0
    def addfile(self):
        filelist = QFileDialog.getOpenFileNames(None, QString("Selcet files"), QString(""), QString("Audio Files(*.mp3 *.wma);;All Files(*.*)"))
        if len(filelist) > 0:
            self.audiolist.extend(filelist)
            self.updatelistui()
    def updatelistui(self):
        #print self.audiolist
        self.listshow.clear()
        for strpath in self.audiolist:
            item = QListWidgetItem(os.path.basename(unicode(strpath)))
            item.setData(Qt.ToolTipRole, QVariant(strpath))
            self.listshow.addItem(item)
    def startleft(self):
        if len(self.audiolist) < 1:
            return
        self.mediaobj.stop()
        if self.curindex > 0:
            self.curindex -= 1
        else:
            self.curindex = len(self.audiolist)-1
        self.mediaobj.setCurrentSource(Phonon.MediaSource(self.audiolist[self.curindex]))
        self.mediaobj.play()
        self.listshow.setCurrentRow(self.curindex)
    def startright(self):
        if len(self.audiolist) < 1:
            return
        self.mediaobj.stop()
        if self.curindex < len(self.audiolist)-1:
            self.curindex += 1
        else:
            self.curindex = 0
        self.mediaobj.setCurrentSource(Phonon.MediaSource(self.audiolist[self.curindex]))
        self.mediaobj.play()
        self.listshow.setCurrentRow(self.curindex)
    def startplay(self):
        state = self.mediaobj.state()
        if state == Phonon.PlayingState:
            self.mediaobj.pause()
            print "playing -> pause"
            self.toolButton_play.setText("|>")
            return
        if state == Phonon.PausedState:
            self.mediaobj.play()
            print "pause -> play"
            self.toolButton_play.setText("||")
            return
        if state == Phonon.StoppedState or state == Phonon.LoadingState:
            if len(self.audiolist) < 1:
                return
            print "set and play"
            self.mediaobj.setCurrentSource(Phonon.MediaSource(self.audiolist[self.curindex]))
            self.mediaobj.play()
            self.listshow.setCurrentRow(self.curindex)
        # else nothing
    def tickInterval(self, time):
        self.audiotime_all = self.mediaobj.totalTime()
        self.audiotime_cur = time
        (m1, s1) = divmod(int(self.audiotime_all/1000), 60)
        (m2, s2) = divmod(int(self.audiotime_cur/1000), 60)
        strshow = "{:02d}:{:02d}/{:02d}:{:02d}".format(m2, s2, m1, s1)
        self.label_time.setText(QString(strshow))
    def finished(self):
        print "finish"
        self.mediaobj.stop()
    def metaDataChanged(self):
        metainfo = self.mediaobj.metaData()
        print metainfo
        trackArtist = metainfo.get(QString("ARTIST"))
        trackTitle = metainfo.get(QString("TITLE"))
        #print trackTitle
        #print trackArtist
        strshow = os.path.basename(unicode(self.audiolist[self.curindex]))
        (strshow, ty) = os.path.splitext(strshow)
        if trackArtist is not None and trackTitle is not None:
            strshow = QString("%1 - %2").arg(trackArtist[0]).arg(trackTitle[0])
            self.label_author.setText(strshow)
        else:
            if trackTitle is not None:
                strshow = QString("%1").arg(trackTitle[0])
                self.label_author.setText(strshow)
            else:
                self.label_author.setText(QString(strshow))
    def pluginsmgr(self):
        self.pluginui.show()
    def searchbaidu(self):
        txt = unicode(self.lineEdit_search.text()).encode(encoding="utf-8", errors="ignore")
        audioinf = self.pluginui.search(txt, 1)
        print audioinf
        print txt
        #strshow = "{} - {}".format(audioinf['title'], audioinf['artist'])
        if len(audioinf['title']) > 0:
            strshow = QString("%1 - %2").arg(QString(audioinf['title'])).arg(QString(audioinf['artist']))
            strtip = QString(audioinf['audiourl'])
            item = QListWidgetItem(QString(strshow))
            item.setToolTip(strtip)
            self.listsearch.addItem(item)
    def search163(self):
        txt = unicode(self.lineEdit_search.text()).encode(encoding="utf-8", errors="ignore")
        audioinf = self.pluginui.search(txt, 2)
        print audioinf
        print txt
        #strshow = "{} - {}".format(audioinf['title'], audioinf['artist'])
        if len(audioinf['title']) > 0:
            strshow = QString("%1 - %2").arg(QString(audioinf['title'])).arg(QString(audioinf['artist']))
            strtip = QString(audioinf['audiourl'])
            item = QListWidgetItem(QString(strshow))
            item.setToolTip(strtip)
            self.listsearch.addItem(item)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = PQPlayer()
    ui.setskin("background-color: rgb(64, 128, 128);color: rgb(255, 128, 64);")
    ui.show()
    sys.exit(app.exec_())