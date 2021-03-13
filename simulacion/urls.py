from django.urls import path
from .views import *

urlpatterns = [
    path('cuadrado-medio/', CuadradoMedio.as_view(), name='cuadrado-medio' ),
    path('congruencial-lineal/', CongruencialLineal.as_view(), name='congruencial-lineal' ),
    path('congruencial-multiplicativo/', CongruencialMultiplicativo.as_view(), name='congruencial-multiplicativo' ),
    path('promedio-movil/', PromedioMovil.as_view(), name='promedio-movil' ),
    path('alisamiento-exponencial/', AlisamientoExponencial.as_view(), name='alisamiento-exponencial' ),
    path('regresion-lineal/', RegresionLineal.as_view(), name='regresion-lineal' ),
    path('regresion-no-lineal/', RegresionNoLineal.as_view(), name='regresion-no-lineal' ),
    path('montecarlo/', Montecarlo.as_view(), name='montecarlo' ),
    path('inversa-aditivo/', TransformadaInversaAditivo.as_view(), name='inversa-aditivo' ),
    path('inversa-multiplicativo/', TransformadaInversaMultiplicativo.as_view(), name='inversa-multiplicativo' ),
    path('linea-espera/', LineaEspera.as_view(), name='linea-espera' ),
    path('modelo-inventario/', ModeloInventario.as_view(), name='modelo-inventario' ),
    # path('grafico/', Grafico.as_view() ),
    # path('graficopm/', GraficoPM.as_view() ),
    path('grafico/<valores>/', Grafico.as_view() ),
    path('graficopm/<x>/<m3>/<m4>/', GraficoPM.as_view() ),
    path('graficols/<ALL>/<TILL>/<TISE>/<TIRLL>/<TIISE>/<TIFSE>/<TIESP>/<TIESA>/', GraficoLS.as_view() ),
    # path('graficolineal/', GraficoLineal.as_view() ),

    

    



    

    
]