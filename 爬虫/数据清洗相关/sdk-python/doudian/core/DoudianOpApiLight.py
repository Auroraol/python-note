from doudian.core.DoudianOpApiRequest import DoudianOpApiRequest
from doudian.core.TokenHolder import TokenHolder
import os


class DoudianOpApiLight:

    @staticmethod
    def executeForLight(request: DoudianOpApiRequest):
        DoudianOpApiLight.resetOpenUrl(request)
        accessToken = TokenHolder.getToken()

        result = request.execute(accessToken)

        # 判断 token 是否过期
        if "isv.access-token-expired" == result.sub_code or "isv.access-token-no-existed" == result.sub_code:
            accessToken = TokenHolder.refreshToken()
            result = request.execute(accessToken)
        return result

    @staticmethod
    def resetOpenUrl(request: DoudianOpApiRequest):
        openUrl = os.getenv('cloud.open.url')
        if openUrl is not None:
            request.config.openRequestUrl = openUrl
