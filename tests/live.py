# -*- coding: utf-8 -*-
# website: https://loovien.github.io
# author: luowen<bigpao.luo@gmail.com>
# time: 2018/9/29 21:41
# desc:

import ffmpeg
import unittest
import os


class TestLive(unittest.TestCase):

    def test_stream(self):
        """ffmpeg.input("C:/Users/luowen/Downloads/Video/live.mp4").output(
            # "rtmp://yfrtmpup.cdn.zhanqi.tv/zqlive/292805_9nl9E?k=b5011c6f70ec674aa218fea8612159c6&t=5f69c003",
            "xxx.mp4",
            codec="copy", format="flv").run()"""
        from_url = "C:/Users/luowen/Downloads/Video/live.mp4"
        to_url = "rtmp://alrtmpup.cdn.zhanqi.tv/zqlive/292805_9nl9E?k=0fa549b60407bc4b12a94be6ba2fd8d8&t=5f69cd34"

        cmd = "ffmpeg -re -i {} -codec copy -f flv {}".format(from_url, to_url)

        os.system(cmd)