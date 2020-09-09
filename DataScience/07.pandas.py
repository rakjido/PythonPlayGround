import pandas as pd 

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


df = pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12]], index=list('abc'), columns=list('ABCD'))
print(df)
print("df.values : \n {}".format(df.values))
print("type(df.values) :  {}".format(type(df.values)))
print("df.index :  {}".format(df.index))
print("df.columns :  {}".format(df.columns))
print("df.shape :  {}".format(df.shape))
print("rows :  {}".format(df.shape[0]))
print("columns :  {}".format(df.shape[1]))
print("df.ndim :  {}".format(df.ndim))
print("df.size :  {}".format(df.size))
# column 선택 
print("df['B'] :  {}".format(df['B']))
# loc[row index, column index]
print("df.loc['b'] :  {}".format(df.loc['b']))
print("df.loc['b','A':'B'] :  {}".format(df.loc['b', 'A':'B']))

df['B'] = 100

# iloc[row no, column no]
print("df.iloc[2] :  {}".format(df.iloc[2]))
print("df.loc[2,1:2] :  {}".format(df.iloc[2, 1:2]))
