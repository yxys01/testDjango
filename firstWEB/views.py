from django.shortcuts import render
from firstWEB.models import cal
from django.http import HttpResponse
# Create your views here.

# 渲染index.html页面，返回到前端浏览器
# 在urls.py中调用
def index(request):
    # render 渲染
    return render(request, 'index.html')


def CalPage(request):
    return render(request,'cal.html')
# post回来的数据都在request中
# 注意异常处理；如果不是post请求将无法访问
def Cal(request):
    # if request.method == 'POST':
    # 第二种
    if request.POST:
        value_a = request.POST['valueA']
        value_b = request.POST['valueB']
        result = int(value_a) + int(value_b)
        cal.objects.create(value_a=value_a,
                           value_b=value_b,
                           result=result)


        # 把得到的结果渲染给result模板
        # 给模板赋值,context=键值对
        return render(request, 'result.html', context={'data': result})
    else:
        return HttpResponse('please visit us with POST')

def CalList(request):
    # 读取cal表全部数据
    data = cal.objects.all()
    # for data in datas:
    #     print(data.value_a,data.value_b,data.result)
    return render(request, 'list.html', context={'data': data})

def DelData(request):
    # 删除所有数据
    cal.objects.all().delete()
    # 返回一个HttpResponse字符串
    return HttpResponse('data delete')