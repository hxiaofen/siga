import cv2, numpy as np, math
import process

voting = [0]*66

def run_setting_entrance():
	fn = 'flower_ori.jpg'
	img = cv2.imread(fn)
	gray_images = process.output_gray_image(img) #array

	for ds in xrange(0, 100, 10):
		for rs in xrange(0, 100, 10):
			gray_bia_images = process.output_bila_image(gray_images, ds, rs)
			ori_bia_img = process.bilaterialFilter(img, ds, rs)
			diff_values = process.output_diff_image_value(ori_bia_img, gray_bia_images) #array

			f = open('result.txt', 'a')
			f.write('ds is ' + str(ds) + ' and rs is ' + str(rs) + '\n')

			for i in xrange(0, len(diff_values)):
				if(diff_values[i] < diff_values[i-1] and diff_values[i] < diff_values[i+1]):
					voting[i] += 1
					save_img(gray_images[i], i)
					f.write('The ' + str(i) + ' image has ' + str(voting[i]) + ' tickets.\n')	
			f.write('------------------------------------------\n')


def save_img(img, i):
	cv2.imwrite('Temp/gray_images'+str(i)+'.jpg', img)


run_setting_entrance()

'''
f = open('result.txt', 'a')
for i in xrange(66):
	f.write('The ' + str(i+1) + ' image has ' + str(voting[i]) + ' tickets.\n')
'''






