import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import os

def save_imgs(folder, file, out_folder, save=False):
    
    out_template = file.split('.')[0].strip()
    # Load File 
    mag_f  = nib.load(os.path.join(folder,file))

    print(mag_f)

    if save:
        mag  = mag_f.get_fdata()
        print('mag type', type(mag))
        print(mag.shape)

        # Show Objects
        for i in range(mag.shape[2]):
            plt.figure()
            plt.imshow(mag[:,:,i])
            plt.colorbar()
            plt.title(f'slice {i}')

            print(os.path.join(out_folder, f'{out_template}_{i}.png') )

            plt.savefig(os.path.join(out_folder, f'{out_template}_{i}.png') )
            plt.close()

def save_img_comp(folder1, folder2, file, out_folder, save=False):
    
    out_template = file.split('.')[0].strip()
    # Load File 
    mag_f  = nib.load(os.path.join(folder1,file))
    mask_f  = nib.load(os.path.join(folder2, 'mag_mask.nii.gz')) #file))

    print(mag_f)

    if save:
        mag  = mag_f.get_fdata()
        mask = mask_f.get_fdata()
        print('mag type', type(mag))
        print(mag.shape)

        # Show Objects
        for i in range(mag.shape[1]):
            plt.figure(figsize=(4,2))
            plt.subplot(121)
            plt.imshow(mag[:,i,:])
            plt.colorbar()
            plt.clim([np.min(mag), np.max(mag)])
            plt.subplot(122)
            plt.imshow(mask[:,i,:])
            plt.colorbar()
            plt.title(f'slice {i}')

            print(os.path.join(out_folder, f'{out_template}_{i}.png') )

            plt.savefig(os.path.join(out_folder, f'{out_template}_{i}.png') )
            plt.close()

# Setup Input and output paths
folder = "/home/jac/data_start"
folder2 = "/home/jac/data_mask"

files = [i for i in os.listdir(folder) if i.find('nii') > 0]
print(files)

out_folder = f'/home/jac/debug/' 

for f in files:
    save_img_comp(folder, folder2, f, out_folder, save=True)
    break

