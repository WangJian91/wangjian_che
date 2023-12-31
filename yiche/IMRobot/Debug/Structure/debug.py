# -*- coding: utf-8 -*-

import pymysql
import time
import requests
import json

# db = pymysql.connect(host='10.168.47.14',
#                      user='root',
#                      password='root',
#                      database='car_infos')
# start_time = time.time()
# cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
# sql = "select  distinct * from car_wide_table_v2 cwtv where exter_config like '%可开启全景天窗%' "
# cursor.execute(sql)
# data = cursor.fetchall()
# print(data)
# print('查询完成'.center(50, '-'))
# print('花费时间：', time.time() - start_time)


# all_config_list = []

# for i in data:
#     all_config_list.extend(i["seat_config"].split('#'))
# all_config_set = set(all_config_list)
# new_all_config_list = list(all_config_set)
# print(new_all_config_list)
# cursor.close()
# db.close()


seat_config = ['主座椅调节方式腰部调节(4向)',
               '座椅材质织物/Alcantara混搭',
               '副座椅调节方式靠背调节',
               '前排座椅功能通风',
               '座椅材质皮/织物混搭',
               '第二排座椅调节方式腰夹调节',
               '主座椅调节方式肩部调节',
               '第二排座椅调节方式腰部调节(4向)',
               '副座椅调节方式腰部调节(2向)',
               '后排座椅功能通风',
               '主座椅调节方式腰夹调节',
               '后排座椅功能加热',
               '副座椅调节方式高低调节(4向)',
               '前排座椅功能通风(主驾)',
               '座椅布局2+3',
               '主座椅电动调节带记忆电动调节',
               '后中央扶手',
               '第二排座椅调节方式腿托调节',
               '后排杯架第二排',
               '第二排座椅电动调节电动调节',
               '副座椅调节方式前后调节',
               '第三排座椅第四排',
               '第二排座椅调节方式高低调节(4向)',
               '运动风格座椅',
               '第二排座椅调节方式腰部调节',
               '第二排座椅调节方式前后调节',
               '座椅材质仿皮',
               '主座椅调节方式高低调节(4向)',
               '座椅材质皮质',
               '后排杯架第三排',
               '座椅材质真皮/Alcantara混搭',
               '后排座椅放倒方式整体放倒',
               '副座椅调节方式高低调节(2向)',
               '座椅材质真皮/仿皮混搭',
               '座椅材质真皮',
               '主座椅电动调节电动调节',
               '副座椅电动调节电动调节',
               '第二排座椅电动调节带记忆电动调节',
               '第二排座椅调节方式腰部调节(2向)',
               '主座椅调节方式高低调节(2向)',
               '第二排座椅调节方式旋转调节',
               '主座椅调节方式腰部调节',
               '前中央扶手第二排',
               '主座椅调节方式腿托调节',
               '前排座椅功能按摩(主驾)',
               '座椅材质织物/翻毛材质混搭',
               '副座椅调节方式肩部调节',
               '座椅材质织物/仿皮混搭',
               '前排座椅功能按摩(副驾)',
               '后排折叠桌板第二排',
               '副座椅调节方式腰部调节',
               '主座椅调节方式腰部调节(2向)',
               '第二排座椅调节方式靠背调节',
               '座椅材质Alcantara',
               '座椅材质翻毛材质',
               '副座椅调节方式高低调节',
               '第二排座椅调节方式高低调节',
               '前中央扶手第一排',
               '前排座椅功能加热(主驾)',
               '后排座椅功能按摩',
               '副座椅调节方式腿托调节',
               '副座椅调节方式腰部调节(4向)',
               '主座椅调节方式靠背调节',
               '主座椅调节方式高低调节',
               '第二排座椅调节方式左右调节',
               '主座椅调节方式前后调节',
               '座椅材质皮/翻毛材质混搭',
               '第二排座椅调节方式肩部调节',
               '前排座椅功能按摩',
               '座椅材质真皮/翻毛材质混搭',
               '后排座椅放倒方式比例放倒',
               '前排座椅功能加热',
               '副座椅电动调节带记忆电动调节',
               '副座椅调节方式腰夹调节',
               '第二排座椅调节方式高低调节(2向)',
               '座椅材质织物']

