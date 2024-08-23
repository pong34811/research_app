from django.shortcuts import render, redirect
from .forms import ShopForm
from .models import Shop, Tag

def add_shop(request):
    if request.method == 'POST':
        shop_name = request.POST.get('shop_name')
        tag_ids = request.POST.getlist('tags')
        tags = Tag.objects.filter(id__in=tag_ids)

        shop = Shop.objects.create(name=shop_name)
        shop.tags.set(tags)
        shop.save()

        return redirect('shop_list')  # Assuming you have a shop list view

    tags = Tag.objects.all()  # Get all tags to pass to the template
    return render(request, 'shop/add_shop_modal.html', {'tags': tags})


def shop_list(request):
    shops = Shop.objects.all()
    tags = Tag.objects.all()  # Get all tags to pass to the template
    return render(request, 'shop/shop_list.html', {'shops': shops, 'tags': tags})