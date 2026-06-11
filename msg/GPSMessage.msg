# GPSMessage
# GPS position data with local coordinate offsets.
# Topic: /gps

std_msgs/Header header

float64 latitude  # Geographic latitude [deg]
float64 longitude  # Geographic longitude [deg]
float64 altitude  # Altitude above sea level [m]

float64 east_offset  # East (X) offset from map origin [m]
float64 north_offset  # North (Y) offset from map origin [m]
int16 status  # GPS status indicator
