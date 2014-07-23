#! /usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
from xml.dom import minidom
import re
"""\
user baidu music server to fetch audio info and lrc download address
this one only can fetch audiourl and lrcurl no others
"""
class MusicsearchAPI():
    def __init__(self):
        self.sysencode = "utf-8"#sys.getdefaultencoding()
        self.PluginName = "百度音乐搜索插件"
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
    def __parsexmlcn(self, strxml):
        """\
        strxml old text read from url
        替换xml文本中的编码，并且转化为utf8返回
        """
        strutf8 = strxml.decode(encoding="GB2312").encode("utf-8")
        repaser = re.compile("encoding=\"gb2312\"")
        return repaser.sub("encoding=\"utf-8\"", strutf8, 1)
    def __searchdownloadurl(self):
        detail_url = 'http://music.163.com/api/song/detail/?id={0}&ids=[{0}]'.format(self.audioinfo['songid'])
    def searchaduioinfo(self, **kwargs):
        """\
        SearchAduioInfo(**kwargs):
        :keyword title = 歌曲名 [, artist = 歌唱者 , album = 专辑]
        """
        title = kwargs.get("title", None)
        if title is None:
            return None
        search_url = "http://box.zhangmen.baidu.com/x?op=12&count=1&"
        params = {
            'title': title,
        }
        params = urllib.urlencode(params)
        artist = kwargs.get('artist')
        if artist:
            params += "$$" + urllib.quote(artist) + "$$"
        else:
            params += "$$"
        print(search_url+params)
        request = urllib2.Request(search_url+params, headers=self.headers)
        resp = urllib2.urlopen(request)
        xml_c = self.__parsexmlcn(resp.read())
        domdoc = minidom.parseString(xml_c)
        if domdoc is not None:
            root = domdoc.documentElement
            counteles = root.getElementsByTagName('count')
            counts = counteles[0].firstChild.nodeValue
            if counts > 0:
                urlele = root.getElementsByTagName('url')[0]
                encodeele = urlele.getElementsByTagName('encode')[0]
                decodeele = urlele.getElementsByTagName('decode')[0]
                url1 = encodeele.firstChild.nodeValue
                url1 = url1[0:url1.rfind('/')+1]
                url2 = decodeele.firstChild.nodeValue
                self.audioinfo['audiourl'] = url1 + url2
                lrcele = urlele.getElementsByTagName('lrcid')[0]
                lrcid = int(lrcele.firstChild.nodeValue)
                if lrcid > 0:
                    self.audioinfo['lrcurl'] = "http://box.zhangmen.baidu.com/bdlrc/{0}/{1}.lrc".format(lrcid//100, lrcid)

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
    p.searchaduioinfo(title="小苹果")
    for k, v in p.audioinfo.items():
        print k, "=", v

if __name__ == "__main__": test()
