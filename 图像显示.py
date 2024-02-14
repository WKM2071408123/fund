import pandas as pd 
import streamlit as st 
import os
import requests
import httpx
import pandas as pd
import datetime
from akshare.utils import demjson
from joblib import Parallel, delayed
from bs4 import BeautifulSoup
import random
import akshare as ak
from time import sleep
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.float_format',lambda x : '%.5f' % x)
from tqdm import tqdm
client = httpx.Client(verify=False,timeout=None)
def get_headers():
    '''
    随机获取一个headers，应对反爬的一种方式
    '''
    user_agents =  ['Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50','Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11']
    headers = {'User-Agent':random.choice(user_agents)}
    return headers


# 输出所有文件和文件夹

option = st.selectbox(
    '请选择浏览内容',
    ('自拍偷拍','美腿丝袜'))

number=st.number_input(label='数字', min_value=0, max_value=1000,  step=1)



if number:
    if option=='自拍偷拍':

        url=f'https://www.543ef.com/pic/toupai/index_{number}.html'
    else:
        url=f'https://www.543ef.com/pic/meitui/index_{number}.html'
    response = client.get(url,headers=get_headers())
    soup = BeautifulSoup(response, 'html.parser')
    li=soup.find_all('dt')
    local=[]
    for i in li:
        rt=i.a.attrs
        if rt['href'][-4:]=='html':
            ht='https://www.543ef.com'+rt['href']
            local.append(ht)
    index=st.number_input(label='起始位置',min_value=0,max_value=len(local),step=1)
    if index:
        response1 = client.get(local[index],headers=get_headers())
        soup1 = BeautifulSoup(response1, 'html.parser')
        l1=soup1.find_all('img')
        op=[]
        for x in l1:
            img=x.get('src')
            if img!=None:
                op.append(img)

        st.image(op)