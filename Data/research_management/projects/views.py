from django.shortcuts import render, redirect
from .models import ResearchProject
from .forms import ResearchForm ,EventForm

def project_list(request):
    projects = ResearchProject.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})



# def project_add(request):
#     if request.method == 'POST':
#         project_name = request.POST['project_name']
#         author_name = request.POST['author_name']
#         pdf_file = request.FILES['pdf_file']  # Handle file uploads

#         # Create and save a new ResearchProject instance
#         project = ResearchProject(
#             project_name=project_name,
#             author_name=author_name,
#             pdf_file=pdf_file
#         )
#         project.save()


#         return redirect('project_list')

#     return render(request, 'projects/project_form.html')

def project_add(request):
    if request.method == "POST":
        form = ResearchForm(request.POST, request.FILES)  # เพิ่ม request.FILES
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ResearchForm()
    return render(request, 'projects/project_form.html', {'form': form})

    
    

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')  # Redirect to a list view or another page after saving
    else:
        form = EventForm()

    return render(request, 'events/add_event.html', {'form': form})

