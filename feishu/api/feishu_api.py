"""
与业务相关的封装，封装一些公共方法，比如公共api等
"""
import json

from feishu.api.base_api import BaseApi
from feishu.util.logger import logger


class FeishuApi(BaseApi):
    app_id = "cli_a2b797fcccf95013"
    app_secret = "Fk3IysOwDqxrxeuN98DyoeGBNv7NJvHq"

    def feishu_requests(self,method,url,**kwargs):
        if "headers" in kwargs:
            kwargs["headers"]["Authorization"] = f"Bearer {self.get_token()}"
        else:
            kwargs["headers"] = {"Authorization": f"Bearer {self.get_token()}"}
        r = self.base_requests(method=method,url=url,**kwargs)
        return r.json()


    def get_token(self):
        token_url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        json_data = {
            "app_id":self.app_id,
            "app_secret":self.app_secret
        }
        r = self.base_requests(url = token_url,method= "post",json = json_data)
        self.token = r.json()["tenant_access_token"]
        logger.debug(f"获取token的响应信息为{self.token}")
        return self.token



