import matplotlib.pyplot as plt
import numpy as np

# Task 1 — Mathematical Function Visualization
x = np.linspace(-10, 10, 200)

y1 = x
y2 = x**2
y3 = np.sin(x)
y4 = np.exp(-0.1 * x) * np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y1, linestyle="-", label="y = x")
ax.plot(x, y2, linestyle="--", label="y = x²")
ax.plot(x, y3, linestyle="-.", label="y = sin(x)")
ax.plot(x, y4, linestyle=":", label="y = e^(-0.1x) · cos(x)")

ax.set_title("Mathematical Function Visualization")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("function_plot.png", dpi=150)
plt.close()


# Task 2 — Own Equation
# Mixed equation: cubic trend + damped oscillation
# y = 0.03x³ - 0.4x² + sin(x) + 2
x2 = np.linspace(-10, 10, 300)
y_own = 0.03 * x2**3 - 0.4 * x2**2 + np.sin(x2) + 2

fig, ax = plt.subplots()
ax.plot(x2, y_own, linestyle="-", label="y = 0.03x³ − 0.4x² + sin(x) + 2")

ax.set_title("Own Equation: Cubic + Oscillation")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("own_equation.png", dpi=150)
plt.close()


# Task 3 — Student Score Data Visualization
students = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]
midterm = np.array([85, 72, 90, 66, 78, 92, 60, 74, 88, 95])
final = np.array([80, 70, 94, 68, 75, 90, 65, 72, 84, 96])
total = 0.4 * midterm + 0.6 * final

# A — Scatter plot
fig, ax = plt.subplots()
ax.scatter(midterm, final, zorder=3)
for i, s in enumerate(students):
    ax.annotate(s, (midterm[i], final[i]), textcoords="offset points", xytext=(6, 4))
ax.set_title("Midterm vs Final Scores")
ax.set_xlabel("Midterm Score")
ax.set_ylabel("Final Score")
ax.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("score_scatter.png", dpi=150)
plt.close()

# B — Histogram of total scores
fig, ax = plt.subplots()
ax.hist(total, bins=6)
ax.set_title("Distribution of Total Scores")
ax.set_xlabel("Total Score")
ax.set_ylabel("Number of Students")
ax.grid(True, axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("score_histogram.png", dpi=150)
plt.close()

# C — Bar chart of each student's total score
fig, ax = plt.subplots()
bars = ax.bar(students, total)
ax.bar_label(bars, fmt="%.1f", padding=3)
ax.set_title("Total Score per Student")
ax.set_xlabel("Student")
ax.set_ylabel("Total Score")
ax.set_ylim(0, max(total) * 1.12)
ax.grid(True, axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("score_bar_chart.png", dpi=150)
plt.close()


# Task 4 — Best-Fit Line / Simple Prediction
slope, intercept = np.polyfit(midterm, final, 1)

x_line = np.linspace(midterm.min() - 5, midterm.max() + 5, 200)
y_line = slope * x_line + intercept

fig, ax = plt.subplots()
ax.scatter(midterm, final, zorder=3, label="Actual data")
ax.plot(
    x_line, y_line, label=f"Best-fit: final = {slope:.2f}×midterm + {intercept:.2f}"
)
for i, s in enumerate(students):
    ax.annotate(s, (midterm[i], final[i]), textcoords="offset points", xytext=(6, 4))

ax.set_title("Midterm → Final Score Prediction")
ax.set_xlabel("Midterm Score")
ax.set_ylabel("Final Score")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("score_prediction.png", dpi=150)
plt.close()

print("Prediction Examples ---")
for m in [50, 75, 100]:
    pred = slope * m + intercept
    print(f"  Midterm = {m:3d}  →  Predicted final = {pred:.2f}")
