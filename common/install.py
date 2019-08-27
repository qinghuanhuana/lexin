# coidng=utf-8
import time
from uiautomator import Device
from appium import webdriver
import os, yaml
from threading import Thread
from common.lxyd import Lxyd
d = Device("")
print(d.info)
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
appPath = os.path.join(path, "apk", "lxyd.apk")
url = Lxyd.test_data('url.yaml')['url']
desired_caps={
            'platformName': 'Android',
            'deviceName': 'X2P5T16114009484',
            'platformVersion': '5.1',
            'app': appPath,
            'noreset': True,
            'appPackage': 'gz.lifesense.weidong.qa',
            'appActivity': 'gz.lifesense.weidong.ui.activity.main.LaunchActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
dr = webdriver.Remote(url, desired_caps)
