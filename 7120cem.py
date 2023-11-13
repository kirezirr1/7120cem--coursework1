# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
from collections import defaultdict
import re
import json
import matplotlib.pyplot as plt
import warnings
import pandas as pd
import seaborn as sns

friends = pd.read_csv('H:/friends_transcripts.csv')
pd.set_option('display.max_colwidth', 50) #50 characters in the data frame
data=pd.DataFrame.from_dict(friends)
data.head()