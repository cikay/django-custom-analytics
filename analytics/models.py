from django.db import models
from User.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .manager import ViewedObjectManager
from .signals import object_viewed_signal


class ObjectViewed(models.Model):

    PC = 'pc'
    MOBILE = 'mobile'
    TABLET = 'tablet'
    BOT = 'bot'
    UNKNOWN = 'unknown'
    DEVICE_TYPE = (
        (PC, 'PC'),
        (MOBILE, 'Mobile'),
        (TABLET, 'Tablet'),
        (BOT, 'Bot'),
        (UNKNOWN, 'Unknown'),
    )

    user = models.ForeignKey(User, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    ip_address = models.CharField(max_length=120, blank=True, null=True)
    content_object = GenericForeignKey("content_type", "object_id")
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_country = models.TextField()
    ip_region = models.CharField(max_length=255, null=True, blank=True)
    ip_city = models.CharField(max_length=255, blank=True, null=True)
    referrer = models.URLField(null=True, blank=True)
    device_type = models.CharField(
        max_length=200, choices=DEVICE_TYPE, default=UNKNOWN)
    device = models.CharField(max_length=30, null=True, blank=True)
    browser = models.CharField(max_length=30, null=True, blank=True)
    browser_version = models.CharField(max_length=30, null=True, blank=True)
    system = models.CharField(max_length=30, null=True, blank=True)
    system_version = models.CharField(max_length=30, null=True, blank=True)

    objects = ViewedObjectManager()

    def __str__(self):
        return f'{self.user} viewed {self.content_object} at {self.timestamp}'


def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    content_object = ContentType.objects.get_for_model(sender)
    ip_address = None
    # try:
    #     ip_address = get_client_ip(request)
    # except:
    #     pass
    print("sender", sender)
    print("request", request)
    print("instance", instance)
    device_type = ObjectViewed.UNKNOWN
    if request.user_agent.is_mobile:
        device_type = ObjectViewed.MOBILE
    elif request.user_agent.is_tablet:
        device_type = ObjectViewed.TABLET
    elif request.user_agent.is_pc:
        device_type = ObjectViewed.PC
    elif request.user_agent.is_bot:
        device_type = ObjectViewed.BOT

    new_view_instance = ObjectViewed.objects.create(
        user=request.user,
        content_object=content_object,
        # ip_address=ip_address,
        # ip_country=city.get('country_code', '') or '',
        # ip_region=city.get('region', '') or '',
        # ip_city=city.get('city', '') or '',
        object_id=instance.id,
        referrer=request.META.get('HTTP_REFERER', ''),
        device_type=device_type,
        device=request.user_agent.device.family,
        browser=request.user_agent.browser.family[:30],
        browser_version=request.user_agent.browser.version_string,
        system=request.user_agent.os.family,
        system_version=request.user_agent.os.version_string,
    )


object_viewed_signal.connect(object_viewed_receiver)
