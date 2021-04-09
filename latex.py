import math
import latexify
import numpy as np
import random
from fractions import Fraction
from decimal import Decimal
from random import choice
##整数加减乘除
def type1():
    print("-----------整数加减乘除-----------")
    all1=[]
    for i in range(1000):
        a_value=random.randint(0,100)
        a_str=str(a_value)
        b_value=random.randint(0,100)
        b_str=str(b_value)
        c_str=str(a_value+b_value)
        sample = a_str+"+"+b_str+"="+c_str+"\n"
        all1.append(sample)
    for i in range(1000):
        a_value=random.randint(0,100)
        a_str=str(a_value)
        b_value=random.randint(0,100)
        b_str=str(b_value)
        c_str=str(a_value-b_value)
        sample = a_str+"-"+b_str+"="+c_str+"\n"
        all1.append(sample)
    for i in range(1000):
        a_value=random.randint(1,5)
        a_str=str(a_value)
        b_value=random.randint(1,25)
        b_str=str(b_value)
        c_str=str(a_value*b_value)
        sample = a_str+"\\times"+b_str+"="+c_str+"\n"
        all1.append(sample)
    for i in range(1000):
        a_value=random.randint(0,30)
        a_str=str(a_value)
        b_value=random.randint(1,10)
        b_str=str(b_value)
        c_value=a_value/b_value
        c_str=str(a_value/b_value)
        if(c_value%1==0):
            if(c_value==int(c_value)):
                c_value=int(c_value)
                c_str=str(c_value)
        if(c_value*1000%10!=0):
            c_str=a_str+"/"+b_str
        sample = a_str+ r"\div"+b_str+"="+c_str+"\n"
        if(c_value*100%1==0):
            all1.append(sample)
        print(sample)
    print(all1)
    return all1
    #file = open('file整数.txt','w');
    #file.writelines(all1);
    #file.close();
#分数加减乘除
def type2():
    print("-----------分数加减乘除-----------")
    all1=[]
    for i in range(1000):
        a_value=random.randint(1,10)
        aa_value=random.randint(1,10)
        a_str=str(a_value)
        aa_str=str(aa_value)
        b_value=random.randint(1,10)
        bb_value=aa_value
        b_str=str(b_value)
        bb_str=str(bb_value)
        a_frac = Fraction(a_value,aa_value)
        b_frac = Fraction(b_value,bb_value)
        c_value=a_value+b_value
        c_str = str(c_value)
        sample = r"\frac{"+a_str+"}{"+aa_str+"}+"+r"\frac{"+b_str+"}{"+bb_str+"}="+r"\frac{"+c_str+"}{"+bb_str+"}"+"\n"
        #sample = a_str+"/"+aa_str+"+"+b_str+"/"+bb_str+"="+c_str+"\n"
        all1.append(sample)
    print(all1)
    for i in range(1000):
        a_value=random.randint(1,10)
        aa_value=random.randint(1,10)
        a_str=str(a_value)
        aa_str=str(aa_value)
        b_value=random.randint(1,10)
        bb_value=aa_value
        b_str=str(b_value)
        bb_str=str(bb_value)
        a_frac = Fraction(a_value,aa_value)
        b_frac = Fraction(b_value,bb_value)
        c_str=str(a_value-b_value)
        sample = r"\frac{"+a_str+"}{"+aa_str+"}-"+r"\frac{"+b_str+"}{"+bb_str+"}="+r"\frac{"+c_str+"}{"+bb_str+"}"+"\n"
        #sample = r"\frac{"+a_str+"}{"+aa_str+"}-"+r"\frac{"+b_str+"}{"+bb_str+"}="+c_str+"\n"
        #sample = a_str+"/"+aa_str+"-"+b_str+"/"+bb_str+"="+c_str+"\n"
        all1.append(sample)
    for i in range(1000):
        a_value=random.randint(1,10)
        aa_value=random.randint(1,10)
        a_str=str(a_value)
        aa_str=str(aa_value)
        b_value=random.randint(1,10)
        bb_value=aa_value
        b_str=str(b_value)
        bb_str=str(bb_value)
        a_frac = Fraction(a_value,aa_value)
        b_frac = Fraction(b_value,bb_value)
        c_str=str(int(a_value)*b_value)
        sample = r"\frac{"+a_str+"}{"+aa_str+r"}\times"+r"\frac{"+b_str+"}{"+bb_str+"}="+r"\frac{"+c_str+"}{"+bb_str+"}"+"\n"
        #sample = r"\frac{"+a_str+"}{"+aa_str+r"}\times"+r"\frac{"+b_str+"}{"+bb_str+"}="+c_str+"\n"
        # sample = a_str+"/"+aa_str+"*"+b_str+"/"+bb_str+"="+c_str+"\n"
        all1.append(sample)
    #for i in range(5):
        #a_value=random.randint(1,10)
        #aa_value=random.randint(1,10)
        #a_str=str(a_value)
        #aa_str=str(aa_value)
        #b_value=random.randint(1,10)
        #bb_value=aa_value
        #b_str=str(b_value)
        #bb_str=str(bb_value)
        #a_frac = Fraction(a_value,aa_value)
        #b_frac = Fraction(b_value,bb_value)
        #c_str=str(int(a_value)/b_value)
        
        #sample = r"\frac{"+a_str+"}{"+aa_str+r"}\div"+r"\frac{"+b_str+"}{"+bb_str+"}="+r"\frac{"+c_str+"}{"+bb_str+"}"+"\n"
        #sample = r"\frac{"+a_str+"}{"+aa_str+r"}\div"+r"\frac{"+b_str+"}{"+bb_str+"}="+c_str+"\n"
        #sample = a_str+"/"+aa_str+"/"+b_str+"/"+bb_str+"="+c_str+"\n"
        #all1.append(sample)
    return all1
    #file = open('file分数.txt','w');
    #file.writelines(all1);
    #file.close();