exter_config = ['车窗一键升降全车',
                '多层隔音玻璃第一排',
                '天窗类型单天窗',
                '灯光特色功能像素式',
                '前雨刷器雨量感应式',
                '大灯功能高度调节',
                '前雾灯卤素',
                'APP远程遥控功能座椅通风',
                '可加热喷水嘴',
                'APP远程遥控功能方向盘加热',
                '轮圈材质铝合金',
                '内后视镜自动防眩目自动防眩目',
                '外后视镜电动调节倒车辅助',
                '前雾灯LED',
                '大灯功能延时关闭',
                'APP远程遥控功能车主服务(查找充电桩、加油站、停车场等)',
                '电吸门第二排',
                'NFC/RFID钥匙',
                'APP远程遥控功能预约保养/维修',
                '远光灯光源LED',
                '后排侧遮阳帘电动',
                '流媒体后视镜',
                '天窗类型分段式不可开启天窗',
                '大灯调节/清洗',
                '外后视镜电动调节自动防眩目',
                '外后视镜电动调节倒车自动下翻',
                '遥控钥匙',
                '车窗防夹手功能第一排',
                '多层隔音玻璃',
                '外后视镜电动调节透雾功能',
                'APP远程遥控功能车窗控制',
                '大灯功能自适应远近光',
                '外后视镜电动调节后视镜记忆',
                '远光灯光源卤素',
                '几何多光束',
                '多层隔音玻璃全车',
                'APP远程遥控功能车况查询/诊断',
                '触摸液晶屏钥匙',
                '多层隔音玻璃第二排',
                'APP远程遥控功能车辆启动',
                '车窗防夹手功能',
                'APP远程遥控功能空调控制',
                '可编程智能大灯',
                '远光灯光源氙气',
                '中控锁遥控钥匙',
                '近光灯光源氙气',
                'LED日间行车灯',
                '内后视镜自动防眩目流媒体后视镜',
                '行李厢开启功能位置记忆',
                '轮圈材质碳纤维',
                '大灯功能自动转向',
                '大灯功能自动开闭',
                '灯光特色功能矩阵式',
                '外后视镜电动调节流媒体后视镜',
                '主动闭合式进气格栅',
                'APP远程遥控功能充电管理',
                '天窗类型可开启全景天窗',
                '近光灯光源LED',
                '外后视镜电动调节电动折叠',
                '蓝牙钥匙',
                '行李厢开启功能电动开合',
                '运动外观套件',
                '前电动车窗',
                '智能钥匙',
                '车窗防夹手功能全车',
                '智能手环钥匙',
                '中控锁机械钥匙',
                '后排侧遮阳帘手动',
                '车窗防夹手功能驾驶位',
                '大灯功能雨雾模式',
                'APP远程遥控功能车辆定位/寻车',
                '中控锁触摸液晶屏钥匙',
                '前雨刷器车速感应式',
                '电吸门第一排',
                '外后视镜电动调节后视镜加热',
                '后电动车窗',
                '天窗类型分段式电动天窗',
                '轮圈材质钢',
                'APP远程遥控功能座椅加热',
                'APP远程遥控功能车门控制',
                '灯光特色功能可编程智能大灯',
                '自动防眩目',
                'APP远程遥控功能车灯控制',
                'UWB数字钥匙',
                '外后视镜电动调节锁车自动折叠',
                '中控锁蓝牙钥匙',
                '天窗类型不可开启全景天窗',
                '天窗类型不可开启天窗',
                '电吸门',
                '车顶行李架',
                '中控锁NFC/RFID钥匙',
                '外后视镜电动调节视野放大',
                '灯光特色功能几何多光束',
                '内后视镜自动防眩目手动防眩目',
                '生物识别',
                '外后视镜电动调节电动调节',
                '车窗一键升降第一排',
                '车窗一键升降驾驶位',
                '电吸门全车',
                '远光灯光源激光',
                '后排侧遮阳帘',
                '近光灯光源卤素'
                ]

