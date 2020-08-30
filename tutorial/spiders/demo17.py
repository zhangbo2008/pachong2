import shutil
from urllib.request import quote
import scrapy
from scrapy.http import HtmlResponse
import re
from tutorial.items import *
from urllib import parse
from w3lib.html import *
from w3lib.html import remove_tags

num=__file__.split('/')[-1][:-3][4:]        #直接用文件名动态生成. 以后只改好文件名即可.
class DmozSpider4(scrapy.Spider): # 继承Spider类

    print("进入%s了!!!!!!!!!"%num)
    import os
    if  os.path.exists('output'):
        shutil.rmtree('output')
    yuming='中国青年'
    lang='英语'

    '''
    超参数都在这里修改, 就下面这2个有用.name 随便起一个,在main函数里面调用这个名就行.
    html就是要爬取的网站.
    '''
    name = "dmoz%s"%num # 爬虫的唯一标识，不能重复，启动爬虫的时候要用
    print("name",name)
    # html='http://www.171english.cn/news/'
    # html='http://www.171english.cn/news/2018'
    # html='http://www.171english.cn/news/2019'
    html=' http://www.qqenglish.com/bn/business/'
    # html=' http://roll.edu.sina.com.cn/english/syxw/ss4/index_5.shtml'
    html=html.strip()










    from bs4 import BeautifulSoup
    #首页写这里

    baseUrl=html

    import requests
    # a=requests.get(html).content

    # bs = BeautifulSoup(a, "html.parser")  # 缩进格式
    # print(bs)
    # 下面冲bs中找到所有爬取的页.
    # print(bs.find_all("a"))  # 获取所有的a标签,也就是超链接
    from selenium import webdriver
    import sys



    # browser = webdriver.Firefox()  # Get local session of firefox
    # aaa=browser.get("http://news.sina.com.cn/c/2013-07-11/175827642839.shtml ")  # Load page
    # print(aaa)
    saveall=[html]
    print(777777777777777777777777777777,baseUrl)
    if 0:#调试用, 一般不用这么跑.这个只是动态js代码需要这么使用而已. 一般网页没有这种方式.这个方式太慢爬虫.但是可以避免不必要的js bug
     while 1:
        tmpurl=saveall[-1]
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        from  .utilsme import driver

        base_url = tmpurl
        driver.get(base_url)  # 注意这里面结果直接写到deriver里面
        # print(driver.page_source)
        a=driver.page_source

        bs = BeautifulSoup(a, "html.parser")  # 缩进格式
        # print(bs)
        # 下面冲bs中找到所有爬取的页.
        # print(bs.find_all("a"))
        import re
        # tmp=bs.find_all(text=re.compile("Next[ ]*"))
        # print(tmp)
        now=None

        for s in bs('a'):
            # print(s.text,444444444444444444444444444444444444444444444444)
            if s.text=="»":
                now=s.extract()
                # 需要对now进行中文转码
                # now=parse.quote(now.get('href'))
                print("loook",now)
                # 注意这种旧网站的编码方式.
                now = parse.quote(now.get('href'), safe=";/?:@&=+$, ", encoding="gbk")
                now='https://ru.hujiang.com/'+now
                print(now,"now网页是!!!!!!!!!!")
        if now==None or now in saveall: #防止循环
            break
        else:
            saveall.append(now)
     print(saveall,'最后获取的所有index页')









#-------------推荐的方式获取全部index页

