from .forms import *
from django.views import *
from django.shortcuts import *
from django.contrib.auth import *
from django.utils.decorators import *
from django.views.decorators.csrf import *
from typing import *
from django.contrib import messages
import json
from .models import *
from .forms import *



class RegistrarUsuarioView(View):
    template_name = 'registroUsu.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        form = UserForm()  # Definir form con un valor predeterminado
        if request.method == 'POST':
            print("en el metodod")
            #if request.headers.get('content-type') == 'application/json':
            if 'application/json' in request.headers.get('content-type', ''):
                print("en el json")
                self.handle_flutter_data(request)
            else:
                print("no json")
                form = UserForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Usuario registrado correctamente desde formulario HTML.')
                    return redirect('iniciar_sesion')
                else:
                    messages.error(request, 'Error al registrar el usuario desde formulario HTML.')
        else:
            print("no metodo")
            form = UserForm()
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = UserForm()
        return render(request, self.template_name, {'form': form})

    def handle_flutter_data(self, request):
        try:
            data = json.loads(request.body)
            print("Datos recibidos desde Flutter:")
            print(data)  # Imprime los datos recibidos desde Flutter
            form = UserForm(data)
            if form.is_valid():
                print("Datos válidos:")
                print(form.cleaned_data)  # Imprime los datos validados por el formulario
                form.save()
                messages.success(request, 'Usuario registrado correctamente desde Flutter.')
            else:
                print("Errores en el formulario:")
                print(form.errors)  # Imprime los errores de validación del formulario
        except json.JSONDecodeError:
            messages.error(request, 'Error en los datos enviados desde Flutter.')


10261026
class IniciarSesionView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'iniciosesion.html', {'form':form})
    
    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            datt = authenticate(username = username, password=password)

            if datt is not None:
                login(request, datt)
                if datt.rol == 'Cliente':
                    try:
                        documento = datt.documento_id
                        print("000000000000", documento)

                        cliente =  Cliente.objects.get(documento=documento)

                        if request.method == "POST" and 'editar' in request.POST:
                            print("entrando a clientes")
                            cliente_form = UserForm(request.POST, instance=cliente)
                            if cliente_form.is_valid():
                                cliente_form.save()
                                messages.success(request, 'cambios guardados')
                                return redirect('frmCliente')
                            else:
                                messages.error(request, 'corregir errores')
                        else:
                            cliente_form = UserForm(instance=cliente)
                        return render(request, 'no se encontro el cliente')
                    except Cliente.DoesNotExist:
                        messages.error(request, 'no se encontro el cliente')
                else:
                    return redirect('clientes')
            form.add_error(None, 'intentar nuevamente')
        return render(request, 'iniciosesion.html', {'form':form})
    

def frmCliente(request):
    return render(request, "actcliente.html")
