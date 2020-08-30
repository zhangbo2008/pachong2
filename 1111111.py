import  requests

tmp=requests.get('http://www.i21st.cn/story/3574.html')
# tmp=requests.get('http://www.baidu.com')
print(tmp)






import requests
res = requests.get('http://www.i21st.cn/story/3574.html')
res.encoding = 'utf-8'
print(res.text)
print(1111111)




import urllib.request    #导入urllib.request库
b ='http://www.i21st.cn/story/3574.html'
a = urllib.request.urlopen(b)#打开指定网址
html = a.read()       #读取网页源码
html = html.decode("utf-8") #解码为unicode码
print(html)         #打印网页源码