#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Attribute Sink Example
# Author: Travis Collins
# GNU Radio version: 3.10.11.0

from gnuradio import blocks
import pmt
from gnuradio import blocks, gr
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import iio
import attr_sink_example_msg_source as msg_source  # embedded python module
import threading




class attr_sink_example(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Attribute Sink Example", catch_exceptions=True)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Blocks
        ##################################################

        self.iio_attr_sink_0 = iio.attr_sink("ip:192.168.2.1", "ad9361-phy", "voltage0", 0, False)
        self.blocks_message_strobe_0_0 = blocks.message_strobe(msg_source.msg_dic, 1000)
        self.blocks_message_debug_0 = blocks.message_debug(True, gr.log_levels.info)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0_0, 'strobe'), (self.blocks_message_debug_0, 'print'))
        self.msg_connect((self.blocks_message_strobe_0_0, 'strobe'), (self.iio_attr_sink_0, 'attr'))





def main(top_block_cls=attr_sink_example, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()
    tb.flowgraph_started.set()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
