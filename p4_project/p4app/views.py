from django.shortcuts import render

def check_palindrome(number):
    
    num_str = str(number)
    
    return num_str == num_str[::-1]

def home(request):
    result = None
    if request.method == 'POST':
        number = request.POST.get('number')
        if number.isdigit():
            is_palindrome = check_palindrome(number)
            result = f"{number} is {'a palindrome' if is_palindrome else 'not a palindrome'}."
        else:
            result = "Please enter a valid number."

    return render(request, 'home.html', {'result': result})

