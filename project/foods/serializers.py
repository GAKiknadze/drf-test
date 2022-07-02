from rest_framework import serializers


from .models import FoodCategory, Food


class FilteredFoodListSerializer(serializers.ListSerializer):
    
    def to_representation(self, data):
        data = data.filter(is_publish=True)
        return super(FilteredFoodListSerializer, self).to_representation(data)


class FoodSerializer(serializers.ModelSerializer):
    additional = serializers.SlugRelatedField(many=True, read_only=True, slug_field='internal_code')

    class Meta:
        list_serializer_class = FilteredFoodListSerializer
        model = Food
        fields = ('internal_code', 'code', 'name_ru', 'description_ru', 'description_en',
                  'description_ch', 'is_vegan', 'is_special', 'cost', 'additional')


class FoodListSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(source='food', many=True, read_only=True)
    
    class Meta:
        model = FoodCategory
        fields = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id', 'foods')