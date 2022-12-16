from .models import Category, ProjectSettings

def data_pass(request):
    data={
        'categoryMenuData': Category.objects.all(),
        'settingData': ProjectSettings.objects.last()
    }


    return data