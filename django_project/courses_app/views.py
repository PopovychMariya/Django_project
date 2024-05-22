from django.shortcuts import render

def courses_page(request):
    if request.user.is_authenticated:
        message = "This is the Courses page."
    else:
        message = "You have no permission to view this page."
    return render(request, 'courses_app/courses_page.html', {'message': message})
