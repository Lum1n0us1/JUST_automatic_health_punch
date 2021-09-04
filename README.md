# 前言

该脚本主要实现江苏科技大学每日的健康打卡功能，主要使用python的`selenium`模块完成。

注意：该脚本仅提供个人学习使用，切勿用于其他途径，由此造成的损失与本人无关！

# 环境安装与配置

```bash
pip install lxml
pip install selenium
```

以chrome浏览器为例，需要去下载chrome浏览器对应版本的[驱动](http://npm.taobao.org/mirrors/chromedriver/)，下载完成后，在代码第`11`和`12`行填入对应的绝对路径。

该脚本能批量打卡，在代码第`50、51`行的列表内填入打卡目标的学号和密码，即可开始运行程序。

