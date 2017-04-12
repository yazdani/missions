#!/usr/bin/env python  
import roslib
roslib.load_manifest('gps_tracks')
import rospy
import math
import tf
import rospkg
import sys 
from subprocess import Popen
import re
import string 

if __name__ == '__main__':
    rospy.init_node('tf')
  
    rospack = rospkg.RosPack()
    path = rospack.get_path('gps_tracks')
    path = path+"/csv/tracks.csv"
    f = open(path, 'r')
    collector = f.readlines()
    collection = []
  
    for index in collector:
        elems = index.split('\n')
        collection.append(elems[0])
  
    br = tf.TransformBroadcaster()

    while not rospy.is_shutdown():
        for index in collection:
            elems = index.split(',')
            if elems[0] == "By-foot":
                text = "gps_waypoints"
            else:
                text = "gps_routes"
            values=(float(elems[1]),float(elems[2]),float(elems[3]))
            br.sendTransform(values,
                             (0.0, 0.0, 0.0, 1.0),
                             rospy.Time(),
                             "map",
                             text)

