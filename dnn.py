#!/usr/bin/env python

import sys, glob
from fast_tlutmap import run, setMaxMemory

def main():
    setMaxMemory(2048)
    try:
        run('accelerator.vhd' , ['LAYER_1.vhd', 'LAYER_2.vhd', 'LAYER_3.vhd', 'LAYER_4.vhd', 'LAYER_5.vhd', 'LAYER_6.vhd'], K=6, performCheck=False, verboseFlag=False, resynthesizeFlag=True)
    except Exception as e:
        print >>sys.stderr, e
        exit(1)

if __name__=="__main__":
    main()
