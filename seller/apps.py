from django.apps import AppConfig


class SellerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'seller'
    verbose_name = 'Продавцы'

    def ready(self):
        import seller.signals
