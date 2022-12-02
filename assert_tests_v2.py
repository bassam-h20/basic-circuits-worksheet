import task5_v3
from task5_v3 import ohm_law

v = 30
i = 3
r = 50
sr = [100, 50, 220, 330]

def test_voltage(current, resistance, exp):
    assert ohm_law.voltage(current, resistance) == exp, print("\nVoltage test did not pass, should be:",current * resistance)
    print("Voltage test passed")
    return ohm_law.voltage(current, resistance)
    
def test_resistance(voltage, current, exp):
    assert ohm_law.resistance(voltage, current) == exp, print("\nResistance test did not pass, should be:",voltage / current)
    print("Ohm test passed")
    return ohm_law.resistance(voltage, current)

def test_current(voltage, resistance, exp):
    assert ohm_law.current(voltage, resistance) == exp, print("\nCurrent test did not pass, should be:",voltage / resistance)
    print("Current test passed")
    return ohm_law.current(voltage, resistance)

def test_serial_resistance(serial_resistance, exp):
    assert ohm_law.serial_resistance(serial_resistance) == exp, print("Serial Resistance test did not pass, should be the total of:",serial_resistance)
    print("Serial Resistance test passed")
    return ohm_law.serial_resistance(serial_resistance)



if __name__ == "__main__":
    print(test_voltage(i ,r, 150), "Volts\n")

    print(test_resistance(v, i, 10), "Ohms\n")

    print(test_current(v, r, 0.6), "Amps\n")

    print(test_serial_resistance(sr, 800), "Total Ohms\n")
