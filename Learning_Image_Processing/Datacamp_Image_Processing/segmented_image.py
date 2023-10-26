from skimage import segmentation as seg
from skimage import color, io
import matplotlib.pyplot as plt


image = io.imread("image2.jpg")

segments = seg.slic(image, n_segments=100)

segmented_image = color.label2rgb(segments, image, kind='avg')


plt.imshow(segmented_image)
plt.show()
