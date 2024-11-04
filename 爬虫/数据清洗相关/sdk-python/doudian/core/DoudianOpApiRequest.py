from doudian.core.DoudianOpApiClient import DoudianOpApiClient
from doudian.core.DoudianOpConfig import GlobalConfig


class DoudianOpApiRequest:
    def __init__(self, client=DoudianOpApiClient(), config=GlobalConfig):
        self.client = client
        self.config = config
        return

    def getParams(self):
        pass

    def getUrlPath(self):
        pass

    def execute(self, accessToken=None):
        return self.client.request(self, accessToken)

    def getConfig(self):
        return self.config

    def setConfig(self, config):
        self.config = config
