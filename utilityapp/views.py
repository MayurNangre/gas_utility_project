from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('submit_success')  # Redirect to a success page
    else:
        form = ServiceRequestForm()
    return render(request, 'utilityapp/submit_request.html', {'form': form})

def track_request(request):
    # Assuming you have a way to identify the request (e.g., request ID)
    request_id = request.GET.get('request_id')
    if request_id:
        try:
            service_request = ServiceRequest.objects.get(id=request_id)
            return render(request, 'utilityapp/track_request.html', {'request': service_request})
        except ServiceRequest.DoesNotExist:
            return render(request, 'utilityapp/track_request.html', {'error': 'Request not found'})
    else:
        return render(request, 'utilityapp/track_request.html', {'error': 'Request ID not provided'})
