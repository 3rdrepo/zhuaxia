# -*- coding:utf-8 -*-
head_xm                          = u'[xia]'
head_163                         = u'[163]'

fmt_all_finished                 = u' All jobs are finished.'
fmt_dl_lyric_start               = u' Start downloading lyrics...'

fmt_dl_header                    = u' Save to :[%s] | Threads Pool:[%d]\n'
fmt_dl_progress                  = u'Progress [%d/%d]:'
fmt_dl_last_finished             = u'  Latest %d finished task:\n'

fmt_quality_fallback             = u'cannot find 128kbps song (%s). Try to get lower quality resource'
fmt_init_song                    = u'start init song [%s]'
fmt_err_song_parse               = u'song url cannot be parsed/downloaded: [%s]'
fmt_init_song_ok                 = u'song initialized [%s]'
fmt_init_album                   = u'start init album [%s]'
fmt_create_album_dir             = u'creating album dir [%s]'
fmt_dl_album_cover               = u'downloading cover of album [%s]'
fmt_save_album_desc              = u'downloading description of album [%s]'
fmt_init_fav                     = u'start init user favorite [%s]'
fmt_parse_song_url               = u'parsing song url [%s]'
fmt_init_fav_ok                  = u'user favorite initialized [%s]'
fmt_init_collect                 = u'start init collection [%s]'
fmt_init_collect_ok              = u'collection initialized [%s]'
fmt_init_artist                  = u'start init artist TopSong [%s]'
fmt_init_artist_ok               = u' artist TopSong initialized [%s]'
dl_128kbps_xm                    = u' downloading without login. quality: 128kbps'
fmt_login_ok_xm                  = u'[Login] user: %s (id:%s) login successful'
login_xm                         = u'[xia] login...'
login_err_xm                     = u' login failed, skip login, using 128kbps quality.'
short_xm                         = head_xm + ' '
short_163                        = head_163 + ' '
fmt_parsing                      = u'Parsing: "%s" ..... [%s] %s'
fmt_has_song_nm                  = u'has %d songs.'
fmt_single_song                  = u'[song] %s'
init_proxypool                   = u'Init proxy pool'
fmt_init_proxypool_done          = u'proxy pool:[%d] init done'
fmt_total_dl_nm                  = u' Total downloading tasks: %d \n Downloading starts in 3 seconds'
no_dl_task                       = u' No downloading task, exit.'
fmt_skip_unknown_url             = u' Skipping unknown url [%s].'
fmt_xm_unknown_url               = u'%s [xia]unknown url [%s].'
fmt_163_unknow_url               = u'%s [163]unknown url [%s].'
song                             = u'song'
album                            = u'album'
playlist                         = u'playlist'
artistTop                        = u'artist TopN'
collection                       = u'collection'
favorite                         = u'user favorite'
warning_many_collections         = u'[xia] parsing can take some time if user favorite has many songs. Please stand by.'
fmt_links_in_file                = u' file contains urls: %d'

experimental                     = u'-p is an experimental option: '
proxypool                        = u'auto fetching proxy from proxy pool. Since zhuaxia does not check the speed of proxy, downloading could be slow or unstable.'
ver_text                         = u'zhuaxia '
help_info                        = u""" %(cyan)s
    zhuaxia -- download mp3 music from [xiami.com] and [music.163.com]%(clear)s

    [%(uline)sCONFIG FILE:%(clear)s]   $HOME/.zhuaxia/zhuaxia.conf

    [%(uline)sOPTIONS%(clear)s]
        %(bold)s-H%(clear)s : prefer High Quality(320kbps),
            > xiami <
                - xiami vip user email/password should be set in config
                - user should set HQ on xiami vip setting page
                - if any above requirements was not satisfied, 128kbps will be taken
            > 163 <
                - no special requirement

        %(bold)s-p%(clear)s : auto choose proxy from proxy pool (experimental option)
            when frequency of request to target host is high enough, host could ban the client
            for some time. zhuaxia will auto take proxy from pool. However this may make
            downloading slow or unstable.

        %(bold)s-h%(clear)s ：show help
        %(bold)s-l%(clear)s ：download lyric (lrc format)
        %(bold)s-f%(clear)s ：download from url file
        %(bold)s-v%(clear)s ：show version information

    [%(uline)sUSAGE%(clear)s]

        %(bold)szx [OPTION] <URL>%(clear)s
            : auto recognize and download the given url resource, supports:
                - [xm] song, album, favorite, collection, artist TopN
                - [163]song, album, list, artist topN
            example:
                zx "http://www.xiami.com/space/lib-song/u/25531126"
                zx "http://music.163.com/song?id = 27552647"

        %(bold)szx [OPTION] -f <file>%(clear)s
            : download from url file. one url per line. The urls could be 163 and xm mixed. Example:
              $ cat /tmp/foo.txt
                http://music.163.com/artist?id=5345
                http://www.xiami.com/song/1772130322
                http://music.163.com/album?id=2635059
                http://www.xiami.com/album/32449

              $ zx -f /tmp/foo.txt
        """

