from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import operator
import math, random
from math import sqrt
from pandas import DataFrame
import json
#images
import io
from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.backends.backend_agg import FigureCanvasAgg
from random import sample

# Create your views here.
class CuadradoMedio(View): 
    def post(self, request):
        # data = request.POST 
        data = json.loads(request.body)


        n=int(data['n']) # interacciones
        #r=7182 # seleccionamos el valor inicial r
        r=int(data['r']) # seleccionamos el valor inicial r
        l=len(str(r)) # determinamos el número de dígitos
        lista = [] # almacenamos en una lista
        lista2 = []
        lista3 =[]
        i=1
        #while len(lista) == len(set(lista)):
        for i in range(n):
            x=str(r*r) # Elevamos al cuadrado r
            if l % 2 == 0:
                x = x.zfill(l*2)
            else:
                x = x.zfill(l)
            y=(len(x)-l)/2
            y=int(y)
            r=int(x[y:y+l])
            lista.append(r)
            lista2.append(x)
            i=i+1

        df = pd.DataFrame({'X2':lista2,'Xi':lista})
        dfrac = df["Xi"]/10**l
        df["ri"] = dfrac
        for xi in lista:
            lista3.append(xi/10**1)
        df.head()
       
       
        # x1=df['ri']
        # plt.plot(x1)
        # plt.title('Generador de Numeros Aleatorios Cuadrados Medios')
        # plt.xlabel('Serie')
        # plt.ylabel('Aleatorios')
        # plt.show()

        

        return JsonResponse({'X2':lista2,'Xi':lista, 'ri':lista3 }, safe=False)


#prueba grafico


class Grafico(View):
    def get(self, request, valores):
    
        convert = eval(valores) # Devuelve [1,2,3] (list)
        x1= convert
        
    
        # Creamos una figura y le dibujamos el gráfico
        f = plt.figure()

        # Creamos los ejes
        axes = f.add_axes([0.15, 0.15, 0.75, 0.75]) # [left, bottom, width, height]
        axes.plot(x1)
        axes.set_xlabel("Eje X")
        axes.set_ylabel("Eje Y")
        axes.set_title("Gráfico generado")

        # Como enviaremos la imagen en bytes la guardaremos en un buffer
        buf = io.BytesIO()
        canvas = FigureCanvasAgg(f)
        canvas.print_png(buf)

        # Creamos la respuesta enviando los bytes en tipo imagen png
        response = HttpResponse(buf.getvalue(), content_type='image/png')

        # Limpiamos la figura para liberar memoria
        f.clear()

        # Añadimos la cabecera de longitud de fichero para más estabilidad
        response['Content-Length'] = str(len(response.content))

        # Devolvemos la response
        return response















        #GRAFICO CUADRADO MEDIO
# class Grafico(View):
#     def post(self, request):
#         # data = json.loads(request.body)
#         # x1=data
#         # plt.plot(x1)
#         # plt.title('Gráfico generado')
#         # plt.xlabel('')
#         # plt.ylabel('')
#         # # plt.show()
        
#         # f = plt.figure()

#         # buf = io.BytesIO()
#         # canvas = FigureCanvasAgg(f)
#         # canvas.print_png(buf)

#         # # # Creamos la respuesta enviando los bytes en tipo imagen png
#         # response = HttpResponse(buf.getvalue(), content_type='image/png')

#         # # # Limpiamos la figura para liberar memoria
#         # # # f.clear()

#         # # # Añadimos la cabecera de longitud de fichero para más estabilidad
#         # response['Content-Length'] = str(len(response.content))

#         # # Devolvemos la response
#         # return JsonResponse({response}, safe=False)
#         # # return render('grafica.html', imagen={ 'imagen': plot_url })
#         # # return JsonResponse({}, safe=False)
#         x = range(1,11)
#         y = sample(range(20), len(x))

#         # Creamos una figura y le dibujamos el gráfico
#         f = plt.figure()

#         # Creamos los ejes
#         axes = f.add_axes([0.15, 0.15, 0.75, 0.75]) # [left, bottom, width, height]
#         axes.plot(x, y)
#         axes.set_xlabel("Eje X")
#         axes.set_ylabel("Eje Y")
#         axes.set_title("Mi gráfico dinámico")

