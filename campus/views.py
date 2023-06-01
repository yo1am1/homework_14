from django.shortcuts import render
from django.views.decorators.cache import cache_page

from campus.forms import StudentNumberForm
from campus.models import Student

import faker

faker = faker.Faker()


def index(request):
    form = StudentNumberForm(request.POST)
    if form.is_valid() and request.method == "POST":
        number = form.cleaned_data["number"]
        for _ in range(number):
            Student.objects.create(
                name=faker.name(),
                age=faker.random_int(min=18, max=30),
                email=faker.email(),
                phone=faker.phone_number(),
                address=faker.address(),
            )
        return render(
            request,
            "index.html",
            {
                "form": form,
                "number": f"{number} student(-s) has/have been generated.",
            },
        )
    else:
        form = StudentNumberForm()
        return render(request, "index.html", {"form": form})


def display_students(request):
    students = Student.objects.values("id", "name", "age", "email", "phone").order_by(
        "id"
    )
    return render(request, "students.html", {"students": students})
