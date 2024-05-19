# HydraulicsTermProject
This project uses Python to solve for flow rates and head losses in a pipe network. It employs numerical methods to balance continuity and energy equations, ensuring accurate fluid distribution. The solution leverages scipy.optimize for iterative calculations, providing an efficient analysis of complex water distribution systems.


# Pipe Network Analysis

This project uses Python to analyze flow rates and head losses in a pipe network. It employs numerical methods to balance continuity and energy equations, ensuring accurate fluid distribution within the network.

## Overview

The code solves a system of nonlinear equations representing the fluid dynamics in a pipe network. Using the scipy.optimize library, it iteratively calculates flow rates and head losses, providing a detailed analysis of the network.

## Features

- *Flow Rate Calculation*: Computes the flow rates in each pipe of the network.
- *Head Loss Estimation*: Estimates the head (pressure) at each node based on the flow rates and pipe characteristics.
- *Numerical Methods*: Utilizes the root function from scipy.optimize for solving nonlinear equations.
- *Flexible Setup*: Easy to adapt for different pipe network configurations and parameters.

## Prerequisites

Ensure you have the following Python libraries installed:

- numpy
- scipy

You can install them using pip:
```bash
pip install numpy scipy
