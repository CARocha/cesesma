from eventos.models import Eventos
from noticias.models import Noticias
from django.contrib.flatpages.models import FlatPage

def globales(request):
	evento = Eventos.objects.order_by('-id')[:3]
	noticia = Noticias.objects.order_by('-id')[:4]
	menu_flat = FlatPage.objects.exclude(id__in=[1,2,3])

	return {'eventos':evento, 'noticias':noticia, 'menu_flat':menu_flat}