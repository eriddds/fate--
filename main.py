import random
import os

mouth = int(input("请输入要算的日期（农历）[月]："))
day = int(input("请输入要算的日期（农历）[日]："))

def get_time_period(time_str):
    # 将输入的时间字符串解析为小时和分钟
    try:
        hour, minute = map(int, time_str.split(':'))
    except ValueError:
        try:
            hour, minute = map(int, time_str.split('：'))
        except:
            return "请输入正确的时间格式，例如：21:23"

    # 判断时间属于哪个区间
    if 0 <= hour < 1:  # 24:00-01:00
        return 1
    elif 1 <= hour < 3:  # 01:00-03:00
        return 3
    elif 3 <= hour < 5:  # 03:00-05:00
        return 3
    elif 5 <= hour < 7:  # 05:00-07:00
        return 4
    elif 7 <= hour < 9:  # 07:00-09:00
        return 5
    elif 9 <= hour < 11:  # 09:00-11:00
        return 6
    elif 11 <= hour < 13:  # 11:00-13:00
        return 7
    elif 13 <= hour < 15:  # 13:00-15:00
        return 8
    elif 15 <= hour < 17:  # 15:00-17:00
        return 9
    elif 17 <= hour < 19:  # 17:00-19:00
        return 10
    elif 19 <= hour < 21:  # 19:00-21:00
        return 11
    elif 21 <= hour < 23:  # 21:00-23:00
        return 12
    elif 23 <= hour < 24:  # 23:00-24:00
        return 12
    else:
        return "无效的时间输入"


# 用户输入时间
time_input = input("请输入时间（格式：HH:MM）：")
result = get_time_period(time_input)

cout_list = [mouth,day,result]
type_list = ["大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡""大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡""大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡",
             "大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡""大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡""大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡",
             "大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡""大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡""大安","留连","速喜","赤口","小吉","空亡","大安","留连","速喜","赤口","小吉","空亡"]
print(cout_list)
def main(num):
    z = []
    for i in range(num):
        z.append(type_list[i])
    print(z)
    print(z[-1])
    return z[-1],z

mo,mo_data = main(mouth)
da,da_data = main(day+mouth)
re,re_data = main(result+(day+mouth))

data = {
    "大安" : 0,
    "留连" : 0,
    "速喜" : 0,
    "赤口" : 0,
    "小吉" : 0,
    "空亡" : 0
}

if mo == "大安":
    data["大安"] += 1
elif mo == "留连":
    data["留连"] += 1
elif mo == "速喜":
    data["速喜"] += 1
elif mo == "赤口":
    data["赤口"] += 1
elif mo == "小吉":
    data["小吉"] += 1
elif mo == "空亡":
    data["空亡"] += 1

if da == "大安":
    data["大安"] += 1
elif da == "留连":
    data["留连"] += 1
elif da == "速喜":
    data["速喜"] += 1
elif da == "赤口":
    data["赤口"] += 1
elif da == "小吉":
    data["小吉"] += 1
elif da == "空亡":
    data["空亡"] += 1

if re == "大安":
    data["大安"] += 1
elif re == "留连":
    data["留连"] += 1
elif re == "速喜":
    data["速喜"] += 1
elif re == "赤口":
    data["赤口"] += 1
elif re == "小吉":
    data["小吉"] += 1
elif re == "空亡":
    data["空亡"] += 1

print(data)

html_data_1 = """ 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data</title>
    <script src="chart.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        canvas {
            width: 100%;
            height: 400px;
        }
        .description {
            margin-top: 20px;
            font-size: 0.9em;
            color: #666;
        }
        .red{
            color: red;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="red">本程序仅限娱乐，请勿迷信</h1>
        <h1>大致原理来源中国古代的小六壬</h1>
        <h1>Data</h1>
        <canvas id="myPieChart"></canvas>
        <div class="description">
        </div>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', (event) => {
            var ctx = document.getElementById('myPieChart').getContext('2d');
            var myPieChart = new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: ["大安","留连","速喜","赤口","小吉","空亡"],
                    datasets: [{
                        label: 'Data',"""
