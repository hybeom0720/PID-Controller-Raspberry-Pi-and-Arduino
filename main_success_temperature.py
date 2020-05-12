import serial
import time
import json

#User module
from Capstone_simple_pid import PID


#Serial communiation Raspberry Pi-Arduino

ser = serial.Serial("/dev/ttyUSB0", 9600)
while True:
    with open('experiment.json','r') as f:
        json_data = json.load(f)
        s_exp = json_data['Option']['start_exp']
        t_temp = json_data['Option']['t_temp']
        t_time = json_data['Option']['t_time']
    s_exp = int(s_exp)
    target_time = float(t_time)*60
    exp_result = dict()
    ex1 = dict()
    exp_results = dict()
    ex2 = dict()


    

    pid = PID(5,0.01,0.1, setpoint=int(t_temp))
    pid.output_limits = (0,100)

    relay = 'a'
    temp_temp = 0
    
    int_temp = ser.readline()
    eval_temp = float(int_temp[0:6])
    
    power = pid(eval_temp)
        
    print(power)
    exp_result["Now"] = ex1
    ex1["pid"] = float(power)
    ex1["temperature"] = eval_temp
    ex1["second"] = 0
    print(int_temp[0:6])
    
    with open('exp_result.json', 'w', encoding = 'utf-8') as make_file:
        json.dump(exp_result, make_file, indent = "\t")

    time.sleep(0.5)
    print("non-processing")
    relay = "a" #스위치 켜기
    
    
    ser.write(relay.encode())
    if eval_temp > int(t_temp):
        start_time = time.time()
        past_time =0
        while past_time < target_time and s_exp==1:
        #PID-Controller partww
            current_time = time.time()
            past_time = float(current_time - start_time)
            
            semi_eval_temp = eval_temp
            int_temp = ser.readline()
            print(int_temp[0:6])
            eval_temp = float(int_temp[0:6])
        
            if eval_temp <=0:
                eval_temp = temp_temp
        
            temp_temp = eval_temp
        
            power = pid(eval_temp)
        
            print(power)
            print("processing")
            if power <=0:
                relay = "b" # 스위치 끄기
            else :
                relay = "a" #스위치 켜기
    
    
            ser.write(relay.encode())
        
            index_time = float(past_time)
            print(past_time)
            
            if abs(semi_eval_temp - eval_temp)>20:
                eval_temp = semi_eval_temp
                print("Adjusting eval_temp")
            
            exp_result["Now"] = ex1
            ex1["pid"] = float(power)
            ex1["temperature"] = eval_temp
            ex1["second"] = int(past_time)
    
            exp_results[index_time] = ex2
            ex2["pid"] = float(power)
            ex2["temperature"] = eval_temp
            ex2["minute"] = int(past_time/60)
            time.sleep(0.5)
    
    
    
            with open('exp_result.json', 'w', encoding = 'utf-8') as make_file:
                json.dump(exp_result, make_file, indent = "\t")

          

    
    
        s_exp=0
        with open('exp_results.json', 'w', encoding = 'utf-8') as make_file:
            json.dump(exp_results, make_file, indent = "\t")



