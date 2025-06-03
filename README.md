# Graph Coloring with Grover's Algorithm: Optimizing Time and Space Efficiencies
Graph coloring, an NP-complete problem, involves assigning colors to vertices of a graph such that no adjacent vertices share the same color. With an exponential time complexity of O(m^V), where m is the number of colors and V is the number of vertices, classical algorithms struggle due to high time complexity and memory consumption. This project leverages Grover's algorithm, a quantum search algorithm with O(√N) time complexity for unstructured searches, to solve the graph coloring problem on a map of the 50 states. In particular, this study compares time and space complexities in Qiskit and Q#. Qiskit achieved an average execution time of 14.94 seconds over 20 trials, outperforming Q# at 34.78 seconds. The classical recursive Python algorithm was slowest at 43.75 seconds. Furthermore, Q# demonstrated better space efficiency with a circuit depth of 26–38 gates compared to Qiskit’s 34–42 gates. This study’s finding suggest that Qiskit was the most efficient programming language in terms of time, but Q# had better space efficiency. Quantum approaches showed competitive performance against classical methods. Current quantum hardware limits testing on larger graphs, however. Future work could apply the method to US counties or other constraint satisfaction problems. Additional quantum languages, such as Cirq and Ocean, could be also tested in the future.

## How to Run (Qiskit):
1. Clone this repository onto Visual Studio Code
2. Click on the folder titled "QiskitGrovers"
3. Ensure you have the necessary dependencies downloaded (Python, numpy, qiskit, geopandas, matplotlib)
4. Run main.py
5. Output contains the colored map, total time, circuit depth, and an image of the Grover's circuit

## How to Run (Q#):
1. Clone this repository onto Visual Studio Code
2. Click on the folder titled "QSharpGrovers"
3. Download the extension "Microsoft Quantum Development Kit and Q# Extension Pack" on Visual Studio Code
4. Ensure you have the necessary dependencies downloaded (Q#, geopandas, matplotlib)
5. Click into the folder src
6. Run Main.qs and copy the output
7. Paste the output into the string 'input' in output.py
8. Run output.py to visualize the colored map
