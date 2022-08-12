#-------- Django import--------#

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

#-------Model Import--------#
from services_management.models import complaint

#-------Registeration Form import--------#
from .forms import UserRegisterForm
from .forms import UserUpdateForm
from .forms import ProfileUpdateForm

# Create your views here.
def home(request):
    context = {
        'complaints': complaint.objects.all()
    }
    return render(request, 'user_management/home.html', context)


    
#-------- User Registeration Logic --------#

def register(request):
    if request.method == 'POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            
            username=form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            form.save()
            return redirect('Login')
           
    else:
        form = UserRegisterForm()
    return render(request,'user_management/register.html',{'form':form})


#-------- Profile  Logic --------#

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user_management/profile.html', context)

#-------- Complain Class Based View's--------#

class UserComplainListView(ListView):
    model = complaint
    context_object_name = 'complaints'
    paginate_by = 5
    template_name = 'user_management/complaint_list.html'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return complaint.objects.filter(user_complain=user).order_by('-complain_date')    


class ComplaintDetailView(DetailView):
    model = complaint      
    template_name = 'user_management/complaint_detail.html'



class ComplaintDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = complaint
    success_url = '/'
    template_name = 'user_management/complaint_confirm_delete.html'

    def test_func(self):
        complaint = self.get_object()
        if self.request.user == complaint.user_complain:
            return True
        return False



#--------Complain Update View --------#
class ComplaintUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = complaint
    template_name = 'user_management/complaint_form.html'
    fields = ['complain_title', 'complain_description','image']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user_complain = self.request.user
        return super().form_valid(form)

    def test_func(self):
        complaint = self.get_object()
        if self.request.user == complaint.user_complain:
            return True
        return False



