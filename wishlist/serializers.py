from rest_framework import serializers
from wishlist.models import Wishlist

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = (
            'id',
            'name',
            'created_at',
            'user',
            'products'
        )
        depth = 1
