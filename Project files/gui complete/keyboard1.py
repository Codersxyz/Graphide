import tkinter as tk

def keyboard (window,left_down_frame,entries) :

    left_down_frame.config(bg='#ffffff')
    # Keyboard

    # Numpad
    k = 1
    for i in reversed (range (3)) :
        for j in range (3) :
            def key_press (num = k) :
                window.focus_get().insert('end',str(num))

            nums = tk.Button(master=left_down_frame,width=8,height=2,text=str(k),
                            font=('consolas',12,'normal'),command=key_press,border=0.5,bg='#ffffff')
            nums.grid(row=i+4,column=j,padx=2,pady=2)
            k+=1

    # 0
    nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'normal'),
                    text=str(0),border=0.5,command=lambda:key_press(0),bg='#ffffff')
    nums.grid(row=7,column=0,padx=1,pady=1)


    # Decimal Point
    nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'normal'),
                    text='.',border=0.5,command=lambda:key_press('.'),bg='#d5d5d5')
    nums.grid(row=7,column=1,padx=1,pady=1)

    #Equals to
    nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'normal'),
                    text='=',border=0.5,command=lambda:key_press('='),bg='#d5d5d5')
    nums.grid(row=7,column=2,padx=1,pady=1)

    # Other
    row_1_buttons = (chr(960),'e',chr(8730),'INV')
    row_2_button = ('(',')','x','y')
    arith_button = (chr(247),chr(215),'-','+')

    # Row 1 
    for i in range (4) :
        def key_press (num = row_1_buttons[i]) :
                window.focus_get().insert('end',str(num))
        nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'normal'),
                    text=row_1_buttons[i],border=0.5,command=key_press,bg='#d5d5d5')
        nums.grid(row=1,column=i,padx=1,pady=1)

    # Row 2
    for i in range (4) :
        def key_press (num = row_2_button[i]) :
                window.focus_get().insert('end',str(num))
        nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'normal'),
                    text=row_2_button[i],border=0.5,command=key_press,bg='#d5d5d5')
        nums.grid(row=3,column=i,padx=1,pady=1)


    # Arithmetic buttons
    for i in range (4) :
        def key_press (num = arith_button[i]) :
                if num == chr(215) :
                    num = '*'
                elif num == chr(247) :
                    num = '/'
            
                window.focus_get().insert('end',num)

        nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'normal'),
                    text=arith_button[i],border=0.5,command=key_press,bg='#d5d5d5')
        nums.grid(row=i+4,column=3,padx=1,pady=1)

    # Row 0
    # Power
    nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'normal'),
                    text='^',border=0.5,command=lambda:key_press('^'),bg='#d5d5d5')
    nums.grid(row=1,column=1,padx=1,pady=1)

    # Log 
    nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'normal'),
                    text='log',border=0.5,command=lambda:key_press('log('),bg='#d5d5d5')
    nums.grid(row=1,column=2,padx=1,pady=1)

    # Function for all clear
    def all_clear() :
        window.focus_get().delete(0,'end')

    # Functino to clear 
    def clear () :
        curr = ''
        entry_box = window.focus_get()
        n = len(entry_box.get())-1
        for i in range (n) :
            curr += entry_box.get()[i]
        entry_box.delete(0,'end')
        entry_box.insert(0,curr)
        
        
    # All Clear
    nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'bold'),
                    text='AC',border=0.5,command=lambda:all_clear(),bg='#d5d5d5')
    nums.grid(row=1,column=0,padx=1,pady=1)

    # Clear 
    nums= tk.Button(master=left_down_frame,width=8,height=2,font=('consolas',12,'normal'),
                    text='Clear',border=0.5,command=lambda:clear(),bg='#d5d5d5')
    nums.grid(row=1,column=3,padx=1,pady=1)


    # Trignometric functions

    trig = tk.StringVar()
    trig.set('Trignometric')

    def trig_fun (none) : 
        num = trig.get()
        trig.set('Trignometric')
        if num == 'sec' :
            num = '(1/cos'
        elif num == 'cosec' :
            num = '(1/sin'
        elif num == 'cot' :
            num = '(1/tan'

        window.focus_get().insert('end',num+'(')
        
    trig_options = ('sin','cos','tan','sec','cosec','cot')
    trig_menu = tk.OptionMenu(left_down_frame,trig,*trig_options,command=trig_fun)
    trig_menu.config(width=12,height=2,border=0,font=('consolas',12,'normal'))
    trig_menu.grid(row=0,column=0,padx=1,pady=2,columnspan=2,sticky='nw')
