from django.shortcuts import render, redirect

def input_page(request):
    if request.method == 'POST':
        user_input = request.POST.get('input_field', 'No input provided')
        request.session['user_input'] = user_input
        return redirect('display_page')
    return render(request, 'members_app/input_page.html')

def display_page(request):
    user_input = request.session.get('user_input', 'No input provided')
    return render(request, 'members_app/display_page.html', {'user_input': user_input})

def session_page(request):
    if request.method == 'POST':
        if 'clear' in request.POST:
            request.session.pop('user_input', None)
        return redirect('session_page')
    
    user_input = request.session.get('user_input', 'No input provided')
    return render(request, 'members_app/session_page.html', {'user_input': user_input})
