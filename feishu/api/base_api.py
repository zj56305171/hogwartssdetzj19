"""
和接口操作相关的封装，与业务无关
"""
import requests

from feishu.util.logger import logger

class BaseApi():
    def base_requests(self,method,url,**kwargs):
        logger.debug(f"请求的参数为：{method}，请求的url为：{url}")
        r = requests.request(method,url,**kwargs)
        return r
