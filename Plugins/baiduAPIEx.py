#! /usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
from xml.dom import minidom
import json
import re
"""\
user baidu music server to fetch audio info and lrc download address

"""
class MusicsearchAPI():
    def __init__(self):
        self.sysencode = "utf-8"#sys.getdefaultencoding()
        #self.__setcookie()
        self.PluginName = "百度音乐搜索插件Ex"
        self.PluginAuthor = "BBDXF"
        self.PluginVersion = "1.0.0"
        self.audioinfo = {
            "songid": "",
            "title": "",
            "artist": "",
            "album": "",
            "duration": "",
            "audiourl": "",
            "lrcurl": "",
            "picurl": "",
        }
        self.headers = {
            "Accept": "image/gif, */*",
            "Referer": "http://mp3.baidu.com",
            "Accept-Language": "zh-cn",
            "Content-Type": "application/x-www-form-urlencoded",
            #"Accept-Encoding": "gzip, deflate",
            "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
            "Host": "mp3.baidu.com",
            "Connection": "Keep-Alive",
            "Cache-Control": "no-cache"
        }
    def __searchdownloadurl(self):
        detail_url = 'http://ting.baidu.com/data/music/links?songIds={0}'.format(self.audioinfo['songid'])
        #request = urllib2.Request(detail_url, headers=self.headers)
        jsontxt = urllib2.urlopen(detail_url).read()
        #print jsontxt
        resp_js = json.loads(jsontxt)
        if resp_js['errorCode'] == 22000:
            result = resp_js['data']['songList'][0]
            self.audioinfo['artist'] = result['artistName']
            self.audioinfo['album'] = result['albumName']
            self.audioinfo['duration'] = result['time']
            self.audioinfo['audiourl'] = result['songLink']
            self.audioinfo['lrcurl'] = result['lrcLink']
            if len(result['lrcLink']) > 0:
                self.audioinfo['lrcurl'] = "http://ting.baidu.com" + result['lrcLink']
    def searchaduioinfo(self, **kwargs):
        """\
        SearchAduioInfo(**kwargs):
        :keyword title = 歌曲名 [, artist = 歌唱者 , album = 专辑]
        """
        title = kwargs.get("title", None)
        if title is None:
            return None
        stxt = title
        #if kwargs.get("artist") is not None:
        #    stxt = "{} {}".format(title, kwargs.get("artist"))
        search_url = "http://mp3.baidu.com/dev/api/?tn=getinfo&ct=0&word={0}&ie=utf-8&format=xml&callback=Pub.music.searchResult"\
            .format(urllib.quote(stxt))
        print(search_url)
        request = urllib2.Request(search_url, headers=self.headers)
        resp = urllib2.urlopen(request)
        xml_c = resp.read()
        #print(xml_c)
        domdoc = minidom.parseString(xml_c)
        if domdoc is not None:
            root = domdoc.documentElement
            if root.hasChildNodes():
                resele = root.getElementsByTagName('res')[0]
                songele = resele.getElementsByTagName('song')[0]
                song = songele.firstChild.nodeValue
                songidele = resele.getElementsByTagName('song_id')[0]
                songid = songidele.firstChild.nodeValue
                singerele = resele.getElementsByTagName('singer')[0]
                albumele = resele.getElementsByTagName('album')[0]
                #print albumele.toxml()
                picele = resele.getElementsByTagName('singerPicLarge')[0]
                self.audioinfo['title'] = song
                self.audioinfo['songid'] = songid
                if singerele.firstChild is not None:
                    self.audioinfo['artist'] = singerele.firstChild.nodeValue
                if albumele.firstChild is not None:
                    self.audioinfo['album'] = albumele.firstChild.nodeValue
                if picele.firstChild is not None:
                    self.audioinfo['picurl'] = picele.firstChild.nodeValue
                self.__searchdownloadurl()



def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
def test():
    p = MusicsearchAPI()
    """
    song_id = 190072
    detail_url = 'http://music.163.com/api/song/detail/?id={0}&ids=[{0}]'.format(song_id)
    resp = urllib2.urlopen(detail_url)
    song_js = json.loads(resp.read())
    rest = song_js['songs'][0]
    print convert(rest)
    return None
    """
    p.searchaduioinfo(title="黄昏", artist="周传雄")
    for k, v in p.audioinfo.items():
        print k, "=", v

if __name__ == "__main__": test()
