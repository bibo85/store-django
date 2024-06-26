from rest_framework import fields, serializers

from products.models import Basket, Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=ProductCategory.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity', 'image', 'category')


class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    sum = fields.FloatField()
    total_sum = fields.SerializerMethodField()
    total_quantity = fields.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ("id", "product", "quantity", "sum", "total_sum", "total_quantity", "create_timestamp")
        read_only_fields = ("create_timestamp", )

    @staticmethod
    def get_total_sum(obj):
        return Basket.objects.filter(user_id=obj.user).total_sum()

    @staticmethod
    def get_total_quantity(obj):
        return Basket.objects.filter(user_id=obj.user).total_quantity()
