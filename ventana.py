import tkinter as tkinter
import pandas as pd
import tkinter.filedialog as fd
from tkinter import messagebox
import matplotlib.pyplot as plt
import seaborn as sn
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def buscarArchivo():
    filetypes = (
        ('Excel files', '*.xlsx'),
    )

    pathArchivo = fd.askopenfilename(
        title='Abra un archivo',
        initialdir='C:\\Users\\kusag\\Documents\\PracticasAnalisisDeDatos\\PracticaPerros',
        filetypes=filetypes)

    if not pathArchivo:
        return

    mostrarGraficosConElArchivoExcel(pathArchivo)


def mostrarGraficosConElArchivoExcel(pathArchivo):
    # Lectura del archivo excel con pandas
    df = pd.read_excel(pathArchivo)
    # Obtenemos las columnas de edad y razas, ademas de traer una prueba con df.head
    try:
        edad = df["edad"]
        raza = df["raza"]
        #print(edad)
        #print(raza)
        print(df.head())
    except Exception as e:
        # Mostramos el error de mensaje si ocurre una excepcion
        messagebox.showerror("Error", f"Verifica las columnas")
        print(e)
        return
    
        #Ejecutamos gráficas secundarias con seaplot donde se puede ver con zoom
    
    sn.histplot(df["edad"], kde=True, color="red")
    plt.show()
    sn.histplot(df["raza"], kde=True, color = "green")
    plt.show()   

        # Generamos un label para mostrar el titulo
    lblTitle = tkinter.Label(ventana, text="Graficas Resultantes", font=("Arial", 25, "bold"))
    lblTitle.pack()

        # Creamos un canvas para poder plotear la grafica 1 en la ventana

    figEdad, axEdad = plt.subplots(figsize=(5, 5), dpi = 100)
    axEdad.hist(edad, alpha=0.5)
    axEdad.set_title("Distribucion De edades")
    axEdad.set_xlabel("edad")
    axEdad.set_ylabel("count")
    canvasEdades = FigureCanvasTkAgg(figEdad, master=ventana)
    canvasEdades.draw()
    canvasEdades.get_tk_widget().pack(side=tkinter.LEFT)

   
    #Creamos un segundo canvas para poder plotear la gráfica 2 en la ventana
      
    figRaza = plt.figure(figsize=(10, 5), dpi=100)
    axRaza = figRaza.add_subplot(111)
    axRaza.set_title('Distribucion De Razas')
    bar = FigureCanvasTkAgg(figRaza, ventana)
    bar.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.NONE)
    breedsDataFrame = raza.value_counts().sort_index()
    breedsDataFrame.plot(kind='bar', legend=False, ax=axRaza, colormap='Greens_r')

ventana = tkinter.Tk()

ventana.geometry("1500x1000")


framePrincipal = tkinter.Frame(ventana, bg="blue")
framePrincipal.grid()
framePrincipal.pack()

lblBienvenida = tkinter.Label(framePrincipal, text="Bienvenido al programa para graficar Perritos", bg="blue", width=250, font=("Arial", 25, "bold"))
lblBienvenida.pack()
cerrarBtn = tkinter.Button(framePrincipal, text="Cerrar", command=ventana.destroy, bg="red", width=50, font=("Arial", 12, "bold"))
cerrarBtn.pack()

button = tkinter.Button(framePrincipal, text='Abrir archivo', command=buscarArchivo, bg="green", width=50, font=("Arial", 12, "bold"))
button.pack(side=tkinter.TOP, pady=10)


ventana.mainloop()
