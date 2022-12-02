# Bassam Ali - Student 21047697 #

import pint

from pint import UnitRegistry

ureg = UnitRegistry()




#print(voltage.to('volt'))
#print(voltage.to('millivolt'))

class ohm_law:

    resistance = 5.0 * ureg.ohm
    current = 2.5 * ureg.milliampere
    voltage = (resistance * current).to('volt')
    serial_resistance = [100, 50, 220, 330]

    def voltage(current, resistance):
        voltage = (current * resistance)
        #print(voltage.to('volt'))
        #print(voltage.to('millivolt'))
        return voltage
        

    def resistance(voltage, current):
        resistance = voltage / current
        #print(resistance.to('Ohms'))
        return resistance

    def current(voltage, resistance):
        current = voltage / resistance
        #print(i.to('ampere'))
        #print(i.to('milliampere'))
        return current

    def serial_resistance(serial_resistance):
        sum = 0
        j = 0
        for x in serial_resistance:
            sum = sum + serial_resistance[j]
            j = j + 1
        return sum

