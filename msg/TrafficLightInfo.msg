# TrafficLightInfo
# Traffic light information returned by the TrafficLightInfo service.
# Service: /Morai_TLSrv (response)

std_msgs/Header header

string idx  # Unique index of the traffic light
int16 status  # Light status (1: Red, 4: Yellow, 16: Green, 32: Green left arrow, -1: not lit)
