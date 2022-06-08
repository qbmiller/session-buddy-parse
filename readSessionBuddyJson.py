import csv
import json
import io

data = []
data.append("../file/session_buddy_backup_2018_12_09_21_20_41.json")
data.append("../file/session_buddy_backup_2019_05_01_23_11_46.json")
data.append("../file/session_buddy_backup_2019_07_22_16_49_42.json")
data.append("../file/session_buddy_backup_2020_06_26_21_22_18.json")
data.append("../file/session_buddy_export_2022_01_10_13_38_18.json")
data.append("../file/session_buddy_export_2022_02_28_10_41_36.json")
data.append("../file/session_buddy_export_2022_06_06_13_54_18.json")


def parse(data):
    if (type(data).__name__ == 'list'):
        for ele in data:
            if 'url' in ele and 'title' in ele:
                if ele['url'].startswith('chrome-extension:') and ('#uri=' in ele['url'] or '&uri=' in ele['url']):
                    url = ele['url']
                    if '#uri=' in ele['url']:
                        idx = url.find('#uri=')
                    else:
                        idx = url.find('&uri=')
                    acurl = url[idx + 5:len(url)]
                    writer.writerow([ele['title'], acurl])
                    # print(ele['title'], '-----------', acurl)
                else:
                    writer.writerow([ele['title'], ele['url']])
            elif (type(ele).__name__ == 'dict'):
                parse(ele)
    elif (type(data).__name__ == 'dict'):
        for k, v in data.items():
            parse(v)

# if __name__ == '__main__':
with open("extension_chrome_history.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    for ele in data:
        with io.open(ele, 'r', encoding='utf-8-sig') as json_file:
            print(ele, "-----------")
            originData = json.load(json_file)
            parse(originData)