#         # Como enviaremos la imagen en bytes la guardaremos en un buffer
#         buf = io.BytesIO()
#         canvas = FigureCanvasAgg(f)
#         canvas.print_png(buf)

#         # Creamos la respuesta enviando los bytes en tipo imagen png
#         response = HttpResponse(buf.getvalue(), content_type='image/png')

#         # Limpiamos la figura para liberar memoria
#         f.clear()

#         # Añadimos la cabecera de longitud de fichero para más estabilidad
#         response['Content-Length'] = str(len(response.content))
        
#         print(response)
#         # Devolvemos la response
#         return JsonResponse({}, safe=False)

#         # return response
class GraficoPM(View):
    def get(self, request, x, m3, m4):
      
        xvalor = eval(x) # Devuelve [1,2,3] (list)
        m3valor = eval(m3) # Devuelve [1,2,3] (list)
        m4valor = eval(m3) # Devuelve [1,2,3] (list)
        
    
        # Creamos una figura y le dibujamos el gráfico
        f = plt.figure()

        # Creamos los ejes
        axes = f.add_axes([0.15, 0.15, 0.75, 0.75]) # [left, bottom, width, height]
        axes.plot(xvalor)
        axes.plot(m3valor)
        axes.plot(m4valor)
        axes.set_xlabel("Eje X")
        axes.set_ylabel("Eje Y")
        axes.set_title("Gráfico generado")

        # Como enviaremos la imagen en bytes la guardaremos en un buffer
        buf = io.BytesIO()
        canvas = FigureCanvasAgg(f)
        canvas.print_png(buf)

        # Creamos la respuesta enviando los bytes en tipo imagen png
        response = HttpResponse(buf.getvalue(), content_type='image/png')

        # Limpiamos la figura para liberar memoria
        f.clear()

        # Añadimos la cabecera de longitud de fichero para más estabilidad
        response['Content-Length'] = str(len(response.content))

        # Devolvemos la response
        return response



         #GRAFICO PROMEDIO MOVIL
# class GraficoPM(View):
#     def post(self, request):
#         data = json.loads(request.body)
      
#         plt.plot(data['x'])
#         plt.plot(data['m3'])
#         plt.plot(data['m4'])
#         plt.title('Gráfico generado')
#         plt.xlabel('')
#         plt.ylabel('')
#         plt.show()
        

#         return JsonResponse({}, safe=False)




class CongruencialLineal(View):    
    def post(self, request):
        data = json.loads(request.body)

        n = int(data['n'])
        m = int(data['m'])
        a = int(data['a'])
        x0 = int(data['x0'])
        c = int(data['c'])
        x = [1] * n
        r = [0.1] * n
        # print (" Método de Congruencia Lineal ")
        # print("-------------------------------")
        # print ("n=cantidad de números generados : ", n)
        # print()
        # print ("m : ", m)
        # print ("a : ", a)
        # print ("c : ", c)
        # print ("Xo : ", x0 )
        for i in range(0, n):
            x[i] = ((a*x0)+c) % m
            x0 = x[i]
            r[i] = x0 / m
        # llenamos nuestro DataFrame
        d = {'Xn': x, 'ri': r }
        df = pd.DataFrame(data=d)


       
        # plt.plot(r)
        # plt.title('Generador de Numeros Aleatorios ')
        # plt.xlabel('Serie')
        # plt.ylabel('Aleatorios')
        # plt.show()


        return JsonResponse({'Xn': x, 'ri': r }, safe=False)

class CongruencialMultiplicativo(View):    
    def post(self, request):
        data = json.loads(request.body)
        n = int(data['n'])
        m = int(data['m'])
        a = int(data['a'])
        x0 = int(data['x0']) 
        x = [1] * n
        r = [0.1] * n
        # print (" Generador Congruencial multiplicativo")
        # print ("--------------------------------------")
        for i in range(0, n):
            x[i] = (a*x0) % m
            x0 = x[i]
            r[i] = x0 / m
        d = {'Xn': x, 'ri': r }
        df = pd.DataFrame(data=d)


        # print(d)

       
        # plt.plot(r)
        # plt.title('Generador de Numeros Aleatorios ')
        # plt.xlabel('Serie')
        # plt.ylabel('Aleatorios')
        # plt.show()


        return JsonResponse({'Xn': x, 'ri': r }, safe=False)


