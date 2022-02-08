from app.common.consts import MAX_API_KEY, MAX_API_WHITELIST


class StatusCode:
    HTTP_500 = 500
    HTTP_400 = 400
    HTTP_401 = 401
    HTTP_403 = 403
    HTTP_404 = 404
    HTTP_405 = 405


class APIException(Exception):
    status_code: int
    code: str
    msg: str
    detail: str
    ex: Exception

    def __init__(
            self,
            *,
            status_code: int = StatusCode.HTTP_500,
            code: str = "000000",
            msg: str = None,
            detail: str = None,
            ex: Exception = None,
    ):
        self.status_code = status_code
        self.code = code
        self.msg = msg
        self.detail = detail
        self.ex = ex
        super().__init__(ex)


# 현업에서는 detail과 error code 정도만 보내주면 frontend에서 사용자 친화적으로 메시지를 구성해 전달한다.
# 서비스 규모가 커지면 늘어나는 exception을 DB화 해 관리한다.
class NotFoundUserEx(APIException):
    def __init__(self, user_id: int = None, ex: Exception = None):
        super().__init__(
            status_code=StatusCode.HTTP_404,
            msg=f"Not Found User.",
            detail=f"Not Found User ID : {user_id}",
            code=f"{StatusCode.HTTP_404}{'1'.zfill(4)}",
            ex=ex,
        )


class NotAuthorized(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=StatusCode.HTTP_401,
            msg=f"You need to Log In.",
            detail=f"Authorized Required",
            code=f"{StatusCode.HTTP_401}{'1'.zfill(4)}",
            ex=ex,
        )


class TokenExpiredEx(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=StatusCode.HTTP_400,
            msg=f"Token Expired",
            detail=f"Token Expired",
            code=f"{StatusCode.HTTP_400}{'1'.zfill(4)}",
            ex=ex,
        )


class TokenDecodeEx(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=StatusCode.HTTP_400,
            msg=f"Uncommon Access",
            detail=f"Token has been compromised.",
            code=f"{StatusCode.HTTP_400}{'2'.zfill(4)}",
            ex=ex,
        )


class NoKeyMatchEx(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=StatusCode.HTTP_404,
            msg=f"해당 키에 대한 권한이 없거나 해당 키가 없습니다.",
            detail="No keys Matched.",
            code=f"{StatusCode.HTTP_404}{'3'.zfill(4)}",
            ex=ex,
        )


class MaxKeyCountEx(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=StatusCode.HTTP_400,
            msg=f"API 키 생성은 {MAX_API_KEY}까지 가능합니다.",
            detail="Max Key Count Reached.",
            code=f"{StatusCode.HTTP_400}{'3'.zfill(4)}",
            ex=ex,
        )


class MaxWLCountEx(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=StatusCode.HTTP_400,
            msg=f"White List 생성은 {MAX_API_WHITELIST}개 까지 가능합니다.",
            detail="Max Whitelist Count Reached",
            code=f"{StatusCode.HTTP_400}{'5'.zfill(4)}",
            ex=ex,
        )


class InvalidIpEx(APIException):
    def __init__(self, ip: str, ex: Exception = None):
        super().__init__(
            status_code=StatusCode.HTTP_400,
            msg=f"{ip}는 올바른 IP가 아닙니다.",
            detail=f"Invalid IP : {ip}",
            code=f"{StatusCode.HTTP_400}{'6'.zfill(4)}",
            ex=ex,
        )


class SqlFailureEx(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=StatusCode.HTTP_500,
            msg=f"서버 에러입니다. 자동으로 리포팅되며, 빠르게 수정하겠습니다.",
            detail="Inter Server Error",
            code=f"{StatusCode.HTTP_500}{'2'.zfill(4)}",
            ex=ex,
        )


class APIQueryStringEx(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=StatusCode.HTTP_400,
            msg=f"쿼리스트링은 key, timestamp 2개만 허용되며, 2개 모두 요청시 제출되어야 합니다.",
            detail="Query String Only Accept key and timestamp.",
            code=f"{StatusCode.HTTP_400}{'7'.zfill(4)}",
            ex=ex,
        )


class APIHeaderInvalidEx(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=StatusCode.HTTP_400,
            msg=f"헤더에 키 해싱된 Secret이 없거나, 유효하지 않습니다.",
            detail="Invalid HMAC secret in Header.",
            code=f"{StatusCode.HTTP_400}{'8'.zfill(4)}",
            ex=ex,
        )


class APITimestampEx(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=StatusCode.HTTP_400,
            msg=f"쿼리스트링에 포함된 타임스탬프는 KST이며, 현재 시간보다 작아야 하고, 현재 시간 -10초 보다는 커야 합니다.",
            detail="timestamp in Query String must be KST, Timestamp must be less than now, and greater than now - 10.",
            code=f"{StatusCode.HTTP_400}{'9'.zfill(4)}",
            ex=ex,
        )


class NotFoundAccessKeyEx(APIException):
    def __init__(self, api_key: str, ex: Exception = None):
        super().__init__(
            status_code=StatusCode.HTTP_404,
            msg=f"API 키를 찾을 수 없습니다.",
            detail=f"Not found such API Access Key : {api_key}.",
            code=f"{StatusCode.HTTP_400}{'10'.zfill(4)}",
            ex=ex,
        )


class KakaoSendFailureEx(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=StatusCode.HTTP_400,
            msg=f"카카오톡 전송에 실패했습니다.",
            detail=f"Failed to send KAKAO MSG.",
            code=f"{StatusCode.HTTP_400}{'11'.zfill(4)}",
            ex=ex,
        )