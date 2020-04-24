#!/usr/bin/python
# -*- coding: utf-8 -*-
print ('MINI PROJECT 2 -DOT PRODUCT- ')
print ('STUDENT ID- 013765336')
ID1_36 = '013765336'
ID2_36 = '235987558'

R0_36 = 0

R1_36 = 0  # USED FOR STORING THE RESULT

R2_36 = []  # FIRST VECTOR
R4_36 = []  # SECOND VECTOR

R3_36 = 0 * 1  # NEXT ELEMENT POINTER IN R2
R5_36 = 0 * 1  # NEXT ELEMENT POINTER IN R4

R7_36 = int(len(ID1_36))  # STORE THE LENGTH OF A VECTOR
Stalls_36 = 0

for var in ID1_36:
    R2_36.append(var)  # STORE 1st VECTOR

for var in ID2_36:
    R4_36.append(var)  # STORE SECOND VECTOR


def done():
    global Stalls_36
    print ('RESULT AND ANALYSIS')
    print ('Dot Product Without Forwarding')
    print ('Two vectors are', ID1_36, 'and', ID2_36)
    Stalls_36 = Stalls_36 + 3  # 3 INSTRUCTION DELAY
    print ('Dot Product Result=', R1_36, 'stalls', Stalls_36)
    exit()


                                            # START OF THE CODE

R1_36 = R0_36 + R0_36  # ADDU $R1 $R0 $R0 ; result = 0
while 1:
    if R7_36 == R0_36:  # BEQ $R7 $R0 DONE ; done looping?
        done()
    else:
        if R2_36:  # Fetch  LW $R2 0($R3) ; load a element
            True

        if R2_36[R3_36] != '':  # Decode LW $R2 0($R3) ; load a element
            if R4_36:  # Fetch  lw $R4 0($R5) ; load b element........
                True

        if len(R2_36) >= 0:  # Execute lW $R2 0($R3) ; load a element
            if R4_36[R5_36] != '':  # Decode  lW $R4 0($R5) ; load b element
                if R2_36:  # Fetch mul $R2 $R2 $R4 ;
                    True

        if R2_36[R3_36]:  # Memory  lW $R2 0($R3) ; load a element
            if len(R4_36) >= 0:  # Execute lW $R4 0($R5) ; load b element
                Stalls_36 = Stalls_36 + 1
                pass  # NOP due to STALL............

        if R2_36[R3_36]:  # Write  lW $R2 0($R3) ; load a element
            m_v_12 = float(R2_36[R3_36])
            m_v_12 = m_v_12 + 0
            if float(R4_36[R5_36]) >= 0:  # Memory lW $R4 0($R5) ; load b element
                Stalls_36 = Stalls_36 + 1
                pass  # NOP due to STALL............

        if R4_36[R5_36]:  # Write  lW $R4 0($R5) ; load b element
            l_v_12 = float(R4_36[R5_36])
            l_v_12 = l_v_12 + 0
            Stalls_36 = Stalls_36 + 1
            pass  # NOP due to STALL

        if R4_36[R5_36] != '':  # Decode MUL $R2 $R2 $R4 ;
            if R2_36:  # Fetch addu $R1 $R1 $R2....
                True

        if len(R4_36) >= 0:  # Execute #MUL $R2 $R2 $R4 ;
            Stalls_36 = Stalls_36 + 1
            pass  # NOP due to STALL....

        if float(R4_36[R5_36]) >= 0:  # Memory mul $r2 $r2 $r4 ;
            Stalls_36 = Stalls_36 + 1
            pass  # NOP due to STALL

        if R4_36[R5_36]:  # Write  MUL $R2 $R2 $R4
            R2_36[R3_36] = float(R2_36[R3_36]) * float(R4_36[R5_36])
            Stalls_36 = Stalls_36 + 1
            pass  # NOP due to STALL

        if R4_36[R5_36] != '':  # Decode ADDU $r1 $r1 $R2
            if R2_36[R3_36] != '':  # Execute ADDU $R1 $R1 $R2............
                R1_36 = R1_36 + float(R2_36[R3_36])  # Memory addu $R1 $R1 $R2....
                R1_36 = R1_36  # Write addu $R1 $R1 $R2....
        R3_36 = R3_36 + 1  # Increment counter addiu $R3 $R3 #4
        R5_36 = R5_36 + 1  # Increment counter addiu $R5 $R5 #4....

                                           # R7_36=R7_36-1

        if R7_36:  # Fetch  beq $R7 $R0 done ; done looping?
            Stalls_36 = Stalls_36 + 1
            pass  # NOP due to STALL

        if R7_36 != '':  # Decode beq Rr7 R0 done ; done looping?
            Stalls_36 = Stalls_36 + 1
            pass  # NOP due to STALL

        if len(str(R7_36)) >= 0:  # Execute BEQ $R7 $R0 done ; done looping?
            if R7_36 == R7_36:  # Memory  BEQ $R7 $R0 done ; done looping?
                R7_36 = R7_36 - 1  # Write and Decrement counter addiu $R7 $R7 #-1
        print (R2_36[0:R3_36])
