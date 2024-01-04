from django.shortcuts import render


# Create your views here.
def CreateOrderRequest(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = DocumentForm()
    return render(request, "core/model_form_upload.html", {"form": form})


def CustomerDashboard(req):
    return render(req, "CustomerDashboard.Jinja2")
