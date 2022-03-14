#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 23:10
# @Author  : 张大鹏
# @Site    : 
# @File    : z01_读写配置.py
# @Software: PyCharm
from zdppy_yaml import Yaml

y = Yaml()
print(y)

# 更新配置
y.update_config({"debug": False, "a": 11, "b": [22, 33]})
print(y)

# 保存配置
y.save_config()
