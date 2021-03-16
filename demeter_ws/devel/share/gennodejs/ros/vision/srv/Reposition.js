// Auto-generated. Do not edit!

// (in-package vision.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------


//-----------------------------------------------------------

class RepositionRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Location = null;
    }
    else {
      if (initObj.hasOwnProperty('Location')) {
        this.Location = initObj.Location
      }
      else {
        this.Location = new geometry_msgs.msg.Point();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RepositionRequest
    // Serialize message field [Location]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.Location, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RepositionRequest
    let len;
    let data = new RepositionRequest(null);
    // Deserialize message field [Location]
    data.Location = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a service object
    return 'vision/RepositionRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '42bda7d7fa622f066e545e9d3f38c04e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    geometry_msgs/Point Location 
    
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
    const resolved = new RepositionRequest(null);
    if (msg.Location !== undefined) {
      resolved.Location = geometry_msgs.msg.Point.Resolve(msg.Location)
    }
    else {
      resolved.Location = new geometry_msgs.msg.Point()
    }

    return resolved;
    }
};

class RepositionResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Ack = null;
    }
    else {
      if (initObj.hasOwnProperty('Ack')) {
        this.Ack = initObj.Ack
      }
      else {
        this.Ack = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RepositionResponse
    // Serialize message field [Ack]
    bufferOffset = _serializer.bool(obj.Ack, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RepositionResponse
    let len;
    let data = new RepositionResponse(null);
    // Deserialize message field [Ack]
    data.Ack = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'vision/RepositionResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '62ae02024e7918414d8b66756f34a1c6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool Ack
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RepositionResponse(null);
    if (msg.Ack !== undefined) {
      resolved.Ack = msg.Ack;
    }
    else {
      resolved.Ack = false
    }

    return resolved;
    }
};

module.exports = {
  Request: RepositionRequest,
  Response: RepositionResponse,
  md5sum() { return '47be5df2ac38fbdb1ce8731a7f11ea4b'; },
  datatype() { return 'vision/Reposition'; }
};
