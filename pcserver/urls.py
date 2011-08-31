from django.conf.urls.defaults import * #@UnusedWildImport
from django.conf import settings
from webservice_tools.utils import Resource
from django.contrib import admin
from mainapp.handlers import * #@UnusedWildImport
from webservice_tools.views import handler404_view
from webservice_tools.views import DocHandler
handler404 = handler404_view
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

basepatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^terms/?$', Resource(PhotosHandler)),
    (r'^term/(?P<id>[\d]+)/?$', Resource(PhotoHandler)),    
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^$', Resource(DocHandler)),
)

urlpatterns = patterns('',
    (r'^pcserver/', include(basepatterns)),
    (r'', include(basepatterns)),

)
