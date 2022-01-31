from app.database.conn import db
from app.database.schema import Users


def test_registration(client, session):
    """
    레버로그인
    :param client:
    :param session:
    :return:
    """
    user = dict(email="berzzubunny@gmail.com", pw="1111", name="Daniel Kim", phone="01050128587")
    res = client.post("api/auth/registration/email", json=user)
    res_body = res.json()
    print(res.json())
    assert res.status_code == 201
    assert "Authorization" in res_body.keys()


def test_registration_exist_email(client, session):
    """
    레버로그인
    :param client:
    :param session:
    :return:
    """
    user = dict(email="bunnycast@naver.com", pw="1111", name="이를 본 네티즌", phone="01050128587")
    db_user = Users.create(session=session, **user)
    session.commit()
    res = client.post("api/auth/register/email", json=user)
    res_body = res.json()
    assert res.status_code == 400
    assert "EMAIL_EXISTS" == res_body["msg"]
