#!/usr/bin/python3
x = input('x=')
y = input('y=')
op = input('operator=')
if op != '+' and op != '-' and op != '*' and op != '/':
  print('Invalid operator: '+op+'')
  exit()
if x != '0' and x != '0' and x != '1' and x != '2' and x != '3' and x != '4' and x != '5':
  print('X number out of range: '+str(x)+'')
  exit()
if y != '0' and y != '0' and y != '1' and y != '2' and y != '3' and y != '4' and y != '5':
  print('Y number out of range: '+str(y)+'')
  exit()
if x=='0' and y=='0' and op=='+':
  print('0+0=0')
  exit()
if x=='0' and y=='0' and op=='-':
  print('0-0=0')
  exit()
if x=='0' and y=='0' and op=='*':
  print('0*0=0')
  exit()
if x=='0' and y=='0' and op=='/':
  print('division by zero')
  exit()
if x=='0' and y=='1' and op=='+':
  print('0+1=1')
  exit()
if x=='0' and y=='1' and op=='-':
  print('0-1=-1')
  exit()
if x=='0' and y=='1' and op=='*':
  print('0*1=0')
  exit()
if x=='0' and y=='1' and op=='/':
  print('0/1=0.0')
  exit()
if x=='0' and y=='2' and op=='+':
  print('0+2=2')
  exit()
if x=='0' and y=='2' and op=='-':
  print('0-2=-2')
  exit()
if x=='0' and y=='2' and op=='*':
  print('0*2=0')
  exit()
if x=='0' and y=='2' and op=='/':
  print('0/2=0.0')
  exit()
if x=='0' and y=='3' and op=='+':
  print('0+3=3')
  exit()
if x=='0' and y=='3' and op=='-':
  print('0-3=-3')
  exit()
if x=='0' and y=='3' and op=='*':
  print('0*3=0')
  exit()
if x=='0' and y=='3' and op=='/':
  print('0/3=0.0')
  exit()
if x=='0' and y=='4' and op=='+':
  print('0+4=4')
  exit()
if x=='0' and y=='4' and op=='-':
  print('0-4=-4')
  exit()
if x=='0' and y=='4' and op=='*':
  print('0*4=0')
  exit()
if x=='0' and y=='4' and op=='/':
  print('0/4=0.0')
  exit()
if x=='0' and y=='5' and op=='+':
  print('0+5=5')
  exit()
if x=='0' and y=='5' and op=='-':
  print('0-5=-5')
  exit()
if x=='0' and y=='5' and op=='*':
  print('0*5=0')
  exit()
if x=='0' and y=='5' and op=='/':
  print('0/5=0.0')
  exit()
if x=='1' and y=='0' and op=='+':
  print('1+0=1')
  exit()
if x=='1' and y=='0' and op=='-':
  print('1-0=1')
  exit()
if x=='1' and y=='0' and op=='*':
  print('1*0=0')
  exit()
if x=='1' and y=='0' and op=='/':
  print('division by zero')
  exit()
if x=='1' and y=='1' and op=='+':
  print('1+1=2')
  exit()
if x=='1' and y=='1' and op=='-':
  print('1-1=0')
  exit()
if x=='1' and y=='1' and op=='*':
  print('1*1=1')
  exit()
if x=='1' and y=='1' and op=='/':
  print('1/1=1.0')
  exit()
if x=='1' and y=='2' and op=='+':
  print('1+2=3')
  exit()
if x=='1' and y=='2' and op=='-':
  print('1-2=-1')
  exit()
if x=='1' and y=='2' and op=='*':
  print('1*2=2')
  exit()
if x=='1' and y=='2' and op=='/':
  print('1/2=0.5')
  exit()
if x=='1' and y=='3' and op=='+':
  print('1+3=4')
  exit()
if x=='1' and y=='3' and op=='-':
  print('1-3=-2')
  exit()
if x=='1' and y=='3' and op=='*':
  print('1*3=3')
  exit()
if x=='1' and y=='3' and op=='/':
  print('1/3=0.3333333333333333')
  exit()
if x=='1' and y=='4' and op=='+':
  print('1+4=5')
  exit()
if x=='1' and y=='4' and op=='-':
  print('1-4=-3')
  exit()
if x=='1' and y=='4' and op=='*':
  print('1*4=4')
  exit()
if x=='1' and y=='4' and op=='/':
  print('1/4=0.25')
  exit()
