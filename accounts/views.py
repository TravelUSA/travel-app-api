from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        print('SUBMITTED REG')
        return redirect(register)
    else:
        return render(request, 'accounts/register.html')


