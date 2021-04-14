// Generated by gencpp from file vision/RepositionResponse.msg
// DO NOT EDIT!


#ifndef VISION_MESSAGE_REPOSITIONRESPONSE_H
#define VISION_MESSAGE_REPOSITIONRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace vision
{
template <class ContainerAllocator>
struct RepositionResponse_
{
  typedef RepositionResponse_<ContainerAllocator> Type;

  RepositionResponse_()
    : Ack(false)  {
    }
  RepositionResponse_(const ContainerAllocator& _alloc)
    : Ack(false)  {
  (void)_alloc;
    }



   typedef uint8_t _Ack_type;
  _Ack_type Ack;





  typedef boost::shared_ptr< ::vision::RepositionResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::vision::RepositionResponse_<ContainerAllocator> const> ConstPtr;

}; // struct RepositionResponse_

typedef ::vision::RepositionResponse_<std::allocator<void> > RepositionResponse;

typedef boost::shared_ptr< ::vision::RepositionResponse > RepositionResponsePtr;
typedef boost::shared_ptr< ::vision::RepositionResponse const> RepositionResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::vision::RepositionResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::vision::RepositionResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::vision::RepositionResponse_<ContainerAllocator1> & lhs, const ::vision::RepositionResponse_<ContainerAllocator2> & rhs)
{
  return lhs.Ack == rhs.Ack;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::vision::RepositionResponse_<ContainerAllocator1> & lhs, const ::vision::RepositionResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace vision

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::vision::RepositionResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vision::RepositionResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::vision::RepositionResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::vision::RepositionResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vision::RepositionResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vision::RepositionResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::vision::RepositionResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "62ae02024e7918414d8b66756f34a1c6";
  }

  static const char* value(const ::vision::RepositionResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x62ae02024e791841ULL;
  static const uint64_t static_value2 = 0x4d8b66756f34a1c6ULL;
};

template<class ContainerAllocator>
struct DataType< ::vision::RepositionResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "vision/RepositionResponse";
  }

  static const char* value(const ::vision::RepositionResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::vision::RepositionResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool Ack\n"
"\n"
;
  }

  static const char* value(const ::vision::RepositionResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::vision::RepositionResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.Ack);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RepositionResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::vision::RepositionResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::vision::RepositionResponse_<ContainerAllocator>& v)
  {
    s << indent << "Ack: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.Ack);
  }
};

} // namespace message_operations
} // namespace ros

#endif // VISION_MESSAGE_REPOSITIONRESPONSE_H
