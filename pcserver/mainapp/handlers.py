from webservice_tools.utils import BaseHandler, AutoListHandler
from webservice_tools.decorators import login_required
from mainapp.models import * #@UnusedWildImport


#Create your handlers here
class PhotosHandler(AutoListHandler):
    model = Photo
    allowed_methods = ('GET',)
    extra_fields = ('image_url',)
    exclude = ('image', )
    
    @login_required
    def read(self, request,  response):
        """
        Fetch a photo by id.
        API Handler: GET /photos
        Params:
           @key [string] your api key
           
        Returns:
           @photos [Photo] list of photos, see Photo docs for details
        
        """
        return super(PhotosHandler, self).read(request, response)


class PhotoHandler(BaseHandler):
    model = Photo
    allowed_methods = ('GET',)
    extra_fields = ('image_url',)
    exclude = ('image', )
    
    @login_required
    def read(self, request, id, response):
        """
        Fetch a list of Photos
        API Handler: GET /photo/{id}
        Params:
           @id [id] id of the photo (in the url)
           @key [string] your api key 
        Returns:
           @title [string] title
           @description [string] a short description
           @image_url [url] a url to the corresponding image
        
        """
        return super(PhotoHandler, self).read(request, id, response)


#ALL DEFINITION EOF
module_name = globals().get('__name__')
handlers = sys.modules[module_name]
handlers._all_ = []
for handler_name in dir():
    m = getattr(handlers, handler_name)
    if type(m) == type(BaseHandler):
        handlers._all_.append(handler_name)
