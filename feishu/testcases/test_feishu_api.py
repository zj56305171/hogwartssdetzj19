from feishu.api.feishu_api import FeishuApi


class TestFeishuApi():

    def test_token(self):
        feishu_api = FeishuApi()
        feishu_api.get_token()
