from django.contrib import admin
from .models import Obat
from .models import Pembayaran
from .models import Pasien
from .models import Polklinik
from .models import Dokter
from .models import Pendfataran
from .models import Resep
from .models import Detail




admin.site.register(Obat)
admin.site.register(Pembayaran)
admin.site.register(Pasien)
admin.site.register(Polklinik)
admin.site.register(Dokter)
admin.site.register(Pendfataran)
admin.site.register(Resep)
admin.site.register(Detail)
