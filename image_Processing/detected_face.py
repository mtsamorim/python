from skimage import io, feature, feature, data
import matplotlib.pyplot as plt
from matplotlib import patches


def show_detected_face(result, detected, title="Face Image"):
    plt.imshow(result)
    img_desc = plt.gca()
    plt.set_cmap('gray')
    plt.title(title)
    plt.axis('off')

    for patch in detected:
        img_desc.add_patch(
            patches.Rectangle(
                (patch['c'], patch['r']),
                patch['width'],
                patch['height'],
                fill=False, color='r', linewidth=2)
        )
    plt.show()


image = io.imread("face3.jpg")

trained_file = data.lbp_frontal_face_cascade_filename()

detector = feature.Cascade(trained_file)

detected = detector.detect_multi_scale(
    img=image, scale_factor=1.2, step_ratio=1, min_size=(50, 50), max_size=(300, 300))

show_detected_face(image, detected)
