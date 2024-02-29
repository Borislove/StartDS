from scipy.stats import pearsonr

x, y = [-1, 0, 5, -3, 6, 7, 0], [5, 7, 3, 8, 4, 6, 5]

res = pearsonr(x, y)

print(f'{res[0]:.2f}')
