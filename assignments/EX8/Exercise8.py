
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from faceTrackingDemo import faceTracker
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(10,10))

# frames of the processed input video
# change the input to obama.avi in part b)
#frames = faceTracker('santi.avi')
frames = faceTracker('myVid.webm')

print('Done')
# create an animation that can be embedded in the notebook
ani = animation.ArtistAnimation(fig, frames, interval=50, blit=True, repeat_delay=2000)

plt.show()

#display(HTML(ani.to_html5_video()))