class PromedioMovil(View):    
    def post(self, request):
        
        list = json.loads(request.body)
      
      
        MMO3=[0, 0]
        MMO4=[0, 0, 0]
        eMMO3=[]
        eMMO4=[]
        N3 = 3
        N4 = 4

        cumsum, moving_averages = [0], []

        for i, x in enumerate(list, 1):
            cumsum.append(cumsum[i-1] + x)
            if i>=N3:                
                MMO3.insert(i, (cumsum[i] - cumsum[i-N3])/N3 )               
                    

        for j, x in enumerate(list, 1):
            cumsum.append(cumsum[j-1] + x)
            if j>=N4:                
                MMO4.insert(j, (cumsum[j] - cumsum[j-N4])/N4 ) 

        for k, x in enumerate(list, 1):

            if list[k-1] - MMO3[k-1] == list[k-1] :

                eMMO3.insert(k, 0)    
            else:
                eMMO3.insert(k, list[k-1] - MMO3[k-1])     

        for q, x in enumerate(list, 1):
    
            if list[q-1] - MMO4[q-1] == list[q-1] :

                eMMO4.insert(q, 0)    
            else:
                eMMO4.insert(q, list[q-1] - MMO4[q-1])  

        return JsonResponse({'MUESTRA': list, 'MM03':MMO3, 'MMO4':MMO4,'eMM03': eMMO3, 'eMM04': eMMO4}, safe=False)

class AlisamientoExponencial(View):    
    def post(self, request):
       
        data = json.loads(request.body)
        list = data['lista']
        # print(json.loads(request.body))

        SN = [0]      
       
       # el DataFrame se llama movil

        movil = pd.DataFrame(list)
        # mostramos los 5 primeros registros
        movil.head()
        # alfa = float(data['alfa[4]'])s
        alfa = float(data['alfa'])
        unoalfa = 1. - alfa
        for i, x in enumerate(list, 1):                   
      
            SN.insert(i, (list[i-1] * alfa ) + (list[0]*unoalfa))        
        return JsonResponse({'X':list, 'SN': SN}, safe=False)


class RegresionLineal(View):    
    def post(self, request):
        
        data = json.loads(request.body)
        x = data['x']       
        y = data['y']

        #filtrar
        # for i, result in enumerate(data, 0):
            
        #     if (result == 'x['+str(i)+']'):    
        #         x.insert(i, float(data['x['+str(i)+']']))        
        #         # x.insert(i, float(result[i]))
        #     else:
        #         y.insert(i, float(data['y['+str(i)+']']))      

             

        xcuadrado = [r ** 2 for r in x]
        xy = list(map(operator.mul, x, y))
        ycuadrado = [r ** 2 for r in y]


      
        # ajuste de la recta (polinomio de grado 1 f(x) = ax + b)
        p = np.polyfit(x,y,1) # 1 para lineal, 2 para polinomio ...
        p0,p1 = p

        return JsonResponse({'X':x, 'Y':y, 'X2':xcuadrado, 'XY':xy, 'Y2':ycuadrado, 'Result': "El valor de p0 = " + str(round(p0, 4) ) +"Valor de p1 = " + str(round(p1, 4) )  }, safe=False)

class RegresionNoLineal(View):    
    def post(self, request):
        data = json.loads(request.body)    
      
        x = data['x']       
        y = data['y']

        # for i, result in enumerate(data, 0):
            
        #     if (result == 'x['+str(i)+']'):    
        #         x.insert(i, float(data['x['+str(i)+']']))        
        #         # x.insert(i, float(result[i]))
        #     else:
        #         y.insert(i, float(data['y['+str(i)+']']))


        xcuadrado = [r ** 2 for r in x]
        xcubo = [r ** 3 for r in x]
        xcuarta = [r ** 4 for r in x]
        xy = list(map(operator.mul, x, y))
        xcuadradoy = list(map(operator.mul, xcuadrado, y))

      
        # ajuste de la recta (polinomio de grado 1 f(x) = ax + b)
        p = np.polyfit(x,y,2) # 1 para lineal, 2 para polinomio ...
        p1,p2,p3 = p
        result = "El valor de p0 = " + str(round(p1, 4) ) + " Valor de p1 = " + str(round(p2, 4) ) + " el valor de p2 = " + str(round(p3, 4) )

        return JsonResponse({'X':x, 'Y':y, 'X2':xcuadrado, 'X3':xcubo, 'X4':xcuarta, 'XY':xy, 'X2Y':xcuadradoy, 'Result':result}, safe=False)

