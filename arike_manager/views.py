from datetime import date
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from arike_manager.forms import *
from arike_manager.models import *


class UserCreateView(CreateView):
    model = UserProfile
    form_class = CustomUserCreationForm
    template_name = "auth/create.html"
    success_url = "/login/"


class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "auth/login.html"
    success_url = "/dashboard/"

class UserUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "auth/profile.html"
    success_url = "/dashboard"

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UserListView(ListView):
    queryset = Facility.objects.filter(deleted=False)
    template_name = "auth/list.html"
    context_object_name = "facility"
    paginate_by = 10

    def get_queryset(self):
        return Facility.objects.filter(deleted=False)

class UserDeleteView(DeleteView):
    model = Facility
    template_name = "CRUD/delete.html"
    success_url = "/users/"


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "auth/dashboard.html"


# Facility Views

# class AuthorizedFacilityManager(LoginRequiredMixin):
#     login_url = "/login"
#     success_url = "/dashboard"
#     model = Facility

#     def get_queryset(self):
#         return Facility.objects.filter(deleted=False, userprofile=self.request.user)


class FacilityListView(ListView):
    queryset = Facility.objects.filter(deleted=False)
    template_name = "facility/list.html"
    context_object_name = "facility"
    paginate_by = 10

    def get_queryset(self):
        return Facility.objects.filter(deleted=False)


class FacilityCreateView(CreateView):
    model = Facility
    form_class = FacilityCreationForm
    template_name = "facility/create.html"
    success_url = "/facility/"


class FacilityDeleteView(DeleteView):
    model = Facility
    template_name = "CRUD/delete.html"
    success_url = "/facility/"


class FacilityDetailView(DetailView):
    model = Facility
    template_name = "facility/detail.html"


class FacilityUpdateView(UpdateView):
    model = Facility
    form_class = FacilityCreationForm
    template_name = "facility/update.html"
    success_url = "/dashboard/"

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Patient Views

# class AuthorizedPatientManager(LoginRequiredMixin):
#     login_url = "/login"
#     success_url = "/dashboard"
#     model = Patient

#     def get_queryset(self):
#         return Patient.objects.filter(deleted=False, userprofile=self.request.user)


class PatientListView(ListView):
    queryset = Patient.objects.filter(deleted=False)
    template_name = "patient/list.html"
    context_object_name = "patient"
    paginate_by = 10

    def get_queryset(self):
        return Patient.objects.filter(deleted=False)


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientCreationForm
    template_name = "patient/create.html"
    success_url = "/patient"


class PatientDeleteView(DeleteView):
    model = Patient
    template_name = "CRUD/delete.html"
    success_url = "/patient"


class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientCreationForm
    template_name = "patient/update.html"
    success_url = "/patient"

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Treatment Views

# class AuthorizedTreatmentManager(LoginRequiredMixin):
#     login_url = "/login"
#     success_url = "/dashboard"
#     model = Treatment

#     def get_queryset(self):
#         return Treatment.objects.filter(deleted=False, userprofile=self.request.user)


class TreatmentListView(ListView):
    queryset = Treatment.objects.filter(deleted=False)
    template_name = "treatment/list.html"
    context_object_name = "treatment"
    paginate_by = 10

    def get_queryset(self):
        pid = self.request.GET.get("patient_id")
        res = Treatment.objects.filter(deleted=False)
        if pid:
            res = res.filter(patient__id=pid)
        return res


class TreatmentCreateView(CreateView):
    model = Treatment
    form_class = TreatmentCreationForm
    template_name = "treatment/create.html"
    success_url = "/treatment"


class TreatmentDeleteView(DeleteView):
    model = Treatment
    template_name = "CRUD/delete.html"
    success_url = "/treatment"


class TreatmentUpdateView(UpdateView):
    model = Treatment
    form_class = TreatmentCreationForm
    template_name = "treatment/update.html"
    success_url = "/treatment"

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Family Views

# class AuthorizedFamilyManager(LoginRequiredMixin):
#     login_url = "/login"
#     success_url = "/dashboard"
#     model = Family

#     def get_queryset(self):
#         return Family.objects.filter(deleted=False, userprofile=self.request.user)


class FamilyListView(ListView):
    queryset = Family_Detail.objects.filter(deleted=False)
    template_name = "family/list.html"
    context_object_name = "family"
    paginate_by = 10

    def get_queryset(self):
        pid = self.request.GET.get("patient_id")
        res = Family_Detail.objects.filter(deleted=False)
        if pid:
            res = res.filter(patient__id=pid)
        return res


class FamilyCreateView(CreateView):
    model = Family_Detail
    form_class = FamilyCreationForm
    template_name = "family/create.html"
    success_url = "/family"


class FamilyDeleteView(DeleteView):
    model = Family_Detail
    template_name = "CRUD/delete.html"
    success_url = "/family"


class FamilyUpdateView(UpdateView):
    model = Family_Detail
    form_class = FamilyCreationForm
    template_name = "family/update.html"
    success_url = "/family"

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Disease Views

# class AuthorizedDiseaseManager(LoginRequiredMixin):
#     login_url = "/login"
#     success_url = "/dashboard"
#     model = Patient_Disease

#     def get_queryset(self):
#         return Patient_Disease.objects.filter(deleted=False, userprofile=self.request.user)


class DiseaseListView(ListView):
    queryset = Patient_Disease.objects.filter(deleted=False)
    template_name = "disease/list.html"
    context_object_name = "disease"
    paginate_by = 10

    def get_queryset(self):
        pid = self.request.GET.get("patient_id")
        res = Patient_Disease.objects.filter(deleted=False)
        if pid:
            res = res.filter(patient__id=pid)
        return res


class DiseaseCreateView(CreateView):
    model = Patient_Disease
    form_class = PatientDiseaseForm
    template_name = "disease/create.html"
    success_url = "/disease"


class DiseaseDeleteView(DeleteView):
    model = Patient_Disease
    template_name = "CRUD/delete.html"
    success_url = "/disease"


class DiseaseUpdateView(UpdateView):
    model = Schedule_Visit
    form_class = PatientDiseaseForm
    template_name = "disease/update.html"
    success_url = "/disease"

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Visit Views

# class AuthorizedVisitManager(LoginRequiredMixin):
#     login_url = "/login"
#     success_url = "/dashboard"
#     model = Visit

#     def get_queryset(self):
#         return Schedule_Visit.objects.filter(deleted=False, userprofile=self.request.user)


class VisitListView(ListView):
    queryset = Schedule_Visit.objects.filter(deleted=False)
    template_name = "visits/list.html"
    context_object_name = "visit"
    paginate_by = 10

    def get_queryset(self):
        pid = self.request.GET.get("patient_id")
        res = Schedule_Visit.objects.filter(deleted=False)
        if pid:
            res = res.filter(patient__id=pid)
        return res


class VisitCreateView(CreateView):
    model = Schedule_Visit
    form_class = VisitCreationForm
    template_name = "visits/create.html"
    success_url = "/visit"


class VisitDeleteView(DeleteView):
    model = Schedule_Visit
    template_name = "CRUD/delete.html"
    success_url = "/visit"


class VisitUpdateView(UpdateView):
    model = Schedule_Visit
    form_class = VisitCreationForm
    template_name = "visits/update.html"
    success_url = "/visit"

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
