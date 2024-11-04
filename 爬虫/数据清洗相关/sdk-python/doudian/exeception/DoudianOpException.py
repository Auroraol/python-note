class DoudianOpException(Exception):
    UNKNOWN_ERROR = 9999
    HTTP_RESPONSE_STATUS_CODE_NOT_2XX = 10001  # 开放平台http返回code非2xx
    HTTP_REQUEST_ERROR = 10002

    def __init__(self, code, causeBy=None):
        self.code = code
        self.causeBy = None