class Montecarlo(View):    
    def post(self, request):
        
        data = json.loads(request.body)    
        # print()
        muestra = data['lista']    
        
        # for i, result in enumerate(data, 0):
                        
        #     if (result == 'lista['+str(i)+']'):
        #         muestra.insert(i, float(data['lista['+str(i)+']']))        
             
              
        suma = sum(muestra)
        probabilidad = []
        FPA = []
        Max = []

        for i, m in enumerate(muestra, 1):
            probabilidad.insert(i,round(m/suma, 4))
            FPA.append(round(sum(probabilidad), 4))
        
        Max = FPA
        Min = [0]

        for i, m in enumerate(Max, 1):
            if i<len(Max):                
                Min.insert(i, round(m, 4))

        n = int(data['n'])
        m = float(data['m'])
        a = float(data['a'])
        x0 = float(data['x0'])
        c = int(data['c'])



        x = [1] * n
        r = [0.1] * n
        for i in range(0, n):
            x[i] = ((a*x0)+c) % m
            x0 = x[i]
            r[i] = round(x0 / m, 3)
        # llenamos nuestro DataFrame
        d = {'ri': r }
        # print(d)
        # dfMCL = pd.DataFrame(data=d)

      
        return JsonResponse({'Muestra':muestra, 'Probabilidad':probabilidad, 'FPA':FPA, 'Min':Min, 'Max' :Max, 'ri': r, 'Simulacion':x}, safe=False)

class TransformadaInversaAditivo(View):    
    def post(self, request):

        data = json.loads(request.body)    

        n = data['n']
        m = data['m']
        a = data['a']
        x0 = data['x0']
        c = data['c']
        landa = data['landa']
        x = [1] * n
        r = [0.1] * n
        inversa = []
        
        # print (" Método de Congruencia Lineal ")
        # print("-------------------------------")
        # print("n=cantidad de números generados : ", n)
        # print()
        # print ("m : ", m)
        # print ("a : ", a)
        # print ("c : ", c)
        # print ("Xo : ", x0 )
        for i in range(0, n):
            x[i] = ((a*x0)+c) % m
            x0 = x[i]
            r[i] = round(x0 / m,4)
            inversa.insert(i, round(r[i]*(-1/landa)*np.log(r[i]),4) )

        # llenamos nuestro DataFrame
        d = {'Xn': x, 'ri': r }
        df = pd.DataFrame(data=d)


       # print(d)

       
        # plt.plot(r)
        # plt.title('Generador de Numeros Aleatorios ')
        # plt.xlabel('Serie')
        # plt.ylabel('Aleatorios')
        # plt.show()


        return JsonResponse({'Xn': x, 'ri': r, 'inversa':inversa }, safe=False)



class TransformadaInversaMultiplicativo(View):    
    def post(self, request):
        data = json.loads(request.body)    
        n = data['n']
        m = data['m']
        a = data['a']
        x0 = data['x0']
        landa = data['landa']
        x = [1] * n
        r = [0.1] * n
        inversa = []

        
        # print (" Generador Congruencial multiplicativo")
        # print ("--------------------------------------")
        for i in range(0, n):
            x[i] = (a*x0) % m
            x0 = x[i]
            r[i] = x0 / m
            inversa.insert(i, round(r[i]*(-1/landa)*np.log(r[i]),4) )   
        
        d = {'Xn': x, 'ri': r }
        df = pd.DataFrame(data=d)


       
        # plt.plot(r)
        # plt.title('Generador de Numeros Aleatorios ')
        # plt.xlabel('Serie')
        # plt.ylabel('Aleatorios')
        # plt.show()


        return JsonResponse({'Xn': x, 'ri': r, 'Inversa':inversa }, safe=False)


