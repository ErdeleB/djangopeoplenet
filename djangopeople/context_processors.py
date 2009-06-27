from django.conf import settings

def context(request):

    data = {'TEMPLATE_DEBUG': settings.TEMPLATE_DEBUG,
            'DEBUG': settings.DEBUG,
            #'OFFLINE': settings.OFFLINE,
            'base_template': "base.html",
            'mobile_version': False,
            'mobile_user_agent': False,
            'PROJECT_NAME': u"Kung Fu People",
            'PROJECT_MARTIAL_ART': u"Kung Fu",
            }

    return data

