
""" Code unit-tests go here. """
import numpy as np

import image_ema_project

def test_roi_xy():
    xy = np.arange(-4, 5)
    result = [xy, xy]
    roi_xy = image_ema_project.roi_xy([0, 0], [8, 8])
    assert np.all(np.equal(roi_xy, result))
