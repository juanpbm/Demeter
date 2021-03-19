#!/usr/bin/env python3
import rospy 
import vision.srv as v 
import kinova_msgs.msg 
def starting(req):
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
    rospy.spin()
    print("telling the arm to stop")
    resp = stop_srv(True)
    
    if resp.Ack:
        print("the arm sttoped")
    else:
        print("something went wrong with the arm")

