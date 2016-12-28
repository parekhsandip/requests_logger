import time
from django.core.files import File

try:
    # needed to support Django >= 1.10 MIDDLEWARE
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    # needed to keep Django <= 1.9 MIDDLEWARE_CLASSES
    MiddlewareMixin = object

class RequestHandler(MiddlewareMixin):
    rdataholder = ''
    rdatacounter = 0

    def process_response(self, request, response):
        rmethod = str(request.META.get('REQUEST_METHOD'))
        qstring = str(request.META.get('QUERY_STRING'))
        referer = request.path
        ip = str(request.META.get('REMOTE_ADDR'))
        rtime = time.strftime("%Y-%m-%d %H:%M:%S")
        rdata = ip + ' ' + rmethod + ' ' + rtime + ' ' + referer + ' ' + qstring
        self.rdatacounter+=1
        self.rdataholder += rdata + '\n'
        print(rdata)
        if self.rdatacounter >= 1000:
            with open("weblog.txt", "a") as myfile:
                myfile.write(self.rdataholder)
            self.rdatacounter = 0
            self.rdataholder = ''
        return response