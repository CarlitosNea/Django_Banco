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
from django.contrib.auth.decorators import * 
from .formsCliente import *



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
                    print("form valid")
                    if form.cleaned_data['imagen'] or form.cleaned_data['imagen'] is None:
                        print("is none")
                        form.save()
                        imagen_file = request.FILES['imagen']

                        user_instance = form.save(commit=False)
                        user_instance.imagen = imagen_file
                        user_instance.save()

                        messages.success(request, 'registrado desde html')
                        return redirect("iniciar_sesion")
                else:
                    print("EERRR")
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
                    return redirect('insertarf')
                else:
                    form.add_error(None, 'Credenciales inválidas. Por favor, intenta nuevamente.')


@method_decorator(login_required(login_url='iniciar_sesion'), name='dispatch')
class PerfilClienteView(View):
    template_name = 'actCliente.html'

    def get(self, request):
        try:
            cliente = Cliente.objects.get(documento=request.user.documento_id)
            usuario = request.user
            print(usuario.imagen)
        except Cliente.DoesNotExist:
            messages.error(request, 'No se encontraron los datos del cliente.')
            return redirect('iniciar_sesion')

        form = ClienteForm(instance=cliente)
        return render(request, self.template_name, {'form': form, 'cliente': cliente, 'usuario':usuario})

    def post(self, request):
        try:
            cliente = Cliente.objects.get(documento=request.user.documento_id)
        except Cliente.DoesNotExist:
            messages.error(request, 'No se encontraron los datos del cliente.')
            return redirect('iniciar_sesion')

        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()

            messages.success(request, 'Cambios guardados correctamente.')
            return redirect('clientes')

        return render(request, self.template_name, {'form': form, 'cliente': cliente})


def frmCliente(request):
    return render(request, "actcliente.html")