if x=='1' and y=='5' and op=='+':
  print('1+5=6')
  exit()
if x=='1' and y=='5' and op=='-':
  print('1-5=-4')
  exit()
if x=='1' and y=='5' and op=='*':
  print('1*5=5')
  exit()
if x=='1' and y=='5' and op=='/':
  print('1/5=0.2')
  exit()
if x=='2' and y=='0' and op=='+':
  print('2+0=2')
  exit()
if x=='2' and y=='0' and op=='-':
  print('2-0=2')
  exit()
if x=='2' and y=='0' and op=='*':
  print('2*0=0')
  exit()
if x=='2' and y=='0' and op=='/':
  print('division by zero')
  exit()
if x=='2' and y=='1' and op=='+':
  print('2+1=3')
  exit()
if x=='2' and y=='1' and op=='-':
  print('2-1=1')
  exit()
if x=='2' and y=='1' and op=='*':
  print('2*1=2')
  exit()
if x=='2' and y=='1' and op=='/':
  print('2/1=2.0')
  exit()
if x=='2' and y=='2' and op=='+':
  print('2+2=4')
  exit()
if x=='2' and y=='2' and op=='-':
  print('2-2=0')
  exit()
if x=='2' and y=='2' and op=='*':
  print('2*2=4')
  exit()
if x=='2' and y=='2' and op=='/':
  print('2/2=1.0')
  exit()
if x=='2' and y=='3' and op=='+':
  print('2+3=5')
  exit()
if x=='2' and y=='3' and op=='-':
  print('2-3=-1')
  exit()
if x=='2' and y=='3' and op=='*':
  print('2*3=6')
  exit()
if x=='2' and y=='3' and op=='/':
  print('2/3=0.6666666666666666')
  exit()
if x=='2' and y=='4' and op=='+':
  print('2+4=6')
  exit()
if x=='2' and y=='4' and op=='-':
  print('2-4=-2')
  exit()
if x=='2' and y=='4' and op=='*':
  print('2*4=8')
  exit()
if x=='2' and y=='4' and op=='/':
  print('2/4=0.5')
  exit()
if x=='2' and y=='5' and op=='+':
  print('2+5=7')
  exit()
if x=='2' and y=='5' and op=='-':
  print('2-5=-3')
  exit()
if x=='2' and y=='5' and op=='*':
  print('2*5=10')
  exit()
if x=='2' and y=='5' and op=='/':
  print('2/5=0.4')
  exit()
if x=='3' and y=='0' and op=='+':
  print('3+0=3')
  exit()
if x=='3' and y=='0' and op=='-':
  print('3-0=3')
  exit()
if x=='3' and y=='0' and op=='*':
  print('3*0=0')
  exit()
if x=='3' and y=='0' and op=='/':
  print('division by zero')
  exit()
if x=='3' and y=='1' and op=='+':
  print('3+1=4')
  exit()
if x=='3' and y=='1' and op=='-':
  print('3-1=2')
  exit()
if x=='3' and y=='1' and op=='*':
  print('3*1=3')
  exit()
if x=='3' and y=='1' and op=='/':
  print('3/1=3.0')
  exit()
if x=='3' and y=='2' and op=='+':
  print('3+2=5')
  exit()
if x=='3' and y=='2' and op=='-':
  print('3-2=1')
  exit()
if x=='3' and y=='2' and op=='*':
  print('3*2=6')
  exit()
if x=='3' and y=='2' and op=='/':
  print('3/2=1.5')
  exit()
if x=='3' and y=='3' and op=='+':
  print('3+3=6')
  exit()
if x=='3' and y=='3' and op=='-':
  print('3-3=0')
  exit()
if x=='3' and y=='3' and op=='*':
  print('3*3=9')
  exit()
if x=='3' and y=='3' and op=='/':
  print('3/3=1.0')
  exit()
if x=='3' and y=='4' and op=='+':
  print('3+4=7')
  exit()
if x=='3' and y=='4' and op=='-':
  print('3-4=-1')
  exit()
if x=='3' and y=='4' and op=='*':
  print('3*4=12')
  exit()
if x=='3' and y=='4' and op=='/':
  print('3/4=0.75')
  exit()
if x=='3' and y=='5' and op=='+':
  print('3+5=8')
  exit()
if x=='3' and y=='5' and op=='-':
  print('3-5=-2')
  exit()
