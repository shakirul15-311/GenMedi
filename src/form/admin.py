from django.contrib import admin

from .models import Doctor
from .models import Perasitamol
from .models import Ketorolac
from .models import Fexofenadine
from .models import Ceftriaxone

admin.site.register(Doctor)
admin.site.register(Perasitamol)
admin.site.register(Ketorolac)
admin.site.register(Fexofenadine)
admin.site.register(Ceftriaxone)