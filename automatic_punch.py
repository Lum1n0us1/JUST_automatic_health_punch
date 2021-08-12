from selenium import webdriver
from time import sleep
from lxml import etree
from selenium.webdriver.chrome.options import Options


def clock_in(uname, passwd):
    # 实现无可视化操作
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.binary_location = r'/Applications/Chrome.app/Contents/MacOS/Google Chrome'
    bro = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=chrome_options)

    bro.get('http://ids2.just.edu.cn/cas/login?service=http%3A%2F%2Fmy.just.edu.cn%2F')
    print('信息门户加载完成')

    username_btn = bro.find_element_by_id('username')
    password_btn = bro.find_element_by_id('password')
    username_btn.send_keys(uname)
    password_btn.send_keys(passwd)
    login_btn = bro.find_element_by_id('passbutton')
    login_btn.click()

    if '认证信息无效' in bro.page_source:
        print('登录失败，账号或密码可能错误')
    else:
        print('登录成功')

    # 网页加载时间过长，设置最长加载时间5秒
    bro.set_page_load_timeout(5)
    bro.set_script_timeout(5)
    try:
        # 信息门户的bug，要返回上一页
        if '重新登录' in bro.page_source:
            bro.back()
    except:
        bro.execute_script('window.stop()')

    # 开始点击打卡
    clock_in_btn = bro.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div/div/div/div/div/div/ul/li[2]/div/div/div[1]/img')
    clock_in_btn.click()
    print('已进入打卡页面')

    # 将旧url更新到打卡的url
    sleep(3)
    n = bro.window_handles  # 获取当前浏览器所有窗口句柄
    # print('当前句柄：', n)
    bro.switch_to.window(n[-1])  # 切换到打卡窗口的句柄

    # 如果当日提交过，选择关闭按钮
    # if '当天已经' in bro.page_source:
    #     close_btn = bro.find_element_by_class_name('layui-layer-btn0')
    #     close_btn.click()

    # 体温数值填入
    tw = bro.find_element_by_xpath('//*[@id="input_tw"]')
    tw.send_keys('36.7')
    zwtw = bro.find_element_by_xpath('//*[@id="input_zwtw"]')
    zwtw.send_keys('36.7')
    print('温度已填写')

    # 提交
    submit_btn = bro.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/button[1]')
    submit_btn.click()
    # print('打卡成功')

    bro.quit()

if __name__ == '__main__':
    uname_passwd = [
        # ['学号1', '密码1'],
        # ['学号2', '密码2']
    ]
    for up in uname_passwd:
        clock_in(up[0], up[1])
        print(f'{up[0]}打卡成功')
