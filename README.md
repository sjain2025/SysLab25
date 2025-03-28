# Graph Coloring with Grover's Algorithm: Optimizing Time and Space Efficiencies
Graph coloring, a NP-complete problem that involves assigning colors to vertices of a graph such that no two adjacent vertices share the same color, is computationally intensive for traditional recursive approaches. However, advances in quantum computing show promise for reducing the search time complexity by offering a quadratic speedup over classical brute-force strategies. This project leverages Grover's algorithm, a quantum search method, to solve the graph coloring problem on a map of the 50 states while comparing time and space efficiencies between various programming languages like Python (Qiskit) and Q#.

### How to Run
To test this code, clone this repository to Visual Studio Code and run the Python file **main.py**. It will output a PNG of the Grover's circuit (grovers_circuit.png) and a figure of the 50 states, generated using GeoPandas and Matplotlib.

Please ensure that you have the following dependencies downloaded before running the file:

**NumPy:** pip install numpy

**Qiskit:** pip install qiskit

**Matplotlib:** pip install matplotlib

**GeoPandas:** pip install geopandas
