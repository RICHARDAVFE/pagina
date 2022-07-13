from tkinter import*
from tkinter import messagebox
import matplotlib.animation as anim
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np 
from sympy import*  
class Grafica(Tk):        
    def __init__(self,*args, **kwargs):
        super().__init__(*args,*kwargs)
        self.geometry("600x700")
        self.config(bg="cyan")
        self.resizable(0,0)#(1,1)(True,True)
        self.rango1=False
        self.rango2=""
        self.rango3=""
        self.fun={"sin":"np.sin","cos":"np.cos","tan":"np.tan","sqrt":"np.sqrt","exp":"np.exp","log":"np.log","pi":"np.pi"}
        self.widgets()
       
    def reemplazar(self,funcion):
        for i in self.fun:
            if i in funcion:
                funcion=funcion.replace(i,self.fun[i])
        return funcion
    def animacion(self,i):
        if self.rango1==True:
            try:
                min=float(self.rango3[0]);max=float(self.rango3[1])
                
                if min<max:
                    x=np.arange(min,max,0.01)
                    self.rango2=[min,max]
                else:
                    self.rango1=False
            except:
                messagebox.showerror(title="Error",message="Ingrese un rango separadon por una coma (min,max)")
                self.rango1=False
                self.variacion.delete(0,len(self.variacion.get()))
        else:
            if self.rango2!="":
                x=np.arange(self.rango2[0],self.rango2[1],0.01)
            else:
                x=np.arange(1,10,0.01)
        try:
            
            y=eval(self.datos)
            y1=eval(self.datos1)
            self.ax.clear()
            self.ax.grid(True)
            self.ax.plot(x,y1,"r",label="Derivada")
            self.ax.plot(x,y,"g",label="Funcion")
            self.ax.legend(loc="best")
            self.resul=str(self.resul).replace('**','^')
            self.ax.set_title(f'${self.resul}$')
        except:
            self.ax.grid(True)
            self.ax.plot()
            
        self.ax.grid(True)
        self.ax.axhline(0,color="blue")
        self.ax.axvline(0,color="blue")
        self.ani.event_source.stop()
        
    def graficar(self):
        x=symbols('x')
        if self.variacion.get()!="":
            rann=self.variacion.get()
            self.rango3=rann.split(",")#retorna una lista
            self.rango1=True
        try:
            func=self.funcion.get()#recupero la funcion
            self.resul=diff(func,x)#derivo la funcion
            self.datos1=self.reemplazar(str(self.resul))
            self.datos=self.reemplazar(func)
            self.ani.event_source.start()
        except:
            messagebox.showerror(title="Error",message="Ingrese una funcion")
    def boton(self,x,y,text,bcolor,fcolor,cmd):
        def on_leave(e):
            btn["background"]=fcolor
            btn["foreground"]=bcolor
        def on_enter(e):
            btn["background"]=bcolor
            btn["foreground"]=fcolor
        btn=Button(self,text=text,
        fg=bcolor,
        bg=fcolor,
        activeforeground=fcolor,
        activebackground=bcolor,
        command=cmd,)
        btn.bind("<Enter>",on_enter)
        btn.bind("<Leave>",on_leave)
        btn.place(x=x,y=y,width=150)
    def widgets(self):
        etiqueta=Label(self,text="Introduzca una funcion de x",fg="blue", font="16")
        etiqueta.pack()
        etiqueta.place(x=150,y=30,width=300)
        self.funcion=Entry(self)
        self.funcion.pack()
        self.funcion.place(x=150,y=60,width=300)
        var=Label(self,text="Ingrese una variacion (opcional)",fg="blue", font="16")
        var.pack()
        var.place(x=170,y=85)
        self.variacion=Entry(self)
        self.variacion.pack()
        self.variacion.place(x=210,y=115,width=150)
        frame=Frame(self,bg="gold")
        frame.place(x=0,y=170,width=600,height=522)

        fig=Figure()
        self.ax=fig.add_subplot(111)
        cvs=FigureCanvasTkAgg(fig,frame)
        cvs.draw()
        cvs.get_tk_widget().pack(side=TOP,fill=BOTH)
        tlb=NavigationToolbar2Tk(cvs,frame)
        tlb.update()
        self.ani=anim.FuncAnimation(fig,self.animacion,interval=500)
        btn1=self.boton(210,140,"Derivar y Graficar","blue","white",cmd=self.graficar)
            

if __name__=="__main__":
    app=Grafica()
    app.mainloop()