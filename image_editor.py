from tkinter import *
from tkinter import filedialog,colorchooser,messagebox
from PIL import Image,ImageOps,ImageTk,ImageFilter,ImageDraw,ImageFont
import numpy as np
# from tkinter import ttk
def error():
    messagebox.showerror('Error','Please add an image')
def p():
    pass
def apply():
    global filepath,img_,img,r
    ext=filepath.split('.')[-1]
    if(r!=1):

        if(ext=='jpg'):
            file=filedialog.asksaveasfilename(initialdir='C:\\Users\\SAYAN\Desktop\\python projects',defaultextension='.jpg')
            img_.save(file)   
        else:
            file=filedialog.asksaveasfilename(initialdir='C:\\Users\\SAYAN\Desktop\\python projects',defaultextension='.png')
            img_.save(file)
    else:
        file=filedialog.asksaveasfilename(initialdir='C:\\Users\\SAYAN\Desktop\\python projects',defaultextension='.png')
        if(file.split('.')[-1]=='png'):
            img.save(file)
        else:
            messagebox.showerror('Error','Invalid extension!! Save to png ')
def apply_round():
    global filepath,img_,r,img
    r=1
    if(filepath.split('.')[-1]=='png'):
        p=img_.convert('RGB')
        p.save('x.jpg')
        img_=Image.open('x.jpg')
    canv.destroy()
    canv1=Canvas(root,width=img_.width,height=img_.height)
    canv1.place(x=350,y=250)
    width,height=int(img_.width/2),int(img_.height/2)
    img_=img_.resize((width,height),Image.LANCZOS)        
    height_,width_ = img_.size
    
    lum_img = Image.new('L', [height_,width_] , 0)
    draw = ImageDraw.Draw(lum_img)
    draw.pieslice([(0,0), (height_,width_)], 0, 360, 
                fill = 255, outline = "white")
    img_arr =np.array(img_)
    lum_img_arr =np.array(lum_img)
    final_img_arr = np.dstack((img_arr,lum_img_arr))
    img=Image.fromarray(final_img_arr)
    canv1.config(width=img.width,height=img.height)
    imgg=ImageTk.PhotoImage(img)
    canv1.imgg=imgg
    canv1.create_image(0,0,image=imgg,anchor='nw')
def apply_filter():
    global filepath,img_,clicked,canv
    width,height=int(img_.width/2),int(img_.height/2)
    img_=img_.resize((width,height),Image.LANCZOS)
    # img=img_
    if clicked.get()=='Black and white':
        img_=img_.convert('L')
    elif clicked.get()=='Blur':
        img_=img_.filter(ImageFilter.BLUR)
    elif clicked.get()=='Sharpen':
        img_=img_.filter(ImageFilter.SHARPEN)
    elif clicked.get()=='Emboss':
        img_=img_.filter(ImageFilter.EMBOSS)
    else:
        img_=img_.filter(ImageFilter.SMOOTH)
    img=ImageTk.PhotoImage(img_)
    canv.img=img
    canv.create_image(0,0,image=img,anchor='nw')
    
    
def apply_text():
    global img_,filepath,color_,clicked,font_,entertxt,xentry,yentry
    x=int(xentry.get())
    y=int(yentry.get())
    width,height=int(img_.width/2),int(img_.height/2)
    img_=img_.resize((width,height),Image.LANCZOS)
    if(int(font_.get())<=50 and x < img_.width and y < img_.height):
        I1 = ImageDraw.Draw(img_)
        if(clicked.get()=='Times new roman'):
            myFont = ImageFont.truetype('Times New Roman\\times new roman.ttf',int(font_.get()))
        elif(clicked.get()=='Times new roman bold'):
            myFont = ImageFont.truetype('Times New Roman\\times new roman bold.ttf',int(font_.get()))
        elif(clicked.get()=='Times new roman italic'):
            myFont = ImageFont.truetype('Times New Roman\\times new roman italic.ttf',int(font_.get()))
        elif(clicked.get()=='Times new roman bold italic'):
            myFont = ImageFont.truetype('Times New Roman\\times new roman bold italic.ttf',int(font_.get()))
        elif(clicked.get()=='Calibri'):
            myFont = ImageFont.truetype('Calibri\Calibri.ttf',int(font_.get()))
        elif(clicked.get()=='Calibri bold'):
            myFont = ImageFont.truetype('Calibri\Calibrib.ttf',int(font_.get()))
        elif(clicked.get()=='Calibri italic'):
            myFont = ImageFont.truetype('Calibri\Calibril.ttf',int(font_.get()))
        I1.text((x,y),entertxt.get(), font=myFont, fill =color_)
        img=ImageTk.PhotoImage(img_)
        canv.img=img
        canv.create_image(0,0,image=img,anchor='nw')
    else:
        messagebox.showerror("Error","font limit exceeded")

