import json

from feishu.api.feishu_api import FeishuApi
from feishu.util.logger import logger


class Calendar(FeishuApi):
    """
    接口的具体实现
    """

    # 接口用例逻辑和接口本身逻辑保持一致
    def create(self, summary="hogwarts_ad",
               description="使用开放接口创建日历hogwarts_ad",
               permissions="public",
               color=-1,
               summary_alias="hogwarts_Adddddds"):
        url = "https://open.feishu.cn/open-apis/calendar/v4/calendars"
        method = "POST"
        json_data = {
                "summary":summary,
                "description":description,
                "permissions":permissions,
                "color":color,
                "summary_alias":summary_alias,
            }
        r = self.feishu_requests(url = url,method = method,json = json_data)
        logger.debug(f"创建接口的响应信息为{r}")
        return r

    def delete(self,calendar_id):
        url = f"https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}"
        r = self.feishu_requests(url=url, method="DELETE")
        logger.debug(f"获取接口的响应信息为{r}")
        return r


    def get(self,calendar_id):
        url = f"https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}"
        r = self.feishu_requests(url=url,method = "get")
        logger.debug(f"获取接口的响应信息为{r}")
        return r

    def getlist(self):
        url = "https://open.feishu.cn/open-apis/calendar/v4/calendars"
        r = self.feishu_requests(url=url, method="get")
        logger.debug(f"获取接口的响应信息为{r}")
        return r

    def update(self,calendar_id,summary="hogwarts_ad",
               description="使用开放接口创建日历hogwarts_ad",
               permissions="public",
               color=-1,
               summary_alias="hogwarts_Adddddds"):
        url = f"https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}"
        method = "PATCH"
        json_data = {
            "summary": summary,
            "description": description,
            "permissions": permissions,
            "color": color,
            "summary_alias": summary_alias,
        }
        r = self.feishu_requests(url=url, method=method, json=json_data)
        logger.debug(f"创建接口的响应信息为{r}")
        return r

    def search(self):
        pass