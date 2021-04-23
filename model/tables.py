# -*- coding: utf-8 -*-
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import datetime
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'comment': '用户'}
    id = Column(Integer, autoincrement=True, primary_key=True, comment='id')
    collect_date = Column(DateTime, default=datetime.datetime.now, comment='时间')

    username = Column(String(255), comment='用户名')
    password = Column(String(255), comment='密码')


class Info(Base):
    __tablename__ = 'info'
    __table_args__ = {'comment': '用户'}
    id = Column(Integer, autoincrement=True, primary_key=True, comment='id')
    collect_date = Column(DateTime, default=datetime.datetime.now, comment='时间')

    school_num = Column(String(255) , comment='学号')
    year = Column(String(255), comment='年')
    reason = Column(String(255),  comment='季度')
    week = Column(String(255),  comment='第几周')
    xingqi = Column(String(255),  comment='上课星期几')
    lesson_num = Column(String(255),  comment='第几节课')
    student_name = Column(String(255),  comment='学生姓名')
    professional_class = Column(String(255),  comment='专业班级')
    project_name = Column(String(255),  comment='项目名称')
    project_hours = Column(String(255),  comment='项目学时')
    teacher = Column(String(255),  comment='指导教师')
    score = Column(String(255),  comment='实验成绩')
    experiment_project = Column(String(255),  comment='实验项目')

    purpose = Column(Text,  comment='实验目的')
    experimental_equipment = Column(Text,  comment='实验设备')
    principle = Column(Text,  comment='实验原理')
    step = Column(Text,  comment='实验步骤')
    operation_recording = Column(Text,  comment='实验操作及数据记录')
    data_processing = Column(Text,  comment='实验数据处理')
    conclusion = Column(Text,  comment='实验结论')
    error_analysis = Column(Text,  comment='系统误差的分析')
    summary = Column(Text,  comment='实验总结')

    score_preview = Column(String(255),  comment='实验成绩评定_预习')
    score_attendance_classroom_discipline = Column(String(255),  comment='实验成绩评定_出勤和课堂纪律')
    score_operation_performance = Column(String(255),  comment='实验成绩评定_操作表现')
    score_data_processing = Column(String(255),  comment='实验成绩评定_数据处理')
    score_error_analysis = Column(String(255),  comment='实验成绩评定_误差分析')
    score_report_writing = Column(String(255),  comment='实验成绩评定_报告书写')
    score_score = Column(String(255),  comment='实验成绩评定_实验成绩')
