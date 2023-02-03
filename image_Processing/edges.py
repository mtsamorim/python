from skimage import color, io, feature
import matplotlib.pyplot as plt


image = io.imread("coins.jpg")

coins = color.rgb2gray(image)

canny_edges = feature.canny(coins)

canny_edges1 = feature.canny(coins, sigma=1.3)

fig, (img1, img2, img3) = plt.subplots(nrows=1, ncols=3)

img1.imshow(coins, cmap="gray")
img1.axis('off')

img2.imshow(canny_edges, cmap="gray")
img2.axis('off')

img3.imshow(canny_edges1, cmap="gray")
img3.axis('off')

plt.show()
