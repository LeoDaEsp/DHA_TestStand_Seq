import pyvisa
import sys

    
def openInstrument():
    rm = pyvisa.ResourceManager()
    inst = rm.open_resource('ASRL11::INSTR')
    inst.write('INST:NSEL 6')
    inst.write('GLOB:OUTP:STAT OFF')
    inst.write('DISP:WIND:STAT ON')
    return inst, rm
    


if __name__=="__main__":
    
    inst, rm = openInstrument()
    
    case_n = sys.argv[1]
    
    if case_n == "start":  
        
        inst.write('GLOB:CURR:AMPL 2')
        
        inst.write('GLOB:VOLT:AMPL 28')
        
        inst.write('GLOB:OUTP:STAT ON')
                
    elif case_n == "stop":
        inst.write('GLOB:OUTP:STAT OFF')
        
    
    else:
        pass
        
    inst.close()
    rm.close()
        




