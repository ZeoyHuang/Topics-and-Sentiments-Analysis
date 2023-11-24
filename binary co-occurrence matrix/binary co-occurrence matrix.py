import csv

INPUT_PATH = "C:/Users/郎如流水/Desktop/wb.csv"
OUTPUT_PATH = "C:/Users/郎如流水/Desktop/output.csv"
KEYWORD_LIST = ["上海", "方舱", "解封", "医院", "微博", "核酸", "视频", "隔离", "防控", "无症状", "感染者", "小区", "物资", "新冠", "确诊", "抗疫", "加油", "医疗队", "阳性", "新增"]


# statement.count(keyword)

def check_keywords(statement: str):
    is_exists_list = []
    for keyword in KEYWORD_LIST:
        # 循环检测关键字
        if keyword in statement:
            is_exists_list.append(1)
        else:
            is_exists_list.append(0)
    return is_exists_list


if __name__ == "__main__":
    posts = []
    with open(INPUT_PATH, 'rb') as csv_file:
        for line in csv_file:
            line = line.decode('gbk', 'ignore').strip()
            posts.append(line)

    # 检测
    outcome_list = []
    for post in posts:
        outcome_list.append(check_keywords(post))

    for i in range(0, len(KEYWORD_LIST)):
        keyword = KEYWORD_LIST[i]
        counter = 0
        for outcome in outcome_list:
            if outcome[i] > 0:
                counter += 1
        print(keyword + ": " + str(counter))

    for i in range(0, len(KEYWORD_LIST)):
        for j in range(i+1, len(KEYWORD_LIST)):
            first_keyword = KEYWORD_LIST[i]
            second_keyword = KEYWORD_LIST[j]

            counter = 0
            for outcome in outcome_list:
                if outcome[i] > 0 and outcome[j] > 0:
                    counter += 1
            print(first_keyword + " " + second_keyword + ": " + str(counter))



    # 复制关键字当做表头
    header = KEYWORD_LIST.copy()
    header.insert(0, '')

    with open(OUTPUT_PATH, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        # 按行写入
        for i in range(0, len(outcome_list)):
            outcome_list[i].insert(0, posts[i])
            writer.writerow(outcome_list[i])
