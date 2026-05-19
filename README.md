# Math Visualization Assignment

## Project Overview
This project is a Python-based data visualization assignment that plots mathematical functions and analyzes student score data.

It covers function plotting, custom equations, score distribution, and simple linear prediction using NumPy and Matplotlib.

---

## Objectives
- Visualize common mathematical functions in one figure
- Plot a custom mixed equation
- Analyze student score data through scatter, histogram, and bar charts
- Apply linear regression to predict final scores from midterm scores

---

## Features
- Multi-function plot with different line styles
- Custom cubic + oscillation equation plot
- Scatter plot of midterm vs final scores
- Histogram of total score distribution
- Bar chart of each student's total score
- Best-fit line with printed score predictions

---

## Tools and Technologies
- Python 3.11
- Git
- GitHub

---

## Environment
This project was made using:
- Visual Studio Code (recommended)

---

## Requirements

### Imports Used
```python
import numpy as np
import matplotlib.pyplot as plt
```

Install dependencies:
```bash
pip install numpy matplotlib
```

---

## How to Run
```bash
python3 math_visualization.py
```

All plots are saved as .png files in the same directory.

---

## Screenshots

### Mathematical Function Visualization
![Function Plot](function_plot.png)

### Midterm → Final Score Prediction
![Score Prediction](score_prediction.png)

---

## Reflection

**How does visualization help us understand mathematical functions and data?**
Visualization helps us understand relationships and patterns harvestable from data, but hard to detect in raw numbers. It also eases comparing multiple functions since the results are shown together in a single graph.

**Which plot was most useful in this assignment and why?**
The best-fit line scatter plot (Task 4) was the most useful. It actually does something with the data instead of just showing it to the viewer.

**What is the role of NumPy and Matplotlib in your project?**
NumPy handles all the math — generating evenly spaced x values with linspace, computing array operations, and fitting the regression line with polyfit. Matplotlib takes those arrays and turns them into clean, labeled plots that can be saved as image files.
