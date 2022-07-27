import pandas as pd
from tqdm import tqdm



def Process_TXT(input,output):


    fopen = open(input, 'r',encoding='utf8')
    lines = fopen.readlines()
    data=[]
    flag = 1
    columns = ['describe']
    print("************** Process  txt **************")
    excel_writer = pd.ExcelWriter(output)  # 定义writer，选择文件（文件可以不存在）

    for line in tqdm(lines):
        if line.strip('\n')=='':
            continue


        #find columns
        try:

            #If the first column of the row is empty('') and other columns are in string format, this line is columns

            A = list(map(type,list(line.strip('\n').split('\t'))))


            if list(line.strip('\n').split('\t'))[0] ==''  and set(A)=={str}:

                df = pd.DataFrame(data)
                # df.columns = columns
                df.to_excel(excel_writer,sheet_name='sheet'+str(flag), index=False)
                excel_writer.save()
                print('sheet'+str(flag)+" Generated")

                flag=flag+1
                columns = list(line.strip('\n').split('\t'))
                data = []
                # continue
        except:
            pass
        data.append(list(line.strip('\n').split('\t')))

    df = pd.DataFrame(data)
    df.to_excel(excel_writer,sheet_name='sheet'+str(flag), index=False)
    excel_writer.save()
    print('sheet'+str(flag)+" Generated")
    fopen.close()

if __name__ == 'main':


    Process_TXT('data.txt', 'output.xlsx')