from django.shortcuts import render

# Create your views here.

def index (request):
    datas={

    }
    return render (request,"index.html", datas)

def About (request):
    datas={

    }
    return render (request,"about.html", datas)

def Blog (request):
    datas={

    }
    return render (request,"blog.html", datas)

def Contact (request):
    datas={

    }
    return render (request,"contact.html", datas)    

def Rooms (request):
    datas={

    }
    return render (request,"rooms.html", datas)


def elements (request):
    datas={

    }
    return render (request,"elements.html", datas) 

def Services (request):
    datas={

    }
    return render (request,"services.html", datas)    


def Single_blog (request):
    datas={

    }
    return render (request,"single-blog.html", datas)    

def main (request):
    datas={

    }
    return render (request,"main.html", datas) 

