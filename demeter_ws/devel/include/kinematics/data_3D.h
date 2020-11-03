// Generated by gencpp from file kinematics/data_3D.msg
// DO NOT EDIT!


#ifndef KINEMATICS_MESSAGE_DATA_3D_H
#define KINEMATICS_MESSAGE_DATA_3D_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Point.h>
#include <geometry_msgs/Point.h>
#include <geometry_msgs/Point.h>

namespace kinematics
{
template <class ContainerAllocator>
struct data_3D_
{
  typedef data_3D_<ContainerAllocator> Type;

  data_3D_()
    : center()
    , top()
    , bottom()  {
    }
  data_3D_(const ContainerAllocator& _alloc)
    : center(_alloc)
    , top(_alloc)
    , bottom(_alloc)  {
  (void)_alloc;
    }



   typedef  ::geometry_msgs::Point_<ContainerAllocator>  _center_type;
  _center_type center;

   typedef  ::geometry_msgs::Point_<ContainerAllocator>  _top_type;
  _top_type top;

   typedef  ::geometry_msgs::Point_<ContainerAllocator>  _bottom_type;
  _bottom_type bottom;





  typedef boost::shared_ptr< ::kinematics::data_3D_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::kinematics::data_3D_<ContainerAllocator> const> ConstPtr;

}; // struct data_3D_

typedef ::kinematics::data_3D_<std::allocator<void> > data_3D;

typedef boost::shared_ptr< ::kinematics::data_3D > data_3DPtr;
typedef boost::shared_ptr< ::kinematics::data_3D const> data_3DConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::kinematics::data_3D_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::kinematics::data_3D_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::kinematics::data_3D_<ContainerAllocator1> & lhs, const ::kinematics::data_3D_<ContainerAllocator2> & rhs)
{
  return lhs.center == rhs.center &&
    lhs.top == rhs.top &&
    lhs.bottom == rhs.bottom;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::kinematics::data_3D_<ContainerAllocator1> & lhs, const ::kinematics::data_3D_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace kinematics

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::kinematics::data_3D_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::kinematics::data_3D_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::kinematics::data_3D_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::kinematics::data_3D_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::kinematics::data_3D_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::kinematics::data_3D_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::kinematics::data_3D_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6ac37e820af93783df7652e7b435f796";
  }

  static const char* value(const ::kinematics::data_3D_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6ac37e820af93783ULL;
  static const uint64_t static_value2 = 0xdf7652e7b435f796ULL;
};

template<class ContainerAllocator>
struct DataType< ::kinematics::data_3D_<ContainerAllocator> >
{
  static const char* value()
  {
    return "kinematics/data_3D";
  }

  static const char* value(const ::kinematics::data_3D_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::kinematics::data_3D_<ContainerAllocator> >
{
  static const char* value()
  {
    return "geometry_msgs/Point center\n"
"geometry_msgs/Point top\n"
"geometry_msgs/Point bottom\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
;
  }

  static const char* value(const ::kinematics::data_3D_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::kinematics::data_3D_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.center);
      stream.next(m.top);
      stream.next(m.bottom);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct data_3D_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::kinematics::data_3D_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::kinematics::data_3D_<ContainerAllocator>& v)
  {
    s << indent << "center: ";
    s << std::endl;
    Printer< ::geometry_msgs::Point_<ContainerAllocator> >::stream(s, indent + "  ", v.center);
    s << indent << "top: ";
    s << std::endl;
    Printer< ::geometry_msgs::Point_<ContainerAllocator> >::stream(s, indent + "  ", v.top);
    s << indent << "bottom: ";
    s << std::endl;
    Printer< ::geometry_msgs::Point_<ContainerAllocator> >::stream(s, indent + "  ", v.bottom);
  }
};

} // namespace message_operations
} // namespace ros

#endif // KINEMATICS_MESSAGE_DATA_3D_H
