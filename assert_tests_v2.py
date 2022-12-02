import task5_v3
from task5_v3 import ohm_law

v = 30
i = 3
r = 50
sr = [100, 50, 220, 330]

def test_voltage(current, resistance):
    assert ohm_law.voltage(current, resistance)
    print("Voltage test passed")
    return ohm_law.voltage(current, resistance)
    
def test_resistance(voltage, current):
    assert ohm_law.resistance(voltage, current)
    print("Ohm test passed")
    return ohm_law.resistance(voltage, current)

def test_current(voltage, resistance):
    assert ohm_law.current(voltage, resistance)
    print("Current test passed")
    return ohm_law.current(voltage, resistance)

def test_serial_resistance(serial_resistance):
    assert ohm_law.serial_resistance(serial_resistance)
    print("Serial Resistance test passed")
    return ohm_law.serial_resistance(serial_resistance)

print(test_voltage(i ,r), "Volts\n")

print(test_resistance(v, i), "Ohms\n")

print(test_current(v, r), "Amps\n")

print(test_serial_resistance(sr), "Ohms\n")
