
from django.contrib import admin
from django.urls import path


from . import views
from .views import profile_view, login, login1, signup, signup1, feedback_view, adminlogin, adminfeedback_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('SignUp/', views.SignUp),
    path('mainpage/', views.mainpage),
    path('', views.homepage),
   #  path('signup/', views.signup_view, name='signup'),
   # path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('login1/',views.login1,name='login1'),
    path('/forgot_password1', views.forgot_password1, name='forgot_password1'),
     path('profile/', profile_view, name='profile'),
     # Main page URL
    path('profile/', views.profile, name='profile'),  # Profile page URL

    path('programming-books/', views.programming_books, name='programming_books'),
    path('programming-books/', views.programming_books, name='programming_books'),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('knowledge-books/', views.knowledge_books, name='knowledge_books'),
    path('knowledge-books/', views.knowledge_books, name='knowledge_books'),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('profile/', views.profile, name='profile'),
    path('profile/', views.profile, name='profile'),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('finance-books/', views.finance_books, name='finance_books'),
    path('finance-books/', views.finance_books, name='finance_books'),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('encyclopedia-books/', views.encyclopedia_books, name='encyclopedia_books'),
    path('encyclopedia-books/', views.encyclopedia_books, name='encyclopedia_books'),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('contact', views.contact_us, name='contact_us'),
    path('contact/', views.contact_us, name='contact_us'),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('loginpage/', login, name='login'),
    path('login1/', login1, name='login1'),
    path('adminlogin/',adminlogin, name='adminlogin'),
    path('signup/', signup, name='signup'),
    path('signup1/', signup1, name='signup1'),
    path('add_books/', views.add_books, name='add_books'),
    path('added_books/', views.added_books, name='added_books'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('feedback/', feedback_view, name='feedback'),
    path('adminhomepage/', views.adminhomepage, name='adminhomepage'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('about_us/', views.about_us, name='about_us'),
    path('explore/', views.explore, name='explore'),
    path('adminfeedback/', adminfeedback_view, name='adminfeedback'),
    path('insert/', views.insert_emp, name='insert-emp'),
    path('show/', views.show_emp, name='show-emp'),
    path('edit/<int:pk>', views.edit_emp, name='edit-emp'),
    path('remove/<int:pk>', views.remove_emp, name='remove-emp'),
    path('book', views.book_list, name='book_list'),  # URL for displaying the list of books
    path('add/', views.add_book, name='add_book'),  # URL for adding a new book
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),  # URL for editing a book
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),  # URL for deleting a book
    path('book/', views.book_list, name='book_list'),




]