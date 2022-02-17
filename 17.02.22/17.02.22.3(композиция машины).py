from typing import List

class Engine:
    def __init__(self, power, volume, weight, q):
        self.power = power
        self.volume = volume
        self.weight = weight
        self.q = q

class Wheel:
    def __init__(self, weight, mfr, radius, q):
        self.weight = weight
        self.mfr = mfr
        self.radius = radius
        self.q = q

class Steering:
    def __init__(self, shape, mfr, weight, q):
        self.shape = shape
        self.mfr = mfr
        self.weight = weight
        self.q = q
        self.orientation = 'right' if mfr in ['eng', 'jpn'] else 'left'

class Car:
    def __init__(self, eng:Engine, whs:List[Wheel], st:Steering):
        w_all = sum([item.weight for item in [eng, st].extend(whs)])
        self.hp =   self.power / w_all
        self.steering_wheel = st
        self.wheels = whs
        self.engine = eng
        q_whs = sum([wh.q for wh in whs]) / len(whs)
        self.q = (eng.q + q_whs + st.q)