class DoudianOpConfig:
    def __init__(self):
        self.appKey = ""
        self.appSecret = ""
        self.httpConnectTimeout = 1000  # http连接时间1s
        self.httpReadTimeout = 10000  # http读取时间10s
        self.openRequestUrl = "openapi-fxg.jinritemai.com"
        self.useHttps = True
        return


GlobalConfig = DoudianOpConfig()
