import json
import pymysql
import requests
import re
import time
from common import Global

#生成学号
def GenerateStuNum(college, year, major, classNum, stuNum):  # 生成学号
    college = str(college)
    year = str(year)
    major = str(major)
    classNum = str(classNum)
    stuNum = str(stuNum)
    if college.__len__() == 1:
        college = '0' + college
    if classNum.__len__() == 1:
        classNum = '0' + classNum
    if year.__len__() == 1:
        year = '0' + year
    if stuNum.__len__() == 1:
        stuNum = '0' + stuNum
    return college + year + major + classNum + stuNum

def request_html(stu_no):
    try:
        url = "http://librep.nuaa.edu.cn/res.maka.im/user/5610965/template/T_C7A3A6HT/T_C7A3A6HT_v21.json?v=2&xuehao={}&pwd=D41D8CD98F00B204E9800998ECF8427E".format(stu_no)
        response = requests.get(url, timeout=5)
        tojson = json.loads(response.text)
        name = tojson['data']['pdata']['json'][1]['content'][22]['con']
        if (name.__contains__("姓名")):
            return -1
        return tojson
    except Exception as e:
        print(stu_no)
        print(e)
        return -1

def get_data_from_response(stuno,response):
    first_page = response['data']['pdata']['json'][1]['content'][22]['con']        #"姓名：<br/><br/>您一年借了 <b>13</b> 本书<br/>超越了 <b>75.31%</b> 的本科生！<br/><br/>您热衷 <b>工学</b> 类书籍<br/>共借阅 <b>9</b> 本<br/>占借阅总数的 <b>69.23%</b> ！"
    second_page = response['data']['pdata']['json'][2]['content'][29]['con']      #<b>《我有一壶酒, 可以慰风尘》</b> <br/>它在您身旁 <b>129</b> 天
    third_page_1 = response['data']['pdata']['json'][3]['content'][28]['con']     #"<b>2018年01月18日</b>"
    third_page_2 = response['data']['pdata']['json'][3]['content'][29]['con']     #"您借了 <b>6</b> 本书"
    forth_page = response['data']['pdata']['json'][4]['content'][27]['con']       #"您一共来馆 <b>162</b> 次"
    fifth_page_1 = response['data']['pdata']['json'][5]['content'][28]['con']     #"<b>2017年10月27日</b>"
    fifth_page_2 = response['data']['pdata']['json'][5]['content'][29]['con']     #"这一天<br/>您来得最早<br/> <b>07:56</b> <br/>已经开始一天的学习"
    sixth_page = response['data']['pdata']['json'][6]['content'][24]['con']       #"这一学年<br/>您有 <b>4</b> 天<br/>夜晚仍沉浸在书海中<br/> 唯有馆中灯光静静陪伴"
    seventh_page = response['data']['pdata']['json'][7]['content'][24]['con']     #"本学年<br/>您一共自助打印了 <b>105</b> 页<br/>复印了 <b>0</b> 页<br/>相当于 <b>5.9</b> 枚1元硬币厚！ "

    res = {}
    res['no'] = str(stuno)
    res['name'] = first_page.split("：")[0]
    pattern = re.compile(r'<b>([^<]*)<\/b>')
    match = pattern.findall(first_page)
    res['total_book_num'] = 0 if match[0].__len__()==0 else match[0]
    res['like_book_type'] = match[2]
    res['like_book_type_num'] = 0 if match[3].__len__()==0 else match[3]     #共借阅 like_book_type多少本
    match = pattern.findall(second_page)
    res['longest_book'] = match[0]
    res['longest_book_day'] = 0 if match[1].__len__()==0 else match[1]
    match = pattern.findall(third_page_1+third_page_2)
    res['most_book_date'] = match[0]
    res['most_book_num'] = 0 if match[1].__len__()==0 else match[1]
    match = pattern.findall(forth_page)
    res['library_count'] = 0 if match[0].__len__()==0 else match[0]
    match = pattern.findall(fifth_page_1+fifth_page_2)
    res['earliest_date'] = match[0]
    res['earliest_time'] = match[1]
    match = pattern.findall(sixth_page)
    res['night_day'] = 0 if match[0].__len__()==0 else match[0]
    match = pattern.findall(seventh_page)
    res['daying_page'] = match[0]
    res['fuying_page'] = match[1]
    return res

def save_to_mysql(year,datas):
    conn = pymysql.connect(host=Global.get_value('host'), user=Global.get_value('user'), passwd=Global.get_value('password'), db=Global.get_value('dbname'), port=Global.get_value('port'),charset='utf8',autocommit = True)
    cursor = conn.cursor()
    for data in datas:
        try:
            sql = "INSERT INTO `{}` VALUES('{}','{}',{},'{}',{},\"{}\",{},'{}',{},{},'{}','{}',{},{},{})".format(year,data['no'],data['name'],data['total_book_num'],data['like_book_type'],data['like_book_type_num'],data['longest_book'],data['longest_book_day'],data['most_book_date'],data['most_book_num'],data['library_count'],data['earliest_date'],data['earliest_time'],data['night_day'],data['daying_page'],data['fuying_page'])
            cursor.execute(sql)
        except Exception as e:
            print(data['no'])
            print(e)
            print("[ERROR] Failed to save data")
    cursor.close()
    conn.close()

def get_data():
    for j in range(14, 17 + 1):             # 年级
        for i in range(1, 17):              #学院
            begin_zhuanye = 1
            if i == 4:                      #四院从0开始
                begin_zhuanye = 0
            for k in range(begin_zhuanye, 10):          #专业
                error_banji = 0  # 班级出错次数
                for m in range(1, 15):  # 班级
                    error_bannei = 0  # 班级内出错次数
                    datas = []
                    for n in range(1, 50):  # 班内编号
                        stuno = GenerateStuNum(i, j, k, m, n)
                        response = request_html(stuno)
                        time.sleep(0.5)
                        if response == -1:  # 该学号爬取错误
                            error_bannei += 1
                        else:
                            datas.append(get_data_from_response(stuno, response))
                            if datas.__len__() == 10:
                                save_to_mysql(j, datas)
                                datas.clear()
                            error_bannei = 0
                        if error_bannei == 3 and n == 3:  # 前三个都出错，说明该班级不存在跳出循环，遍历下一个班级、
                            error_banji += 1
                            break
                        if error_bannei == 5:  # 连续出错5个说明该班级遍历结束，跳出循环
                            break
                    if error_banji == 2:  # 该专业下连续两个班出错就说明该专业遍历结束，跳出循环
                        break
                    if datas.__len__() != 0:
                        save_to_mysql(j, datas)

if __name__ == '__main__':
    Global.__init__()
    get_data()