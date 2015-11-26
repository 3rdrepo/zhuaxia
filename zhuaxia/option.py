# -*- coding:utf-8 -*-
import log
LOG = log.get_logger("zxLogger")

class Option(object):
    """
    a class containing user given options
    """
    def __init__(self):
        self.is_hq = False
        self.need_proxy_pool = False
        self.proxies=None
        self.dl_lyric = False
        self.inFile = ''
        self.inUrl = ''
        self.incremental_dl= False

    def debug_me(self):
        LOG.debug( "hq:"+str(self.is_hq))
        LOG.debug( "inFile:"+self.inFile)
        LOG.debug( "inUrl:"+self.inUrl)
        LOG.debug( "needProxyPool:"+ str(self.need_proxy_pool))
        LOG.debug( "dl_lyric:"+str(self.dl_lyric))
        LOG.debug( "incremental_dl:"+str(self.incremental_dl))
