from feishu.api.calendar import Calendar


class TestCalendar():

    def setup_class(self):
        self.calendar = Calendar()

    def test_get(self):
        self.calendar.get("feishu.cn_GPfLbKXlnBJajgCmHbmxZe@group.calendar.feishu.cn")

    def test_getlist(self):
        self.calendar.getlist()

    def test_create(self):
        # 创建日历，获取日历，断言日历是否创建成功
        r = self.calendar.create(summary="冰镇西瓜")
        # 单接口校验，查看响应值是否为设定的内容
        assert r["data"]["calendar"]["summary"]== "冰镇西瓜"

    def test_create_success(self):
        r = self.calendar.create(summary="冰镇西瓜")
        calendar_id = r["data"]["calendar"]["calendar_id"]
        # 通过别的接口来完成测试
        # 封装一些数据库操作，读取数据库完成断言
        get_res = self.calendar.get(calendar_id)
        # 业务逻辑的校验，确定日历已经创建成功
        assert get_res["code"] == 0

    def test_delete(self):
        r = self.calendar.create(summary="冰镇西瓜")
        calendar_id = r["data"]["calendar"]["calendar_id"]
        print(calendar_id)
        # 通过别的接口来完成测试
        # 封装一些数据库操作，读取数据库完成断言
        get_del = self.calendar.delete(calendar_id)
        # 业务逻辑的校验，确定日历已经创建成功
        assert get_del["code"] == 0

    def test_update(self):
        # 创建日历，获取日历，断言日历是否更新成功
        r = self.calendar.update("feishu.cn_7TP6SBZZ57OJKuRJRB4cye@group.calendar.feishu.cn",summary="冰镇西瓜2")
        # 单接口校验，查看响应值是否为设定的内容
        assert r["data"]["calendar"]["summary"] == "冰镇西瓜2"


