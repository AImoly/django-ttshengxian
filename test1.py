from django.shortcuts import render
from django.conf import settings
def provice_area(request, num):
    if num == "":
        num = 1
    # 查询出所有省级地区的信息
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    # 对显示出来的信息进行分类
    # area1 = Paginator(areas,10) 后面跟上的参数是要分页的数据的对象和每页显示几条数据
    areas_pag = Paginator(areas, 10)
    # 打印分页之后的总页数
    print(areas_pag.num_pages)
    # 打印页码的列表
    print(areas_pag.page_range)
    # 提取出第num页的内容对象
    # areas_pag.page() 跳转到第几页,获取他的对象
    areas = areas_pag.page(num)
    print(type(num))
    # 打印当前页的页码
    print(areas.number)
    # 所有数据的总数目
    print(areas_pag.count)
    # areas的paginator属性就是上面的areas_pag对象
    # 返回当前页的查询集
    # areas.object_list
    print(areas.paginator)
    # 判断当前页是否有上一页,返回的是布尔值
    # areas.has_previous()
    # 判断当前页是否有下一页,返回的是布尔值
    # areas.has_next()
    # 返回的是当前页的上一页的页码
    # areas.previous_page_number()
    # 返回的是当前页的下一页的页码
    # areas.next_page_number()
    return render(request, "area/provice_area.html", {"areas": areas})

def aimi():
    print("我是真的爱你！")