def apply_rotate():
     global angle,dir_,filepath,img_
     width,height=int(img_.width/2),int(img_.height/2)
     img_=img_.resize((width,height),Image.LANCZOS)
     if(int(angle_.get())<=360):
        angle=int(angle_.get())
        dir_=clicked.get()
        if(dir_=='Clockwise'):
            img_= img_.rotate(360-angle)
        else:
            img_=img_.rotate(angle)
        
        img=ImageTk.PhotoImage(img_)
        canv.img=img
        canv.create_image(0,0,image=img,anchor='nw')
     else:
        messagebox.showerror('Error','Angle limit exceeded')

def apply_border():
    global width_,color_,filepath,img_
    width,height=int(img_.width/2),int(img_.height/2)
    img_=img_.resize((width,height),Image.LANCZOS)
    if(int(width_.get())<=50):
        width=int(width_.get())
        color=color_
        img_= ImageOps.expand(img_, border=width, fill=color)
        img=ImageTk.PhotoImage(img_)
        canv.img=img
        canv.create_image(0,0,image=img,anchor='nw')
    else:
         messagebox.showerror("Error","width Limit exceeded")
def apply_resize():
    
        
        global w,h,img_,filepath
        img_=img_.resize((w,h),Image.ANTIALIAS)
        img=ImageTk.PhotoImage(img_)
        canv.img=img
        canv.create_image(0,0,image=img,anchor='nw')
def apply_crop():
        global img_,filepath
        x=int(x_.get())
        y=int(y_.get())
        w=int(width_.get())+x
        h=int(height_.get())+y
        img_=img_.crop(box=(x,y,w,h))
        img=ImageTk.PhotoImage(img_)
        canv.img=img
        canv.create_image(0,0,image=img,anchor='nw')
def change_color():
    global pen_color,color_
    pen_color=colorchooser.askcolor(title='Select Color')[1]
    # print(type(pen_color))
    color_=pen_color
def change_size(size):
    global pen_size
    pen_size = size
def clear_():
    canv.delete("all")
    canv.create_image(0, 0, image=canv.img, anchor="nw")

def set_wh():
    global w,h
    width,height=img_.size
    ratio=height/width
    w=int(width_.get())
    h=int(w*ratio)
    height_.config(text=h)
def resize_():
    global width_,height_
    crop.config(command=p)
    draww.config(command=p)
    border.config(command=p)
    rotate.config(command=p)
    roundimg.config(command=p)
    addtxt.config(command=p)
    filter.config(command=p)
    lbl=Label(left_frame,text='Resize',font=('times new roman',35,'bold'),bg='skyblue',fg='red')
    lbl.place(x=40,y=50)
    wlabel=Label(left_frame,text='Width',font=('times new roman',25,'bold'),bg='skyblue')
    wlabel.place(x=30,y=150)
    hlabel=Label(left_frame,text='Height',font=('times new roman',25,'bold'),bg='skyblue')
    hlabel.place(x=30,y=250)
    width_=Entry(left_frame,width=8,font=('times new roman',20))
    width_.focus_set()
    width_.place(x=30,y=200)
    height_=Label(left_frame,width=8,bg='white',font=('times new roman',20))
    height_.place(x=30,y=300)
    setbtn=Button(left_frame,text='SET',font=('times new roman',15),command=set_wh)
    setbtn.place(x=90,y=400)
    previewbtn=Button(left_frame,text='PREVIEW',font=('times new roman',15),command=apply_resize)
    previewbtn.place(x=90,y=450)
    applybtn=Button(left_frame,text='APPLY',font=('times new roman',15),command=apply)
    applybtn.place(x=90,y=500)
    # pass
