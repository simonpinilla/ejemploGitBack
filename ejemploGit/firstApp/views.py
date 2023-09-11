from django.shortcuts import render
from django.http import HttpResponse


def vista1(request):
    html = """
    <style>
        /* Estilo del banner */
        .banner {
            background-color: #0074E4;
            color: white;
            text-align: center;
            padding: 20px;
        }

        /* Estilo de la fuente */
        .fuente-especial {
            font-family: 'Courier New', Courier, monospace;
            font-size: 24px;
        }
    </style>
    <div class="banner">
        <h1 class="fuente-especial">
            Bienvenido a la app2!
        </h1>
    </div>
    """
    return HttpResponse(html)
