import cv2, numpy as np, math

#There are 66 number weight style
def weight_setting():
	weight_array = []
	for i in xrange(0,11):
		for j in xrange(0,11):
			for k in xrange(0,11):
				if i+j+k == 10:
					r = i / 10.0
					g = j / 10.0
					b = k / 10.0
					weight_array.append([r,g,b])
	return weight_array

#input a original image and the weight , output the final gray image
def color_to_gray_image(img, weight):
	width = img.shape[0]
	height = img.shape[1]
	gray_image = img.copy()
	for i in xrange(0,width):
		for j in xrange(0,height): 
			gray_image[i,j] = img[i,j,0]*weight[0] +img[i,j,1]*weight[1] + img[i,j,2]*weight[2]
	return gray_image

def output_gray_image(original_image):
	weight_array = weight_setting()
	gray_images = []
	for i in xrange(0,len(weight_array)):
		gray_images.append(color_to_gray_image(original_image, weight_array[i]))
	return gray_images

def bilaterialFilter(img, ds, rs):
	blur = cv2.bilateralFilter(img,9,ds,rs)
	return blur

def output_bila_image(gray_img, ds, rs): #gray_img is array
	bila_imgs = []
	for gi in gray_img:
		bila_imgs.append(bilaterialFilter(gi, ds, rs))
	return bila_imgs

def diff_between_bila_and_gray(bila_img, gray_img):
	h = bila_img.shape[0]
	w = bila_img.shape[1]
	img_diff = np.zeros((h,w),np.int)
	for i in xrange(h):
		for j in xrange(w): 
			px = 0
			for c in xrange(3):
				px += (int(bila_img[i,j][c]) - int(gray_img[i,j][c])) ** 2
			img_diff[i,j] = math.sqrt(px)
	return img_diff

def output_diff_image_value(bila_img, gray_imgs):
	diff_imgs_values = []

	for gi in gray_imgs:
		diff_img = diff_between_bila_and_gray(bila_img, gi)
		h,w = diff_img.shape[:2]
		px = 0
		for i in xrange(h):
			for j in xrange(w):
				px += diff_img[i,j] ** 2
		diff_imgs_values.append(math.sqrt(px))

	return diff_imgs_values		











