from django.test import TestCase

# Create your tests here.
def home(request):
    return render(request,'base.html')