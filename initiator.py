import json
import os

while True:

    with open('experiment','r') as f:
        json_data = json.load(f)
    
        t_temp = json_data['Option']['t_temp']
        t_time = json_data['Option']['t_time']
        s_exp = json_data['Option']['start_exp']
    
print(json.dumps(json_data))
print(float(t_temp))


      
      