#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2016 Dr. Klaus Schaefer.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

import numpy,time
from gnuradio import gr

def clip( value, minimum, maximum):
    value  =min( value ,maximum)
    value  =max( value ,minimum)
    return value

class dmx(gr.sync_block):
    """
    dmx driver sink block 9 channels
    RGB LEDs are configured to be on DMX channels 1/2/3 and 7/8/9 and 13/14/15
    Par56LED switch settings group one:10000000 group two:11100000 group three:10110000
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="dmx",
            in_sig=[numpy.float32,numpy.float32,numpy.float32,numpy.float32,numpy.float32,numpy.float32,numpy.float32,numpy.float32,numpy.float32],
            out_sig=None)
        self.pipe = open('/dev/dmx1','w',0)

#       worker=TimedTask()
 
    def put2dmx( self,  r1=0, g1=0, b1=0, r2=0,  g2=0,  b2=0, r3=0,  g3=0,  b3=0):
        s='\0%c%c%c\0\0\0%c%c%c\0\0\0%c%c%c\0\0\0' % (r1, g1, b1, r2, g2, b2, r3, g3, b3)
        self.pipe.write(s)

    def work(self, input_items, output_items):
        size=len(input_items[:][0])
        use = min( size, 32)
#       print('size={} using={}'.format( size, use))
        for k in range( 0, use):

            r1  =clip( int((input_items[0][k])*255),0,255)
            g1  =clip( int((input_items[1][k])*255),0,255)
            b1  =clip( int((input_items[2][k])*255),0,255)

            r2  =clip( int((input_items[3][k])*255),0,255)
            g2  =clip( int((input_items[4][k])*255),0,255)
            b2  =clip( int((input_items[5][k])*255),0,255)

            r3  =clip( int((input_items[6][k])*255),0,255)
            g3  =clip( int((input_items[7][k])*255),0,255)
            b3  =clip( int((input_items[8][k])*255),0,255)

#           print('rgb={} {} {} {} {} {} {} {} {}'.format( r1, g1, b1, r2, g2, b2, r3, g3, b3))

            self.put2dmx( r1, g1, b1, r2, g2, b2, r3, g3, b3)
            time.sleep(0.0195)

        return( use)
    