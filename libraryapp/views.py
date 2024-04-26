import books as books
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from requests import auth
from django.contrib.auth.models import User

# Create your views here.



def login(request):
    return render(request, 'loginpage.html')

def SignUp(request):
    return render(request, 'SignUp.html')


def homepage(request):
    return render(request, 'home.html')


def mainpage(request):
    return render(request, 'mainpage.html')

# accounts/views.py

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

'''def signup_view(request):
    if request.method == 'POST':
        # Handle signup form submission here
        # This is where you would process the form data, create a new user, etc.
        # Once signup is successful, you can redirect to the homepage
        return redirect('/login')  # Redirect to the homepage URL
    else:
        # Render the signup form template
        # Render the signup form template
        return render(request, 'signup.html')  # Assuming your signup form template is named signup.html'''
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['username']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'home.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'loginpage.html')
    else:
        return render(request, 'loginpage.html')



from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm

def forgot_password1(request):
    return request(render,'forgot_password.html')


def forgot_password1(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password reset email has been sent.')
            return redirect('/login')  # Redirect to login page after sending reset email
    else:
        form = PasswordResetForm()
    return render(request, 'forgot_password.html', {'form': form})


def main_page(request):
    username = request.session.get('username')
    if username:
        return render(request, 'mainpage.html', {'username': username})
    else:
        messages.error(request, 'You are not logged in.')
        return redirect('/login/')

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import User

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # You may need additional form validation here
        user = User.objects.create(email=email, password=make_password(password))
        request.session['username'] = user.email  # Store username in session
        messages.success(request, 'Registration successful. You are now logged in.')
        return redirect('/mainpage/')
    return render(request, 'SignUp.html')


from django.shortcuts import render


from django.shortcuts import render

def profile_view(request):
    # Your view logic goes here
    return render(request, 'profile.html')


def profile(request):
    return render(request, 'profile.html')
from django.shortcuts import render



def programming_books(request):

    # Here you can fetch programming books data from your database or any other source
    # For now, let's just render the programming books page
    return render(request, 'Programming_books.html')
def programming_books(request):
    return render(request, 'Programming_books.html')
from django.shortcuts import render

def mainpage(request):
    return render(request, 'mainpage.html')
def knowledge_books(request):

    # Here you can fetch programming books data from your database or any other source
    # For now, let's just render the programming books page
    return render(request, 'Knowledge_books.html')
def knowledge_books(request):
    return render(request, 'Knowledge_books.html')
from django.shortcuts import render

def mainpage(request):
    return render(request, 'mainpage.html')
def profile(request):
    return render(request, 'profile.html')
def mainpage(request):
    return render(request, 'mainpage.html')

def finance_books(request):

    # Here you can fetch programming books data from your database or any other source
    # For now, let's just render the programming books page
    return render(request, 'Finance_books.html')
def finance_books(request):
    return render(request, 'Finance_books.html')
from django.shortcuts import render

def mainpage(request):
    return render(request, 'mainpage.html')
def encyclopedia_books(request):

    # Here you can fetch programming books data from your database or any other source
    # For now, let's just render the programming books page
    return render(request, 'Encyclopedia_books.html')
def encyclopedia_books(request):
    return render(request, 'Encyclopedia.html')
from django.shortcuts import render

def mainpage(request):
    return render(request, 'mainpage.html')

from django.shortcuts import render

from django.shortcuts import render

def contact_us(request):
    # Your view logic here
    return render(request, 'contact_us.html')
def mainpage(request):
    return render(request, 'mainpage.html')
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    return redirect('home')
from django.shortcuts import render
from django.shortcuts import render

def main_page(request):
    # Assuming you have a variable called 'username' containing the username of the logged-in user
    username = request.user.username
    return render(request, 'main_page.html', {'username': username})
def login(request):
    return render(request, 'loginpage.html')


def signup(request):
    return render(request, 'SignUp.html')

def adminhomepage(request):
    return render(request, 'adminhomepage.html')


from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render

from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']

        # Authenticate the user
        user = auth.authenticate(username=username, password=pass1)

        if user is not None:
            # Log in the user
            auth.login(request, user)
            if len(username) == 10:
                return redirect('mainpage')
            elif len(username) == 4:
                return redirect('adminhomepage')
            else:
                return redirect('home')
            # return render(request, 'mainpage.html')
        else:
            # Authentication failed
            messages.info(request, 'Invalid credentials')
            return render(request, 'loginpage.html')
    else:
        return render(request, 'loginpage.html')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']

        # Authenticate the user
        user = auth.authenticate(username=username, password=pass1)

        if user is not None:
            # Log in the user
            auth.login(request, user)
            if len(username) == 10:
                return redirect('mainpage')
            elif len(username) == 4:
                return redirect('adminhomepage')
            else:
                return redirect('home')
            # return render(request, 'mainpage.html')
        else:
            # Authentication failed
            messages.info(request, 'Invalid credentials')
            return render(request, 'admin_login.html')
    else:
        return render(request, 'admin_login.html')


from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import render


def signup1(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            # Get the User model dynamically
            User = get_user_model()

            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken')
                return render(request, 'SignUp.html')
            else:
                # Create the user
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully!')
                return render(request, 'loginpage.html')
        else:
            messages.info(request, 'Passwords do not match')
            return render(request, 'SignUp.html')


from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

def add_books(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('added_books')  # Redirect to the page displaying added books
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def added_books(request):
    books = Book.objects.all()  # Retrieve all added books from the database
    return render(request, 'added_books.html', {'books': books})

from django.shortcuts import render, redirect
from .models import Book

def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect('added_books')  # Redirect to the page displaying added books
from django.shortcuts import render
from .models import Feedback

def feedback_view(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback.html', {'feedbacks': feedbacks})

from django.shortcuts import render

def admin_profile(request):
    # You can include any necessary data retrieval or processing here
    return render(request, 'adminprofile.html')

def about_us(request):
    return render(request, 'aboutus.html')
def explore(request):
    # You can include any necessary data retrieval or processing here
    return render(request, 'exploreus.html')
def adminfeedback_view(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'adminfeedback.html', {'feedbacks': feedbacks})
from django.shortcuts import render, redirect
from .models import Employee

def insert_emp(request):
    if request.method == "POST":
        EmpId = request.POST['EmpId']
        EmpName = request.POST['EmpName']
        EmpGender = request.POST['EmpGender']
        EmpEmail = request.POST['EmpEmail']
        EmpDesignation = request.POST['EmpDesignation']
        data = Employee(EmpId=EmpId, EmpName=EmpName, EmpGender=EmpGender, EmpEmail=EmpEmail,
                        EmpDesignation=EmpDesignation)
        data.save()

        return redirect('show-emp')
    else:
        return render(request, 'insert.html')
from django.contrib.auth.decorators import login_required

def show_emp(request):
    employees = Employee.objects.all()
    return render(request, 'show.html', {'employees': employees})

# Update Employee

def edit_emp(request,pk):
    employees = Employee.objects.get(id=pk)
    if request.method == 'POST':
            print(request.POST)
            employees.EmpName = request.POST['EmpName']
            employees.EmpGender = request.POST['EmpGender']
            employees.EmpEmail = request.POST['EmpEmail']
            employees.EmpDesignation = request.POST['EmpDesignation']
            employees.EmpDesignation = request.POST['EmpDesignation']
            employees.save()
            return redirect('show-emp')
    context = {
        'employees': employees,
    }

    return render(request,'edit.html',context)

#Delete Employee
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Employee

def remove_emp(request, pk):
    try:
        employee = get_object_or_404(Employee, id=pk)
    except Employee.DoesNotExist:
        return HttpResponse("Employee not found", status=404)

    if request.method == 'POST':
        employee.delete()
        return redirect('show-emp')

    context = {
        'employee': employee,
    }

    return render(request, 'delete.html', context)
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('book_list')
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'book_list.html', {'books': books})
    # Render the book_list.html template with the list of books passed as context



