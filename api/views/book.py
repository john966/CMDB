from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from api import models
from api.utils.response import BaseResponse
import uuid
from api.serializers.book import BookSerializer
from api.utils.serialization_general import SerializedData
from api.utils.auth import Authentication
from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book  # user表
        fields = '__all__'  # 所有字段


class BookView(ViewSetMixin, APIView):
    authentication_classes = [Authentication]  # 开启认证

    def list(self, request, *args, **kwargs):
        """
        书籍列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        queryset = models.Book.objects.all()
        serializer_class = BookSerializer
        data = SerializedData(request, queryset, serializer_class).get_data()
        return Response(data)

    def edit(self, request,pk, *args, **kwargs):
        """
        书籍编辑/修改
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        res = BaseResponse()
        # 去提交的数据
        # comment_data = self.request.data
        # print(comment_data)
        # 对用户提交的数据做校验
        # ser_obj = BookSerializer(data=comment_data)

        # if ser_obj.is_valid():
            # 表示数据没问题,可以创建
            # ser_obj.save()]
        # BookFormSet = forms.formset_factory(BookForm, extra=0)
        # formset = BookForm(request.POST)
        obj = models.Book.objects.filter(id=pk).first()
        form = BookForm(data=request.POST, instance=obj)
        print(request.POST)
        print(obj.__dict__)

        if form.is_valid():  # 判断数据
            # queryset = form.cleaned_data
            #
            # serializer_class = BookSerializer
            # data = SerializedData(request, queryset, serializer_class).get_data()
            # res = models.Book.objects.filter(id=pk).update(**queryset)
            # print(data,type(data))
            form.save()
            # print(formset.cleaned_data,type(formset.cleaned_data))

            # flag = False  # 标志位

            # for row,v in formset.cleaned_data.items():
            #     print(row,type(row))
            #     print(v,type(v))
                # pop() 方法删除字典给定键 key 及对应的值，返回值为被删除的值
                # id = row.pop('id')  # 获取id

                # if id:  # 判断数据不为空
                    # print(row)  # 它是一个字典
                    # **表示将字典扩展为关键字参数

                    # if res:  # 判断返回信息
                    #     flag = True



            # if flag:
            #     # print('修改成功')
            #     # return HttpResponse('修改成功')
            #     res.code = '1000'
            # else:
            #     # print('修改失败')
            #     # return HttpResponse('修改失败')
            #     res.code = '500'
            #     res.error = '修改失败'

        else:
            print(forms.errors)

        return Response(res.__dict__)






        # ser_obj = models.Book.objects.filter(id=pk).update(**request.POST)

            # print(ser_obj)
        # else:
        #     # 表示数据有问题
        #     res.code = 1
        #     res.error = ser_obj.errors
        #
        # print(ser_obj.errors)
        # print(ser_obj.errors.__dict__)

        # return Response(res)


    def add(self,request,*args,**kwargs):
        # res = {"code":0}
        res = BaseResponse()
        #去提交的数据
        comment_data = self.request.data
        print(comment_data)
        #对用户提交的数据做校验
        ser_obj = BookSerializer(data=comment_data)

        if ser_obj.is_valid():
            #表示数据没问题,可以创建
            ser_obj.save()
            print(ser_obj)
        else:
            #表示数据有问题
            res.code = 1
            res.error = ser_obj.errors

        return Response(res.__dict__)

    def delete(self,request,pk,*args,**kwargs):
        """
        删除书籍列表
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        res = BaseResponse()
        ret = models.Book.objects.filter(id=pk).delete()
        # ..............
        obj = models.Book.objects.filter(id=pk).first()
        obj.authors.clear()  #第二种方式联级清除多对多的关系

        if not ret[0]:
            res.code = 500

        return Response(res.__dict__)


