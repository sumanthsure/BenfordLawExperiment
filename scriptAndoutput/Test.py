from PIL import Image
import numpy as np
import os
from os.path import isfile, join
import benfordslaw as bl
exp = sorted(os.listdir())
for file in exp:
    if("jp" in file):
        print(file)
        im = Image.open(file)
        a = np.asarray(im)
        freq={}
        temp = []
        for i in a:
            for j in i:
                for t in j:
                    try:
                        l=str(t)
                        st_v = int(l[0])
                        temp.append(int(l))
                        if(st_v not in freq):
                            freq[st_v]=1
                        else:
                            freq[st_v]+=1
                    except:
                        continue
        del freq[0]
        # out = bl.fit(np.asarray(temp))
        # bl.plot(out, file)
        print({k: v for k, v in sorted(freq.items(),reverse=True, key=lambda item: item[1])})