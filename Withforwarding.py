print("Mini Project 3 - MIPS ISA Dot Product Implementation with Forwarding")
ID1_36 = "014538238"
ID2_36 = "236750450"

R0_36=0

R1_36=0 #stores the sum

R2_36=[] #stores the fist vector
R4_36=[] #stores the second vector

R3_36=0*1 #point at next element in R2_36
R5_36=0*1 #point at next element in R4_36

R7_36=int(len(ID1_36)) #stores the length of vector which reduces after every cycle by one
ps_12=0

for var in ID1_36:
    R2_36.append(var) #1st vector stored

for var in ID2_36:
    R4_36.append(var) #2nd vector stored

def done():
    global ps_12 
    print("RESULTS AND ANALYSIS")
    print("Dot Product Using Forwarding")
    print("Two vectors are", ID1_36,"and",ID2_36)
    ps_12 = ps_12 + 1 #1 stalls due to beq $r7 $r0 done ; done  looping? Control Hazard 
    print("Dot Product Result=", R1_36, "stalls",ps_12) 
    exit()
#code starts here

R1_36=(R0_36 + R0_36)                       #addu $r1 $r0 $r0 ; result = 0
while(1):
 if R7_36==R0_36:                           #beq $r7 $r0 done ; done looping?
    done()
 else:
    if(R2_36):                          #Fetch  lw $r2 0($r3) ; load a elem
        True

    if(R2_36[R3_36])!="":                       #Decode lw $r2 0($r3) ; load a elem
        if(R4_36):                      #Fetch  lw $r4 0($r5) ; load b elem     
            True
    
    if len(R2_36)>=0:                       #Execute lw $r2 0($r3) ; load a elem
        if(R4_36[R5_36])!="":                   #Decode  lw $r4 0($r5) ; load b elem
            if(R2_36):                  #Fetch mul $r2 $r2 $r4 ;
                True                        

    if(R2_36[R3_36]):                       #Memory  lw $r2 0($r3) ; load a elem
        if len(R4_36)>=0:                   #Execute lw $r4 0($r5) ; load b elem
            if(R4_36[R5_36])!="":               #Decode mul $r2 $r2 $r4 ;
                if(R2_36):              #Fetch addu $r1 $r1 $r2 
                    True                            
                            
    if(R2_36[R3_36]):                       #Write  lw $r2 0($r3) ; load a elem
        m_v_12 = float(R2_36[R3_36])        
        m_v_12=m_v_12+0     
        if float(R4_36[R5_36])>=0:              #Memory lw $r4 0($r5) ; load b elem     
            ps_12=ps_12+1               
            pass                #NOP due to STALL           
            

    if(R4_36[R5_36]):                       #Write  lw $r4 0($r5) ; load b elem
        l_v_12 = float(R4_36[R5_36])        
        l_v_12=l_v_12+0 
        if len(R4_36)>=0:                   #Execute #mul $r2 $r2 $r4 ;
            if(R4_36[R5_36])!="":               #Decode addu $r1 $r1 $r2
             True

    if float(R4_36[R5_36])>=0:                  #Memory mul $r2 $r2 $r4 ; 
            ps_12=ps_12+1               
            pass                #NOP due to STALL           
    
                                                                    
    if(R4_36[R5_36]):                       #Write  mul $r2 $r2 $r4 
        if(R2_36[R3_36])!="":                   #Execute addu $r1 $r1 $r2             
            True        
        R2_36[R3_36] = float(R2_36[R3_36])*float(R4_36[R5_36])  
        R1_36=R1_36 + float(R2_36[R3_36])           #Memory addu $r1 $r1 $r2    
        R1_36=R1_36                     #Write addu $r1 $r1 $r2
        print(R2_36[0:R3_36])
        #print R1_36    
    R3_36=R3_36+1                           #Increment counter addiu $r3 $r3 #4
    R5_36=R5_36+1                           #Increment counter addiu $r5 $r5 #4 
    R7_36=R7_36-1