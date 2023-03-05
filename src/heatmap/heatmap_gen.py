import geopandas
import pandas
import matplotlib.pyplot
from sys import path as syspath
from os import path as ospath

syspath.append(ospath.dirname(ospath.abspath(__file__))+'/../database')
from sqlGetter import sqlGetter

us_map = geopandas.read_file("States_shapefile.shp")

get = sqlGetter()
billData = get.get_query("SELECT * FROM lst")

stats = pandas.DataFrame(billData, columns = ['state', 'bills'])

#print(stats)
                                              

map_stats = us_map.merge(stats, left_index=True, right_index=True)

fig, ax = matplotlib.pyplot.subplots(1, figsize=(16,9))

map_stats.plot(column="bills", cmap="Reds", ax=ax, edgecolor=".4")

vb = matplotlib.pyplot.cm.ScalarMappable(cmap="Reds", norm=matplotlib.pyplot.Normalize(vmin=0, vmax=100))
vb._A=[]
fig.colorbar(vb,shrink=.4, label="Bills")
ax.axis("off")

matplotlib.pyplot.savefig("map.png")
#matplotlib.pyplot.show()
