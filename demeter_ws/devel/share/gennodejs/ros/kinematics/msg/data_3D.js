// Auto-generated. Do not edit!

// (in-package kinematics.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class data_3D {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.center = null;
      this.top = null;
      this.bottom = null;
    }
    else {
      if (initObj.hasOwnProperty('center')) {
        this.center = initObj.center
      }
      else {
        this.center = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('top')) {
        this.top = initObj.top
      }
      else {
        this.top = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('bottom')) {
        this.bottom = initObj.bottom
      }
      else {
        this.bottom = new geometry_msgs.msg.Point();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type data_3D
    // Serialize message field [center]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.center, buffer, bufferOffset);
    // Serialize message field [top]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.top, buffer, bufferOffset);
    // Serialize message field [bottom]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.bottom, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type data_3D
    let len;
    let data = new data_3D(null);
    // Deserialize message field [center]
    data.center = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [top]
    data.top = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [bottom]
    data.bottom = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 72;
  }

  static datatype() {
    // Returns string type for a message object
    return 'kinematics/data_3D';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6ac37e820af93783df7652e7b435f796';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    geometry_msgs/Point center
    geometry_msgs/Point top
    geometry_msgs/Point bottom
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new data_3D(null);
    if (msg.center !== undefined) {
      resolved.center = geometry_msgs.msg.Point.Resolve(msg.center)
    }
    else {
      resolved.center = new geometry_msgs.msg.Point()
    }

    if (msg.top !== undefined) {
      resolved.top = geometry_msgs.msg.Point.Resolve(msg.top)
    }
    else {
      resolved.top = new geometry_msgs.msg.Point()
    }

    if (msg.bottom !== undefined) {
      resolved.bottom = geometry_msgs.msg.Point.Resolve(msg.bottom)
    }
    else {
      resolved.bottom = new geometry_msgs.msg.Point()
    }

    return resolved;
    }
};

module.exports = data_3D;
