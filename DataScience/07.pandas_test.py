import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import pandas as pd 
import numpy as np

# a = pd.Series([1,2,3,4], index=list('abcd'))
# print(a)
# print("a.values : {}".format(a.values))
# print("a.index : {}".format(a.index))


# b = pd.Series([1,2,3,4], index=list(['2020-01-01','2020-01-02', '2020-01-03', '2020-01-04']))
# print(b)
# print("b.values : {}".format(b.values))
# print("b.index : {}".format(b.index))
# print("b.shape : {}".format(b.shape))
# print("b.ndim : {}".format(b.ndim))
# print("b.size : {}".format(b.size))
# print("b[0] : {}".format(b[0]))
# print("b['2020-01-02'] : {}".format(b['2020-01-02']))
# print("b['2020-01-02':'2020-01-04'] : {}".format(b['2020-01-02':'2020-01-04']))

# # 시리즈는 새로운 데이터 추가 가능
# b['2020-01-05'] = 11
# print(b)

# # dataframe으로 전환
# c = b.to_frame()
# print(type(c))


# df = pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12]], index=list('abc'), columns=list('ABCD'))
# print(df)
# print("df.values : \n {}".format(df.values))
# print("type(df.values) :  {}".format(type(df.values)))
# print("df.index :  {}".format(df.index))
# print("df.columns :  {}".format(df.columns))
# print("df.shape :  {}".format(df.shape))
# print("rows :  {}".format(df.shape[0]))
# print("columns :  {}".format(df.shape[1]))
# print("df.ndim :  {}".format(df.ndim))
# print("df.size :  {}".format(df.size))
# # column 선택 
# print("df['B'] :  {}".format(df['B']))
# # loc[row index, column index]
# print("df.loc['b'] :  {}".format(df.loc['b']))
# print("df.loc['b','A':'B'] :  {}".format(df.loc['b', 'A':'B']))

# df['B'] = 100

# # iloc[row no, column no]
# print("df.iloc[2] :  {}".format(df.iloc[2]))
# print("df.loc[2,1:2] :  {}".format(df.iloc[2, 1:2]))

# # 자료형 변환 astype

# lists = [[1,3],[4,5]]
# columns = ['Math','Eng']
# dt = pd.DataFrame(data=lists, columns=columns) 
# print(dt)
# print("dt.dtypes : \n {}".format(dt.dtypes))

# dt2 = dt.astype({'Math': np.int32, 'Eng' : str})
# print("dt2.dtypes \n : {}".format(dt2.dtypes))

# # Series을 Dataframe으로 변환

# dt3 = pd.DataFrame({'A': pd.Series([1,2,3], dtype='int'), 'B': pd.Series([7,8,9], dtype='float')})
# print("dt3.dtypes : \n {}".format(dt3.dtypes))

# # dictionary형태로 데이터 입력 
# dt4 = pd.DataFrame({'date':['2020-01-01','2020-01-02','2020-01-03','2020-01-04'], 'type':['A','B','C','D']})
# print(dt4)

# # reshape(row수, column수)
# a = np.arange(10).reshape(2,5)
# print(a)
# df5 = pd.DataFrame(a, columns=list('abcde'))
# print(df5)

# # df['a'] : array return
# print("df5['a'] \n {}".format(df5['a']))

# # df[['a']] : dataframe return
# print("df5[['a']] \n {}".format(df5[['a']]))
# print("df5[['a','c','d']] \n {}".format(df5[['a','c','d']]))

# b = a > 5
# # 1차원으로 변환 
# c = b.flatten()
# print(c)
# # array로 return하는 논리연산
# print(df5.values.flatten()[c])
# # dataframe을 return하는 논리연산
# print(df5[df5>5])

# df1 = pd.DataFrame([[1,2],[3,4]], columns=list('가나'))
# print(df1)
# df2 = pd.DataFrame([[5,6],[7,8]], columns=list('가나'))
# print(df1)

# # append : vertical 결합
# print(df1.append(df2))
# # index를 새로 설정하려면 ignore_index=True
# print(df1.append(df2, ignore_index=True))

# # concat : vertical 결합 (axis=0 default)
# print(pd.concat([df1, df2], ignore_index=True))
# # concat : horizonal 결합 (axis=1)
# df3 = pd.DataFrame([[1],[2]], columns=list('다'))
# print(pd.concat([df1,df3], sort=True, axis=1))

# # merge : index 또는 공통컬럼을 통한 horizontal 결합 
# df1 = pd.DataFrame({
#     '고객번호': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
#     '이름': ['둘리', '도우너', '또치', '길동', '희동', '마이콜', '영희']
# }, columns=['고객번호', '이름'])
# print(df1)

