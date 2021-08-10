import re
import csv

from django.shortcuts import get_object_or_404, redirect, render

from .core import unique_sales_manager_id
from .models import SalesBranch, Csv, SalesManager
from .forms import CsvModelForm, SalesManagerForm


def upload_sales_manager_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, "r") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    row = "".join(row)
                    row = row.split(";")
                    sales_branch_raw = str(row[2])
                    var1 = unique_sales_manager_id()
                    sales_branch = SalesBranch.objects.get(short_name=sales_branch_raw)
                    SalesManager.objects.create(
                        first_name=str(row[0]),
                        last_name=str(row[1]),
                        sales_branch=sales_branch,
                        area=str(row[3]),
                        position=str(row[4]),
                        supervisor=str(row[5]),
                        phone_number=int(row[6]),
                        email=str(row[7]),
                        id_number=var1,
                        is_active=True,
                    )
            obj.activated = True
            obj.save()
    return render(request, "upload.html", {"form": form})


def upload_sales_branch_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, "r") as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    row = "".join(row)
                    row = row.split(";")
                    SalesBranch.objects.create(
                        short_name=str(row[0]),
                        full_name=str(row[1]),
                    )
            obj.activated = True
            obj.save()
    return render(request, "upload-branches.html", {"form": form})


def all_traders(request):
    traders = SalesManager.objects.all()
    return render(request, "all-selers.html", {"test": traders})


def specific_trader(request, pk):
    trader = SalesManager.objects.filter(id_number=pk)
    return render(request, "sales-manager.html", {"test": trader})


def specific_trader_last_name(request, pk):
    pk = f"{pk}"
    trader = SalesManager.objects.filter(last_name=f"{pk}")
    return render(request, "sales-manager.html", {"test": trader})


def find_trader(request):
    if request.method == "POST":
        pk = request.POST.get("fname")
        try:
            pk = re.search("\d+", pk)[0]
            try:
                pk = int(pk)
                return specific_trader(request, pk)
            except ValueError:
                return render(request, "submit.html")
        except TypeError:
            return render(request, "submit.html")
    return render(request, "submit.html")


def find_trader_dok(request):
    if request.method == "POST":

        pk_number = request.POST.get("fname")
        if pk_number is not None:
            try:
                pk = int(pk_number)
                find_id_in_base = SalesManager.objects.filter(id_number=pk)
                if len(find_id_in_base) == 0:
                    find_object = SalesManager.objects.filter(phone_number=pk)
                    try:
                        pk = find_object[0]
                        pk = pk.id_number
                    except:
                        pass
                return specific_trader(request, pk)

            except ValueError:
                data = str(pk_number.capitalize())
                try:
                    find_object = SalesManager.objects.filter(last_name=data)
                    pk = find_object[0]
                    pk = pk.id_number
                    return specific_trader(request, pk)
                except IndexError:
                    return render(request, "submit-dok.html")

    return render(request, "submit-dok.html")


def add_sales_manager(request):
    id_number = unique_sales_manager_id()
    if request.method == "POST":
        form = SalesManagerForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.id_number = id_number
            post.save()
            return redirect("/sheet/all-traders/")
    else:
        form = SalesManagerForm()

    return render(request, "add-sales-manager.html", {"form": form})


def edit_sales_manager(request, id_number):
    instance = get_object_or_404(SalesManager, id_number=id_number)
    form = SalesManagerForm(data=request.POST or None, instance=instance)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            traders = SalesManager.objects.all()
            return redirect("/sheet/all-traders/")

    return render(request, "add-sales-manager.html", {"form": form})


def delete_sales_manager(request, id_number):
    instance = get_object_or_404(SalesManager, id_number=id_number)
    form = SalesManagerForm(data=request.POST or None, instance=instance)

    if request.method == "POST":
        instance.delete()
        return redirect("/sheet/all-traders/")

    return render(request, "delete-sales-manager.html", {"form": form})
