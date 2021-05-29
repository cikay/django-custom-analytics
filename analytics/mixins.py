from .signals import object_viewed_signal


class ObjectViewMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(ObjectViewMixin, self).get_context_data(
            *args, **kwargs)
        instance = context.get('object')
        request = self.request

        if instance:
            object_viewed_signal.send(
                instance.__class__, instance=instance, request=request)
        return context
