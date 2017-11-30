
# if you are on 32 bit os
# import Image

# 64 bit with pillow:

"""
This color means 255 red, 255 green, 255 blue, and then 255 Alpha.

Alpha is a measure of how opaque an image is. The higher the number,
the more solid the color is, the lower the number, the more transparent it is.
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

i_blackdot = Image.open('images/dot.png')
i_dotndot = Image.open('images/dotndot.png')

iar_blkdot = np.asarray(i_blackdot)
iar_dotndot = np.asanyarray(i_dotndot)
#print(iar)

fig1= plt.figure()

ax1 = plt.subplot2grid((8,6), (0,0), rowspan=2, colspan=1)
ax2 = plt.subplot2grid((8,6), (0,1), rowspan=2, colspan=1)

ax1.imshow(iar_blkdot)

ax2.imshow(iar_dotndot)
#print(iar)
plt.show()
	  