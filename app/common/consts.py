JWT_SECRET = "ABCD1234!"
JWT_ALGORITHM = "HS256"
EXCEPT_PATH_LIST = ["/", "/openapi.json"]
EXCEPT_PATH_REGEX = "^(/docs|/redoc|/api/auth)"     # 토큰 검사 예외 경로
MAX_API_KEY = 1000
MAX_API_WHITELIST = 10
