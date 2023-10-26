from skimage import io, color, measure, filters
import matplotlib.pyplot as plt

image = io.imread("dice.jpg")

image = color.rgb2gray(image)

thresh = filters.threshold_otsu(image)

thresholded_image = image > thresh

contours = measure.find_contours(thresholded_image, 0.8)

# for contour in contours:
#     print(contour.shape)

# small_contours = [c for c in contours if c.shape[0] < 205]

# print(len(small_contours))

# plt.imshow(thresholded_image, cmap="gray")
# plt.show()
