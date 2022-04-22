from basket.models import Basket


def basket(request):
    basket_list = []
    if request.user.is_authenticated:
        basket_list= Basket.objects.filter(user=request.user)

    return {'baskets':basket_list}