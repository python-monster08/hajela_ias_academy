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

    path('get-subjects-list/', views.get_subjects_list, name='get_subjects_list'),
    path('get-areas-list/', views.get_areas_list, name='get_areas_list'),
    path('get-parts-list/', views.get_parts_list, name='get_parts_list'),
    path('get-topics-list/', views.get_topics_list, name='get_topics_list'),
    path('get-chapters-list/', views.get_chapters_list, name='get_chapters_list'),

    path('view-questions/', views.view_questions, name='view_questions'),

    path('add-quote-idiom-phrase/', views.add_quote_idiom_phrase, name='add_quote_idiom_phrase'),
    path('quotes-idioms-phrases/', views.quotes_idioms_phrases_view, name='quotes_idioms_phrases'),
    path('dashboard/analytics/', views.analytics_dashboard, name='analytics_dashboard'),  # Analytics dashboard
    path('new-dashboard/', views.new_dashboard_view, name='new_dashboard_view'),  # Analytics dashboard

    # path('export/this_week/csv/', views.export_this_week_csv, name='export_this_week_csv'),
    # path('export/this_week/pdf/', views.export_this_week_pdf, name='export_this_week_pdf'),
    # path('export/earlier/csv/', views.export_earlier_csv, name='export_earlier_csv'),
    # path('export/earlier/pdf/', views.export_earlier_pdf, name='export_earlier_pdf'),
    path('generate_this_week_csv/', views.generate_this_week_csv, name='generate_this_week_csv'),
    path('generate_earlier_week_csv/', views.generate_earlier_week_csv, name='generate_earlier_week_csv'),
]