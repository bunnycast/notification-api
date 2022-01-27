import json

import requests
from fastapi import APIRouter
from fastapi.logger import logger
from starlette.requests import Request

from app.errors import exceptions as ex

from app.models import MessageOk


router = APIRouter(prefix="/services")


@router.get("")
async def get_all_services(request: Request):
    return dict(your_email=request.state.user.email)


@router.post("/kakao/send")
async def send_kakao(request: Request):
    token = ""
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/x-www-form-urlencoded"}
    body = dict(objedct_type="text", text="Bunnycast Sample for FastAPI", link=dict(web_url=""), button_title="지금 확인")
    data = {"template_object": json.dumps(body, ensure_ascii=False)}

    res = requests.post("https://kapi.kakao.com/v2/api/talk/memo/default/send", headers=headers, data=data)
    try:
        res.raise_for_status()
        if res.json()["result_code"] != 0:
            raise Exception("KAKAO SEND FAILED")
    except Exception as e:
        print(res.json())
        logger.warnign(e)
        raise ex.KakaoSendFailureEx

    return MessageOk()
