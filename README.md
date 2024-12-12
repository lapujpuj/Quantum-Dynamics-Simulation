# Quantum Dynamics Simulation

This repository contains a project that implements numerical methods to simulate the dynamics of quantum systems using the time-dependent Schrödinger equation. The study explores both the stationary states and the time evolution of a particle in a one-dimensional potential. The project demonstrates the application of numerical techniques to solve quantum mechanical problems and visualizes the results for various potentials.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Results](#results)
7. [Acknowledgments](#acknowledgments)

## Introduction
Quantum mechanics is a fundamental theory of physics with applications in many scientific fields. This project focuses on solving the time-dependent Schrödinger equation to study:
- The stationary states of quantum systems.
- The dynamics of wave packets under various potentials.

The numerical methods implemented in this project include:
- **Finite Difference Method**: For spatial discretization.
- **Euler Method**: For basic time evolution.
- **Runge-Kutta Method (4th Order)**: For improved accuracy in time evolution.

## Features
- Simulates quantum systems with various potentials:
  - Infinite potential well
  - Double-well potential
  - Periodic potential
  - Harmonic potential
  - Electronic potential
- Visualizes stationary states and dynamic evolution of wavefunctions.
- Analyzes the stability and accuracy of numerical methods using error graphs.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/quantum-dynamics-simulation.git
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Solve the stationary Schrödinger equation:
   ```bash
   python resol.py
   ```
2. Simulate time evolution using the Euler method:
   ```bash
   python evolution_euler.py
   ```
3. Simulate time evolution using the Runge-Kutta method:
   ```bash
   python evolution_rk4.py
   ```
4. Visualize the results:
   - Stationary states with `resol.py`.
   - Time evolution graphs and animations with `evolution_euler.py` and `evolution_rk4.py`.

## Project Structure
- `resol.py`: Computes stationary states using finite difference methods.
- `euler.py`: Implements the Euler method for time evolution.
- `rk4.py`: Implements the 4th-order Runge-Kutta method for time evolution.
- `potentiels.py`: Defines various potential functions (e.g., harmonic, double-well).
- `deriv.py`: Computes wavefunction derivatives using finite difference.
- `visualization/`: Contains scripts for plotting and animation.

## Results
### Stationary States
- Probability densities and energy levels were computed for different potentials.
- The eigenfunctions show consistent physical patterns, including quantized energy levels and system symmetry preservation.

### Time Evolution
- The wave packet dynamics were studied in various potential environments.
- Error analysis demonstrated the superior accuracy of the Runge-Kutta method compared to the Euler method.

### Visualizations
- Animations of Gaussian wave packets in harmonic and electronic potentials.
- Mean position and energy error plots over time.

## Acknowledgments
This project was developed as part of the LU3PY126 FOAD course at Sorbonne Université, 2023. Special thanks to the professors and peers who supported this initiative.
