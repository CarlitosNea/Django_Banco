from .forms import UserForm
from django.views import *
from django.shortcuts import *


class RegistrarUsuarioView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'registroUsu.html', {'form': form})
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iniciar_sesion')
        return render(request, 'iniciar_sesion.html', {'form':form})