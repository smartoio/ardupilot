import arducopter

def unit_test(mavproxy, mav):
    '''A scripted flight plan'''
    if ( 
        arducopter.calibrate_level(mavproxy, mav) and
        arducopter.arm_motors(mavproxy, mav) and  
        arducopter.takeoff(mavproxy,mav, alt_min=30, takeoff_throttle=1510) and
        arducopter.change_alt(mavproxy, mav, alt_min=60) and
        arducopter.change_alt(mavproxy, mav, alt_min=20)
    ):
        return True
    return False

