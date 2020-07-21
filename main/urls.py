from django.urls import path


from main import views

urlpatterns = [
    path('article/<int:pk>',views.article,name='get_article'),
    path('author/<int:pk>',views.author,name='get_author'),
    path('article',views.create_article,name='create_article'),

    path('',views.index,name='index'),
    

]