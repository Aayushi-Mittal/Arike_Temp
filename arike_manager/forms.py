from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from arike_manager.models import *

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field!="deleted" or field!="is_verified":
                self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"    
    class Meta:
        model = UserProfile
        fields = ("user", "phone", "is_verified", "role", "facility", "district")


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
            
class UserProfileForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
            
    class Meta:
        model = UserProfile
        fields = ("phone", "is_verified", "role", "facility", "district", "user")
        
class FacilityCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field!="deleted":
                self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
    class Meta(forms.ModelForm):
        model = Facility
        fields = ("kind", "name", "address", "pincode", "phone", "ward", "deleted")

      
class PatientCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field!="deleted":
                self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"

    class Meta(forms.ModelForm):
        model = Patient
        fields = ("full_name", "date_of_birth", "address", "landmark", "phone", "gender", "emergency_phone_number", "ward", "facility", "deleted", "expired_time")

class TreatmentCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field!="deleted":
                self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"

    class Meta(forms.ModelForm):
        model = Treatment
        fields = ("description", "care_type", "care_sub_type", "patient", "nurse", "deleted")
        
        
class FamilyCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field!="deleted" and field!="is_primary":
                self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"

    class Meta(forms.ModelForm):
        model = Family_Detail
        fields = ("full_name", "date_of_birth", "phone", "email", "relation", "address", "education", "occupation", "remarks", "is_primary", "patient", "deleted")
        
class VisitCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field!="deleted":
                self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
    class Meta(forms.ModelForm):
        model = Schedule_Visit
        fields = ("date", "time", "duration", "patient", "nurse", "deleted")

class VisitDetailsCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field!="deleted":
                self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
    class Meta(forms.ModelForm):
        model = Visit_Details
        fields = ("palliative_phase", "blood_pressure", "pulse", "general_random_blood_sugar", "personal_hygiene", "mouth_hygiene", "pubic_hygiene", "systemic_examination", "patient_at_peace", "pain", "symptoms", "note", "visit_schedule")

class PatientDiseaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field!="deleted":
                self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
    class Meta(forms.ModelForm):
        model = Patient_Disease
        fields = ("patient", "disease", "treatment", "note", "nurse", "deleted")