# 下面是直接匹配方式获取所有index页. 也就是一般需求这么跑就可以获取所有index页了.
    import urllib.request  # 导入urllib.request库



    if 0:#调试用
         while 1:



            tmpurl=saveall[-1]

            import urllib
            from bs4 import BeautifulSoup

            url = tmpurl
            print(url,8989898998)
            print(repr(url),9999999999999999999999999999999999999999999999999999)

            a = urllib.request.urlopen(url)  # 打开指定网址
            page = a.read()  # 读取网页源码
            try:
                page=page.decode('gbk')  # 会有2中编码方式. gbk 或者utf-8
            except:
                page = page.decode('utf-8')  # 会有2中编码方式. gbk 或者utf-8

            print(type(page),'yuio')
            # page = requests.get(url)         # 开不开,一直404.
            # page = requests.get('http://www.i21st.cn/story/index_1.html')         # 开不开,一直404.
            # page.encoding = 'utf-8'
            # soup = BeautifulSoup(page,"html.parser")
            print(page,3434343434343)
            bs = BeautifulSoup(page, "html.parser")  # 缩进格式
            print(bs,999999999999999999999999999999999999)
            # print(bs)
            # 下面冲bs中找到所有爬取的页.
            # print(bs.find_all("a"))
            import re
            # tmp=bs.find_all(text=re.compile("Next[ ]*"))
            # print(tmp)
            now=None

            print(url,bs('a'),'uiop')
            for s in bs('a'):
                print(s.text,'yyyyyyyyyy')
                if s.text=="下一页":
                    now=s.extract()
                    print(now,12345)
                    # 需要对now进行中文转码
                    # now=str(now)
                    print(now,888888888888888888888888)
                    # now=parse.quote(re.findall(r'href=".*"',now)[0])

                    print("loook",now)
                    # 注意这种旧网站的编码方式.
                    now = parse.quote(now.get('href'), safe=";/?:@&=+$%, ", encoding="gbk") # 中文的处理方式是里面加上%即可!!!!!!!!!!!!!!!!!!!!!!
                    print(89898934392423423,now)

                    if now[0]=='.':
                        now=now[2:]
                    now=now

                    # now=r'https://' + 'jp.hjenglish.com'+now
                    print(now,"now网页是!!!!!!!!!!")
            if now==None:
                break
            else:
                # print(now,556565656565)
                saveall.append(now)
         print("我们通过普通index算法得到所有的index页信息是",saveall)






    # 直接修改这里面!!!!!!!!!!!!! ,可以手动的吧上面的到的saveall直接改下面即可.就得到了全爬虫.

    saveall=[

        #'http://www.171english.cn/news/2018/june/',
            html,


                        ]
    start_urls = saveall  # 开始爬取的链接 start_urls必须用这个名.




    def parse(self, response): # 一级爬取代码
        print("进入了一级爬虫")
        #xpath教学:https://blog.csdn.net/qq_27283619/article/details/88704479
        #https://www.cnblogs.com/wt7018/p/11749778.html
        # @表示属性
        # 好像使用框架scrapy没法debug.只能疯狂print了
        # help(response.url)
        print(response.url,77777777777777777777777777777777777777777777777777)
        print(response,'**********************当前爬取的网页链接')
        div_list = response.xpath('//h2//a/@href')  # 加入正则
        # div_list = response.xpath('//div[@class="module cl xl"]/ul/li')  # 加入正则

        # print(85654645654, div_list)
        div_list=[i.extract() for i in div_list]

        # 去掉调回的情况.
        div_list=[i for i in div_list if i !=response.url]
        div_list=list(set(div_list))
        print(85654645654, div_list)
        # div_list = response.xpath('//div[@class="newslist solid"]')  # 加入正则
        # print(90909090,div_list)

        # print(div_list)
        # print(div_list[0])
        # print(div_list[-1])
        # print((div_list))

        print(div_list,99999999999999999999999999999999999999)
        for i in div_list:
            # print(self.baseUrl+i.extract())# 获得了全部链接,进入二级爬虫.
            item = en_youth()
            item['link'] = i
            item['link']=item['link']
            # print(item['link'],"lianjie !!!!!!!!!!!!!!!!!!!!!!")
            #每一次一级爬虫得到的页面,都触发一次二级爬虫.
            yield scrapy.Request(item['link'], callback=self.parse_detail
                                 ,meta={'item':item},encoding='raw_unicode_escape')

    #https://blog.csdn.net/Light__1024/article/details/88763541 如何进行爬取二级界面

    def parse_detail(self, response):  # 二级爬取代码
        infomation=response.meta['item']['link']
        # print(infomation,988776754456435345435345435)
        print(infomation,"二级爬取的地址是")
        item = response.body
        # print(item,9090909090909090909090909090)
        # print(item,444444444444444444444444444444444444)
        # print(item)
        # print(response.body,"???????????????")
        # print("********打印二次爬虫结果")#[@class="TRS_Editor"]
        item=en_youth()
        print('进入2极品宠')

        # 预过滤: 改了body,但是还是不生效.??
        #
        # # response.body="dfadsf"
        #
        # tmp=re.sub(r'<script.*</script>','',str(response.body))
        # print(tmp,6666666666666666666666666666666666666666)
        # response._set_body(tmp.encode(response.encoding))
        # print(response.body,777777777777777777777777777777777777777777777)
        # print(response.body,88888888888888888888888888888888888)
        # HtmlResponse.replace()
        # HtmlResponse.replace('body',remove_tags_with_content(response.body, 'script'))
        # HtmlResponse.replace('body',remove_tags_with_content(response.body, 'script'))

        # tmp2=response.xpath('//td[@class="e14"]//text()').extract()
       #下面要设计多重xpath判断.因为格式不同意.
        # 下面这个是只有div 里面写没有p标签.

        # 如果要提取这个标签里面的不管多深的全部文本, 就不用写细节了.直接div extract就可以实现!
        item['neirong']= response.xpath('//div[@class="entry"]//p').extract()
        item['neirong']= response.xpath('//div[@class="entry"]').extract()
        # item['neirong']+= response.xpath('//div[@class="content"]//p').extract()
        # item['neirong']+= response.xpath('//div[@id="article"]//p').extract()
        # item['neirong']+= response.xpath('//td[@class="e14"]').extract()
        # item['neirong']+= response.xpath('//td[@id="article_content"]').extract()
        # print(item['neirong'],22222222222222222222222)


        save=[]

        item['neirong']=[i for i in item['neirong'] if '<script' not in i]
        item['neirong']=[replace_tags(i,'') for i in item['neirong']]


        print('neirong2222222222222',item['neirong'])






        # item['neirong']+= response.xpath('//div[@id="article"]/div/p/text()').extract()
        # item['neirong']+= response.xpath('//div[@id="article"]/p/text()').extract()

        # 下面进行脚本滤过.

        # item['neirong'] = filter(lambda x: '<script>'not in x, item['neirong'])












        # print(item['neirong'], '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        # print(item['neirong'], 8888888888888888888)


        save2='\n'.join(item['neirong'])
        print(save2,9999999999999999999999999999999999999)
        item['neirong']=save2
        item['title']=infomation
        yield item
        # 下面学习pipeline, 进行文件读写.
        # setttings里面设置pipeline写入文件
        #https://www.cnblogs.com/python2687806834/p/9836935.html
        pass

#
# if __name__=="__main__":
#     DmozSpider()