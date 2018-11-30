
# coding: utf-8

# In[2]:


import numpy as np
import datetime as dt
import sqlalchemy

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import ession
from sqlalchemy import inspect, create_engine, func

from flask import Flask, jsonify


# In[3]:


app = Flask(__name__)


# In[9]:


engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()

Base.prepare(engine, reflect=True)


# In[10]:


Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)


# In[ ]:


def 

