import re
def add_time(start, duration,dayOfWeek=''):
    # start="11:06 PM"
    # duration="26:02"
    hh = int(re.findall('([0-9]*):',start)[0])
    mm = int(re.findall(':([0-9]*)',start)[0])
    ap = re.findall(' (..)',start)[0]
    hrs = int(re.findall('([0-9]*):',duration)[0])
    mins = int(re.findall(':([0-9]*)',duration)[0])
    days=0
    mm+=mins
    if(mm>=60):
        hrs+=1
        mm=mm%60
    hh+=hrs
    if(hh%12==0):
        if ap=='AM':
            ap='PM'
        elif ap=='PM':
            ap='AM'
            days+=1        
    while(hh>12):
        hh-=12
        if ap=='AM':
            ap='PM'
        elif ap=='PM':
            ap='AM'
            days+=1
    daysOfWeek=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    # daysOfWeek=dict()
    # daysOfWeek['Monday']= 0
    # daysOfWeek['Tuesday']= 1
    # daysOfWeek['Wednesday']=2 
    # daysOfWeek['Thursday']= 3
    # daysOfWeek['Friday']= 4
    # daysOfWeek['Saturday']=5 
    # daysOfWeek['Sunday']= 6
    for day in daysOfWeek:
        if(day.lower()==dayOfWeek.lower()):
            dayOfWeekValue= daysOfWeek.index(day)
    if(mm<10):
        mm='0'+str(mm)
    if(days==0):    
        new_time=str(hh)+':'+str(mm)+' '+ap
    if(days==1):    
        new_time=str(hh)+':'+str(mm)+' '+ap+' (next day)'
    if(days>1):    
        new_time=str(hh)+':'+str(mm)+' '+ap+' ('+str(days)+' days later)'
    if(dayOfWeek!=''):
        if(days==0):    
            new_time=str(hh)+':'+str(mm)+' '+ap+', '+daysOfWeek[(dayOfWeekValue+days)%7]
        if(days==1):    
            new_time=str(hh)+':'+str(mm)+' '+ap+', '+daysOfWeek[(dayOfWeekValue+days)%7]+' (next day)'
        if(days>1):    
            new_time=str(hh)+':'+str(mm)+' '+ap+', '+daysOfWeek[(dayOfWeekValue+days)%7]+' ('+str(days)+' days later)'
    # print(new_time) 
    return new_time