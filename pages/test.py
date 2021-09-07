from selenium import webdriver

driver = webdriver.Chrome()
driver.get("www.baidu.com")

"""
web页面定位元素的方式
1、通过id定位
2、通过name定位
3、通过class定位
4、通过xpath定位
4-1 属性定位

5、通过link_text定位

"""