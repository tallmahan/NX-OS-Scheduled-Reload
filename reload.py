#!/bin/env python                                                        
#                                                                        
# Python reload command.                                                 
# Accepts reload in <minutes> and reload cancel commands                 
#                                                                        
# Run with source background reload in xx                                
#                                                                        
#                                                                        
import cisco  
                                                                                                                                  
def issue_cancel():                                                      
    clip('kill background reload')                                       
    print 'Reload cancelled.'                                            
    return;                                                              
                                                                         
def send_alert(time_left, time_txt):                                     
    msg = str('send Reload in ') + str(time_left) + str(' ') + time_txt  
    clip(msg)                                                            
    return;                                                              
                                                                         
def process_reload(delay): 
	msg = str('send Reload in ') + str(delay) + str(' minutes... Type "source reload.py cancel" to cancel.') 
	clip(msg)
	i=0
	while i<2:
		if i==1:
  			clip('reload')
  		sleep = str('sleep ') + str(delay)
		clip(sleep)
		i=i+1            
	return;                                                                                               
    
                                                                         
#####################                                                    
#                                                                        
# Main processing                                                        
#                                                                        
#####################                                                    

if len(sys.argv) < 1:                                                    
    print 'Missing argument(s)'                                          
    sys.exit()  
                                                                           
if len(sys.argv) < 2:                                                    
    print 'Missing argument(s)'                                          
    sys.exit()                                                           

if  str(sys.argv[1]) == 'cancel':                                        
    if len(sys.argv) > 2:                                                
        print 'Too many arguments'                                       
        sys.exit()                                                       
    issue_cancel()                                                       
    sys.exit() 
    
if str(sys.argv[1]) != 'in': 
	print 'Missing "in" agruement. "source background reload.py >>>in<<< xx"' 
    sys.exit()
                                                                         
if str(sys.argv[1]) == 'in':                                             
    if len(sys.argv) < 3:                                                
        print 'Missing time delay argument'                              
        sys.exit()                                                       
    if len(sys.argv) > 3:                                                
        print 'Too many arguments'                                       
        sys.exit()                                                       
    if not str(sys.argv[2]).isdigit():                                   
        print 'Time delay argument(', str(sys.argv[2]), ') invalid.'     
        sys.exit()                                                       
    reload_delay = int(sys.argv[2])                                      
    if reload_delay > 14335:                                             
        print 'Reload delay cannot exceed 596 hours and 31 minutes'      
        sys.exit()                                                       
    if reload_delay < 1:                                                 
        print 'Reload delay must be greater than 0'                      
        sys.exit()                                                       
    process_reload(reload_delay*60)                                      
    sys.exit()                                                           
                                                                         
