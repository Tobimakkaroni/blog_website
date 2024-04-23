from django.shortcuts import render

def rust_calculator_view(request):
    return render(request, 'rust/rust_calculator.html')