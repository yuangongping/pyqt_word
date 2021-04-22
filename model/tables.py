# -*- coding: utf-8 -*-
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import datetime
Base = declarative_base()


class Production(Base):
    __tablename__ = 'movie'
    __table_args__ = {'comment': '电影'}
    id = Column(Integer, autoincrement=True, primary_key=True, comment='id')
    collect_date = Column(DateTime, default=datetime.datetime.now, comment='数据采集时间')

    name = Column(String(255), unique=True, comment='名称')
    rank = Column(String(255), comment='评分')
    num = Column(String(255), comment='评价数')
    description = Column(Text, comment='电影概况', default="")
    url = Column(String(255), comment='链接', default="")
    director = Column(String(255), comment='导演', default="")
    screenwriter = Column(String(255), comment='编剧', default="")
    main_role = Column(String(255), comment='主演', default="")
    year = Column(String(255), comment='上映日期', default="")
    type = Column(String(255), comment='类型', default="")
    time = Column(String(255), comment='片长', default="")
