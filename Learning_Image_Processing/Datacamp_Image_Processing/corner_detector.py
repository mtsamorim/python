from skimage import io, color, feature, measure
import matplotlib.pyplot as plt


def show_image_with_corners(image, coords, title="Corners detected"):
    plt.imshow(image, interpolation='nearest', cmap='gray')
    plt.title(title)
    plt.plot(coords[:, 1], coords[:, 0], '+r', markersize=15)
    plt.axis('off')
    plt.show()


image = io.imread("build.jpg")

image = color.rgb2gray(image)

measure_image = feature.corner_harris(image)

coords = feature.corner_peaks(feature.corner_harris(
    image), min_distance=20, threshold_rel=0.02)

show_image_with_corners(image, coords)


# plt.imshow(measure_image, cmap='gray')
# plt.show()
