import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# import statsmodels.api as sm

df_pol = pd.read_csv('spotify/dataset/data.csv', sep=',')
df_genre = pd.read_csv('spotify/dataset/data_by_genres.csv', sep=',')

a = df_pol['popularity']
b = df_genre['genres']

frames = [a, b]

result = pd.concat(frames, axis=1)

# print(result)
print(pd.get_dummies(result))

x = pd.get_dummies(result)['genres_21st century classical']
y = pd.get_dummies(result)['popularity']
m,b = np.polyfit(x, y, 1)

print(m)
print(b)


model = LinearRegression()
model.fit(x, y)

# predict y from the data
x_new = np.linspace(0, 30, 100)
y_new = model.predict(x_new[:, np.newaxis])

# plot the results
plt.figure(figsize=(4, 3))
ax = plt.axes()
ax.scatter(x, y)
ax.plot(x_new, y_new)

ax.set_xlabel('x')
ax.set_ylabel('y')

ax.axis('tight')


plt.show()