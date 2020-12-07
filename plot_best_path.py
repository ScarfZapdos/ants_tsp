import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import fourmis

def plot_line(x1,y1,x2,y2):
    plt.plot([x1,x2],[y1,y2],marker='o')


best_path = fourmis.main()
print(best_path)

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_extent([-5, 10, 42, 52])

ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
lat = []
lon = []
name = []
for c in fourmis._CITIES:
    lon.append(c[1][1])
    lat.append(c[1][0])
    name.append(c[0])
ax.plot(lon, lat, '.')
for i, n in enumerate(name):
    ax.annotate(n, (lon[i], lat[i]))
print(len(best_path))
for k in range(len(best_path)-1):
#    plt.axline((best_path[k][1][0], best_path[k][1][1]),
#    (best_path[k+1][1][0], best_path[k+1][1][1]))
#plt.axline((best_path[-1][1][0], best_path[-1][1][1]),
#(best_path[0][1][0], best_path[0][1][1]))
    plot_line(best_path[k][1][1],best_path[k][1][0],best_path[k+1][1][1],best_path[k+1][1][0])
plot_line(best_path[-1][1][1], best_path[-1][1][0],best_path[0][1][1], best_path[0][1][0])
fig.savefig("map.png")
