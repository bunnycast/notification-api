from typing import Optional

import uvicorn
from fastapi import FastAPI

from app.common.config import conf


def create_app():
    """
    앱 함수 실행
    :return:
    """
    c = conf()
    app = FastAPI()

    # DB initialize

    # redis initialize

    # middleware define

    # router define

    return app

app = create_app()

if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=800, reload=True)