# slam入门代码
1. 请基于单应性矩阵，实现对下⾯两张照⽚的拼接  <br>
image 1: https://github.com/daeyun/Image-Stitching/blob/master/img/hill/1.JPG  
image 2: https://github.com/daeyun/Image-Stitching/blob/master/img/hill/2.JPG

2. 尝试⾃⼰写出⼀个针对基础矩阵的分解函数。已知信息为基础矩阵F, 左右相机
的内参矩阵K1, K2, 以及左右相机的匹配投影点（像素点）m1， m2。
输⼊：F(3X3), K1(3X3), K2(3X3), m1(nX2), m2(nX2)
输出：左右相机的相对旋转R以及相对平移t
