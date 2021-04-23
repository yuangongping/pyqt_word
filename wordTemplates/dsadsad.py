from docxtpl import DocxTemplate, InlineImage
tpl = DocxTemplate('实验报告模板.docx')



context = {
   "school_num": "8107",
   "year": "2021",
   "reason": "春季",
   "week": "1",
   "xingqi": "5",
   "lesson_num": "1-2",
   "student_name": "未来的小富婆",
   "professional_class": "控制科学与工程",
   "project_name": "Python",
   "project_hours": "4",
   "teacher": "李建",
   "score": "99",
   "experiment_project": "Python",
   "purpose": "学习python",
   "experimental_equipment": [
       {"index": 1, "name": "a", "info": "dsads", "num": "1", "status": "dads", "remarks": "dasdsadsa"},
        {"index": 2, "name": "b", "info": "dsads", "num": "2", "status": "dads", "remarks": "dasdsadsa"},
        {"index": 3, "name": "c", "info": "dsads", "num": "4", "status": "dads", "remarks": "dasdsadsa"},
        {"index": 4, "name": "d", "info": "dsads", "num": "14", "status": "dads", "remarks": "dasdsadsa"}

   ],
   "principle": "及其后面的字词均被忽略，因为百度的查询限制在38个汉字以内。",
   "step": "及其后面的字词均被忽略，因为百度的查询限制在38个汉字以内。及其后面的字词均被忽略，因为百度的查询限制在38个汉字以内。及其后面的字词均被忽略，因为百度的查询限制在38个汉字以内。",
   "operation_recording": "及其后面的字词均被忽略，因为百度的查询限制在38个汉字以内。",
   "data_processing": "及其后面的字词均被忽略，因为百度的查询限制在38个汉字以内。",
   "conclusion": "及其后面的字词均被忽略，因为百度的查询限制在38个汉字以内。",
   "error_analysis": "及其后面的字词均被忽略，因为百度的查询限制在38个汉字以内。",
   "summary": "及其后面的字词均被忽略，因为百度的查询限制在38个汉字以内。",
   "score_preview": "100",
   "score_attendance_classroom_discipline": "100",
   "score_operation_performance": "100",
   "score_data_processing": "100",
   "score_error_analysis": "100",
   "score_report_writing": "100"
}
tpl.render(context)
tpl.save("的劳动合同.docx")
