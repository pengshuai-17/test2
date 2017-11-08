#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Employee:
   '所有学生的信息'
   empCount = 0
   empwlr = 0
   empjyr = 0
   emp_wln = 0
   emp_wlnv = 0
   emp_jyn = 0
   emp_jynv = 0
 
   def __init__(self,stu_no,name,stu_class,male):
      self.stu_no = stu_no
      self.name = name
      self.stu_class = stu_class
      self.male = male
      Employee.empCount += 1
      if(stu_class=='wl'):
            if(male == 'n'):
               Employee.emp_wln += 1
            else:
               Employee.emp_wlnv += 1
            Employee.empwlr += 1
      if(stu_class=='jy'):
            if(male == 'n'):
               Employee.emp_jyn += 1
            else:
               Employee.emp_jynv += 1
            Employee.empjyr += 1
   def displayC(self):
     print "Total Employee wl n %d" % Employee.emp_wln
     print "Total Employee jy n %d" % Employee.emp_jyn
   def displayC(self):
     print "Total Employee wl nv %d" % Employee.emp_wlnv
     print "Total Employee jy nv %d" % Employee.emp_jynv
   def displayC(self):
     print "Total Employee wl r %d" % Employee.empwlr
     print "Total Employee jy r %d" % Employee.empjyr
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
   def displayEmployee(self): 
      print "Stu_no : ",self.stu_no,"Name : ",self.name," Stu_class: ",self.stu_class,"Male : ",self.male
