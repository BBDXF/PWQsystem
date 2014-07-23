#! /usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import threading
import os
"""\
download a file or something else
use a thread to download with http
"""
def downloadfile(downloadinfo):
    if downloadinfo['filename'] == "" or downloadinfo['filename'] is None:
        downloadinfo['filename'] = downloadinfo['targeturl'].split('/')[-1]
    filepath = downloadinfo['filepath']
    if filepath == "" or filepath is None:
        if not os.path.exists("./download"):
            os.mkdir("./download/")
        filepath = "./download/"
    else:
        if filepath[-1] != '/':
            filepath += '/'
    downloadinfo['filepath'] = filepath

    downloadinfo['cursize'] = 0
    downloadinfo['filesize'] = 0
    #print downloadinfo
    httpfile = urllib.urlopen(downloadinfo['targeturl'])
    if httpfile is not None:
        downloadinfo['filesize'] = int(httpfile.info().getheaders("Content-Length")[0])
        with open(downloadinfo['filepath'] + downloadinfo['filename'], 'wb') as outfile:
            for data in httpfile:
                outfile.write(data)
                downloadinfo['cursize'] += len(data)
                print downloadinfo


class DownloadAPI():
    def __init__(self):
        self.sysencode = "utf-8"#sys.getdefaultencoding()
        self.PluginName = "Http下载插件"
        self.PluginAuthor = "BBDXF"
        self.PluginVersion = "1.0.0"
        self.downloadinfo = {
            "targeturl": "",
            "filepath": "",
            "filename": "",
            "filesize": 0,
            "cursize": 0,
        }
        self.t = None
    def download(self, **kwargs):
        """\
        download(**kwargs): 单线程下载文件
        :keyword targeturl = 下载的链接[, filepath = 下载的路径, filename = 保存的文件名(包含扩展名)]
        """
        if kwargs.get('targeturl') is not None and len(kwargs.get('targeturl')) > 0:
            self.downloadinfo['targeturl'] = kwargs['targeturl']
            if kwargs.get('filepath') is not None:
                self.downloadinfo['filepath'] = kwargs['filepath']
            if kwargs.get('filename') is not None:
                self.downloadinfo['filename'] = kwargs['filename']
            self.t = threading.Thread(target=downloadfile, args=(self.downloadinfo,))
            self.t.run()
def test():
    p = DownloadAPI()
    p.download(targeturl="http://www.baidu.com/img/baidu_sylogo1.gif", filename="logo.gif")
if __name__ == "__main__": test()
