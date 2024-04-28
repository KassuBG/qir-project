import sys
from src.module.qir_runner import QIRRunner
from src.module.base_profile import BaseProfile

from qadence import QuantumCircuit

''' 
1. It imports the BaseProfile class from the src/qir_compiler module, which is used to 
    define the measurement basis.
2. It sets up the QIR compiler and runner.
3. It runs the teleportation circuit using the run method of the QIRRunner class.
4. It measures the output of the circuit using the measure method of the QIRRunner class, 
    and repeats the measurement 10 times.
5. It validates the results by counting the number of times each possible output is measured, 
    and checks if the expected output is among the measured outputs'''

def main():
    # Set up the QIR compiler and runner
    qir_compiler = QIRCompiler(QIRSpec('teleport.qir'))
    qir_runner = QIRRunner(qir_compiler)

    output = qir_runner.run()

    # Measure the output
    measurements = []
    for i in range(10):  
        measurement = qir_runner.measure(output)
        measurements.append(measurement)

    expected_output = '00'  # Expected output of the teleportation circuit
    counts = {}
    for measurement in measurements:
        if measurement in counts:
            counts[measurement] += 1
        else:
            counts[measurement] = 1

    if expected_output in counts:
        print(f"Teleportation successful! Measured {expected_output} {counts[expected_output]} times.")
    else:
        print("Teleportation failed. Did not measure the expected output.")

if __name__ == '__main__':
    main()