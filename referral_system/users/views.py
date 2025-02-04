from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User
import random
import string
from django.shortcuts import render, get_object_or_404

def generate_referral_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        city = request.POST.get('city')
        referral_code = request.POST.get('referral_code', None)
        password = request.POST.get('password')

        if not email or not name or not mobile_number or not city or not password:
            return JsonResponse({'error': 'All fields except referral_code are required'}, status=400)

        referrer = None
        if referral_code:
            try:
                referrer = User.objects.get(referral_code=referral_code)
            except User.DoesNotExist:
                return JsonResponse({'error': 'Invalid referral code'}, status=400)

        user = User(
            email=email,
            name=name,
            mobile_number=mobile_number,
            city=city,
            password=password,  
            referral_code=generate_referral_code(),
            referred_by=referrer
        )
        user.save()

        return redirect('login')

    return render(request, 'users/signup.html')
          

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if user.password == password:
                request.session['user_id'] = user.id
                return redirect('home')
            else:
                return JsonResponse({'error': 'Invalid password'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=400)

    return render(request, 'users/login.html')


def home(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('login')

    user = User.objects.get(id=user_id)
    return render(request, 'users/home.html', {'user': user})

def referral(request):
    user_id = request.GET.get('user_id')
    user = get_object_or_404(User, id=user_id)    
    referees = User.objects.filter(referred_by=user)    
    return render(request, 'users/referral.html', {'user': user, 'referees': referees})

