import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/pheonix/E-yantra-2024/colcon_ws/install/ur5_control'
