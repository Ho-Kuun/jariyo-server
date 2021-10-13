from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views import View
from django.core.paginator import Paginator

class ShopView(View):
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk) # 로그인중인 사용자 객체를 얻어옴

            # 조회
        if user.profile.ismanager:
            shop_list = user.shop_set.all() # 나의 가게만

            # 페이징처리
            page = request.GET.get('page') # 페이지 번호 알아오기
            if page is None:
                    page = 1
            else:
                    page = int(page)
            paginator = Paginator(shop_list, 1)  # 페이지당 1개씩 보여주기
            page_obj = paginator.get_page(page)
            context = {'shop_list': page_obj}

        return render(request, 'smanager/list.html', context)