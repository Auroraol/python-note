from doudian.api.token.CreateTokenRequest import CreateTokenRequest
from doudian.api.token.RefreshTokenRequest import RefreshTokenRequest
from doudian.core.AccessToken import AccessToken
from doudian.core.DoudianOpConfig import GlobalConfig
from doudian.core.DoudianOpResponse import DoudianOpResponse


class AccessTokenBuilder:
    @staticmethod
    def buildTokenByShopId(shopId, config=GlobalConfig):
        """自用型应用获取accessToken"""
        request = CreateTokenRequest()
        request.getParams().shop_id = shopId
        request.getParams().grant_type = "authorization_self"
        request.getParams().code = ""
        request.setConfig(config)
        response = request.execute()
        accessToken = AccessToken(response)
        return accessToken

    @staticmethod
    def buildTokenByCode(code, config=GlobalConfig):
        """工具型应用获取accessToken"""
        request = CreateTokenRequest()
        request.getParams().grant_type = "authorization_code"
        request.getParams().code = code
        request.setConfig(config)
        response = request.execute()
        accessToken = AccessToken(response)
        return accessToken

    @staticmethod
    def refreshToken(refreshToken, config=GlobalConfig):
        request = RefreshTokenRequest()
        request.getParams().grant_type = "refresh_token"
        request.getParams().refresh_token = refreshToken
        request.setConfig(config)
        response = request.execute()
        accessToken = AccessToken(response)
        return accessToken

    @staticmethod
    def parse(accessTokenStr):
        accessTokenResp = DoudianOpResponse()
        accessTokenResp.data = {'access_token': accessTokenStr}
        accessToken = AccessToken(accessTokenResp)
        return accessToken

