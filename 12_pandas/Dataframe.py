# creating a data frame

import pandas as pd
import numpy as np


np.arange(0,20).reshape(5,4) # arage(0,20) gives you [0,1,2,3,..,17,18,19] 
# and reshape gives you:
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11],
#        [12, 13, 14, 15],
#        [16, 17, 18, 19]]) i.e 5 rows and 4 colums\

data=pd.DataFrame(data=np.arange(0,20).reshape(5,4),index=["Row1","Row2","Row3","Row4","Row5"],columns=["Col1","Col2","Col3","Col4"])

print(data)
print(data.iloc[0:5,0::3])