import pandas as pd
df=pd.read_csv('E-Commerce_sales_Analysis/ecommerce_sales_project.csv')
# Chaning Data types
df['Order_Date']=pd.to_datetime(df['Order_Date'],errors='coerce').dt.tz_localize('Asia/Kolkata')
df['Age']=df['Age'].astype('Int64')
df['Quantity']=df['Quantity'].astype('Int64')
df['Price']=df['Price'].astype('float64')
# Fill Null values
# fill Revenue null values
mask=df['Revenue'].isnull()
df.loc[mask,'Revenue']=(df.loc[mask,'Price']*df.loc[mask,'Quantity']*(df.loc[mask,'Discount']/100))
# Fill Discount null values
mask=df['Discount'].isnull()
df.loc[mask,'Discount']=(1-df.loc[mask,'Revenue']/(df.loc[mask,'Price']*(df.loc[mask,'Quantity']))*100).round()
# Fill Age null values
mask=df['Age'].isnull()
df.loc[mask,'Age']=df['Age'].median()
print(df[df['Age'].isnull()])
