from .models import SubRubric

def bboard_context_processor(request):
    context = {}
    context['rubrics'] = SubRubric.objects.all()
    return context