if x=='3' and y=='5' and op=='*':
  print('3*5=15')
  exit()
if x=='3' and y=='5' and op=='/':
  print('3/5=0.6')
  exit()
if x=='4' and y=='0' and op=='+':
  print('4+0=4')
  exit()
if x=='4' and y=='0' and op=='-':
  print('4-0=4')
  exit()
if x=='4' and y=='0' and op=='*':
  print('4*0=0')
  exit()
if x=='4' and y=='0' and op=='/':
  print('division by zero')
  exit()
if x=='4' and y=='1' and op=='+':
  print('4+1=5')
  exit()
if x=='4' and y=='1' and op=='-':
  print('4-1=3')
  exit()
if x=='4' and y=='1' and op=='*':
  print('4*1=4')
  exit()
if x=='4' and y=='1' and op=='/':
  print('4/1=4.0')
  exit()
if x=='4' and y=='2' and op=='+':
  print('4+2=6')
  exit()
if x=='4' and y=='2' and op=='-':
  print('4-2=2')
  exit()
if x=='4' and y=='2' and op=='*':
  print('4*2=8')
  exit()
if x=='4' and y=='2' and op=='/':
  print('4/2=2.0')
  exit()
if x=='4' and y=='3' and op=='+':
  print('4+3=7')
  exit()
if x=='4' and y=='3' and op=='-':
  print('4-3=1')
  exit()
if x=='4' and y=='3' and op=='*':
  print('4*3=12')
  exit()
if x=='4' and y=='3' and op=='/':
  print('4/3=1.3333333333333333')
  exit()
if x=='4' and y=='4' and op=='+':
  print('4+4=8')
  exit()
if x=='4' and y=='4' and op=='-':
  print('4-4=0')
  exit()
if x=='4' and y=='4' and op=='*':
  print('4*4=16')
  exit()
if x=='4' and y=='4' and op=='/':
  print('4/4=1.0')
  exit()
if x=='4' and y=='5' and op=='+':
  print('4+5=9')
  exit()
if x=='4' and y=='5' and op=='-':
  print('4-5=-1')
  exit()
if x=='4' and y=='5' and op=='*':
  print('4*5=20')
  exit()
if x=='4' and y=='5' and op=='/':
  print('4/5=0.8')
  exit()
if x=='5' and y=='0' and op=='+':
  print('5+0=5')
  exit()
if x=='5' and y=='0' and op=='-':
  print('5-0=5')
  exit()
if x=='5' and y=='0' and op=='*':
  print('5*0=0')
  exit()
if x=='5' and y=='0' and op=='/':
  print('division by zero')
  exit()
if x=='5' and y=='1' and op=='+':
  print('5+1=6')
  exit()
if x=='5' and y=='1' and op=='-':
  print('5-1=4')
  exit()
if x=='5' and y=='1' and op=='*':
  print('5*1=5')
  exit()
if x=='5' and y=='1' and op=='/':
  print('5/1=5.0')
  exit()
if x=='5' and y=='2' and op=='+':
  print('5+2=7')
  exit()
if x=='5' and y=='2' and op=='-':
  print('5-2=3')
  exit()
if x=='5' and y=='2' and op=='*':
  print('5*2=10')
  exit()
if x=='5' and y=='2' and op=='/':
  print('5/2=2.5')
  exit()
if x=='5' and y=='3' and op=='+':
  print('5+3=8')
  exit()
if x=='5' and y=='3' and op=='-':
  print('5-3=2')
  exit()
if x=='5' and y=='3' and op=='*':
  print('5*3=15')
  exit()
if x=='5' and y=='3' and op=='/':
  print('5/3=1.6666666666666667')
  exit()
if x=='5' and y=='4' and op=='+':
  print('5+4=9')
  exit()
if x=='5' and y=='4' and op=='-':
  print('5-4=1')
  exit()
if x=='5' and y=='4' and op=='*':
  print('5*4=20')
  exit()
if x=='5' and y=='4' and op=='/':
  print('5/4=1.25')
  exit()
if x=='5' and y=='5' and op=='+':
  print('5+5=10')
  exit()
if x=='5' and y=='5' and op=='-':
  print('5-5=0')
  exit()
if x=='5' and y=='5' and op=='*':
  print('5*5=25')
  exit()
if x=='5' and y=='5' and op=='/':
  print('5/5=1.0')
  exit()