# df2 = pd.DataFrame({
#     '고객번호': [1001, 1001, 1005, 1006, 1008, 1001],
#     '금액': [10000, 20000, 15000, 5000, 100000, 30000]
# }, columns=['고객번호', '금액'])
# print(df2)
# print(pd.merge(df1, df2))
# # 공통컬럼이 여려개일 일 경우 merge할 기준 key 컬럼 지정
# print(pd.merge(df1, df2, on='고객번호'))

# # how='outer' : 공통컬럼이 한쪽에만 있어도 모두 데이터를 보여준다
# print(pd.merge(df1, df2, how='outer'))

# # how ='letf' : left join
# print(pd.merge(df1, df2, how='left'))

# # how = 'right' : right join 
# print(pd.merge(df1, df2, how='right'))

# url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'
# # read HTML tables into a list of Dataframe objects
# dfs = pd.read_html(url)
# print(type(dfs))
# # list[0]은 dataframe임 
# dfs = dfs[0]
# print(type(dfs))
# print(dfs.head())
# print(dfs.info())
# # covnert to datetime
# dfs['Closing Date'] = pd.to_datetime(dfs['Closing Date'])
# print(dfs.head())
# print(dfs.dtypes)
# dfs['year'] = dfs['Closing Date'].dt.strftime('%Y')
# print(dfs.head())
# # 년도별 합계
# print(dfs['year'].value_counts())

# dfs.to_csv("failed_bank_list.csv")
# dfs2 = pd.read_csv("failed_bank_list.csv", parse_dates=['Closing Date'])
# print(dfs2.dtypes)

# # url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
# # dfs = pd.read_html(url)
# # print(dfs)
# # print(dfs[0])
# # print(type(dfs))


#  https://www.kaggle.com/lava18/google-play-store-apps
googlestore = pd.read_csv('googleplaystore.csv')

print(googlestore.shape)
print(googlestore.head())

# isna : 결측값이 있으면 true
print(googlestore.isna().sum())

# fillna(특정값) : 결측치를 특정값으로 채운다.
googlestore = googlestore.fillna(0)
print(googlestore.isna().sum())
print(googlestore.dtypes)

print(googlestore.head()['Last Updated'])
try :
    googlestore['Last Updated'] = pd.to_datetime(googlestore['Last Updated'], errors='coerce')
except Exception as e :
    print(e)

print(googlestore.isna().sum())
# 결측치가 있는 row
print(googlestore.loc[googlestore['Last Updated'].isna(),:])

# clipboard를 통해 excel로 복사해서 보는 방법이 현재는 best
googlestore.to_clipboard()

# 아래와 같이 이어서 쓰면 앞의 replace만 적용됨
# print(googlestore['Installs'].str.replace(",","").replace("+",""))
googlestore['Installs'] = googlestore['Installs'].str.replace(",","")
googlestore['Installs'] = googlestore['Installs'].str.replace("+","")
print(googlestore['Installs'].head(10))

# https://data36.com/pandas-tutorial-2-aggregation-and-grouping/
print(googlestore.groupby('Installs').count())
googlestore['Installs'] = googlestore['Installs'].str.replace("Free","0")
print(googlestore.dtypes)

# 자료형 변경
googlestore['Installs'] = googlestore['Installs'].astype(int)
print(googlestore.dtypes)


# select Installs, App, Reviews from googlestore
print(googlestore[['Installs', 'App', 'Reviews']])
# select distinct Category, Genres from googlestore
print(googlestore[['Category', 'Genres']].drop_duplicates())

# select * from googlestore where Category ='FAMILY' and Rating < 4 
# # dataframe.where() 는 결과가 이상하게 나온다.
filter1 = googlestore['Category']=='FAMILY'
filter2 = googlestore['Rating'] < 4
googlestore.loc[filter1 & filter2, :].to_clipboard()

# group by
# 이상치 제거
googlestore = googlestore.loc[googlestore['Reviews']!='3.0M', :]
# select sum(Rating) from googlestore group by Category
print(googlestore[['Category', 'Rating']].groupby(['Category']).sum())
# select avg(Rating) from googlestore group by Category
print(googlestore[['Category', 'Rating']].groupby(['Category']).mean())


rating_mean  = googlestore[['Category', 'Rating']].groupby(['Category']).mean()
# Category가 dataframe값이 아닌 index임
print(rating_mean.index)
print(rating_mean.columns)
# select * from rating_mean sort by Category
print(rating_mean.sort_values(by='Category', ascending=True))

# join

