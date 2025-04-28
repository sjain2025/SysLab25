import numpy as np
from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
import geopandas as gpd
import time

input_dict = {
 "Alabama": [
  "Florida",
  "Georgia",
  "Mississippi",
  "Tennessee"
 ],
 "Alaska": [],
 "Arizona": [
  "California",
  "Colorado",
  "Nevada",
  "New Mexico",
  "Utah"
 ],
 "Arkansas": [
  "Louisiana",
  "Mississippi",
  "Missouri",
  "Oklahoma",
  "Tennessee",
  "Texas"
 ],
 "California": [
  "Arizona",
  "Nevada",
  "Oregon"
 ],
 "Colorado": [
  "Arizona",
  "Kansas",
  "Nebraska",
  "New Mexico",
  "Oklahoma",
  "Utah",
  "Wyoming"
 ],
 "Connecticut": [
  "Massachusetts",
  "New York",
  "Rhode Island"
 ],
 "Delaware": [
  "Maryland",
  "New Jersey",
  "Pennsylvania"
 ],
 "Florida": [
  "Alabama",
  "Georgia"
 ],
 "Georgia": [
  "Alabama",
  "Florida",
  "North Carolina",
  "South Carolina",
  "Tennessee"
 ],
 "Hawaii": [],
 "Idaho": [
  "Montana",
  "Nevada",
  "Oregon",
  "Utah",
  "Washington",
  "Wyoming"
 ],
 "Illinois": [
  "Indiana",
  "Iowa",
  "Michigan",
  "Kentucky",
  "Missouri",
  "Wisconsin"
 ],
 "Indiana": [
  "Illinois",
  "Kentucky",
  "Michigan",
  "Ohio"
 ],
 "Iowa": [
  "Illinois",
  "Minnesota",
  "Missouri",
  "Nebraska",
  "South Dakota",
  "Wisconsin"
 ],
 "Kansas": [
  "Colorado",
  "Missouri",
  "Nebraska",
  "Oklahoma"
 ],
 "Kentucky": [
  "Illinois",
  "Indiana",
  "Missouri",
  "Ohio",
  "Tennessee",
  "Virginia",
  "West Virginia"
 ],
 "Louisiana": [
  "Arkansas",
  "Mississippi",
  "Texas"
 ],
 "Maine": [
  "New Hampshire"
 ],
 "Maryland": [
  "Delaware",
  "Pennsylvania",
  "Virginia",
  "West Virginia"
 ],
 "Massachusetts": [
  "Connecticut",
  "New Hampshire",
  "New York",
  "Rhode Island",
  "Vermont"
 ],
 "Michigan": [
  "Illinois",
  "Indiana",
  "Minnesota",
  "Ohio",
  "Wisconsin"
 ],
 "Minnesota": [
  "Iowa",
  "Michigan",
  "North Dakota",
  "South Dakota",
  "Wisconsin"
 ],
 "Mississippi": [
  "Alabama",
  "Arkansas",
  "Louisiana",
  "Tennessee"
 ],
 "Missouri": [
  "Arkansas",
  "Illinois",
  "Iowa",
  "Kansas",
  "Kentucky",
  "Nebraska",
  "Oklahoma",
  "Tennessee"
 ],
 "Montana": [
  "Idaho",
  "North Dakota",
  "South Dakota",
  "Wyoming"
 ],
 "Nebraska": [
  "Colorado",
  "Iowa",
  "Kansas",
  "Missouri",
  "South Dakota",
  "Wyoming"
 ],
 "Nevada": [
  "Arizona",
  "California",
  "Idaho",
  "Oregon",
  "Utah"
 ],
 "New Hampshire": [
  "Maine",
  "Massachusetts",
  "Vermont"
 ],
 "New Jersey": [
  "Delaware",
  "New York",
  "Pennsylvania"
 ],
 "New Mexico": [
  "Arizona",
  "Colorado",
  "Oklahoma",
  "Texas",
  "Utah"
 ],
 "New York": [
  "Connecticut",
  "Massachusetts",
  "New Jersey",
  "Pennsylvania",
  "Rhode Island",
  "Vermont"
 ],
 "North Carolina": [
  "Georgia",
  "South Carolina",
  "Tennessee",
  "Virginia"
 ],
 "North Dakota": [
  "Minnesota",
  "Montana",
  "South Dakota"
 ],
 "Ohio": [
  "Indiana",
  "Kentucky",
  "Michigan",
  "Pennsylvania",
  "West Virginia"
 ],
 "Oklahoma": [
  "Arkansas",
  "Colorado",
  "Kansas",
  "Missouri",
  "New Mexico",
  "Texas"
 ],
 "Oregon": [
  "California",
  "Idaho",
  "Nevada",
  "Washington"
 ],
 "Pennsylvania": [
  "Delaware",
  "Maryland",
  "New Jersey",
  "New York",
  "Ohio",
  "West Virginia"
 ],
 "Rhode Island": [
  "Connecticut",
  "Massachusetts",
  "New York"
 ],
 "South Carolina": [
  "Georgia",
  "North Carolina"
 ],
 "South Dakota": [
  "Iowa",
  "Minnesota",
  "Montana",
  "Nebraska",
  "North Dakota",
  "Wyoming"
 ],
 "Tennessee": [
  "Alabama",
  "Arkansas",
  "Georgia",
  "Kentucky",
  "Mississippi",
  "Missouri",
  "North Carolina",
  "Virginia"
 ],
 "Texas": [
  "Arkansas",
  "Louisiana",
  "New Mexico",
  "Oklahoma"
 ],
 "Utah": [
  "Arizona",
  "Colorado",
  "Idaho",
  "Nevada",
  "New Mexico",
  "Wyoming"
 ],
 "Vermont": [
  "Massachusetts",
  "New Hampshire",
  "New York"
 ],
 "Virginia": [
  "Kentucky",
  "Maryland",
  "North Carolina",
  "Tennessee",
  "West Virginia"
 ],
 "Washington": [
  "Idaho",
  "Oregon"
 ],
 "West Virginia": [
  "Kentucky",
  "Maryland",
  "Ohio",
  "Pennsylvania",
  "Virginia"
 ],
 "Wisconsin": [
  "Illinois",
  "Iowa",
  "Michigan",
  "Minnesota"
 ],
 "Wyoming": [
  "Colorado",
  "Idaho",
  "Montana",
  "Nebraska",
  "South Dakota",
  "Utah"
 ]
}

