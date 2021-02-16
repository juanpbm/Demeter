// Auto-generated. Do not edit!

// (in-package vision.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let sensor_msgs = _finder('sensor_msgs');

//-----------------------------------------------------------


//-----------------------------------------------------------

class RecRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.left_Img = null;
      this.right_Img = null;
    }
    else {
      if (initObj.hasOwnProperty('left_Img')) {
        this.left_Img = initObj.left_Img
      }
      else {
        this.left_Img = new sensor_msgs.msg.CompressedImage();
      }
      if (initObj.hasOwnProperty('right_Img')) {
        this.right_Img = initObj.right_Img
      }
      else {
        this.right_Img = new sensor_msgs.msg.CompressedImage();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RecRequest
    // Serialize message field [left_Img]
    bufferOffset = sensor_msgs.msg.CompressedImage.serialize(obj.left_Img, buffer, bufferOffset);
    // Serialize message field [right_Img]
    bufferOffset = sensor_msgs.msg.CompressedImage.serialize(obj.right_Img, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RecRequest
    let len;
    let data = new RecRequest(null);
    // Deserialize message field [left_Img]
    data.left_Img = sensor_msgs.msg.CompressedImage.deserialize(buffer, bufferOffset);
    // Deserialize message field [right_Img]
    data.right_Img = sensor_msgs.msg.CompressedImage.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += sensor_msgs.msg.CompressedImage.getMessageSize(object.left_Img);
    length += sensor_msgs.msg.CompressedImage.getMessageSize(object.right_Img);
    return length;
  }

  static datatype() {
    // Returns string type for a service object
    return 'vision/RecRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e217f270e4c39c7cd696ab11a0bcae77';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    sensor_msgs/CompressedImage left_Img
    sensor_msgs/CompressedImage right_Img
    
    ================================================================================
    MSG: sensor_msgs/CompressedImage
    # This message contains a compressed image
    
    Header header        # Header timestamp should be acquisition time of image
                         # Header frame_id should be optical frame of camera
                         # origin of frame should be optical center of camera
                         # +x should point to the right in the image
                         # +y should point down in the image
                         # +z should point into to plane of the image
    
    string format        # Specifies the format of the data
                         #   Acceptable values:
                         #     jpeg, png
    uint8[] data         # Compressed image buffer
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RecRequest(null);
    if (msg.left_Img !== undefined) {
      resolved.left_Img = sensor_msgs.msg.CompressedImage.Resolve(msg.left_Img)
    }
    else {
      resolved.left_Img = new sensor_msgs.msg.CompressedImage()
    }

    if (msg.right_Img !== undefined) {
      resolved.right_Img = sensor_msgs.msg.CompressedImage.Resolve(msg.right_Img)
    }
    else {
      resolved.right_Img = new sensor_msgs.msg.CompressedImage()
    }

    return resolved;
    }
};

class RecResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.coordinates = null;
    }
    else {
      if (initObj.hasOwnProperty('coordinates')) {
        this.coordinates = initObj.coordinates
      }
      else {
        this.coordinates = new Array(4).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RecResponse
    // Check that the constant length array field [coordinates] has the right length
    if (obj.coordinates.length !== 4) {
      throw new Error('Unable to serialize array field coordinates - length must be 4')
    }
    // Serialize message field [coordinates]
    bufferOffset = _arraySerializer.float32(obj.coordinates, buffer, bufferOffset, 4);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RecResponse
    let len;
    let data = new RecResponse(null);
    // Deserialize message field [coordinates]
    data.coordinates = _arrayDeserializer.float32(buffer, bufferOffset, 4)
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a service object
    return 'vision/RecResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e0e2db642e35a0d781e9ef60e0750101';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32[4] coordinates 
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RecResponse(null);
    if (msg.coordinates !== undefined) {
      resolved.coordinates = msg.coordinates;
    }
    else {
      resolved.coordinates = new Array(4).fill(0)
    }

    return resolved;
    }
};

module.exports = {
  Request: RecRequest,
  Response: RecResponse,
  md5sum() { return '524aec0a2d224648b866e7ced15102d4'; },
  datatype() { return 'vision/Rec'; }
};
