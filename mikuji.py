#!/usr/bin/env python3
#mikuji.py
#fumiama 20210305

import sys, random
from PIL import Image, ImageDraw, ImageFont
from PIL.Image import LANCZOS
import numpy as np

class mikuji():
	def __init__(self, imagePath, fontName, fontSize, fontColor, miss):
		self.imagePath = imagePath
		self.fontName = fontName
		self.fontSize = fontSize
		self.fontColor = fontColor
		self.miss = miss
		self.prevCenter = (-4, -4)
	
	def get_people(self):
		self.width, self.height = self.image.size
		self.imgArr = self.image.load()
		self.npArr = np.array(self.image, dtype=int, order='C')
		self.bgColor = int(np.mean(self.imgArr[3, self.height/2]))
		print("背景色:", self.bgColor)
		peopleList = []
		prevHeight = 0
		h = 0
		while h < self.height - self.miss:
			if not self.approx(self.around(h), self.bgColor):
				if h - prevHeight > self.miss: peopleList.append(h)
				prevHeight = h
			h += self.miss
		print("找到项目在Y坐标", peopleList)
		return peopleList

	def approx(self, a, b): return abs(a - b) <= self.miss
	
	def around(self, y):
		ay = y + self.miss
		if y == ay: return np.mean(self.npArr[y, 0:self.width//5])
		ey = ay if ay < self.height else self.height - 1
		subArr = self.npArr[y:ey, 0:self.width//5]
		mean = np.mean(subArr)
		return np.nan_to_num(mean, nan=np.mean(self.npArr[y, 0:self.width//5]))

	def pic_open(self, filepath):
		#图片打开与显示
		image = Image.open(filepath)
		return image

	def pic_text(self, image, position, text, font):
		#新建绘图对象
		draw = ImageDraw.Draw(image)
		draw.text(position, text, fill=self.fontColor, font=font)

	def pic_save(self, image, filename): image.save(filename)

	def go(self, saveImg=False):
		self.image = self.pic_open(self.imagePath)
		people = self.get_people()
		peopleLen = len(people)
		rank = random.sample(range(1, peopleLen + 1), peopleLen)
		print("排序:", rank)
		i = 0
		font = ImageFont.truetype(self.fontName, size=self.fontSize)
		for person in people:
			self.pic_text(self.image, (0, person), str(rank[i]), font)
			i += 1
		self.image.show()
		if saveImg:
			name = self.imagePath + ".rank.png"
			self.pic_save(self.image, name)

if __name__=="__main__":
	def usage(cd): print("用法:", cd, "图片路径", "字体", "字号", "颜色", "容差")
	if len(sys.argv) == 6:
		a3 = sys.argv[3]
		if a3.isdigit():
			a5 = sys.argv[5]
			if a5.isdigit():
				try: mikuji(sys.argv[1], sys.argv[2], int(a3), sys.argv[4], int(a5)).go(True)
				except: usage(sys.argv[0])
				else: print("命令成功完成")
			else: print("非法容差")
		else: print("非法字号")
	else: usage(sys.argv[0])
