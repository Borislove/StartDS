import pandas as pd
import matplotlib.pyplot as plt

"""
dct = {
    'Method A': [
        1.0, 5.0, 10.0, 20.0, 50.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0,
        150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 450.0, 500.0, 550.0, 600.0,
        650.0, 700.0, 750.0, 800.0, 850.0, 900.0, 950.0, 1000.0
    ],
    'Method B': [
        8.0, 16.0, 30.0, 24.0, 39.0, 54.0, 40.0, 68.0, 72.0, 62.0, 122.0, 80.0,
        181.0, 259.0, 275.0, 380.0, 320.0, 434.0, 479.0, 587.0, 626.0, 648.0,
        738.0, 766.0, 793.0, 851.0, 871.0, 957.0, 1001.0, 960.0
    ]
}
"""""
dct = {
    'Рост': [-1, 0, 5, -3, 6, 7, 0],
    'Вес': [5, 7, 3, 8, 4, 6, 5]
}
df = pd.DataFrame(dct)

# Formatting options for plots
A = 5  # Want figures to be A5
plt.rc('figure', figsize=[46.82 * .5 ** (.5 * A), 33.11 * .5 ** (.5 * A)])
# plt.rc('text', usetex=True)  # Use LaTeX
# plt.rc('font', family='serif')  # Use a serif font
# plt.rc('text.latex', preamble=r'\usepackage{textgreek}')  # Load Greek letters

# Create plot
ax = plt.axes()
ax.scatter(df['Рост'], df['Вес'], c='k', s=20, alpha=0.6, marker='o')
# Labels
ax.set_title('The Raw Data')
ax.set_xlabel('Рост')
ax.set_ylabel('Вес')
# Get axis limits
left, right = ax.get_xlim()
# Set axis limits
ax.set_xlim(0, right)
ax.set_ylim(0, right)
# Set aspect ratio
ax.set_aspect('equal')
# Show plot
plt.show()