#小数小数加减乘除
def type3():
    print("-----------小数和小数加减乘-----------")
    all1=[]
    for i in range(1000):
        a_value=random.uniform(0, 10) 
        a_value=round(a_value,1)
        a_str=str(a_value)
        b_value=random.uniform(0, 10) 
        b_value=round(b_value,1)
        b_str=str(b_value)
        c_value=Decimal(a_value+b_value).quantize(Decimal('0.0'))
        c_str=str(c_value)
        
        sample = a_str+"+"+b_str+"="+c_str+"\n"
        all1.append(sample)
    for i in range(1000):
        a_value=random.uniform(0, 10) 
        a_value=round(a_value,1)
        a_str=str(a_value)
        b_value=random.uniform(0, 10) 
        b_value=round(b_value,1)
        b_str=str(b_value)
        c_value=Decimal(a_value-b_value).quantize(Decimal('0.0'))
        c_str=str(c_value)
        sample = a_str+"-"+b_str+"="+c_str+"\n"
        all1.append(sample)
    for i in range(1000):
        a_value=random.uniform(0, 10) 
        a_value=round(a_value,1)
        a_str=str(a_value)
        b_value=random.uniform(0, 10) 
        b_value=round(b_value,1)

        b_str=str(b_value)
        c_value=Decimal(a_value*b_value).quantize(Decimal('0.00'))
        c_str=str(c_value)
        sample = a_str+"\\times"+b_str+"="+c_str+"\n"
        all1.append(sample)
    return all1
    #file = open('file小数.txt','w');
    #file.writelines(all1);
    #file.close();
#分数和小数乘法，分数和整数乘法
def type4():
    print("-----------分数和小数乘法，分数和整数乘法-----------")
    all1=[]
    for i in range(1000):
        a_value=random.randint(1,10)
        aa_value=random.randint(1,10)
        a_str=str(a_value)
        aa_str=str(aa_value)
        b_value=random.randint(1,10)
        b_str=str(b_value)
        a_frac = Fraction(a_value,aa_value)
        b_frac = Fraction(b_value,1)
        c_str=str(a_frac*b_frac)
        sample = r"\frac{"+a_str+"}{"+aa_str+r"}\times"+b_str+"="+c_str+"\n"
        #sample = a_str+"/"+aa_str+"\\times"+b_str+"="+c_str+"\n"
        all1.append(sample)
    for i in range(1000):
        a_value=random.randint(1,10)
        aa_value=random.randint(1,10)
        a_str=str(a_value)
        aa_str=str(aa_value)
        b = [0.5,0.25,0.375,0.75]
        bb = choice(b)
        b_str=str(bb)
        b_value = Fraction(bb)
        a_frac = Fraction(a_value,aa_value)
        c_str=str(a_frac*b_value)
        sample = r"\frac{"+a_str+"}{"+aa_str+r"}\times"+b_str+"="+c_str+"\n"
        #sample = a_str+"/"+aa_str+"\\times"+b_str+"="+c_str+"\n"
        all1.append(sample)
    return all1
    #file = open('file分数小数整数乘法.txt','w');
    #file.writelines(all1);
    #file.close();
def type5():
    pass




def main():
    allall=[]
    all1=type1()
    all2=type2()
    all3=type3()
    all4=type4()
    allall.append(all1)
    allall.append(all2)
    allall.append(all3)
    allall.append(all4)
    allall=str(allall)
    file = open('file.txt','w');
    file.writelines(allall);
    file.close();

    
    
    
    
    
if __name__ == '__main__':
    main()
