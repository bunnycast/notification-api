from dataclasses import asdict
from typing import Optional

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import APIKeyHeader
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware

from app.common.config import conf
from app.common.consts import EXCEPT_PATH_LIST, EXCEPT_PATH_REGEX
from app.database.conn import db, Base
from app.middlewares.token_validator import access_control
from app.middlewares.trusted_hosts import TrustedHostMiddleware
from app.routes import index, auth, users, services


API_KEY_HEADER = APIKeyHeader(name="Authorization", auto_error=False)


def create_app():
    """
    앱 함수 실행
    :return:
    """
    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)

    # DB initialize

    # redis initialize

    # middleware define
    app.add_middleware(middleware_class=BaseHTTPMiddleware, dispatch=access_control)
    app.add_middleware(     # Backend와 Frontend 주소가 달라도 연동이 되게 함
        CORSMiddleware,
        allow_origins=conf().ALLOW_SITE,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=conf().TRUSTED_HOSTS, except_path=["/health"])

    # routes define
    app.include_router(index.router)
    app.include_router(auth.router, tags=["Authentication"], prefix="/api")
    if conf().DEBUG:
        app.include_router(services.router, tags=["Services"], prefix="/api", dependencies=[Depends(API_KEY_HEADER)])
    else:
        app.include_router(services.router, tags=["Services"], prefix="/api")
    app.include_router(users.router, tags=["users"], prefix="/api", dependencies=[Depends(API_KEY_HEADER)])
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
