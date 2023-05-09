from django.test import TestCase
from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
         category = Category.objects.create(name='Category')
         author = User.objects.create_user(
            first_name = 'user',
            last_name = 'name',
            username = 'Username',
            password = '123456',
            email = 'username@gmsil.com',
        )
         recipe = Recipe.objects.create(
            category = category,
            author = author,
            title = 'Recipe Title',
            description = 'recipe Description',
            slug = 'recipe-slug',
            preparation_time = 10,
            preparation_time_unit = 'Minutos',
            servings = 10,
            servings_unit = 'Porções',
            preparation_steps = 'Recipe Preparation Steps',
            preparation_steps_is_html =False ,
            is_published =True,
        )
         return super().setUp()