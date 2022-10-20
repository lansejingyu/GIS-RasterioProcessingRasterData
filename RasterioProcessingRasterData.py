# -*- coding: utf-8 -*-
# @Project : GIS-RasterioProcessingRasterData
# @File : RasterioProcessingRasterData
# @IDE：PyCharm
# @Author : KT15
# @Time : 2022/10/19 14:49

import rasterio
import rasterio.sample
import rasterio.vrt
import rasterio._features
from osgeo import gdal


def Blanklines():  # 打印一行空白行，定义一个函数
	print()


def Files():
	global dataset
	FilePath = input("请输入.TIF文件路径+文件名(如:E:\TIF\masaike\K50F038012.tif):")
	dataset = rasterio.open(r'' + FilePath)
	dataset1 = gdal.Open(r'' + FilePath)
	Blanklines()
	print("基本属性数据：")
	print("1.数据路径+文件名:", dataset.name)  # 数据路径+文件名
	print("2.数据格式:", dataset.driver)  # 数据格式
	print("3.数据的投影坐标系:", dataset.crs)  # 数据的投影坐标系
	print("4.数据的波段数目:", dataset.count)  # 数据的波段数目
	print("5.获取波段索引号-从1开始:", dataset.indexes)  # 获取波段索引号 从1开始
	print("6.数据的影像宽度:", dataset.width)  # 数据的影像宽度
	print("7.数据的影像高度:", dataset.height)  # 数据的影像高度
	print("7.数据的影像面积:",
		  dataset.width * dataset.height * (dataset1.GetGeoTransform())[1:2][0] * (dataset1.GetGeoTransform())[1:2][
			  0] / 1000000, "平方千米")  # 数据的影像面积 (dataset1.GetGeoTransform())[1:2][0]#typr=tuple  将8中的像元大小数据取出来.
	print("8.空间参数(栅格数据的六参数:左上角坐标，像元X、Y方向大小，旋转等信息。 要注意，Y方向的像元大小为负值):\n",
		  dataset1.GetGeoTransform())
	print("9.数据的地理范围:\n", dataset.bounds)  # 数据的地理范围
	print('''
	功能点列表：
	1.根据像元的row和col获取当前像元中心坐标
	2.根据像元中心坐标获取像元行列号
	3.获取像元的左上角坐标以及右下角坐标(空间位置)
	4.重新选择.TIF文件
	''')


def SelectionFunction():
	global num
	num = input("请输入数字选择功能:")


def GetCenterCoordinates():  # 根据像元的row和col获取当前像元中心坐标
	global CenterCoordinates
	row = input("请输入要查询的像元所在位置的行号:")  # type=str
	col = input("请输入要查询的像元所在位置的列号:")  # type=str
	CenterCoordinates = dataset.xy(int(row), int(col))  # 参数type=int   type(coi)=tuple


def GetRowCol():  # 根据像元中心坐标获取像元行列号
	global RowCol
	x = input("请输入要查询的像元所在的X轴(行/宽)坐标点:")  # type=str
	y = input("请输入要查询的像元所在的Y轴(列/高)坐标点:")  # type=str
	RowCol = dataset.index(*(float(x), float(y)))  # 参数type=float   type(RowCol)=tuple


def GetSpatialPosition():  # 获取像元的左上角坐标以及右下角坐标(空间位置)
	global row
	global col
	global SpatialPositionleftTop
	global SpatialPositionRightBottom
	row = input("请输入要查询的像元所在位置的行号:")  # type=str
	col = input("请输入要查询的像元所在位置的列号:")  # type=str
	SpatialPositionleftTop = dataset.transform * (int(row), int(col))  # 左上角坐标
	SpatialPositionRightBottom = dataset.transform * (int(row) + 1, int(col) + 1)  # 右下角坐标


def Function():
	if num == '1':
		GetCenterCoordinates()
		print("当前像元中心坐标为:", CenterCoordinates)
		Blanklines()
		SelectionFunction()
		Function()
		Blanklines()
	elif num == '2':
		GetRowCol()
		print("当前像元的行列号为:", RowCol)
		Blanklines()
		SelectionFunction()
		Function()
		Blanklines()
	elif num == '3':
		GetSpatialPosition()
		print("当前像元的左上角坐标:", SpatialPositionleftTop)
		print("当前像元的右下角坐标:", SpatialPositionRightBottom)
		Blanklines()
		SelectionFunction()
		Function()
		Blanklines()
	elif num == '4':
		Files()
		Blanklines()
		SelectionFunction()
		Function()
		Blanklines()
	else:
		print("输入错误，请重新输入数字选择功能!")
		Blanklines()
		SelectionFunction()
		Function()
		Blanklines()


Files()
SelectionFunction()
Function()
