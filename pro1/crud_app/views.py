from django.shortcuts import render, redirect
from .forms import HallTicketForm
from .models import HallTicket
from django.views import View


class CreateView(View):
    template_name = "crud_app/create.html"
    form = HallTicketForm

    def get(self, request):
        form = self.form()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        return render(request, self.template_name, {"form": form})


class ShowView(View):
    template_name = "crud_app/show.html"
    form = HallTicketForm

    def get(self, request):
        form = self.form()
        obj = HallTicket.objects.all()
        context = {"obj": obj, "form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        return render(request, self.template_name, {"form": form})


class UpdateView(View):
    template_name = "crud_app/create.html"
    form = HallTicketForm

    def get(self, request, pk):
        obj = HallTicket.objects.get(id=pk)
        form = HallTicketForm(request.POST, instance=obj)
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        template_name = "crud_app/create.html"
        obj = HallTicket.objects.get(id=pk)
        form = HallTicketForm(request.POST, instance=obj)
        context = {"form": form}
        if form.is_valid():
            form.save()
            return redirect("show_url")
        return render(request, template_name, context)


class DeleteView(View):
    template_name = "crud_app/confirm.html"
    form = HallTicketForm

    def get(self, request, pk):
        obj = HallTicket.objects.get(id=pk)
        form = self.form(request.POST, instance=obj)
        context = {"obj": obj, "form": form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        obj = HallTicket.objects.get(id=pk)
        obj.delete()
        return redirect("show_url")