def crop_():
    global x_,y_,width_,height_
    resize.config(command=p)
    draww.config(command=p)
    border.config(command=p)
    rotate.config(command=p)
    roundimg.config(command=p)
    addtxt.config(command=p)
    filter.config(command=p)
    lbl=Label(left_frame,text='Crop',font=('times new roman',35,'bold'),bg='skyblue',fg='red')
    lbl.place(x=40,y=50)
    xlabel=Label(root,text='Position X',font=('times new roman',25,'bold'),bg='skyblue')
    xlabel.place(x=58,y=200)
    x_=Entry(root,width=10,font=('times new roman',20))
    x_.focus_set()
    x_.place(x=58,y=250)
    ylabel=Label(root,text='Position Y',font=('times new roman',25,'bold'),bg='skyblue')
    ylabel.place(x=58,y=300)
    y_=Entry(root,width=10,font=('times new roman',20))
    y_.focus_set()
    y_.place(x=58,y=350)
    wlabel=Label(root,text='Width',font=('times new roman',25,'bold'),bg='skyblue')
    wlabel.place(x=58,y=400)
    width_=Entry(root,width=10,font=('times new roman',20))
    width_.focus_set()
    width_.place(x=58,y=450)
    hlabel=Label(root,text='Height',font=('times new roman',25,'bold'),bg='skyblue')
    hlabel.place(x=58,y=500)
    height_=Entry(root,width=10,font=('times new roman',20))
    height_.focus_set()
    height_.place(x=58,y=550)
    previewbtn=Button(left_frame,text='PREVIEW',font=('times new roman',15),command=apply_crop)
    previewbtn.place(x=90,y=555)
    applybtn=Button(left_frame,text='APPLY',font=('times new roman',15),command=apply)
    applybtn.place(x=90,y=600)
def border_():
    global width_,color_
    resize.config(command=p)
    crop.config(command=p)
    draww.config(command=p)
    # border.config(command=p)
    rotate.config(command=p)
    roundimg.config(command=p)
    addtxt.config(command=p)
    filter.config(command=p)
    lbl=Label(left_frame,text='Border',font=('times new roman',35,'bold'),bg='skyblue',fg='red')
    lbl.place(x=40,y=50)
    wlabel=Label(left_frame,text='Width',font=('times new roman',25,'bold'),bg='skyblue')
    wlabel.place(x=30,y=150)
    clabel=Label(left_frame,text='Colour',font=('times new roman',25,'bold'),bg='skyblue')
    clabel.place(x=30,y=250)
    width_=Spinbox(left_frame,font=('times new roman',10),from_=1,to=50)
    width_.focus_set()
    width_.place(x=30,y=200)
    color_=Button(left_frame,text='CHOOSE COLOR',font=('times new roman',10),bg='green',fg='white',command=change_color)
    color_.place(x=30,y=300)
    previewbtn=Button(left_frame,text='PREVIEW',font=('times new roman',15),command=apply_border)
    previewbtn.place(x=90,y=400)
    applybtn=Button(left_frame,text='APPLY',font=('times new roman',15),command=apply)
    applybtn.place(x=90,y=450)
def draw_(event):
     x1,y1=(event.x-pen_size),(event.y-pen_size)
     x2,y2=(event.x+pen_size),(event.y+pen_size)
     canv.create_oval(x1,y1,x2,y2,fill=pen_color,outline='')
def draw():
    resize.config(command=p)
    crop.config(command=p)
    # draww.config(command=p)
    border.config(command=p)
    rotate.config(command=p)
    roundimg.config(command=p)
    addtxt.config(command=p)
    filter.config(command=p)
    lbl=Label(left_frame,text='Draw',font=('times new roman',35,'bold'),bg='skyblue',fg='red')
    lbl.place(x=40,y=50)
    canv.bind('<B1-Motion>',draw_)
    color_btn=Button(left_frame,text='Change Colour',font=('times new roman',15),command=change_color)
    color_btn.place(x=50,y=150)
    penlbl=Label(left_frame,text='Pensize',font=('times new roman',20,'bold'),bg='skyblue')
    penlbl.place(x=50,y=200)
    pen_size_frame=Frame(left_frame,bg='skyblue')
    pen_size_frame.place(x=50,y=250)
    pen_size_1=Radiobutton(pen_size_frame,text='Small',value=2,command=lambda: change_size(2),bg='white')
    pen_size_1.pack(padx=10,pady=10)
    pen_size_2 = Radiobutton(pen_size_frame, text="Medium", value=5, command=lambda: change_size(5), bg="white")
    pen_size_2.pack(padx=15,pady=10)
    pen_size_2.select()
    pen_size_3 =Radiobutton(pen_size_frame, text="Large", value=8, command=lambda: change_size(7), bg="white")
    pen_size_3.pack(padx=20,pady=10)
    clear_btn=Button(left_frame,text='Clear',font=('times new roman',15),command=clear_)
    clear_btn.place(x=55,y=400)
    
