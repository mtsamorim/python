from skimage import io, feature, filters, data
import matplotlib.pyplot as plt


def getFace(d):
    x, y = d['r'], d['c']

    width, height = d['r'] + d['width'], d['c'] + d['height']

    face = image[x:width, y:height]

    return face


def applyGaussianBlur(image, detected, sigma=5):
    for d in detected:
        face = getFace(d)

        gaussian_face = filters.gaussian(
            face, channel_axis=2, sigma=sigma) * 255

        x, y = d['r'], d['c']
        width, height = d['r'] + d['width'], d['c'] + d['height']

        image[x:width, y:height, :] = gaussian_face

    return image


image = io.imread("face2.jpg")

trained_file = data.lbp_frontal_face_cascade_filename()

detector = feature.Cascade(trained_file)

detected = detector.detect_multi_scale(
    img=image, scale_factor=1.2, step_ratio=1.0, min_size=(50, 50), max_size=(200, 200))


output = applyGaussianBlur(image, detected)

# If you want to save
# io.imsave("output3.jpg", output)

plt.imshow(output)
plt.axis('off')
plt.show()
