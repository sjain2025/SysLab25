# Graph Coloring with Grover's Algorithm: Optimizing Time and Space Efficiencies
Graph coloring, a NP-complete problem that involves assigning colors to vertices of a graph such that no two adjacent vertices share the same color, is computationally intensive for traditional recursive approaches. However, advances in quantum computing show promise for reducing the search time complexity by offering a quadratic speedup over classical brute-force strategies. This project leverages Grover's algorithm, a quantum search method, to solve the graph coloring problem on a map of the 50 states while comparing time and space efficiencies between various programming languages like Python (Qiskit) and Q#.

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
