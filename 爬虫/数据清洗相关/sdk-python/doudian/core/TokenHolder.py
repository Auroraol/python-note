import threading
import time

from doudian.core.AccessTokenBuilder import AccessTokenBuilder


class TokenHolder:
    tokenHolderDTOMap = {}

    @staticmethod
    def getToken(authId=None):
        if authId is None:
            authId = threading.current_thread().__dict__.get('authId', '')
            if authId is None or len(authId) == 0:
                raise Exception('The AuthId is empty!')

        token = TokenHolder.tokenHolderDTOMap.get(authId, '')
        if len(token) == 0 or TokenHolder.isTokenExpired(token):
            token = TokenHolder.generateTokenByRemote(authId)

        return token.get('access_token')

    @staticmethod
    def isTokenExpired(token: dict) -> bool:
        return int(time.time()) > token.get('expire_time')

    @staticmethod
    def generateTokenByRemote(authId) -> dict:
        token = AccessTokenBuilder.buildTokenByShopId(authId)
        TokenHolder.tokenHolderDTOMap[authId] = {
            'access_token': token,
            # 过期前一个小时即可刷新
            'expire_time': (token.getExpiresIn() - 3600) + int(time.time())
        }
        return TokenHolder.tokenHolderDTOMap[authId]

    @staticmethod
    def refreshToken(authId=None):
        if authId is None:
            authId = threading.current_thread().__dict__.get('authId', '')
            if authId is None or len(authId) == 0:
                raise Exception('The AuthId is empty!')

        token = TokenHolder.generateTokenByRemote(authId)

        return token.get('access_token')
