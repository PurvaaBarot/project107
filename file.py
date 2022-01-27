from statistics import mean
from turtle import color
import pandas as pd
import plotly_express as px


df=pd.read_csv("Book1.csv")

mean1=df.groupby(["student_id" , "level"] , as_index=False).mean()
fig=px.scatter(mean1 , x= "attempt" , y="level" ,  color="student_id" , size="attempt")
fig.show()