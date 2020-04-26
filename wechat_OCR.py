# coding:utf-8
import time
from glob import glob

import numpy as np
from PIL import Image

import model
# ces

#paths = glob('./test/*.*')
paths = glob('/data/apps/wechat/*.*')

if __name__ == '__main__':
    outstring = ""
    fo = open("/data/apps/wechat/moment.txt", "w")
    for i in range(1000):
        try:
            im = Image.open("/data/apps/wechat/screenshots/"+str(i)+".png")
        except Exception as e:
            continue
        
        focr = open("/data/apps/wechat/moment_ocr/"+str(i)+".txt", "w")
        img = np.array(im.convert('RGB'))
        t = time.time()
        '''
        result,img,angel分别对应-识别结果，图像的数组，文字旋转角度
        '''
        result, img, angle = model.model(
            img, model='keras', adjust=False, detectAngle=False)
        print("It takes time:{}s".format(time.time() - t))
        print("---------------------------------------")
        fo.write(  "-------\n" )
        for key in result:
            print(result[key][1])
            outstring = result[key][1]
            fo.write( outstring +"\n" )
            focr.write( outstring +"\n" )

        try:
            focr.close()
        except Exception as e:
            pass
        