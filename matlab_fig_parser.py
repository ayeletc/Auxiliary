from matplotlib.pyplot import *
from scipy.io import loadmat


filename = 'path/to.fig'
d = loadmat(filename,squeeze_me=True, struct_as_record=False)
ax1 = d['hgS_070000'].children
if ax1.shape[0] > 1:
    ax1 = ax1[0]

figure()
counter = 0
for line in ax1.children:
    if line.type == 'graph2d.lineseries':
        marker = "%s" % line.properties.Marker
        # linestyle = "%s" % line.properties.LineStyle
        r,g,b =  line.properties.Color
        # marker_size = line.properties.MarkerSize
        x = line.properties.XData
        y = line.properties.YData
        # plot(x,y,marker,linestyle=linestyle,color = (r,g,b),markersize=marker_size)
        plot(x,y,marker,color = (r,g,b))
    elif line.type == 'text':
        if counter < 1:
            xlabel("%s" % line.properties.String,fontsize =16)
            counter += 1
        elif counter < 2:
            ylabel("%s" % line.properties.String,fontsize = 16)
            counter += 1

show()
