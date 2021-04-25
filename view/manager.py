# # coding: utf-8
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.Qt import QLineEdit
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore
from wordTemplates.WordTemplates import Docxtpl
from view.message import Message
import json
import re


class Manager(QtCore.QThread):
    signal = pyqtSignal(str)

    def __del__(self):
        self.wait()

    def __init__(self):
        # 执行当前类的初始化方法
        super(Manager, self).__init__()
        # 容器组件
        self.Qwidgetlayout = QWidget()
        # 这是组件名称
        self.Qwidgetlayout.setObjectName("Qwidgetlayout")
        self.Qwidgetlayout.setFixedHeight(900)

        self.school_num = QLabel(self.Qwidgetlayout)
        self.school_num.setFont(QFont("Microsoft YaHei"))
        self.school_num.setGeometry(QtCore.QRect(0, 10, 100, 20))
        self.school_num.setText("学号：")
        self.school_num_input = QLineEdit(self.Qwidgetlayout)
        self.school_num_input.setText('')
        self.school_num_input.setGeometry(QtCore.QRect(50, 10, 150, 20))

        self.year_label = QLabel(self.Qwidgetlayout)
        self.year_label.setFont(QFont("Microsoft YaHei"))
        self.year_label.setGeometry(QtCore.QRect(220, 10, 100, 20))
        self.year_label.setText("年：")
        self.year_input = QLineEdit(self.Qwidgetlayout)
        self.year_input.setText('')
        self.year_input.setGeometry(QtCore.QRect(250, 10, 150, 20))

        self.reason_label = QLabel(self.Qwidgetlayout)
        self.reason_label.setFont(QFont("Microsoft YaHei"))
        self.reason_label.setGeometry(QtCore.QRect(420, 10, 100, 20))
        self.reason_label.setText("季度：")
        self.reason_input = QLineEdit(self.Qwidgetlayout)
        self.reason_input.setText('')
        self.reason_input.setGeometry(QtCore.QRect(460, 10, 150, 20))

        self.week_label = QLabel(self.Qwidgetlayout)
        self.week_label.setFont(QFont("Microsoft YaHei"))
        self.week_label.setGeometry(QtCore.QRect(620, 10, 100, 20))
        self.week_label.setText("周：")
        self.week_input = QLineEdit(self.Qwidgetlayout)
        self.week_input.setText('')
        self.week_input.setGeometry(QtCore.QRect(650, 10, 150, 20))
        #

        self.xingqi_label = QLabel(self.Qwidgetlayout)
        self.xingqi_label.setFont(QFont("Microsoft YaHei"))
        self.xingqi_label.setGeometry(QtCore.QRect(800, 10, 100, 20))
        self.xingqi_label.setText("上课星期：")
        self.xingqi_input = QLineEdit(self.Qwidgetlayout)
        self.xingqi_input.setText('')
        self.xingqi_input.setGeometry(QtCore.QRect(860, 10, 150, 20))

        self.lesson_num_label = QLabel(self.Qwidgetlayout)
        self.lesson_num_label.setFont(QFont("Microsoft YaHei"))
        self.lesson_num_label.setGeometry(QtCore.QRect(1030, 10, 100, 20))
        self.lesson_num_label.setText("第几节课：")
        self.lesson_num_input = QLineEdit(self.Qwidgetlayout)
        self.lesson_num_input.setText('')
        self.lesson_num_input.setGeometry(QtCore.QRect(1100, 10, 150, 20))

        self.student_name_label = QLabel(self.Qwidgetlayout)
        self.student_name_label.setFont(QFont("Microsoft YaHei"))
        self.student_name_label.setGeometry(QtCore.QRect(0, 40, 100, 20))
        self.student_name_label.setText("学生姓名：")
        self.student_name_input = QLineEdit(self.Qwidgetlayout)
        self.student_name_input.setText('')
        self.student_name_input.setGeometry(QtCore.QRect(50, 40, 150, 20))

        self.professional_class_label = QLabel(self.Qwidgetlayout)
        self.professional_class_label.setFont(QFont("Microsoft YaHei"))
        self.professional_class_label.setGeometry(QtCore.QRect(220, 40, 100, 20))
        self.professional_class_label.setText("专业班级：")
        self.professional_class_input = QLineEdit(self.Qwidgetlayout)
        self.professional_class_input.setText('')
        self.professional_class_input.setGeometry(QtCore.QRect(280, 40, 150, 20))

        self.project_name_label = QLabel(self.Qwidgetlayout)
        self.project_name_label.setFont(QFont("Microsoft YaHei"))
        self.project_name_label.setGeometry(QtCore.QRect(450, 40, 100, 20))
        self.project_name_label.setText("项目名称：")
        self.project_name_input = QLineEdit(self.Qwidgetlayout)
        self.project_name_input.setText('')
        self.project_name_input.setGeometry(QtCore.QRect(520, 40, 150, 20))

        self.project_hours_label = QLabel(self.Qwidgetlayout)
        self.project_hours_label.setFont(QFont("Microsoft YaHei"))
        self.project_hours_label.setGeometry(QtCore.QRect(680, 40, 100, 20))
        self.project_hours_label.setText("项目学时：")
        self.project_hours_input = QLineEdit(self.Qwidgetlayout)
        self.project_hours_input.setText('')
        self.project_hours_input.setGeometry(QtCore.QRect(740, 40, 150, 20))

        self.teacher_label = QLabel(self.Qwidgetlayout)
        self.teacher_label.setFont(QFont("Microsoft YaHei"))
        self.teacher_label.setGeometry(QtCore.QRect(910, 40, 100, 20))
        self.teacher_label.setText("指导教师：")
        self.teacher_input = QLineEdit(self.Qwidgetlayout)
        self.teacher_input.setText('')
        self.teacher_input.setGeometry(QtCore.QRect(980, 40, 150, 20))

        self.score_label = QLabel(self.Qwidgetlayout)
        self.score_label.setFont(QFont("Microsoft YaHei"))
        self.score_label.setGeometry(QtCore.QRect(1150, 40, 100, 20))
        self.score_label.setText("实验成绩：")
        self.score_input = QLineEdit(self.Qwidgetlayout)
        self.score_input.setText('')
        self.score_input.setGeometry(QtCore.QRect(1220, 40, 150, 20))

        self.experiment_project_label = QLabel(self.Qwidgetlayout)
        self.experiment_project_label.setFont(QFont("Microsoft YaHei"))
        self.experiment_project_label.setGeometry(QtCore.QRect(0, 70, 100, 20))
        self.experiment_project_label.setText("实验项目：")
        self.experiment_project_input = QLineEdit(self.Qwidgetlayout)
        self.experiment_project_input.setText('')
        self.experiment_project_input.setGeometry(QtCore.QRect(150, 70, 1200, 20))

        self.purpose_label = QLabel(self.Qwidgetlayout)
        self.purpose_label.setFont(QFont("Microsoft YaHei"))
        self.purpose_label.setGeometry(QtCore.QRect(0, 100, 100, 20))
        self.purpose_label.setText("实验目的：")
        self.purpose_input = QLineEdit(self.Qwidgetlayout)
        self.purpose_input.setText('')
        self.purpose_input.setGeometry(QtCore.QRect(150, 100, 1200, 60))

        self.experimental_equipment_label = QLabel(self.Qwidgetlayout)
        self.experimental_equipment_label.setFont(QFont("Microsoft YaHei"))
        self.experimental_equipment_label.setGeometry(QtCore.QRect(0, 170, 100, 20))
        self.experimental_equipment_label.setText("实验设备：")
        self.experimental_equipment_input = QLineEdit(self.Qwidgetlayout)
        self.experimental_equipment_input.setText('')
        self.experimental_equipment_input.setGeometry(QtCore.QRect(150, 170, 1200, 60))

        self.principle_label = QLabel(self.Qwidgetlayout)
        self.principle_label.setFont(QFont("Microsoft YaHei"))
        self.principle_label.setGeometry(QtCore.QRect(0, 240, 100, 20))
        self.principle_label.setText("实验原理：")
        self.principle_input = QLineEdit(self.Qwidgetlayout)
        self.principle_input.setText('')
        self.principle_input.setGeometry(QtCore.QRect(150, 240, 1200, 60))

        self.step_label = QLabel(self.Qwidgetlayout)
        self.step_label.setFont(QFont("Microsoft YaHei"))
        self.step_label.setGeometry(QtCore.QRect(0, 310, 100, 20))
        self.step_label.setText("实验步骤：")
        self.step_input = QLineEdit(self.Qwidgetlayout)
        self.step_input.setText('')
        self.step_input.setGeometry(QtCore.QRect(150, 310, 1200, 60))

        self.operation_recording_label = QLabel(self.Qwidgetlayout)
        self.operation_recording_label.setFont(QFont("Microsoft YaHei"))
        self.operation_recording_label.setGeometry(QtCore.QRect(0, 380, 150, 20))
        self.operation_recording_label.setText("实验操作及数据记录：")
        self.operation_recording_input = QLineEdit(self.Qwidgetlayout)
        self.operation_recording_input.setText('')
        self.operation_recording_input.setGeometry(QtCore.QRect(150, 380, 1200, 60))

        self.data_processing_label = QLabel(self.Qwidgetlayout)
        self.data_processing_label.setFont(QFont("Microsoft YaHei"))
        self.data_processing_label.setGeometry(QtCore.QRect(0, 450, 150, 20))
        self.data_processing_label.setText("实验数据处理：")
        self.data_processing_input = QLineEdit(self.Qwidgetlayout)
        self.data_processing_input.setText('')
        self.data_processing_input.setGeometry(QtCore.QRect(150, 450, 1200, 60))

        self.conclusion_label = QLabel(self.Qwidgetlayout)
        self.conclusion_label.setFont(QFont("Microsoft YaHei"))
        self.conclusion_label.setGeometry(QtCore.QRect(0, 520, 150, 20))
        self.conclusion_label.setText("实验结论：")
        self.conclusion_input = QLineEdit(self.Qwidgetlayout)
        self.conclusion_input.setText('')
        self.conclusion_input.setGeometry(QtCore.QRect(150, 520, 1200, 60))

        self.error_analysis_label = QLabel(self.Qwidgetlayout)
        self.error_analysis_label.setFont(QFont("Microsoft YaHei"))
        self.error_analysis_label.setGeometry(QtCore.QRect(0, 590, 150, 20))
        self.error_analysis_label.setText("系统误差的分析：")
        self.error_analysis_input = QLineEdit(self.Qwidgetlayout)
        self.error_analysis_input.setText('')
        self.error_analysis_input.setGeometry(QtCore.QRect(150, 590, 1200, 60))

        self.summary_label = QLabel(self.Qwidgetlayout)
        self.summary_label.setFont(QFont("Microsoft YaHei"))
        self.summary_label.setGeometry(QtCore.QRect(0, 660, 150, 20))
        self.summary_label.setText("实验总结：")
        self.summary_input = QLineEdit(self.Qwidgetlayout)
        self.summary_input.setText('')
        self.summary_input.setGeometry(QtCore.QRect(150, 660, 1200, 60))

        self.score_preview_label = QLabel(self.Qwidgetlayout)
        self.score_preview_label.setFont(QFont("Microsoft YaHei"))
        self.score_preview_label.setGeometry(QtCore.QRect(0, 730, 80, 20))
        self.score_preview_label.setText("成绩_预习：")
        self.score_preview_input = QLineEdit(self.Qwidgetlayout)
        self.score_preview_input.setText('')
        self.score_preview_input.setGeometry(QtCore.QRect(80, 730, 100, 20))

        self.score_preview_label = QLabel(self.Qwidgetlayout)
        self.score_preview_label.setFont(QFont("Microsoft YaHei"))
        self.score_preview_label.setGeometry(QtCore.QRect(200, 730, 150, 20))
        self.score_preview_label.setText("成绩_出勤和课堂纪律：")
        self.score_preview_input = QLineEdit(self.Qwidgetlayout)
        self.score_preview_input.setText('')
        self.score_preview_input.setGeometry(QtCore.QRect(330, 730, 100, 20))

        self.score_operation_performance_label = QLabel(self.Qwidgetlayout)
        self.score_operation_performance_label.setFont(QFont("Microsoft YaHei"))
        self.score_operation_performance_label.setGeometry(QtCore.QRect(460, 730, 150, 20))
        self.score_operation_performance_label.setText("成绩_操作表现：")
        self.score_operation_performance_input = QLineEdit(self.Qwidgetlayout)
        self.score_operation_performance_input.setText('')
        self.score_operation_performance_input.setGeometry(QtCore.QRect(560, 730, 100, 20))

        self.score_data_processing_label = QLabel(self.Qwidgetlayout)
        self.score_data_processing_label.setFont(QFont("Microsoft YaHei"))
        self.score_data_processing_label.setGeometry(QtCore.QRect(700, 730, 150, 20))
        self.score_data_processing_label.setText("成绩_数据处理：")
        self.score_data_processing_input = QLineEdit(self.Qwidgetlayout)
        self.score_data_processing_input.setText('')
        self.score_data_processing_input.setGeometry(QtCore.QRect(800, 730, 100, 20))


        self.score_error_analysis_label = QLabel(self.Qwidgetlayout)
        self.score_error_analysis_label.setFont(QFont("Microsoft YaHei"))
        self.score_error_analysis_label.setGeometry(QtCore.QRect(930, 730, 150, 20))
        self.score_error_analysis_label.setText("成绩_误差分析：")
        self.score_error_analysis_input = QLineEdit(self.Qwidgetlayout)
        self.score_error_analysis_input.setText('')
        self.score_error_analysis_input.setGeometry(QtCore.QRect(1020, 730, 100, 20))

        self.score_report_writing_label = QLabel(self.Qwidgetlayout)
        self.score_report_writing_label.setFont(QFont("Microsoft YaHei"))
        self.score_report_writing_label.setGeometry(QtCore.QRect(1140, 730, 150, 20))
        self.score_report_writing_label.setText("成绩_报告书写：")
        self.score_report_writing_input = QLineEdit(self.Qwidgetlayout)
        self.score_report_writing_input.setText('')
        self.score_report_writing_input.setGeometry(QtCore.QRect(1250, 730, 100, 20))

        self.btn_start = QPushButton(self.Qwidgetlayout)
        self.btn_start.setFont(QFont("Microsoft YaHei"))
        self.btn_start.setGeometry(QtCore.QRect(0, 760, 150, 20))
        self.btn_start.setText("生成模板")
        self.btn_start.setObjectName("btn_start")
        self.btn_start.clicked.connect(self.genTemplate)

    def genTemplate(self):
        imgs = re.findall("<img src='(.+)'>", self.operation_recording_input.text())
        data = {
            "school_num": self.school_num_input.text(),
            "year": self.year_input.text(),
            "reason": self.reason_input.text(),
            "week": self.week_input.text(),
            "xingqi": self.xingqi_input.text(),
            "lesson_num": self.lesson_num_input.text(),
            "student_name": self.student_name_input.text(),
            "professional_class": self.professional_class_input.text(),
            "project_name": self.project_name_input.text(),
            "project_hours": self.project_hours_input.text(),
            "teacher": self.teacher_input.text(),
            "score": self.score_input.text(),
            "experiment_project": self.experiment_project_input.text(),
            "purpose": self.purpose_input.text(),
            "principle": self.principle_input.text(),
            "step": self.step_input.text(),
            "operation_recording": self.operation_recording_input.text(),
            "data_processing": self.data_processing_input.text(),
            "conclusion": self.conclusion_input.text(),
            "error_analysis": self.error_analysis_input.text(),
            "summaryt": self.summary_input.text(),
            "score_preview": self.score_preview_input.text(),
            "score_attendance_classroom_discipline": self.score_preview_input.text(),
            "score_operation_performance": self.score_operation_performance_input.text(),
            "score_data_processing": self.score_data_processing_input.text(),
            "score_error_analysis": self.score_error_analysis_input.text(),
            "score_report_writing": self.score_report_writing_input.text(),
            "experimental_equipment":  self.parse_json(self.experimental_equipment_input.text()),
            "imgs": imgs
        }
        if Docxtpl.genarater(data):
            Message.tips("模板成功！")


    def parse_json(self, s):
        try:
            return json.loads(s)
        except:
            return []