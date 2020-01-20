from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMiddleWare(MiddlewareMixin):

    def process_request(self,request):
        # 在调用主路由之前调用
        print('-----start  process_request-----')

    def process_view(self,request,callback,callback_args,callback_kwargs):
        # 请求通过路由后，在即将进入视图层时调用
        print('-----satrt process_view------')

    def process_response(self,request,response):
        # 响应即将传至浏览器之前调用
        print('-----start process_response-----')
        return response  #返回值必须是个response

class MyMiddleWare2(MiddlewareMixin):

    def process_request(self,request):
        # 在调用主路由之前调用
        print('-----start  process_request2-----')

    def process_view(self,request,callback,callback_args,callback_kwargs):
        # 请求通过路由后，在即将进入视图层时调用
        print('-----satrt process_view2------')

    def process_response(self,request,response):
        # 响应即将传至浏览器之前调用
        print('-----start process_response2-----')
        return response  #返回值必须是个response


class VisitLimitMW(MiddlewareMixin):
    count_dict ={}
    def process_request(self,request):
        ip_addr = request.META['REMOTE_ADDR']
        if request.path_info != '/test':
            return None
        count = self.count_dict.get(ip_addr,0)
        count += 1
        self.count_dict[ip_addr] = count
        if count > 5:
            return HttpResponse('wooo```')