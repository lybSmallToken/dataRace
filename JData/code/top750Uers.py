import pandas as pd
path = ["","","",""]   # �ĸ�action.csv·��
df1 = pd.read_csv(path[0])
df2 = pd.read_csv(path[1])
df3 = pd.read_csv(path[2])
df4 = pd.read_csv(path[3])
dfP = pd.read_csv("")  # Product.csv·��
df = pd.concat([df1,df2,df3,df4])

dfP = dfP['sku_id'].to_frame()

df = df[['user_id','sku_id','type','cate']]
df2 = df[(df.type==4)&(df.cate==8)] 
df3 = df2[['user_id','sku_id']]    # �µ�Ʒ��8��Ϊ��Ӧ���û���Ʒ��
df_onlyP = pd.merge(df3,dfP)       # �ٴι��ˣ�ֻȡp�Ӽ��е���Ʒ,û��ָ��column

# ������û��µ������û���������ȡtop750
user_count = df_onlyP['user_id'].value_counts() # Ĭ�Ͼ��ǽ���
userSortList = user_count.index.tolist()  # ʹ��index��ö�ʧ��key��Ϣ
top750User = userSortList[:750]

# ������txt
s = '\n'.join([str(x) for x in top750User])
fin = open(r'','w')   # �ļ���������·��
fin.write(s)
fin.close()