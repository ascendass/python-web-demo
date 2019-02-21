#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
'''
# @File: sharp-test.py
# @Author: zhutf
# @Time: 2019/1/24 10:33 PM
# @desc:
'''

print('夏普')

if __name__ == '__main__':
    a = pd.Series([1000000, 1, 2, 3])

    print(type(a))
    
    la = np.log(a) - np.log(a.shift(1))

    print((la.mean() - 0.0285 / 252) / la.std() * np.sqrt(252))





