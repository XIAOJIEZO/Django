from django import template

register = template.Library()   #register的名字是固定的,不可改变

# 利用装饰器 @register.filter 自定义过滤器，装饰器参数最多只有两个
@register.filter
def my_filter(v1, v2):
    return v1 * v2

# 利用装饰器 @register.simple_tag 自定义标签。
@register.simple_tag
def my_tag1(v1, v2, v3):
    return v1 * v2 * v3