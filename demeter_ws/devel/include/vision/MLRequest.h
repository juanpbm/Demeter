// Generated by gencpp from file vision/MLRequest.msg
// DO NOT EDIT!


#ifndef VISION_MESSAGE_MLREQUEST_H
#define VISION_MESSAGE_MLREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <sensor_msgs/CompressedImage.h>

namespace vision
{
template <class ContainerAllocator>
struct MLRequest_
{
  typedef MLRequest_<ContainerAllocator> Type;

  MLRequest_()
    : Left_Img()  {
    }
  MLRequest_(const ContainerAllocator& _alloc)
    : Left_Img(_alloc)  {
  (void)_alloc;
    }



   typedef  ::sensor_msgs::CompressedImage_<ContainerAllocator>  _Left_Img_type;
  _Left_Img_type Left_Img;





  typedef boost::shared_ptr< ::vision::MLRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::vision::MLRequest_<ContainerAllocator> const> ConstPtr;

}; // struct MLRequest_

typedef ::vision::MLRequest_<std::allocator<void> > MLRequest;

typedef boost::shared_ptr< ::vision::MLRequest > MLRequestPtr;
typedef boost::shared_ptr< ::vision::MLRequest const> MLRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::vision::MLRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::vision::MLRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::vision::MLRequest_<ContainerAllocator1> & lhs, const ::vision::MLRequest_<ContainerAllocator2> & rhs)
{
  return lhs.Left_Img == rhs.Left_Img;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::vision::MLRequest_<ContainerAllocator1> & lhs, const ::vision::MLRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace vision

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::vision::MLRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vision::MLRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::vision::MLRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::vision::MLRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vision::MLRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vision::MLRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::vision::MLRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6f4385771f956025b0f88b88577f1991";
  }

  static const char* value(const ::vision::MLRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6f4385771f956025ULL;
  static const uint64_t static_value2 = 0xb0f88b88577f1991ULL;
};

template<class ContainerAllocator>
struct DataType< ::vision::MLRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "vision/MLRequest";
  }

  static const char* value(const ::vision::MLRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::vision::MLRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sensor_msgs/CompressedImage Left_Img\n"
"\n"
"================================================================================\n"
"MSG: sensor_msgs/CompressedImage\n"
"# This message contains a compressed image\n"
"\n"
"Header header        # Header timestamp should be acquisition time of image\n"
"                     # Header frame_id should be optical frame of camera\n"
"                     # origin of frame should be optical center of camera\n"
"                     # +x should point to the right in the image\n"
"                     # +y should point down in the image\n"
"                     # +z should point into to plane of the image\n"
"\n"
"string format        # Specifies the format of the data\n"
"                     #   Acceptable values:\n"
"                     #     jpeg, png\n"
"uint8[] data         # Compressed image buffer\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::vision::MLRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::vision::MLRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.Left_Img);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MLRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::vision::MLRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::vision::MLRequest_<ContainerAllocator>& v)
  {
    s << indent << "Left_Img: ";
    s << std::endl;
    Printer< ::sensor_msgs::CompressedImage_<ContainerAllocator> >::stream(s, indent + "  ", v.Left_Img);
  }
};

} // namespace message_operations
} // namespace ros

#endif // VISION_MESSAGE_MLREQUEST_H
