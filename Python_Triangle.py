#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2022, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

import time
from xarm.wrapper import XArmAPI

class TriangleDrawer(object):
    """Class for drawing a triangle with xArm"""
    def __init__(self, robot):
        self._arm = robot
        self._tcp_speed = 200
        self._tcp_acc = 10000
        self._robot_init()

    def _robot_init(self):
        self._arm.clean_warn()
        self._arm.clean_error()
        self._arm.motion_enable(True)
        self._arm.set_mode(0)
        self._arm.set_state(0)
        time.sleep(1)

    def draw_triangle(self):
        """Draw a triangle by moving to three points"""
        try:
            # Move to the starting position
            self._arm.move_gohome()

            # Coordinates for the triangle
            points = [
                [300.0, 100.0, 200.0, 180.0, 0.0, 0.0],  # First point
                [400.0, 200.0, 200.0, 180.0, 0.0, 0.0],  # Second point
                [500.0, 100.0, 200.0, 180.0, 0.0, 0.0]   # Third point
            ]

            # Draw the triangle
            for i in range(len(points)):
                next_point = points[(i + 1) % len(points)]
                code = self._arm.set_position(*points[i], speed=self._tcp_speed, mvacc=self._tcp_acc, radius=-1.0, wait=True)
                if code != 0:
                    print(f"Error moving to point {points[i]}. Error code: {code}")
                    return
                self._arm.set_position(*next_point, speed=self._tcp_speed, mvacc=self._tcp_acc, radius=-1.0, wait=True)
                if code != 0:
                    print(f"Error moving to point {next_point}. Error code: {code}")
                    return

            # Return to home
            self._arm.move_gohome()

        except Exception as e:
            print(f"Exception occurred: {e}")

if __name__ == '__main__':
    arm = XArmAPI('192.168.1.239')
    triangle_drawer = TriangleDrawer(arm)
    triangle_drawer.draw_triangle()