chassis_config = ['车体结构承载式',
                  '前轮制动类型实心盘式',
                  '驱动形式双电机四驱',
                  '前悬架类型麦弗逊独立悬架',
                  '驱动形式前置四驱',
                  '前悬架类型整体桥式非独立悬架',
                  '可调悬架功能软硬调节',
                  '后悬架类型单臂式后独立悬架',
                  '前轮制动类型陶瓷通风盘式',
                  '后悬架类型麦弗逊式独立悬架',
                  '助力类型电子电传助力',
                  '后悬架类型多连杆式非独立悬架',
                  '前悬架类型多连杆式独立悬架',
                  '助力类型电子液压助力',
                  '可调悬架种类电磁感应悬架',
                  '驱动形式后置后驱',
                  '驻车制动类型手刹',
                  '助力类型机械液压助力',
                  '驱动形式中置四驱',
                  '助力类型电动助力',
                  '软硬调节',
                  '驱动形式四电机四驱',
                  '驱动形式后轮驱动',
                  '可调悬架功能高低调节',
                  '后轮制动类型通风盘式',
                  '后悬架类型螺旋弹簧式非独立悬架',
                  '驱动形式中置后驱',
                  '后轮制动类型陶瓷通风盘式',
                  '驻车制动类型脚踩式',
                  '前悬架类型双横臂式独立悬架',
                  '前轮制动类型鼓式',
                  '后悬架类型双横臂式独立悬架',
                  '后悬架类型五连杆螺旋弹簧非独立悬架',
                  '后轮制动类型鼓式',
                  '电磁感应悬架',
                  '后轮制动类型实心盘式',
                  '前轮制动类型通风盘式',
                  '后悬架类型麦弗逊独立悬架',
                  '后悬架类型五连杆式独立悬架',
                  '驱动形式后置四驱',
                  '驻车制动类型手拉式',
                  '可调悬架种类空气悬架',
                  '驻车制动类型电子驻车',
                  '后悬架类型多连杆式独立悬架',
                  '后悬架类型拖曳臂式非独立悬架',
                  '驱动形式前置后驱',
                  '驻车制动类型脚刹',
                  '后悬架类型扭力梁式非独立悬架',
                  '后悬架类型双叉臂式独立悬架',
                  '前悬架类型扭杆弹簧独立悬架',
                  '前悬架类型五连杆式独立悬架',
                  '前悬架类型螺旋弹簧式独立悬架',
                  '前悬架类型麦弗逊式独立悬架',
                  '前悬架类型双叉臂式独立悬架',
                  '后悬架类型整体桥式非独立悬架',
                  '驻车制动类型断气刹',
                  '车体结构非承载式',
                  '驱动形式前置前驱',
                  '驱动形式三电机四驱',
                  '后悬架类型钢板弹簧非独立悬架',
                  '可调悬架功能'
                  ]

safe_config = ['零胎压续行轮胎',
               '安全带气囊',
               '副驾驶安全气囊',
               '膝部气囊主驾',
               '膝部气囊副驾',
               '后排中央气囊第一排',
               '制动力分配',
               '胎压监测胎压报警',
               '牵引力控制',
               '后排中央气囊第二排',
               '车身稳定控制',
               '防抱死制动',
               '前侧气囊',
               '后侧气囊',
               '制动辅助',
               '胎压监测胎压显示',
               '膝部气囊第一排',
               '胎压监测',
               '儿童座椅接口',
               '膝部气囊',
               '被动行人保护',
               '主驾驶安全气囊',
               '侧安全气帘'
               ]