class LineaEspera(View):    
    def post(self, request):
        data = json.loads(request.body)    

        landa = data['landa']
        nu = data['nu']

        #DATOS
        ALL=[]
        ASE=[]
        TILL=[]
        TISE=[]
        TIRLL=[]
        TIISE=[]
        TIFSE=[]
        TIESP=[]
        TIESA=[]
        numClientes=[]
        SUMATIESP=0
        PROMEDIOTIESP=[]
        SUMATIESA=[]
        PROMEDIOTIESA=[]

        i = 0
        """
        ALL # ALEATORIO DE LLEGADA DE CLIENTES
        ASE # ALEATORIO DE SERVICIO
        TILL TIEMPO ENTRE LLEGADA
        TISE TIEMPO DE SERVICIO
        TIRLL TIEMPO REAL DE LLEGADA
        TIISE TIEMPO DE INICIO DE SERVICIO
        TIFSE TIEMPO FINAL DE SERVICIO
        TIESP TIEMPO DE ESPERA
        TIESA TIEMPO DE SALIDA
        numClientes NUMERO DE CLIENTES
        dfLE DATAFRAME DE LA LINEA DE ESPERA
        """
        numClientes=data['clientes']
        i = 0
        # indice = ['ALL','ASE','TILL','TISE','TIRLL','TIISE','TIFSE','TIESP','TIESA']
        Clientes = np.arange(numClientes)
        # dfLE = pd.DataFrame(index=Clientes, columns=indice).fillna(0.000)
        # np.random.seed(100)
        for i in Clientes:
            if i == 0:
                ALL.insert(i, round(random.random(),4))
                ASE.insert(i, round(random.random(),4))
                TILL.insert(i, round(-landa*np.log(ALL[i]),4))
                TISE.insert(i, round(-nu*np.log(ASE[i]),4))
                TIRLL.insert(i, round(TILL[i],4))
                TIISE.insert(i, round(TIRLL[i],4))
                TIFSE.insert(i, round(TIISE[i] + TISE[i],4))
                TIESA.insert(i, round(TILL[i] + TISE[i],4))
            else:
                ALL.insert(i, round(random.random(),4))
                ASE.insert(i, round(random.random(),4))
                TILL.insert(i, round(-landa*np.log(ALL[i]),4))   
                TISE.insert(i, round(-nu*np.log(ASE[i]),4))
                TIRLL.insert(i, round(TILL[i] + TIRLL[i-1],4))
                TIISE.insert(i, round(max(TIRLL[i],TIFSE[i-1]),4))
                TIFSE.insert(i, round(TIISE[i] + TISE[i],4))
                TIESP.insert(i, round(TIISE[i] - TIRLL[i],4))
                TIESA.insert(i, round(TILL[i] + TISE[i],4))
                # sumaSistema = 
                suma1 = sum(TIESP)
                suma2 = sum(TIESA)
                promedio1 = sum(TIESP)/(int(numClientes)-1)
                promedio2 = sum(TIESA)/(int(numClientes))



  
        return JsonResponse({'ALL':ALL,'TILL':TILL,'TISE':TISE,'TIRLL':TIRLL,'TIISE':TIISE,'TIFSE':TIFSE,'TIESP':TIESP,'TIESA':TIESA,'numClientes':numClientes,'suma1':suma1,'suma2':suma2,'promedio1':promedio1,'promedio2':promedio2}, safe=False)

