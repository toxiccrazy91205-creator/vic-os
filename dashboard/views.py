from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class DashboardView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, 'dashboard/index.html')

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'dashboard/login.html')
    
    def post(self, request):
        # Simplistic login for demo/setup
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Login attempt for: {username}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(f"Login successful for: {username}")
            login(request, user)
            return redirect('dashboard')
        else:
            print(f"Login failed for: {username}")
            messages.error(request, "Invalid credentials")
            return render(request, 'dashboard/login.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class DiagnosticsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard/diagnostics.html')
