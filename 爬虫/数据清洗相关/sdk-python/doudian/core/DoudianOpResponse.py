class DoudianOpResponse:
    def __init__(self):
        self.data = None
        self.log_id = ""
        self.code = 0
        self.msg = ""
        self.sub_code = ""
        self.sub_msg = ""

    def isSuccess(self):
        return self.code == 10000
