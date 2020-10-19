from django.http import HttpResponse
from django.template import Template,Context

def paginainicio(request):
    nombre="uwu"
    apellido="owo"
    pagina=open("C:/dwy/miapp/app1/app1/html/inicio.html")
    plt=Template(pagina.read())
    pagina.close()
    ctx=Context({"var_nombre":nombre, "var_apellido":apellido})
    retorno=plt.render(ctx)
    return(HttpResponse(retorno))

def paginaarmar(request):
    nombre="uwu"
    apellido="owo"
    pagina=open("C:/dwy/miapp/app1/app1/html/armar.html")
    plt=Template(pagina.read())
    pagina.close()
    ctx=Context({"var_nombre":nombre, "var_apellido":apellido})
    retorno=plt.render(ctx)
    return(HttpResponse(retorno))

def paginacomprar(request):
    nombre="uwu"
    apellido="owo"
    pagina=open("C:/dwy/miapp/app1/app1/html/comprar.html")
    plt=Template(pagina.read())
    pagina.close()
    ctx=Context({"var_nombre":nombre, "var_apellido":apellido})
    retorno=plt.render(ctx)
    return(HttpResponse(retorno))

def paginadespacho(request):
    nombre="uwu"
    apellido="owo"
    pagina=open("C:/dwy/miapp/app1/app1/html/despacho.html")
    plt=Template(pagina.read())
    pagina.close()
    ctx=Context({"var_nombre":nombre, "var_apellido":apellido})
    retorno=plt.render(ctx)
    return(HttpResponse(retorno))

def paginafinalizar(request):
    nombre="uwu"
    apellido="owo"
    pagina=open("C:/dwy/miapp/app1/app1/html/finalizar.html")
    plt=Template(pagina.read())
    pagina.close()
    ctx=Context({"var_nombre":nombre, "var_apellido":apellido})
    retorno=plt.render(ctx)
    return(HttpResponse(retorno))