html_data_2 = """
                        data: [{daan}, {luilian}, {suxi}, {chikou}, {xiaoji}, {kongwang}],""" .format (daan=data["大安"], luilian=data["留连"], suxi=data["速喜"], chikou=data["赤口"], xiaoji=data["小吉"], kongwang=data["空亡"])
html_data_3 = """
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(153, 102, 255, 0.2)',
                            'rgba(255, 159, 64, 0.2)'
                        ],
                        borderColor: [
                            'rgba(255, 99, 132, 1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)',
                            'rgba(255, 159, 64, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'top',
                        },
                        tooltip: {
                            enabled: true
                        }
                    }
                }
            });
        });
    </script>"""
html_data_4 = """
    <div>{}<hr /><br />{}<hr /><br />{}<hr /><br />{}<hr /><br />{}<hr /><br />{}</div>"""  .format(f"计数时间农历{mouth}月{day},time:{time_input}",
                                                    mo_data,da_data,re_data,
                                                    f"获得数据:{mo},{da},{re}",
                                                    f"字典数据：大安:{data["大安"]},留连:{data["留连"]},速喜:{data["速喜"]},赤口:{data["赤口"]},小吉:{data["小吉"]},空亡:{data["空亡"]}")
html_data_5 = """
    <hr />
    <div>
        1、大安：身不动时，属木，为青龙，凡谋事主一、五、七。<br />
        断辞曰：<br />
        大安事事昌，求谋在东方，失物去不远，<br />
        宅舍保安康，行人身未动，病者主无妨，<br />
        将军回田野，仔细与推详。<br />
        <br />
        2、留连：卒未归时，属水，为玄武，凡谋事主二、八、十。<br />
        断辞曰：<br />
        留连事难成，求谋曰未明，官事只宜缓，<br />
        去者未回程，失物南方见，急讨方称心，<br />
        更须防口舌，人口且平平。<br />
        <br />
        3、速喜：人便至时，属火，为朱雀，凡谋事主三、六、九。<br />
        断辞曰：<br />
        速喜喜来临，求财向南行，失物申午未，<br />
        逢人路上寻，官事有福德，病者无祸侵，<br />
        田家六畜吉，行人有信音。<br />
        <br />
        4、赤口：官事凶时，属金，为白虎，凡谋事主四、七、十。<br />
        断辞曰：<br />
        赤口主口舌，官非切要防，失物急去寻，<br />
        行人有惊慌，鸡犬多作怪，病者出西方，<br />
        更须防咒诅，恐怕染蕴疾。<br />
        <br />
        5、小吉：人来喜时，属木，为六合，凡谋事主一、五、七。<br />
        断辞曰：<br />
        小吉最吉昌，路上好商良，阳人来报喜，<br />
        失物在坤方，行人立便至，交关真是强，<br />
        凡事皆和合，病者事无仿。<br />
        <br />
        6、空亡：音信稀时，属土，为勾陈，凡谋事主一、五、七。<br />
        断辞曰：<br />
        空亡事不长，阴人小乘张，求财无有利，<br />
        行人有灾殃，失物寻不见，官事主刑伤，<br />
        病人逢暗鬼，乞解保安康。<br />
        <hr />
        
        大安：表示光明正大、平平安安；<br />
        留连：表示岁月漫长、纠缠绵绵；<br />
        速喜：表示做事迅速、喜事来临；<br />
        赤口：表示口舌是非、破败多端；<br />
        小吉：表示凡事可谋、多吉多利；<br />
        空亡：表示谋事落空、劳而无成。<br />
    </div>
</body>
</html>"""

html_data = html_data_1+html_data_2+html_data_3+html_data_4+html_data_5
with open("data.html", "w", encoding="utf-8") as f:
    f.write(html_data)
current_file_path = os.path.abspath(__file__)
# 获取当前Python文件所在的目录
current_directory = os.path.dirname(current_file_path)

# 更改工作目录到当前Python文件所在的目录
os.chdir(current_directory)

os.system("data.html")