from django.http import HttpResponse
from app01.models import Test

# 添加数据
# def testdb(request):
#     test1 = Test(name='掰脚失聪')
#     test1.save()
#     return HttpResponse("<p>数据添加成功！</p>")

# 查询数据
# def testdb(request):
#     # 初始化
#     response = ""
#     response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    # list = Test.objects.all()

    # 过滤，where
    # response2 = Test.objects.filter(id=3)

    # 获取单个对象
    # response3 = Test.objects.get(id=3)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    # Test.objects.order_by('name')[0:2]

    # 数据排序
    # Test.objects.order_by("id")

    # 组合使用
    # list = Test.objects.all().order_by('id')
    #
    # for var in list:
    #     response1 += var.name + " "
    # response = response1
    # return HttpResponse("<p>" + response + "</p>")

    # where过滤可能会有多个对象，需要循环取出值
    # for i in response2:
    #     response1 = i.name
    # return HttpResponse("<p>" + response1 + "</p>")

    # return HttpResponse("<p>" + response3.name + "</p>")

# 更新数据，可以使用 save() 或 update()
# def testdb(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    # test1 = Test.objects.get(id=1)
    # test1.name = "骚娃遥望班长泪目"
    # test1.save()

    # update更新
    # Test.objects.filter(id=2).update(name = "骚娃遥望103落泪")

    # 修改所有列
    # Test.objects.all().update(name="骚猪还装柜不嘛")
    #
    # return HttpResponse("<p> 修改成功 </p>")


# 删除数据：删除数据库中的对象只需调用该对象的delete()方法即可
def testdb(request):
    test1 = Test.objects.get(id=3)
    test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")