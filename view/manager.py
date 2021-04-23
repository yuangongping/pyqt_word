# # coding: utf-8
from PyQt5.QtWidgets import QFormLayout, QWidget, QLabel, QPushButton, QGridLayout
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from PyQt5.Qt import QLineEdit
from PyQt5.QtCore import pyqtSignal


class Manager(QtCore.QThread):
    signal = pyqtSignal(str)

    def __del__(self):
        self.wait()

    def __init__(self):
        # 执行当前类的初始化方法
        super(Manager, self).__init__()
        # 表单组件
        self.manager_layout = QGridLayout()
        # 设置垂直方向的间隙
        self.manager_layout.setVerticalSpacing(20)
        # 容器组件
        self.Qwidgetlayout = QWidget()
        # 设置容器布局为表单布局
        self.Qwidgetlayout.setLayout(self.manager_layout)
        # 这是组件名称
        self.Qwidgetlayout.setObjectName("Qwidgetlayout")


        self.school_num = QLabel("学号：")
        self.school_num.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.school_num, 0,0,1,1,Qt.AlignLeft)
        self.school_num_input = QLineEdit()
        self.school_num_input.setText('')
        self.manager_layout.addWidget(self.school_num_input, 0, 2,1,8, Qt.AlignLeft)
        self.year_label = QLabel("年：")
        self.year_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.year_label, 0, 10,1,1)
        self.year_input = QLineEdit()
        self.year_input.setEchoMode(QLineEdit.Password)
        self.year_input.setText('')
        self.manager_layout.addWidget(self.year_input,0,11,1,6)


        self.reason_label = QLabel("季度：")
        self.reason_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.reason_label, 1, 0, 1, 1, Qt.AlignLeft)
        self.reason_input = QLineEdit()
        self.reason_input.setPlaceholderText("")
        self.reason_input.setText('')
        self.manager_layout.addWidget(self.reason_input, 1, 2, 1, 8, Qt.AlignLeft)

        self.week_label = QLabel("第几周：")
        self.week_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.week_label, 1, 10, 1, 1, Qt.AlignLeft)
        self.week_input = QLineEdit()
        self.week_input.setPlaceholderText("")
        self.week_input.setText('')
        self.manager_layout.addWidget(self.week_input, 1, 11, 1, 6,  Qt.AlignLeft)

        self.xingqi_label = QLabel("上课星期：")
        self.xingqi_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.reason_label, 1, 0, 1, 1, Qt.AlignLeft)
        self.xingqi_input = QLineEdit()
        self.xingqi_input.setPlaceholderText("")
        self.xingqi_input.setText('')
        self.manager_layout.addWidget(self.reason_input, 1, 2, 1, 8, Qt.AlignLeft)

        self.lesson_num_label = QLabel("第几节课：")
        self.lesson_num_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.week_label, 1, 10, 1, 1, Qt.AlignLeft)
        self.lesson_num_input = QLineEdit()
        self.lesson_num_input.setPlaceholderText("")
        self.lesson_num_input.setText('')
        self.manager_layout.addWidget(self.week_input, 1, 11, 1, 6, Qt.AlignLeft)

        self.student_name_label = QLabel("学生姓名：")
        self.student_name_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.reason_label, 1, 0, 1, 1, Qt.AlignLeft)
        self.student_name_input = QLineEdit()
        self.student_name_input.setPlaceholderText("")
        self.student_name_input.setText('')
        self.manager_layout.addWidget(self.reason_input, 1, 2, 1, 8, Qt.AlignLeft)

        self.professional_class_label = QLabel("专业班级：")
        self.professional_class_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.week_label, 1, 10, 1, 1, Qt.AlignLeft)
        self.professional_class_input = QLineEdit()
        self.professional_class_input.setPlaceholderText("")
        self.professional_class_input.setText('')
        self.manager_layout.addWidget(self.week_input, 1, 11, 1, 6, Qt.AlignLeft)

        self.project_name_label = QLabel("项目名称：")
        self.project_name_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.reason_label, 1, 0, 1, 1, Qt.AlignLeft)
        self.project_name_input = QLineEdit()
        self.project_name_input.setPlaceholderText("")
        self.project_name_input.setText('')
        self.manager_layout.addWidget(self.reason_input, 1, 2, 1, 8, Qt.AlignLeft)

        self.project_hours_label = QLabel("项目学时：")
        self.project_hours_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.week_label, 1, 10, 1, 1, Qt.AlignLeft)
        self.project_hours_input = QLineEdit()
        self.project_hours_input.setPlaceholderText("")
        self.project_hours_input.setText('')
        self.manager_layout.addWidget(self.week_input, 1, 11, 1, 6, Qt.AlignLeft)

        self.teacher_label = QLabel("指导教师：")
        self.teacher_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.reason_label, 1, 0, 1, 1, Qt.AlignLeft)
        self.teacher_input = QLineEdit()
        self.teacher_input.setPlaceholderText("")
        self.teacher_input.setText('')
        self.manager_layout.addWidget(self.reason_input, 1, 2, 1, 8, Qt.AlignLeft)

        self.score_label = QLabel("实验成绩：")
        self.score_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.week_label, 1, 10, 1, 1, Qt.AlignLeft)
        self.score_input = QLineEdit()
        self.score_input.setPlaceholderText("")
        self.score_input.setText('')
        self.manager_layout.addWidget(self.week_input, 1, 11, 1, 6, Qt.AlignLeft)

        self.experiment_project_label = QLabel("实验项目：")
        self.experiment_project_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.reason_label, 1, 0, 1, 1, Qt.AlignLeft)
        self.experiment_project_input = QLineEdit()
        self.experiment_project_input.setPlaceholderText("")
        self.experiment_project_input.setText('')
        self.manager_layout.addWidget(self.reason_input, 1, 2, 1, 8, Qt.AlignLeft)

        self.purpose_label = QLabel("实验目的：")
        self.purpose_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.week_label, 1, 10, 1, 1, Qt.AlignLeft)
        self.purpose_input = QLineEdit()
        self.purpose_input.setPlaceholderText("")
        self.purpose_input.setText('')
        self.manager_layout.addWidget(self.week_input, 1, 11, 1, 6, Qt.AlignLeft)

        self.principle_label = QLabel("实验原理：")
        self.principle_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.reason_label, 1, 0, 1, 1, Qt.AlignLeft)
        self.principle_input = QLineEdit()
        self.principle_input.setPlaceholderText("")
        self.principle_input.setText('')
        self.manager_layout.addWidget(self.reason_input, 1, 2, 1, 8, Qt.AlignLeft)


        self.step_label = QLabel("实验步骤：")
        self.step_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.week_label, 1, 10, 1, 1, Qt.AlignLeft)
        self.step_input = QLineEdit()
        self.step_input.setPlaceholderText("")
        self.step_input.setText('')
        self.manager_layout.addWidget(self.week_input, 1, 11, 1, 6, Qt.AlignLeft)

        self.operation_recording_label = QLabel("实验操作及数据记录：")
        self.operation_recording_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.reason_label, 1, 0, 1, 1, Qt.AlignLeft)
        self.operation_recording_input = QLineEdit()
        self.operation_recording_input.setPlaceholderText("")
        self.operation_recording_input.setText('')
        self.manager_layout.addWidget(self.reason_input, 1, 2, 1, 8, Qt.AlignLeft)

        self.data_processing_label = QLabel("实验数据处理：")
        self.data_processing_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.week_label, 1, 10, 1, 1, Qt.AlignLeft)
        self.data_processing_input = QLineEdit()
        self.data_processing_input.setPlaceholderText("")
        self.data_processing_input.setText('')
        self.manager_layout.addWidget(self.week_input, 1, 11, 1, 6, Qt.AlignLeft)

        self.conclusion_label = QLabel("实验结论：")
        self.conclusion_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.reason_label, 1, 0, 1, 1, Qt.AlignLeft)
        self.conclusion_input = QLineEdit()
        self.conclusion_input.setPlaceholderText("")
        self.conclusion_input.setText('')
        self.manager_layout.addWidget(self.reason_input, 1, 2, 1, 8, Qt.AlignLeft)

        self.error_analysis_label = QLabel("系统误差的分析：")
        self.error_analysis_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.week_label, 1, 10, 1, 1, Qt.AlignLeft)
        self.error_analysis_input = QLineEdit()
        self.error_analysis_input.setPlaceholderText("")
        self.error_analysis_input.setText('')
        self.manager_layout.addWidget(self.week_input, 1, 11, 1, 6, Qt.AlignLeft)

        self.summary_label = QLabel("实验总结：")
        self.summary_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.reason_label, 1, 0, 1, 1, Qt.AlignLeft)
        self.summary_input = QLineEdit()
        self.summary_input.setPlaceholderText("")
        self.summary_input.setText('')
        self.manager_layout.addWidget(self.reason_input, 1, 2, 1, 8, Qt.AlignLeft)

        self.score_preview_label = QLabel("实验成绩评定_预习：")
        self.score_preview_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.week_label, 1, 10, 1, 1, Qt.AlignLeft)
        self.score_preview_input = QLineEdit()
        self.score_preview_input.setPlaceholderText("")
        self.score_preview_input.setText('')
        self.manager_layout.addWidget(self.week_input, 1, 11, 1, 6, Qt.AlignLeft)

        self.score_attendance_classroom_discipline_label = QLabel("实验成绩评定_出勤和课堂纪律：")
        self.score_attendance_classroom_discipline_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.reason_label, 1, 0, 1, 1, Qt.AlignLeft)

        self.score_attendance_classroom_discipline_input = QLineEdit()
        self.score_attendance_classroom_discipline_input.setPlaceholderText("")
        self.score_attendance_classroom_discipline_input.setText('')
        self.manager_layout.addWidget(self.reason_input, 1, 2, 1, 8, Qt.AlignLeft)

        self.score_operation_performance_label = QLabel("实验成绩评定_操作表现：")
        self.score_operation_performance_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.week_label, 1, 10, 1, 1, Qt.AlignLeft)
        self.score_operation_performance_input = QLineEdit()
        self.score_operation_performance_input.setPlaceholderText("")
        self.score_operation_performance_input.setText('')
        self.manager_layout.addWidget(self.week_input, 1, 11, 1, 6, Qt.AlignLeft)

        self.score_data_processing_label = QLabel("实验成绩评定_数据处理：")
        self.score_data_processing_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.reason_label, 1, 0, 1, 1, Qt.AlignLeft)
        self.score_data_processing_input = QLineEdit()
        self.score_data_processing_input.setPlaceholderText("")
        self.score_data_processing_input.setText('')
        self.manager_layout.addWidget(self.reason_input, 1, 2, 1, 8, Qt.AlignLeft)

        self.score_error_analysis_label = QLabel("实验成绩评定_误差分析：")
        self.score_error_analysis_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.week_label, 1, 10, 1, 1, Qt.AlignLeft)
        self.score_error_analysis_input = QLineEdit()
        self.score_error_analysis_input.setPlaceholderText("")
        self.score_error_analysis_input.setText('')
        self.manager_layout.addWidget(self.week_input, 1, 11, 1, 6, Qt.AlignLeft)

        self.score_report_writing_label = QLabel("实验成绩评定_报告书写：")
        self.score_report_writing_label.setFont(QFont("Microsoft YaHei"))
        self.manager_layout.addWidget(self.reason_label, 1, 0, 1, 1, Qt.AlignLeft)
        self.score_report_writing_input = QLineEdit()
        self.score_report_writing_input.setPlaceholderText("")
        self.score_report_writing_input.setText('')
        self.manager_layout.addWidget(self.reason_input, 1, 2, 1, 8, Qt.AlignLeft)

        self.btn_login = QPushButton("启动")
        self.btn_login.setFixedWidth(100)
        self.btn_login.setFixedHeight(30)
        self.btn_login.setFont(QFont("Microsoft YaHei"))
        self.btn_login.setObjectName("login_btn")
        self.manager_layout.addRow(self.btn_login)


    def eventFilter(self, obj, event):
        """
        事件监听函数
        :param obj:
        :param event:
        :return:
        """
        try:
            # 如果为密码输入框的事件
            if obj == self.password_input:
                # 如果事件类型为焦点进入函数
                if event.type() == QEvent.FocusIn:
                    # 将密码输入框的类型改为普通的输入框的类型，达到密码可见的功能
                    self.password_input.setEchoMode(QLineEdit.Normal)
                elif event.type() == QEvent.FocusOut:
                    self.password_input.setEchoMode(QLineEdit.Password)
            else:
                pass
        except:
            pass
        finally:
            return QWidget.eventFilter(self, obj, event)
