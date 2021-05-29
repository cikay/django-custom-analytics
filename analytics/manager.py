

from django.db import models
from User.models import User
from django.contrib.gis.geoip2 import GeoIP2, GeoIP2Exception


class ViewedObjectManager(models.Model):

    def create_from_request(self, request, content_object):

        user = request.user
        user = user if isinstance(user, User) else None

        if request.user_agent.is_mobile:
            device_type = self.model.MOBILE
        elif request.user_agent.is_tablet:
            device_type = self.model.TABLET
        elif request.user_agent.is_pc:
            device_type = self.model.PC
        elif request.user_agent.is_bot:
            device_type = self.model.BOT
        else:
            device_type = self.model.UNKNOWN

        city = {}
        ip_address = None
        print("META", request.META)
        viewedObject = self.model.objects.create(
            content_object=content_object,
            ip_address=ip_address,
            # ip_country=city.get('country_code', '') or '',
            # ip_region=city.get('region', '') or '',
            # ip_city=city.get('city', '') or '',
            referrer=request.META.get('HTTP_REFERER', ''),
            device_type=device_type,
            device=request.user_agent.device.family,
            browser=request.user_agent.browser.family[:30],
            browser_version=request.user_agent.browser.version_string,
            system=request.user_agent.os.family,
            system_version=request.user_agent.os.version_string,
            user=user
        )

        return viewedObject
