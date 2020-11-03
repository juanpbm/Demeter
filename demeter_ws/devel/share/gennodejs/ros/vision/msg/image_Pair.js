// Auto-generated. Do not edit!

// (in-package vision.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let sensor_msgs = _finder('sensor_msgs');

//-----------------------------------------------------------

class image_Pair {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.center = null;
      this.top = null;
      this.bottom = null;
      this.left_Img = null;
      this.right_Img = null;
    }
    else {
      if (initObj.hasOwnProperty('center')) {
        this.center = initObj.center
      }
      else {
        this.center = new Array(2).fill(0);
      }
      if (initObj.hasOwnProperty('top')) {
        this.top = initObj.top
      }
      else {
        this.top = new Array(2).fill(0);
      }
      if (initObj.hasOwnProperty('bottom')) {
        this.bottom = initObj.bottom
      }
      else {
        this.bottom = new Array(2).fill(0);
      }
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
    // Serializes a message object of type image_Pair
    // Check that the constant length array field [center] has the right length
    if (obj.center.length !== 2) {
      throw new Error('Unable to serialize array field center - length must be 2')
    }
    // Serialize message field [center]
    bufferOffset = _arraySerializer.float32(obj.center, buffer, bufferOffset, 2);
    // Check that the constant length array field [top] has the right length
    if (obj.top.length !== 2) {
      throw new Error('Unable to serialize array field top - length must be 2')
    }
    // Serialize message field [top]
    bufferOffset = _arraySerializer.float32(obj.top, buffer, bufferOffset, 2);
    // Check that the constant length array field [bottom] has the right length
    if (obj.bottom.length !== 2) {
      throw new Error('Unable to serialize array field bottom - length must be 2')
    }
    // Serialize message field [bottom]
    bufferOffset = _arraySerializer.float32(obj.bottom, buffer, bufferOffset, 2);
    // Serialize message field [left_Img]
    bufferOffset = sensor_msgs.msg.CompressedImage.serialize(obj.left_Img, buffer, bufferOffset);
    // Serialize message field [right_Img]
    bufferOffset = sensor_msgs.msg.CompressedImage.serialize(obj.right_Img, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type image_Pair
    let len;
    let data = new image_Pair(null);
    // Deserialize message field [center]
    data.center = _arrayDeserializer.float32(buffer, bufferOffset, 2)
    // Deserialize message field [top]
    data.top = _arrayDeserializer.float32(buffer, bufferOffset, 2)
    // Deserialize message field [bottom]
    data.bottom = _arrayDeserializer.float32(buffer, bufferOffset, 2)
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
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'vision/image_Pair';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b1eeb80bf925ed72664782dd8a9603fe';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32[2] center
    float32[2] top
    float32[2] bottom
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
    const resolved = new image_Pair(null);
    if (msg.center !== undefined) {
      resolved.center = msg.center;
    }
    else {
      resolved.center = new Array(2).fill(0)
    }

    if (msg.top !== undefined) {
      resolved.top = msg.top;
    }
    else {
      resolved.top = new Array(2).fill(0)
    }

    if (msg.bottom !== undefined) {
      resolved.bottom = msg.bottom;
    }
    else {
      resolved.bottom = new Array(2).fill(0)
    }

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

module.exports = image_Pair;
