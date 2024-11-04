class AccessToken:
    def __init__(self, accessTokenResp):
        self.accessTokenResp = accessTokenResp

    def getAccessToken(self):
        if self.accessTokenResp is not None and hasattr(self.accessTokenResp, "data"):
            return self.accessTokenResp.data["access_token"]
        return ""

    def getRefreshToken(self):
        if self.accessTokenResp is not None and hasattr(self.accessTokenResp, "data"):
            return self.accessTokenResp.data["refresh_token"]
        return ""

    def getExpiresIn(self):
        if self.accessTokenResp is not None and hasattr(self.accessTokenResp, "data"):
            return self.accessTokenResp.data["expires_in"]
        return 0

    def getScope(self):
        if self.accessTokenResp is not None and hasattr(self.accessTokenResp, "data"):
            return self.accessTokenResp.data["scope"]
        return ""

    def getShopId(self):
        if self.accessTokenResp is not None and hasattr(self.accessTokenResp, "data"):
            return self.accessTokenResp.data["shop_id"]
        return 0

    def getShopName(self):
        if self.accessTokenResp is not None and hasattr(self.accessTokenResp, "data"):
            return self.accessTokenResp.data["shop_name"]
        return ""

    def getAuthorityId(self):
        if self.accessTokenResp is not None and hasattr(self.accessTokenResp, "data"):
            return self.accessTokenResp.data["authority_id"]
        return ""

    def getShopBizType(self):
        if self.accessTokenResp is not None and hasattr(self.accessTokenResp, "data"):
            return self.accessTokenResp.data["shop_biz_type"]
        return ""

    def isSuccess(self):
        return self.accessTokenResp is not None and self.accessTokenResp.isSuccess()
