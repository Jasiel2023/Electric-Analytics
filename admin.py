from django.contrib import admin
from .models import Usuario
from .models import Informe
from .models import MedidorDeConsumo
from .models import Registro
from .models import registroDispositivos


# Register your models here.
admin.site.register(Usuario)
admin.site.register(Informe)
admin.site.register(MedidorDeConsumo)
admin.site.register(Registro)
admin.site.register(registroDispositivos)