states = list(input_dict.keys())

edges = []
for state, neighbors in input_dict.items():
    for neighbor in neighbors:
        edges.append((state, neighbor))
edges = list(set(edges))

def createCircuitConnection(vertices, edges, num_colors, circuit):
    color_bits = int(np.log2(num_colors))
    for state1, state2 in edges:
        state1idx = vertices.index(state1)
        state2idx = vertices.index(state2)
        for i in range(color_bits):
            circuit.cx(state1idx * color_bits + i, state2idx * color_bits + i)

def diffuser(n_qubits):
    circuit = QuantumCircuit(n_qubits)
    circuit.h(range(n_qubits))
    circuit.x(range(n_qubits))
    circuit.h(n_qubits - 1)
    circuit.mcx(list(range(n_qubits - 1)), n_qubits - 1)
    circuit.h(n_qubits - 1)
    circuit.x(range(n_qubits))
    circuit.h(range(n_qubits))
    return circuit

def oracle(vertices, edges, num_colors):
    color_bits = int(np.log2(num_colors))
    n_qubits = len(vertices) * color_bits
    grover_circuit = QuantumCircuit(n_qubits)
    grover_circuit.h(range(n_qubits))
    createCircuitConnection(vertices, edges, num_colors, grover_circuit)
    grover_circuit.h(range(n_qubits))
    return grover_circuit

def grover_circuit(vertices, edges, num_colors):
    color_bits = int(np.log2(num_colors))
    n_qubits = len(vertices) * color_bits
    circuit = QuantumCircuit(n_qubits)
    circuit.h(range(n_qubits))
    oracle_circuit = oracle(vertices, edges, num_colors)
    circuit.compose(oracle_circuit, inplace=True)
    diffuser_circuit = diffuser(n_qubits)
    circuit.compose(diffuser_circuit, inplace=True)
    return circuit

def is_safe(state, color, colored_dict, states_dict):
    for neighbor in states_dict[state]:
        if neighbor in colored_dict and colored_dict[neighbor] == color:
            return False
    return True

def color_states_helper(states_dict, colors, colored_dict, state_list, index):
    if index == len(state_list):
        return True
    state = state_list[index]
    for color in colors:
        if is_safe(state, color, colored_dict, states_dict):
            colored_dict[state] = color
            if color_states_helper(states_dict, colors, colored_dict, state_list, index + 1):
                return True
            del colored_dict[state]
    return False

def color_states(states_dict, colors):
    colored_dict = {}
    state_list = list(states_dict.keys())
    if color_states_helper(states_dict, colors, colored_dict, state_list, 0): return colored_dict
    else: raise ValueError("No solution")

def interpret_measurement():
    start_time = time.process_time()
    colors = ["red", "green", "blue", "yellow"]
    state_colors = color_states(input_dict, colors)
    us_states = gpd.read_file('QiskitGrovers/ne_110m_admin_1_states_provinces.shp')
    us_states = us_states[us_states['iso_a2'] == 'US']
    us_states['color'] = us_states['name'].map(state_colors)
    us_states['color'].fillna('gray', inplace=True)
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    us_states.boundary.plot(ax=ax, color="black", linewidth=0.5)
    us_states.plot(ax=ax, color=us_states['color'], edgecolor='black')
    end_time = time.process_time()
    print(f"Time: {end_time - start_time} secs")
    plt.show()

def circuit_depth(circuit):
    return circuit.depth()

num_colors = 4
grover_circuit = grover_circuit(states, edges, num_colors)

depth = circuit_depth(grover_circuit)
print(f"Circuit depth: {depth}")

fig = grover_circuit.draw(output='mpl', scale=0.1)
fig.savefig('QiskitGrovers/grovers_circuit.png')
plt.close(fig)

interpret_measurement()