import geopandas
import pandas
import matplotlib.pyplot

us_map = geopandas.read_file("States_shapefile.shp")
stats = pandas.read_csv("testval.csv")

print(stats)

print(type(us_map))

#us_map.plot()

map_stats = us_map.merge(stats, left_index=True, right_index=True)

print(map_stats)

fig, ax = matplotlib.pyplot.subplots(1, figsize=(16,16))

map_stats.plot(column="bills", cmap="Reds", ax=ax, edgecolor=".4")

vb = matplotlib.pyplot.cm.ScalarMappable(cmap="Reds", norm=matplotlib.pyplot.Normalize(vmin=0, vmax=100))
vb._A=[]
fig.colorbar(vb,shrink=.4, label="Bills")
ax.axis("off")

matplotlib.pyplot.savefig("map.png")
#matplotlib.pyplot.show()
