import os
import numpy as np
from PIL import Image

def exist_check(fname):
    s = os.path.exists('./Photos/%s' %fname)
    print(s, end = '')
    if s==True:
        print(' it exists')
    else: print(' not exists')
    
def try_check(k,w,h):
    try:
        h = k.resize((w, h), Image.ANTIALIAS)
        return h
    except:
        print('Image cannot be resized')
        return k

def main():
    #main_array = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    #len(main_array)
    main_array = np.ones([20,200,200,3], dtype = 'uint8')
    new_width  = 200
    new_height = 200


    for dirName, subdirList, fileList in os.walk('./Photos'):
        print('Found directory: %s' %dirName)
        x = 0
        for fname in fileList:
            print('\tFile %d:  ' %(x+1), end = '')
            print('%s' %fname)
            exist_check(fname)                                                     # f1
            img = Image.open('./Photos/%s' %fname) # image extension *.png,*.jpg
            img = try_check(img,new_width,new_height)                              # f2
            #img.save('.\cburj2.png')
            img = np.array(img)
            main_array[x,:,:,:] = img
            x = x+1


    path, dirs, files = next(os.walk("./Photos"))
    file_count = len(files)
    print('\nfile count = ', file_count)

    #main_array[0] = img[0,:,:]
    #first_row = np.array(main_array[0])
    print('\n shabbaaash\n')

    #av = list(img.getdata())
    #len(av)  # 200x200 = 40000

    ##img = Image. fromarray(img)    # to convert array into image
    #img.show()


    print(' shabbaaash\n')

    # Assignment done: the main array with dimensions 20,200,200,3 has been created as 'main_array'
    print('shape of main_array = ',main_array.shape)
    s = input('press s to show the main array or any other key to quit: ')
    if s=='s':
    	print( main_array)

    ################### Just for fun ################

    #main_array[19,:,:,:]
    main_array2 = np.ones([200,200*10,3], dtype = 'uint8')
    #print(type(main_array2))
    main_array2[:,0:200,:] = main_array[0,:,:,:]
    main_array2[:,200:400,:] = main_array[1,:,:,:]
    main_array2[:,400:600,:] = main_array[2,:,:,:]
    main_array2[:,600:800,:] = main_array[3,:,:,:]
    main_array2[:,800:1000,:] = main_array[4,:,:,:]
    main_array2[:,1000:1200,:] = main_array[5,:,:,:]
    main_array2[:,1200:1400,:] = main_array[6,:,:,:]
    main_array2[:,1400:1600,:] = main_array[7,:,:,:]
    main_array2[:,1600:1800,:] = main_array[8,:,:,:]
    main_array2[:,1800:2000,:] = main_array[9,:,:,:]

    roll = Image. fromarray(main_array2)    # to convert array into image
    #roll.show()
    #roll.save('./10images combined.png')
    #######################     ########################


    # Now attempting to solve updated assignment:
    # os.exists function created
        


#main()
if __name__ == '__main__':
    main()