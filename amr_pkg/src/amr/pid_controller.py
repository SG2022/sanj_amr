#!/usr/bin/env python
#
# /* Copyright (C) InventoRobotics - All Rights Reserved
#  * Unauthorized copying of this file, via any medium is strictly prohibited
#  * Proprietary and confidential
#  * Written for InventoRobotics, 2019
#  */
#
import numpy as np
import rospy

class PidController:
    def __init__(self, p, i, d, imax, cmax,cmin):
        self.p = p
        self.i = i
        self.d = d
        self.error_prev = 0
        self.integ_now = 0
        self.ctrl_max = cmax
        self.ctrl_min = cmin
        self.integ_max = imax
        self.is_saturate = False

    def calculate(self, error):
        self.error = error
        if not self.is_saturate:
            self.integ_now += self.error
        self.p_t = self.p * error
        self.i_t = self.i * self.integ_now
        self.d_t = 0
        self.ctrl_out = self.p_t + self.i_t + self.d_t 
        #rospy.logwarn("integral :{}".format(self.integ_now))

        if abs(self.integ_now) > self.integ_max:
            self.is_saturate = True
        else:
            self.is_saturate = False
        if abs(self.ctrl_out) > self.ctrl_max:
            self.ctrl_out = self.ctrl_max * np.sign(self.ctrl_out)
            self.is_saturate = True
        if abs(self.ctrl_out) < self.ctrl_min:
            self.ctrl_out = self.ctrl_min * np.sign(self.ctrl_out)
            self.is_saturate = True
        else:
            self.is_saturate = False
        self.error_prev = self.error

        return self.ctrl_out
