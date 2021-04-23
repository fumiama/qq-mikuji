# qq-mikuji QQ抽签
利用QQ群成员截图进行抽签，生成成员的数字顺序
# 要求
截图最好选择**按加群时间排序**或其他可以尽可能减少背景杂色的排序方式，并裁去标题栏。电脑qq截图也可（包括`macqq`）。

<table>
	<tr>
		<td><center><img src="https://img-blog.csdnimg.cn/20210305225645920.JPEG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE1NzAzMTI=,size_16,color_FFFFFF,t_70#pic_center">最优情况</center></td>
		<td><center><img src="https://img-blog.csdnimg.cn/20210305225751776.JPEG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE1NzAzMTI=,size_16,color_FFFFFF,t_70#pic_center">容许情况（可能出错）</center></td>
	</tr>
</table>

# 开始抽签
### 1. 克隆代码
```bash
git clone https://github.com/SakuraACGN/qq-mikuji.git
```
### 2. 输入命令进行抽签
```bash
cd qq-mikuji
python3 ./mikuji.py [图片路径] [字体] [字号] [颜色] [容差]
```
### 3. 图片的生成与保存
默认会保存一份新的文件到图片同目录，可以选择关闭，只需要将代码中的第`81`行
```python
xxxx.go(True)
```
改为
```python
xxxx.go(False)
```
即可
### 4. 字体
填写系统字体目录下的英文文件名即可，不用加扩展名，如：`PingFang`
### 5. 容差
抽签有误时可尝试更改容差，最优情况可以填写`3`，非最优情况需要增大容差。
# 结果演示

<table>
	<tr>
		<td><center><img src="https://img-blog.csdnimg.cn/20210305231222856.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE1NzAzMTI=,size_16,color_FFFFFF,t_70#pic_center"><center>最优情况，容差3</center></center></td>
		<td><center><img src="https://img-blog.csdnimg.cn/20210305231258722.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTE1NzAzMTI=,size_16,color_FFFFFF,t_70#pic_center"><center>容许情况（一人未被识别，容差21）</center></center></td>
	</tr>
</table>


<table>
	<tr>
		<td><center><img src="https://img-blog.csdnimg.cn/20210305231419573.png"><center>MacQQ</center></center></td>
		<td><center><img src="https://img-blog.csdnimg.cn/20210305231419614.png"><center>容差1</center></center></td>
	</tr>
</table>
