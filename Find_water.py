
import skimage.io
import skimage.transform
import matplotlib.pyplot as plt
 
for k in range(1,100):
    if k <10:
        zeros = "000"
    else:
        zeros = "00"
    if k%10 != 0:
        filename = zeros + str(k) + ".tif"
        img_path = (r'E:\\comp\\train\images\\')+filename
        label_path = (r'E:\\comp\\train\labels\\')+filename
        img_img = skimage.io.imread(img_path)
        img_label = skimage.io.imread(label_path)
        # skimage.io.imshow(img[:,:,1])
        # plt.show()

        import numpy as np
        res = np.full((500,500,32),255)
        for m in range(500):
            for n in range(500):
                if img_label[m,n] == 4:
                    res[m,n,:] = img_img[m,n,:]
        path2 = ('E:\\comp\\water\\')+zeros + str(k)
        np.save(path2+'.npy',res)
    else:
        continue
