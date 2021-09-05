from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


def clock_in(uname, passwd):
    # 实现无可视化操作
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.binary_location = r'/bin/chrome'
    bro = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)

    bro.get('http://ids2.just.edu.cn/cas/login?service=http%3A%2F%2Fmy.just.edu.cn%2F')
    print('信息门户加载完成')

    username_btn = bro.find_element_by_id('username')
    password_btn = bro.find_element_by_id('password')
    username_btn.send_keys(uname)
    password_btn.send_keys(passwd)
    login_btn = bro.find_element_by_id('passbutton')
    login_btn.click()

    # 直接请求打卡页面
    bro.get('http://ehall.just.edu.cn/default/work/jkd/jkxxtb/jkxxcj.jsp?_p=YXM9MiZ0PTImZD0xMDEmcD0xJmY9MzAmbT1OJg__&_l=&_t=')

    # # 如果当日提交过，选择关闭按钮
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
    submit_btn = bro.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/button[1]')
    submit_btn.click()
    # print('打卡成功')

    bro.quit()


if __name__ == '__main__':
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    uname_passwd = [
        ['用户名1', '密码1', '姓名1'],
        ['用户名2', '密码2', '姓名2']
    ]
    for up in uname_passwd:
        clock_in(up[0], up[1])
        print(f'{up[2]}打卡成功')
