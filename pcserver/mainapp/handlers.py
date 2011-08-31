from webservice_tools.utils import BaseHandler, AutoListHandler
from webservice_tools.decorators import login_required
from mainapp.models import * #@UnusedWildImport


#Create your handlers here
class TermsHandler(AutoListHandler):
    model = Term
    allowed_methods = ('GET',)
    extra_fields = ('image_url',)
    exclude = ('image', )
    
#    @login_required
    def read(self, request,  response):
        """
        Fetch a list of Terms
        API Handler: GET /terms
        Params:
           None
           
        Returns:
           @terms [Term] list of terms, see Term docs for details
        
        """
        return super(TermsHandler, self).read(request, response)


class TermHandler(BaseHandler):
    model = Term
    allowed_methods = ('GET',)
    extra_fields = ('image_url',)
    exclude = ('image', )
    
#    @login_required
    def read(self, request, id, response):
        """
        Fetch a list of Terms
        API Handler: GET /term/{id}
        Params:
           id [id] id of the term (in the url)
           
        Returns:
           @title [string] title
           @description [string] a short description
           @image_url [url] a url to the corresponding image
        
        """
        return super(TermHandler, self).read(request, id, response)


#ALL DEFINITION EOF
module_name = globals().get('__name__')
handlers = sys.modules[module_name]
handlers._all_ = []
for handler_name in dir():
    m = getattr(handlers, handler_name)
    if type(m) == type(BaseHandler):
        handlers._all_.append(handler_name)
