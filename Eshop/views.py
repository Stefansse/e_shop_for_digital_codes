from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from Eshop.forms import PaymentForm
from Eshop.models import VideoGame, Company, CustomUser, DigitalCode, Order, Payment
from django.contrib.auth.decorators import login_required


# Create your views here.


# Create your views here.


def videogame_profile(request, videogame_id):
    videogame = get_object_or_404(VideoGame, id=videogame_id)
    return render(request, 'videogame_profile.html', {'videogame': videogame})


def company_profile(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    return render(request, 'company_profile.html', {'company': company})


def signuppage(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("username")
        pass1 = request.POST.get("password1")
        # pass2 = request.POST.get("password2")

        my_user = CustomUser.objects.create_user(uname, email, pass1)
        my_user.save()
        return redirect('login')

    return render(request, "signup.html")


def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass")
        print(username, pass1)
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, "login.html")


def home(request):
    videogames = VideoGame.objects.all()
    videogame_data = []

    for game in videogames:
        order = Order.objects.filter(digital_codes__videogame=game).first()
        digital_code = DigitalCode.objects.filter(videogame=game).first()
        order_id = order.pk if order else None
        digital_code_value = digital_code.code_value if digital_code else None

        videogame_data.append({
            'game': game,
            'order_id': order_id,
            'digital_code': digital_code_value
        })

    context = {
        'videogames': videogame_data
    }

    return render(request, "home.html", context=context)


def logoutPage(request):
    logout(request)
    return redirect('login')


def profile(request):
    user = request.user
    if request.method == 'POST':
        bio = request.POST.get('bio')
        birth_date = request.POST.get('birth-date')
        user.bio = bio
        user.birth_date = birth_date
        user.save()
        return redirect('profile')

    context = {
        'user': user
    }
    return render(request, 'profile.html', context)


def videogamepage(request):
    queryset = VideoGame.objects.all()
    context = {"videogames": queryset}
    return render(request, "videogamepage.html", context=context)


def companypage(request):
    queryset = Company.objects.all()
    context = {"companies": queryset}
    return render(request, "companypage.html", context=context)


def digitalcodepage(request):
    queryset = DigitalCode.objects.all()
    context = {"digitalcodes": queryset}
    return render(request, "digitalcodepage.html", context=context)


def orderpage(request):
    queryset = Order.objects.all()
    context = {"orders": queryset}
    return render(request, "orderpage.html", context=context)


def payment_add(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
            return redirect('home')

    else:
        form = PaymentForm()

    return render(request, 'payment_form.html', {'form': form})


@login_required
def mypayments(request):
    user = request.user
    payments = Payment.objects.filter(user=user)

    context = {
        'payments': payments
    }
    return render(request, 'mypayments.html', context)
