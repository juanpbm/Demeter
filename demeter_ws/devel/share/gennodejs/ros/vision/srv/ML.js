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

class MLRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Left_Img = null;
    }
    else {
      if (initObj.hasOwnProperty('Left_Img')) {
        this.Left_Img = initObj.Left_Img
      }
      else {
        this.Left_Img = new sensor_msgs.msg.CompressedImage();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MLRequest
    // Serialize message field [Left_Img]
    bufferOffset = sensor_msgs.msg.CompressedImage.serialize(obj.Left_Img, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MLRequest
    let len;
    let data = new MLRequest(null);
    // Deserialize message field [Left_Img]
    data.Left_Img = sensor_msgs.msg.CompressedImage.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += sensor_msgs.msg.CompressedImage.getMessageSize(object.Left_Img);
    return length;
  }

  static datatype() {
    // Returns string type for a service object
    return 'vision/MLRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6f4385771f956025b0f88b88577f1991';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    sensor_msgs/CompressedImage Left_Img
    
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
    const resolved = new MLRequest(null);
    if (msg.Left_Img !== undefined) {
      resolved.Left_Img = sensor_msgs.msg.CompressedImage.Resolve(msg.Left_Img)
    }
    else {
      resolved.Left_Img = new sensor_msgs.msg.CompressedImage()
    }

    return resolved;
    }
};

class MLResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Percentage = null;
    }
    else {
      if (initObj.hasOwnProperty('Percentage')) {
        this.Percentage = initObj.Percentage
      }
      else {
        this.Percentage = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MLResponse
    // Serialize message field [Percentage]
    bufferOffset = _serializer.float32(obj.Percentage, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MLResponse
    let len;
    let data = new MLResponse(null);
    // Deserialize message field [Percentage]
    data.Percentage = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'vision/MLResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '618fd4053c63b8f5b6197bff24518c8d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 Percentage
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MLResponse(null);
    if (msg.Percentage !== undefined) {
      resolved.Percentage = msg.Percentage;
    }
    else {
      resolved.Percentage = 0.0
    }

    return resolved;
    }
};

module.exports = {
  Request: MLRequest,
  Response: MLResponse,
  md5sum() { return '4972fcc8dd87e24ab9b33086558f9dc5'; },
  datatype() { return 'vision/ML'; }
};
