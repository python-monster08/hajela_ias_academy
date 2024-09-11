from django.urls import path
from . import views

urlpatterns = [
    # path('add-question/', views.add_question, name='add-question'),
    path('upload-file/', views.upload_file, name='upload-file'),
    # Path for generating the questions document
    path('generate-questions-document/', views.generate_questions_document, name='generate-questions-document'),
    path('generate-questions/', views.generate_questions, name='generate_questions'),
    # add questions urls
    path('add/simple/question/', views.add_simple_type_question, name='add-simple-type-question'),
    path('add/r-and-a/question/', views.add_r_and_a_type_question, name='add-r-and-a-type-question'),
    path('add/list-1/question/', views.add_list_type_1_question, name='add-list-type-1-question'),
    path('add/list-2/question/', views.add_list_type_2_question, name='add-list-type-2-question'),
    path('add-true-and-false-type-question/', views.add_true_and_false_type_question, name='add-true-and-false-type-question'),
    path('add-fill-in-the-blank-question/', views.add_fill_in_the_blank_question, name='add-fill-in-the-blank-question'),
    path('add-input-suggestion/', views.add_input_suggestion, name='add-input-suggestion'),
    path('input-suggestion-list/', views.view_input_suggestion, name='input-suggestion-list'),
    path('view-input-suggestion/<int:question_id>/', views.question_blog_view, name='view-input-suggestion'),


    path('get-subjects/', views.get_subjects, name='get_subjects'),
    path('get-areas/', views.get_areas, name='get_areas'),
    path('get-parts/', views.get_parts, name='get_parts'),
    path('get-topics/', views.get_topics, name='get_topics'),
    path('get-chapters/', views.get_chapters, name='get_chapters'),

    path('view-questions/', views.view_questions, name='view_questions'),

]