inter_config = ['内饰材质塑料',
                '遮阳板化妆镜副驾驶',
                '后排空调双温区自动空调',
                '方向盘材质仿皮',
                '方向盘调节电动上下+前后调节',
                '方向盘材质真皮/碳纤维',
                '多功能方向盘',
                '主驾驶+照明灯',
                '后排空调手动空调',
                '遮阳板化妆镜有',
                '方向盘材质碳纤维/翻毛皮',
                '方向盘调节手动上下+前后调节',
                '车内氛围灯双色',
                '遮阳板化妆镜',
                '车内氛围灯72色',
                '第三排+照明灯',
                '后排空调单温区自动空调',
                '方向盘材质皮质',
                '遮阳板化妆镜主驾驶',
                '主动降噪',
                '方向盘材质木制',
                '车内PM2.5过滤装置',
                '车载空气净化器',
                '方向盘换挡',
                '方向盘材质塑料',
                '方向盘调节手动上下调节',
                '前排空调双温区手动空调',
                '负离子发生器',
                '方向盘加热',
                '后排空调出风口',
                '车载冰箱',
                '副驾驶+照明灯',
                '方向盘调节手动前后调节',
                '前排空调手动空调',
                '车内氛围灯多色',
                '前排空调单温区自动空调',
                '遮阳板化妆镜副驾驶+照明灯',
                '方向盘材质碳纤维',
                '方向盘材质真皮',
                '第二排+照明灯',
                '车内氛围灯彩色',
                '前排空调双温区自动空调',
                '车内氛围灯单色',
                '香氛系统',
                '方向盘材质Alcantara/翻毛皮',
                '遮阳板化妆镜主驾驶+照明灯',
                '方向盘调节方向盘记忆',
                '后排空调双温区手动空调'
                ]

accessories = ['液晶仪表尺寸12.6',
               '液晶屏尺寸7',
               '扬声器数量6',
               '音响品牌Mclntosh麦景图',
               '车载APP应用',
               'OTA升级车机OTA',
               'HUD平视显示',
               '车载WiFi热点WiFi连接',
               '语音控制电话',
               '音响品牌FOCAL',
               '蓝牙/WIFI连接',
               '手机无线充电第一排',
               '车载WiFi热点WiFi热点',
               '手机互联支持HiCar',
               '座椅位置调节',
               '语音控制',
               '后排液晶屏1个',
               '中控彩色液晶屏触控OLED屏',
               '中控彩色液晶屏触控式液晶屏',
               '手机无线充电',
               '外接音源接口HDMI',
               '行车电脑显示屏彩色',
               '手机互联支持CarLife',
               '车载行车记录仪',
               '多媒体系统',
               'OTA升级整车OTA',
               '座椅功能调节',
               '紧急道路救援',
               '语音控制空调',
               '手势控制系统',
               '车载220V电源230V',
               '手机互联支持CarPlay',
               '外接音源接口Type-C',
               '语音控制导航',
               '语音控制智能语音控制',
               '手机无线充电第二排',
               '车载电视',
               '蓝牙/WIFI连接WiFi',
               '全液晶仪表盘',
               '语音控制多媒体系统',
               '外接音源接口SD',
               '后排控制多媒体',
               '外接音源接口AUX',
               'GPS导航系统',
               '外接音源接口USB',
               '后排液晶屏1',
               '车载220V电源220V',
               '手机互联原厂互联/映射',
               '中控彩色液晶屏普通液晶屏',
               '手机互联支持Android Auto'
               ]

# print(len(accessories) + len(seat_config) + len(inter_config) + len(safe_config) + len(exter_config) + len(
#     chassis_config))

text = "长安55的配置"

url = "http://10.168.47.5:10010/mm_im/StructuredToolV2"
data = {"text": text, "session_uuid": 123}
start_time = time.time()
print('开始测试'.center(50, '-'))
result = requests.post(url=url, json=data, timeout=100).content
result = json.loads(result)
print(result)
ai_answer = result["ai_answer"].strip()
sql = result["web_logs_list"][0]
print(text)
print(sql)
print('ai_answer:', ai_answer)
print('花费时间：', time.time() - start_time)
