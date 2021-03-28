#!/usr/bin/env python3
import rospy 
import vision.srv as v 
import kinova_msgs.msg 
import time
import geometry_msgs.msg


def starting(req):
    i = False 
    if req.Action:
        print("the arm driver is ready to go")   
        return v.ActionResponse(True)
    else :
        print("something is wrong witht the arm driver")
        return v.actionResponse(False)

if __name__ == "__main__":
    rospy.init_node("Recognition", anonymous = True)
    stop_srv = rospy.ServiceProxy('stop', v.Action)
    reposition_srv = rospy.ServiceProxy('reposition', v.Reposition)
    harvest_srv = rospy.ServiceProxy('harvest',v.Reposition)
       
    s = rospy.Service('start', v.Action, starting)
    print("waiting for arm")
    rospy.wait_for_service("stop")
    time.sleep(5)

    print("telling the arm to stop")
    resp = stop_srv(True)   
    print(resp)
    if resp.Ack:
        print("the arm sttoped")
    else:
        print("something went wrong with the arm")
    time.sleep(5);
    
    print("telling the arm to cont")
    resp = stop_srv(False)   
    if resp.Ack:
        print("the arm cont")
    else:
        print("something went wrong with the arm")
    time.sleep(5)
    pos = geometry_msgs.msg.Point(x = 0.324862003, y = 0, z = 0.50927627)
    print("telling the arm move 153")
    resp = reposition_srv(pos)   
    if resp.Ack:
        print("moving the arm")
    else:
        print("something went wrong with the arm")

