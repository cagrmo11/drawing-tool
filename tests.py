#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 22:18:58 2019

@author: moran
"""

import unittest
import numpy.testing as npt
import tools as t
import stylus as st
import numpy as np

 
class TestDrawCanvas(unittest.TestCase):
    def test_can_draw_canvas(self):
        """
        Test that it can draw a 20x4 canvas
        """
        w = 20
        h = 4
        check_array = np.array([['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-', '-'],
 ['|', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '|'],
 ['|', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '|'],
 ['|', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '|'],
 ['|', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '|'],
 ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-', '-']],dtype='str')
        npt.assert_equal(t.drawCanvas(w, h),check_array)


class TestDrawLine(unittest.TestCase):
    def test_can_draw_h_line(self):
        """
        Test that it can draw a horiztonal line
        """
        w = 20
        h = 4
        test_canvas = t.drawCanvas(w, h)
        check_array = np.array([['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-', '-'],
 ['|', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '|'],
 ['|', 'x', 'x', 'x', 'x', 'x', 'x', '', '', '', '', '', '', '', '', '', '', '', '', '', '','|'],
 ['|', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '|'],
 ['|', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '|'],
 ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-']],dtype='str')
        npt.assert_equal(st.drawLine(test_canvas,1,2,6,2),check_array)
    
    def test_can_draw_v_line(self):
        """
        Test that it can draw a vertical line
        """
        w = 20
        h = 4
        test_canvas = t.drawCanvas(w, h)
        check_array = np.array([['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-', '-'],
 ['|', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '|'],
 ['|', '', '', '', '', '', 'x', '', '', '', '', '', '', '', '', '', '', '', '', '', '','|'],
 ['|', '', '', '', '', '', 'x', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '|'],
 ['|', '', '', '', '', '', 'x', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '|'],
 ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-']],dtype='str')
        npt.assert_equal(st.drawLine(test_canvas,6,3,6,4),check_array)

class TestDrawRectangle(unittest.TestCase):
    def test_can_draw_rectangle(self):
        """
        Test that it can draw a rectangle
        """
        w = 20
        h = 4
        test_canvas = t.drawCanvas(w, h)
        check_array = np.array([['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-', '-'],
 ['|', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'x', 'x', 'x', 'x', 'x', '|'],
 ['|', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'x', '', '', '', 'x','|'],
 ['|', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'x', 'x', 'x', 'x', 'x', '|'],
 ['|', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '|'],
 ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-']],dtype='str')
        npt.assert_equal(st.drawRectangle(test_canvas,16,1,20,3),check_array)

class TestDrawBackground(unittest.TestCase):
    def test_can_draw_background(self):
        """
        Test that it can color in the background correctly
        """
        w = 20
        h = 4
        test_canvas = t.drawCanvas(w, h)
        test_canvas = st.drawRectangle(test_canvas,16,1,20,3)
        check_array = np.array([['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
 ['|','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','x','x','x','x','x','|'],
 ['|','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','x','','','','x','|'],
 ['|','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','x','x','x','x','x','|'],
 ['|','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','|'],
 ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']],dtype='str')
        npt.assert_equal(st.drawBackground(test_canvas,10,3,'o'),check_array)
    

if __name__ == '__main__':
    unittest.main()