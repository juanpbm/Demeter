// Auto-generated. Do not edit!

// (in-package vision.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class ActionRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Action = null;
    }
    else {
      if (initObj.hasOwnProperty('Action')) {
        this.Action = initObj.Action
      }
      else {
        this.Action = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ActionRequest
    // Serialize message field [Action]
    bufferOffset = _serializer.bool(obj.Action, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ActionRequest
    let len;
    let data = new ActionRequest(null);
    // Deserialize message field [Action]
    data.Action = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'vision/ActionRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '9dda7191b6bdf4f8e7537ec0b272b31c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool Action 
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ActionRequest(null);
    if (msg.Action !== undefined) {
      resolved.Action = msg.Action;
    }
    else {
      resolved.Action = false
    }

    return resolved;
    }
};

class ActionResponse {
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
    // Serializes a message object of type ActionResponse
    // Serialize message field [Ack]
    bufferOffset = _serializer.bool(obj.Ack, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ActionResponse
    let len;
    let data = new ActionResponse(null);
    // Deserialize message field [Ack]
    data.Ack = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'vision/ActionResponse';
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
    const resolved = new ActionResponse(null);
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
  Request: ActionRequest,
  Response: ActionResponse,
  md5sum() { return '48a9460ec0cc64685337f3762768aa1d'; },
  datatype() { return 'vision/Action'; }
};
