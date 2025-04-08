from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Atributo

@csrf_exempt
def actualizar_atributo(request, nombre):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            valor = data.get("valor")

            atributo, created = Atributo.objects.update_or_create(
                nombre=nombre,
                defaults={"valor": valor}
            )

            return JsonResponse({"mensaje": "Actualizado correctamente."})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Método no permitido."}, status=405)


from django.shortcuts import render
from .models import Atributo

def formulario_atributos(request):
    mensaje = ""
    if request.method == "POST":
        campos = ["nombre", "vida", "balas", "nivel", "velocidad", "poder"]
        for campo in campos:
            valor = request.POST.get(campo)
            if valor:
                Atributo.objects.update_or_create(
                    nombre=campo,
                    defaults={"valor": valor}
                )
        mensaje = "Atributos guardados correctamente."

    atributos = Atributo.objects.all()
    return render(request, "api/formulario.html", {"atributos": atributos, "mensaje": mensaje})
