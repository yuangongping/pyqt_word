# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .tables import Base


def create_engine_by_conf():
    return create_engine("sqlite:///experiment.db")


def make_session(engine):
    # 自动建表
    Base.metadata.create_all(engine)
    # 绑定引擎
    Session = sessionmaker(bind=engine)
    # 生成session
    session = Session()
    return session

