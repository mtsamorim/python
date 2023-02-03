# from skimage.restoration import inpaint
# from skimage import io, filters
# import matplotlib.pyplot as plt
# import numpy as np

# defect_image = io.imread("image.jpg")

# mask = filters.threshold_local(defect_image, block_size=5, offset=5)
# mask = defect_image < mask

# mask = np.resize(mask, defect_image.shape[:2])

# restored_image = inpaint.inpaint_biharmonic(
#     defect_image, mask, multichannel=True)

# plt.imshow(restored_image)
# plt.show()

from skimage import io
from skimage import restoration
import matplotlib.pyplot as plt


noisy_image = io.imread("image2.jpg")

# denoised_image = restoration.denoise_tv_chambolle(
#     noisy_image, weight=0.1,  multichannel=True)

denoised_image = restoration.denoise_bilateral(
    noisy_image,  multichannel=True)

io.imsave('image2denoised2.jpg', denoised_image)

plt.imshow(denoised_image)
plt.show()
