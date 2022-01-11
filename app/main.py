from dataclasses import asdict
from typing import Optional

import uvicorn
from fastapi import FastAPI

from app.common.config import conf
from app.database.conn import db, Base
from app.routes import index, auth


def create_app():
    """
    앱 함수 실행
    :return:
    """
    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)
    Base.metadata.create_all(db.engine)

    # DB initialize

    # redis initialize

    # middleware define

    # routes define
    app.include_router(index.router)
    app.include_router(auth.router, tags=["Authentication"], prefix="/auth")
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