def rotate_():
    global angle_,clicked
    resize.config(command=p)
    crop.config(command=p)
    draww.config(command=p)
    border.config(command=p)
    # rotate.config(command=p)
    roundimg.config(command=p)
    addtxt.config(command=p)
    filter.config(command=p)
    lbl=Label(left_frame,text='Rotate',font=('times new roman',35,'bold'),bg='skyblue',fg='red')
    lbl.place(x=40,y=50)
    alabel=Label(left_frame,text='Angle\n(in deg.)',font=('times new roman',20,'bold'),bg='skyblue')
    alabel.place(x=30,y=150)
    angle_=Spinbox(left_frame,font=('times new roman',10),from_=1,to=360)
    angle_.focus_set()
    angle_.place(x=30,y=230)
    dirlabel=Label(left_frame,text='Direction',font=('times new roman',20,'bold'),bg='skyblue')
    dirlabel.place(x=30,y=250)
    options=['Clockwise','Anticlockwise']
    clicked = StringVar()
    clicked.set( "Anticlockwise")
    drop=OptionMenu(left_frame,clicked,*options)
    drop.place(x=30,y=300)
    previewbtn=Button(left_frame,text='PREVIEW',font=('times new roman',15),command=apply_rotate)
    previewbtn.place(x=90,y=400)
    applybtn=Button(left_frame,text='APPLY',font=('times new roman',15),command=apply)
    applybtn.place(x=90,y=450)
def round_():
    resize.config(command=p)
    crop.config(command=p)
    draww.config(command=p)
    border.config(command=p)
    rotate.config(command=p)

    # roundimg.config(command=p)
    addtxt.config(command=p)
    filter.config(command=p)
    lbl=Label(left_frame,text='Round\nCrop',font=('times new roman',35,'bold'),bg='skyblue',fg='red')
    lbl.place(x=40,y=50)
    previewbtn=Button(left_frame,text='PREVIEW',font=('times new roman',15),command=apply_round)
    previewbtn.place(x=90,y=450)
    applybtn=Button(left_frame,text='APPLY',font=('times new roman',15),command=apply)
    applybtn.place(x=90,y=500)
def text_():
    global clicked,font_,entertxt,color_,xentry,yentry
    resize.config(command=p)
    crop.config(command=p)
    draww.config(command=p)
    border.config(command=p)
    rotate.config(command=p)
    roundimg.config(command=p)
    
    # addtxt.config(command=p)
    filter.config(command=p)
    lbl=Label(left_frame,text='Text',font=('times new roman',35,'bold'),bg='skyblue',fg='red')
    lbl.place(x=40,y=50)
    flabel=Label(left_frame,text='Font type',font=('times new roman',20,'bold'),bg='skyblue')
    flabel.place(x=30,y=100)
    options=['Times new roman','Times new roman bold','Times new roman italic','Times new roman bold italic','Calibri','Calibri bold','Calibri italic']
    clicked = StringVar()
    clicked.set("Calibri")
    drop=OptionMenu(left_frame,clicked,*options)
    drop.place(x=30,y=150)
    fsize=Label(left_frame,text='Font size',font=('times new roman',20,'bold'),bg='skyblue')
    fsize.place(x=30,y=200)
    font_=Spinbox(left_frame,font=('times new roman',10),from_=1,to=50)
    font_.focus_set()
    font_.place(x=30,y=250)
    text=Label(left_frame,text='Text',font=('times new roman',20,'bold'),bg='skyblue')
    text.place(x=30,y=300)
    entertxt=Entry(left_frame,width=10,font=('times new roman',20))
    entertxt.place(x=30,y=350)
    xlabel=Label(left_frame,text='X',font=('times new roman',20),bg='skyblue')
    xlabel.place(x=30,y=400)
    xentry=Entry(left_frame,width=5,font=('times new roman',20))
    xentry.place(x=55,y=400)
    ylabel=Label(left_frame,text='Y',font=('times new roman',20),bg='skyblue')
    ylabel.place(x=30,y=450)
    yentry=Entry(left_frame,width=5,font=('times new roman',20))
    yentry.place(x=55,y=450)
    color_=Button(left_frame,text='CHOOSE COLOR',font=('times new roman',10),bg='green',fg='white',command=change_color)
    color_.place(x=30,y=500)
    previewbtn=Button(left_frame,text='PREVIEW',font=('times new roman',15),command=apply_text)
    previewbtn.place(x=90,y=550)
    applybtn=Button(left_frame,text='APPLY',font=('times new roman',15),command=apply)
    applybtn.place(x=90,y=600)
