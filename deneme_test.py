from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Parameters, Base
import datetime
import models
import numpy as np
import plotly.express as px



engine = create_engine('sqlite:///parameters_database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
parameters_list = models.get_parameters(session)
id_list=[]

for parameter in parameters_list:
    id_list.append(parameter.id)

parameter_last = models.get_parameter(session, id_list[-1])
#print("P:{}".format(parameter_last.raw_measured_power,))

x = parameter_last.raw_measured_power


y = x.replace(',,,','/')
z = y.replace(',','')
t = z.replace('/',',')

#list_raw = list(t.split(","))

#print(list_raw)

raw_data = np.fromstring(t, dtype=float, sep=',')
theta = np.arange(0,361,1)
fig = px.line_polar(r=raw_data, theta=theta,start_angle=0)
fig.show()
#print(raw_data)