class GraficoLS(View):
        def get(self, request, ALL, TILL, TISE, TIRLL, TIISE, TIFSE, TIESP, TIESA):
            ALLconvert = eval(ALL) # Devuelve [1,2,3] (list)
            TILLconvert = eval(TILL) # Devuelve [1,2,3] (list)
            TISEconvert = eval(TISE) # Devuelve [1,2,3] (list)
            TIRLLconvert = eval(TIRLL) # Devuelve [1,2,3] (list)
            TIISEconvert = eval(TIISE) # Devuelve [1,2,3] (list)
            TIFSEconvert = eval(TIFSE) # Devuelve [1,2,3] (list)
            TIESPconvert = eval(TIESP) # Devuelve [1,2,3] (list)
            TIESAconvert = eval(TIESA) # Devuelve [1,2,3] (list)            
      
            # xvalor = eval(x) # Devuelve [1,2,3] (list)
            # m3valor = eval(m3) # Devuelve [1,2,3] (list)
            # m4valor = eval(m4) # Devuelve [1,2,3] (list)

            f = plt.figure()

            # axes = pd.DataFrame(index=5, columns=indice).fillna(0.000)

            axes = f.add_axes([0.15, 0.15, 0.75, 0.75]) # [left, bottom, width, height]
           
                 

            # Creamos una figura y le dibujamos el gráfico

            # Creamos los ejes
            axes.plot(ALLconvert,   linestyle="-", label="ALL")
            axes.plot(TILLconvert,   linestyle="-", label="TILL")
            axes.plot(TISEconvert,   linestyle="-", label="TISE")
            axes.plot(TIRLLconvert,   linestyle="-", label="TIRLL")
            axes.plot(TIISEconvert,   linestyle="-", label="TIISE")
            axes.plot(TIFSEconvert,   linestyle="-", label="TIFSE")
            axes.plot(TIESPconvert,   linestyle="-", label="TIESP")
            axes.plot(TIESAconvert,  linestyle="-", label="TIESA")            
            axes.set_xlabel("Eje X")
            axes.set_ylabel("Eje Y")
            axes.set_title("Gráfico generado")
            axes.legend(loc='upper left')


            # Como enviaremos la imagen en bytes la guardaremos en un buffer
            buf = io.BytesIO()
            canvas = FigureCanvasAgg(f)
            canvas.print_png(buf)

            # Creamos la respuesta enviando los bytes en tipo imagen png
            response = HttpResponse(buf.getvalue(), content_type='image/png')

            # Limpiamos la figura para liberar memoria
            f.clear()

            # Añadimos la cabecera de longitud de fichero para más estabilidad
            response['Content-Length'] = str(len(response.content))

            # Devolvemos la response
            return response
            # return JsonResponse({}, safe=False)







class ModeloInventario(View):    
    def post(self, request):
        data = json.loads(request.body)    
        
        # D = Demanda
        # Co = Costo de ordenar
        # Ch = Costo de Mantenimiento
        # P = Costo del Producto: precio por unidad de articulo
        # Q = Cantidad optima de pedido
        # MO(Q)=Costo Mínimo total
        # N= númeor de pedidos
        # T=tiempo entre pedido
        # ChT= Costo anual de mantener
        # CoT = Costo anual de ordenar
        # MO(Q) = Costo total de Inventario
        D = data['D']
        Co = data['Co']
        Ch = data['Ch']
        P = data['P']
        Tespera = data['Tespera']
        DiasAno = data['DiasAno']

        Q = round(sqrt(((2*Co*D)/Ch)),2)
        N = round(D / Q,2)
        R = round((D / DiasAno) * Tespera,2)
        T = round(DiasAno / N,2)
        CoT = N * Co
        ChT = round(Q / 2 * Ch,2)
        MOQ = round(CoT + ChT,2)
        CTT = round(P * D + MOQ,2)
        Resultado = {
        "q":Q,
        "cot": CoT,
        "cht":ChT,
        "moq":MOQ,
        "ctt": CTT,
        "n":N,
        "r":R,
        "t":T
        }
        indice = ['Q','Costo_ordenar','Costo_Mantenimiento','Costo_total','Diferencia_Costo_Total']
        Q_return = []
        Co_return = []
        Ch_return = []
        MO_return = []
        Diferencia_total_return = []

        periodo = np.arange(1,19)
        def genera_lista(Q):
            n=18
            Q_Lista = []
            i=1
            Qi = Q
            Q_Lista.append(Qi)
            for i in range(1,9):
                Qi = Qi - 60
                Q_Lista.append(Qi)

            Qi = Q
            for i in range(9, n):
                Qi = Qi + 60
                Q_Lista.append(Qi)

            return Q_Lista
        Lista= genera_lista(Q)
        Lista.sort()
        dfQ = DataFrame(index=periodo, columns=indice).fillna(0)
        dfQ['Q'] = Lista
            #dfQ
        for i in periodo:
            Q_return.insert(i, round(dfQ['Q'][i],3))
            Co_return.insert(i, round(D * Co / dfQ['Q'][i],3))
            Ch_return.insert(i, round(dfQ['Q'][i] * Ch / 2,3))            
            MO_return.insert(i, round(Co_return[i-1] + Ch_return[i-1],3))
            Diferencia_total_return.insert(i,round(MO_return[i-1] -MOQ,3) )
            
        return JsonResponse({'Q_return':Q_return, 'Co_return':Co_return, 'Ch_return':Ch_return, 'MO_return': MO_return, 'Diferencia_total_return':Diferencia_total_return, 'Resultado':Resultado}, safe=False)