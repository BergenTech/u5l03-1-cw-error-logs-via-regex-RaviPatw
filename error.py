import json,csv, re
with open('logs.json','r') as file:
    data=json.load(file)
    pattern="ERROR"
    newData=[]
    for dict in data:
        item=[]
        if re.search(pattern,dict["level"],re.IGNORECASE):
            item.append(dict['timestamp'])
            item.append('ERROR')
            item.append(dict['message'])
            newData.append(item)
    # for i in range(10):
        # print(newData[10])
    with open('error_logs.csv','w',newline='') as newFile:
        writer=csv.writer(newFile)
        writer.writerow(data[0].keys())
        writer.writerows(newData)
        # print('run')
        