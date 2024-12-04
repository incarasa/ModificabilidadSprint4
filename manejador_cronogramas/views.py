from django.shortcuts import render
from django.http import JsonResponse
from .models import Cronograma
from .models import Estudiante
from .models import Pago

def cronogramas_con_pagos(request):
     # Obtener todos los cronogramas junto con estudiantes y pagos
    cronogramas = Cronograma.objects.prefetch_related('estudiantes', 'pago_set').all()

    data = [
        {
            "id": cronograma.id,
            "nombre": cronograma.nombre,
            "pagos": [
                {
                    "id": pago.id,
                    "mes": pago.mes,
                    "meses": pago.meses,
                    "valor": pago.valor,
                    "fecha_evento": pago.fecha_evento.strftime('%Y-%m-%d') if pago.fecha_evento else None,
                    "intereses": pago.intereses,
                }
                for pago in cronograma.pago_set.all()
            ]
        }
        for cronograma in cronogramas
    ]

    return JsonResponse(data, safe=False)


def estudiantes_con_cronogramas(request):
    # Usa prefetch_related para relaciones ManyToMany
    estudiantes = Estudiante.objects.prefetch_related('cronogramas').all()

    data = [
        {
            "id": estudiante.id,
            "nombre": estudiante.nombre,
            "documento": estudiante.documento,
            "curso": estudiante.curso,
            "edad": estudiante.edad,
            "cronogramas": [
                {
                    "id": cronograma.id,
                    "nombre": cronograma.nombre,
                }
                for cronograma in estudiante.cronogramas.all()  # Cambiado de cronograma a cronogramas
            ]
        }
        for estudiante in estudiantes
    ]

    return JsonResponse(data, safe=False)
