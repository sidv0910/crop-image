from django.shortcuts import render, redirect
from .forms import MatrixForm
from .models import Instructions

subjects = ["BI12", "BI34", "CH12", "CH34", "PH12", "PH34", "MM12", "MM34", "SM12", "SM34", "Junior Maths", "EC34", "PS34", "UCAT"]
booklet_types = ["Workbook", "Workshop", "Homework", "Test", "Exam", "SAC"]


def matrix(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        booklet_type = request.POST.get('bookletType')
        booklet = subject + " " + booklet_type
        results = Instructions.objects.all().order_by('order')
        instruction = []
        for result in results:
            if booklet in result.booklet:
                instruction.append(result.instruction)
        request.session['output'] = True
        request.session['subject'] = subject
        request.session['booklet_type'] = booklet_type
        request.session['instruction'] = instruction
        return redirect(matrix)
    else:
        form = MatrixForm()
        context = {'output': False, 'subjects': subjects, 'booklet_types': booklet_types, 'form': form}
        if request.session.get('output') is not None:
            context['output'] = True
            context['subject'] = request.session.get('subject')
            form.fields['subject'].widget.attrs['value'] = request.session.get('subject')
            context['booklet_type'] = request.session.get('booklet_type')
            form.fields['bookletType'].widget.attrs['value'] = request.session.get('booklet_type')
            context['instruction'] = request.session.get('instruction')
            request.session.pop('output')
            request.session.pop('subject')
            request.session.pop('booklet_type')
            request.session.pop('instruction')
        return render(request, 'matrix.html', context)