def filter_():
    global clicked
    resize.config(command=p)
    crop.config(command=p)
    draww.config(command=p)
    border.config(command=p)
    rotate.config(command=p)
    roundimg.config(command=p)
    addtxt.config(command=p)
    
    # filter.config(command=p)
    lbl=Label(left_frame,text='Filter',font=('times new roman',35,'bold'),bg='skyblue',fg='red')
    lbl.place(x=40,y=50)
    filter_label=Label(left_frame,text='Select Filter',font=('times new roman',20,'bold'),bg='skyblue')
    filter_label.place(x=30,y=200)
    options=['Black and white','Blur','Emboss','Sharpen','Smooth']
    clicked = StringVar()
    clicked.set("Blur")
    drop=OptionMenu(left_frame,clicked,*options)
    drop.place(x=30,y=250)
    previewbtn=Button(left_frame,text='PREVIEW',font=('times new roman',15),command=apply_filter)
    previewbtn.place(x=90,y=300)
    applybtn=Button(left_frame,text='APPLY',font=('times new roman',15),command=apply)
    applybtn.place(x=90,y=400)
    
def add_image():
    
    global img_,filepath,left_frame
    global canv
    filepath=filedialog.askopenfilename(initialdir='C:\\Users\\SAYAN\Desktop\\python projects',title='Open a file')
    ext=filepath.split('.')[-1]
    if(ext!='jpg' and ext!='png' and ext!='jfif' and ext!='pjpg' and ext!='pjp'):
        messagebox.showerror('Error','Only png/jpg are permitted')
    else:

        img=Image.open(filepath)
        img_=img
        width,height=int(img.width/2),int(img.height/2)
        img=img.resize((width,height),Image.LANCZOS)
        canv.config(width=img.width,height=img.height)
        img=ImageTk.PhotoImage(img)
        canv.img=img
        canv.create_image(0,0,image=img,anchor='nw')
        resize.config(command=resize_)
        crop.config(command=crop_)
        draww.config(command=draw)
        border.config(command=border_)
        rotate.config(command=rotate_)

        roundimg.config(command=round_)
       
        addtxt.config(command=text_)
       
        filter.config(command=filter_)
        
        
         
     
root=Tk()
root.geometry("1200x1000")
root.title("Image Editor")
title=Label(root,text='IMAGE EDITOR',font=('times new roman',30,'bold'),bg='#FFBF00',fg='white',bd=1,relief='solid')
title.place(x=0,y=20,relwidth=1)
root.config(bg='#EADDCA')
add_img=Button(root,text='ADD IMAGE',font=('arial',15,'bold'),fg='white',bg='red',command=add_image)
add_img.place(x=500,y=80)
pen_size=5
pen_color='black'
filepath=""
r=0
im1=PhotoImage(file='resize.png')
im2=PhotoImage(file='crop.png')
im3=PhotoImage(file='draw.png')
im4=PhotoImage(file='border.png')
im5=PhotoImage(file='rotate.png')
im6=PhotoImage(file='round.png')
im7=PhotoImage(file='text.png')
im8=PhotoImage(file='filter.png')

left_frame=Frame(root,width=200,height=650,bg='skyblue')
left_frame.pack(side='left',padx=55)
top_frame=Frame(root,width=495,height=80,bg='white')
top_frame.pack(padx=50,pady=150)
canv=Canvas(root,width=700,height=550)
canv.place(x=350,y=250)
resize=Button(root,image=im1,bg='black',command=error)
resize.place(x=350,y=150)
crop=Button(root,image=im2,bg='black',command=error)
crop.place(x=431,y=150)
draww=Button(root,image=im3,bd=1,bg='black',command=error)
draww.place(x=513,y=150)
border=Button(root,image=im4,bg='black',command=error)
border.place(x=592,y=150)
rotate=Button(root,image=im5,bg='black',command=error)
rotate.place(x=670,y=150)
roundimg=Button(root,image=im6,bg='black',command=error)
roundimg.place(x=753,y=150)
addtxt=Button(root,image=im7,bg='white',bd=2,relief='solid',command=error)
addtxt.place(x=830,y=150)
filter=Button(root,image=im8,bg='white',bd=2,relief='solid',command=error)
filter.place(x=913,y=150)
root.mainloop()