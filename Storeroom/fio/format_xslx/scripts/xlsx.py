#!/bin/env python
# -*- coding: utf-8 -*-

import sys
import xlsxwriter


if 2 != len(sys.argv):
    print "unit_format.py <excel filename> <number[with unit]>"
    exit(1)



filename="./xlsx/performance.xlsx"
sds_number=2

print filename

excel = xlsxwriter.Workbook(filename)

#attribute
title_attr = excel.add_format({"bold":True,'bg_color': '00ff00'})
disk_attr = excel.add_format({'font_color': 'red', 'align':'left'})
data_attr = excel.add_format({'align':'left'})


fp = open(sys.argv[1])

while 1:
    #############################################
    #读入数据
    #############################################
    info=fp.readline()
    if not info:
        break
    print info.strip()," log processing ..."
    ssd_number=fp.readline().strip()
    performance_name=fp.readline().strip()
    serise_name=fp.readline().strip().split()
    x_axis=fp.readline().strip()
    y_axis=fp.readline().strip()
    title = fp.readline().strip().split()
    
    #############################################
    #创建sheet
    #############################################
    excel_sheet = excel.add_worksheet(performance_name)
    
    
    #############################################
    #写入excel文件
    #############################################
    excel_sheet.write(0,0,"disk",title_attr)
    excel_sheet.write_row(0,1,title,disk_attr)
    serise_number=0
    for serise in serise_name:
        serise_number += 1
        data  = fp.readline().strip().split()
        data  = [ float(x) for x in data ]
        excel_sheet.write(serise_number,0,performance_name+"("+serise+")",title_attr)
        excel_sheet.write_row(serise_number,1,data,data_attr)
    
    
    
    #############################################
    #chart  插入图表：条形图、柱状图、饼图等
    #############################################
    
    #############################################
    chart1=excel.add_chart({'type':'column'})
    chart2=excel.add_chart({'type':'column'})
    chart3=excel.add_chart({'type':'column'})
    
    serise_number=0
    chart1_categories="="+performance_name+"!$B$1:$N$1"
    chart2_categories="="+performance_name+"!$B$1:$C$1"
    chart3_categories="="+performance_name+"!$D$1:$N$1"
    for serise in serise_name:
        serise_number += 1
        #print serise_number
        #print serise
        chart1_value     ="="+performance_name+"!$B$"+str(serise_number+1)+":$N$"+str(serise_number+1)
        #print chart1_categories
        #print chart1_value
        chart1.add_series({
            'name':serise,
            'categories':chart1_categories,
            'values':chart1_value,
            })

        chart2_value     ="="+performance_name+"!$B$"+str(serise_number+1)+":$C$"+str(serise_number+1)
        chart2.add_series({
            'name':serise,
            'categories':chart2_categories,
            'values':chart2_value,
            })

        chart3_value     ="="+performance_name+"!$D$"+str(serise_number+1)+":$N$"+str(serise_number+1)
        chart3.add_series({
            'name':serise,
            'categories':chart3_categories,
            'values':chart3_value,
            })
    
    
    chart1.set_title({'name':performance_name+"(SSD & HDD)"})
    chart1.set_x_axis({'name':x_axis})
    chart1.set_y_axis({'name':y_axis})
    #->
    #excel_sheet.insert_chart('A6',chart1,{'x_offset':0,'y_offset':0})
    chart_position="A"+str(serise_number+3)
    excel_sheet.insert_chart(chart_position,chart1,{'x_offset':0,'y_offset':0})
    #<-
    
    chart2.set_title({'name':performance_name+"(SSD)"})
    chart2.set_x_axis({'name':x_axis})
    chart2.set_y_axis({'name':y_axis})
    #->
    #excel_sheet.insert_chart('I6',chart2,{'x_offset':0,'y_offset':0})
    chart_position="I"+str(serise_number+3)
    excel_sheet.insert_chart(chart_position,chart2,{'x_offset':0,'y_offset':0})
    #<-

    chart3.set_title({'name':performance_name+"(HDD)"})
    chart3.set_x_axis({'name':x_axis})
    chart3.set_y_axis({'name':y_axis})
    #->
    #excel_sheet.insert_chart('Q6',chart3,{'x_offset':0,'y_offset':0})
    chart_position="Q"+str(serise_number+3)
    excel_sheet.insert_chart(chart_position,chart3,{'x_offset':0,'y_offset':0})
    #<-
    print info.strip()," log process finished\n"

#############################################
#结束处理
#############################################
#excel_sheet.activate()


excel.close()
