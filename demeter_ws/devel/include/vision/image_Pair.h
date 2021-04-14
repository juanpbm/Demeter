// Generated by gencpp from file vision/image_Pair.msg
// DO NOT EDIT!


#ifndef VISION_MESSAGE_IMAGE_PAIR_H
#define VISION_MESSAGE_IMAGE_PAIR_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <sensor_msgs/CompressedImage.h>
#include <sensor_msgs/CompressedImage.h>

namespace vision
{
template <class ContainerAllocator>
struct image_Pair_
{
  typedef image_Pair_<ContainerAllocator> Type;

  image_Pair_()
    : coordinates()
    , Left_Img()
    , Right_Img()  {
      coordinates.assign(0.0);
  }
  image_Pair_(const ContainerAllocator& _alloc)
    : coordinates()
    , Left_Img(_alloc)
    , Right_Img(_alloc)  {
  (void)_alloc;
      coordinates.assign(0.0);
  }



   typedef boost::array<float, 4>  _coordinates_type;
  _coordinates_type coordinates;

   typedef  ::sensor_msgs::CompressedImage_<ContainerAllocator>  _Left_Img_type;
  _Left_Img_type Left_Img;

   typedef  ::sensor_msgs::CompressedImage_<ContainerAllocator>  _Right_Img_type;
  _Right_Img_type Right_Img;





  typedef boost::shared_ptr< ::vision::image_Pair_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::vision::image_Pair_<ContainerAllocator> const> ConstPtr;

}; // struct image_Pair_

typedef ::vision::image_Pair_<std::allocator<void> > image_Pair;

typedef boost::shared_ptr< ::vision::image_Pair > image_PairPtr;
typedef boost::shared_ptr< ::vision::image_Pair const> image_PairConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::vision::image_Pair_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::vision::image_Pair_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::vision::image_Pair_<ContainerAllocator1> & lhs, const ::vision::image_Pair_<ContainerAllocator2> & rhs)
{
  return lhs.coordinates == rhs.coordinates &&
    lhs.Left_Img == rhs.Left_Img &&
    lhs.Right_Img == rhs.Right_Img;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::vision::image_Pair_<ContainerAllocator1> & lhs, const ::vision::image_Pair_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace vision

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::vision::image_Pair_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vision::image_Pair_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::vision::image_Pair_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::vision::image_Pair_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vision::image_Pair_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vision::image_Pair_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::vision::image_Pair_<ContainerAllocator> >
{
  static const char* value()
  {
    return "3be3bcf9d563c8bf7eb1783df2858352";
  }

  static const char* value(const ::vision::image_Pair_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x3be3bcf9d563c8bfULL;
  static const uint64_t static_value2 = 0x7eb1783df2858352ULL;
};

template<class ContainerAllocator>
struct DataType< ::vision::image_Pair_<ContainerAllocator> >
{
  static const char* value()
  {
    return "vision/image_Pair";
  }

  static const char* value(const ::vision::image_Pair_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::vision::image_Pair_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32[4] coordinates\n"
"sensor_msgs/CompressedImage Left_Img\n"
"sensor_msgs/CompressedImage Right_Img\n"
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

  static const char* value(const ::vision::image_Pair_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::vision::image_Pair_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.coordinates);
      stream.next(m.Left_Img);
      stream.next(m.Right_Img);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct image_Pair_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::vision::image_Pair_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::vision::image_Pair_<ContainerAllocator>& v)
  {
    s << indent << "coordinates[]" << std::endl;
    for (size_t i = 0; i < v.coordinates.size(); ++i)
    {
      s << indent << "  coordinates[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.coordinates[i]);
    }
    s << indent << "Left_Img: ";
    s << std::endl;
    Printer< ::sensor_msgs::CompressedImage_<ContainerAllocator> >::stream(s, indent + "  ", v.Left_Img);
    s << indent << "Right_Img: ";
    s << std::endl;
    Printer< ::sensor_msgs::CompressedImage_<ContainerAllocator> >::stream(s, indent + "  ", v.Right_Img);
  }
};

} // namespace message_operations
} // namespace ros

#endif // VISION_MESSAGE_IMAGE_PAIR_H
