#Made by Yash Dholpure
#On Oct 11 2020 to Oct 12 2020
import time
import tkinter
import random
import re
win=tkinter.Tk()
textFGcolor='Black'

win.title('Time')
win.geometry('200x130')
win.iconbitmap(r"C:\Users\yashd\Downloads\Custom-Icon-Design-Flatastic-10-Clock.ico")
List=time.asctime().split(' ')

days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
months=['January','February','March','April','May','June','July','August','September','October','November','December']
obj1=re.compile(f'{List[0]}.+')
obj2=re.compile(f'{List[1]}.+')
def DnM():
        for d in days:
                for m in months:
                        truemonth=obj2.match(m)
                        trueday=obj1.match(d)
                        if trueday:
                                if truemonth:
                                        dayobj=trueday.group()
                                        di=days.index(dayobj)
                                        monthobj=truemonth.group()
                                        mi=months.index(monthobj)
                                        
                                        break
        return [di,mi]
found=DnM()
fday,fmonth=found
d=days[fday]
m=months[fmonth]
heresday=tkinter.Label(win,text='Day-->',fg=textFGcolor)
heresday.place(x=32,y=70)
day=tkinter.Label(win,text=d,fg=textFGcolor)
day.place(x=92,y=70)
heresyear=tkinter.Label(win,text='Year-->',fg=textFGcolor)
heresyear.place(x=32,y=55)
year=tkinter.Label(win,text=List[4],fg=textFGcolor)
year.place(x=92,y=55)
heresmonth=tkinter.Label(win,text='Month-->',fg=textFGcolor)
heresmonth.place(x=32,y=40)
month=tkinter.Label(win,text=m,fg=textFGcolor)
month.place(x=92,y=40)
heresdate=tkinter.Label(win,text='Date-->',fg=textFGcolor)
heresdate.place(x=32,y=25)
date=tkinter.Label(win,text=List[2],fg=textFGcolor)
date.place(x=92,y=25)
herestimer=tkinter.Label(win,text='Time-->',fg=textFGcolor)
herestimer.place(x=32,y=10)
timer=tkinter.Label(win,text=List[3],fg=textFGcolor)
timer.place(x=92,y=10)
def  update():
        def func():
         colors=['red','blue','green','yellow','pink','turquoise','gold','silver','black']
         color=random.choice(colors)
         textFGcolor=color
       
         print(color)
         heresday['fg']=color
         heresyear['fg']=color
         heresmonth['fg']=color
         heresdate['fg']=color
         herestimer['fg']=color
         day['fg']=color
         year['fg']=color
         month['fg']=color
         date['fg']=color
         timer['fg']=color
        List=time.asctime().split(' ')
        day['text']=d
        year['text']=List[4]
        month['text']=m
        date['text']=List[2]
        timer['text']=List[3]
        tkinter.Button(win,command=func,text='Click').place(x=100,y=100)
        
        win.after(1000,update)
        
update()

win.mainloop()
