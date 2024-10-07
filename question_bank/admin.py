from django.contrib import admin
from .models import QuestionBank, InputSuggestion, InputSuggestionImage, InputSuggestionDocument, ExamName, Subject, Area, PartName,ChapterName ,TopicName, QuoteIdiomPhrase

from django.contrib import admin
from question_bank.models import QuestionBank

from django.contrib import admin
from question_bank.models import QuestionBank, Report

class QuestionBankAdmin(admin.ModelAdmin):
    list_display = ('id','created_at', 'created_by', 'question_number', 'get_question', 'get_exam_names', 'get_subjects', 'exam_year', 'type_of_question', 'question_sub_type', 'marks')
    search_fields = ('exam_name', 'subject_name', 'area_name', 'part_name', 'chapter_name', 'topic_name', 'question_part_first', 'correct_answer_choice')
    list_filter = ('exam_name', 'exam_year', 'type_of_question', 'degree_of_difficulty', 'subject_name', 'area_name', 'part_name', 'chapter_name', 'topic_name')
    date_hierarchy = 'created_at'
    ordering = ('exam_year', 'exam_name', 'question_number')

    fieldsets = (
        ('Basic Information', {
            'fields': ('type_of_question', 'exam_name', 'exam_stage', 'exam_year', 'language', 'script', 'evergreen_index', 'marks', 'negative_marks', 'degree_of_difficulty', 'question_sub_type')
        }),
        ('Question Details', {
            'fields': ('question_number', 'question_part', 'reason', 'assertion', 'question_part_first', 'question_part_third')
        }),
        ('List Fields', {
            'fields': (
                'list_1_name', 'list_2_name',
                'list_1_row1', 'list_1_row2', 'list_1_row3', 'list_1_row4', 'list_1_row5', 'list_1_row6', 'list_1_row7', 'list_1_row8',
                'list_2_row1', 'list_2_row2', 'list_2_row3', 'list_2_row4', 'list_2_row5', 'list_2_row6', 'list_2_row7', 'list_2_row8',
            )
        }),
        ('Objective Fields', {
            'fields': ('answer_option_a', 'answer_option_b', 'answer_option_c', 'answer_option_d')
        }),
        ('Correct Answer', {
            'fields': ('correct_answer_choice', 'correct_answer_description')
        }),
        ('Extra Information', {
            'fields': ('image', 'subject_name', 'area_name', 'part_name', 'chapter_name', 'topic_name', 'created_by')
        }),
        ('Table Data', {
            'fields': (
                'table_head_a', 'table_head_b', 'table_head_c', 'table_head_d',
                'head_a_data1', 'head_a_data2', 'head_a_data3', 'head_a_data4',
                'head_b_data1', 'head_b_data2', 'head_b_data3', 'head_b_data4',
                'head_c_data1', 'head_c_data2', 'head_c_data3', 'head_c_data4',
                'head_d_data1', 'head_d_data2', 'head_d_data3', 'head_d_data4'
            )
        }),
    )

    # Custom methods to display related data in list_display
    def get_question(self, obj):
        if obj.question_part_first:
            return obj.question_part_first
        else:
            return obj.question_part
        
    # Custom method to display exams in list_display
    def get_exam_names(self, obj):
        return ", ".join([exam.name for exam in obj.exam_name.all()])
    
    get_exam_names.short_description = 'Exams'  # Display name for the column

    # Custom method to display subjects in list_display
    def get_subjects(self, obj):
        return ", ".join([subject.name for subject in obj.subject_name.all()])
    
    get_subjects.short_description = 'Subjects'  # Display name for the column

    # Custom method to display areas in list_display
    def get_areas(self, obj):
        return ", ".join([area.name for area in obj.area_name.all()])
    
    get_areas.short_description = 'Areas'  # Display name for the column

    # Custom method to display parts in list_display
    def get_parts(self, obj):
        return ", ".join([part.name for part in obj.part_name.all()])
    
    get_parts.short_description = 'Parts'  # Display name for the column

    # Custom method to display chapters in list_display
    def get_chapters(self, obj):
        return ", ".join([chapter.name for chapter in obj.chapter_name.all()])
    
    get_chapters.short_description = 'Chapters'  # Display name for the column

    # Custom method to display topics in list_display
    def get_topics(self, obj):
        return ", ".join([topic.name for topic in obj.topic_name.all()])
    
    get_topics.short_description = 'Topics'  # Display name for the column


admin.site.register(QuestionBank, QuestionBankAdmin)


class InputSuggestionImageInline(admin.TabularInline):
    model = InputSuggestionImage
    extra = 1  # Allows adding extra image fields directly in the admin view

class InputSuggestionDocumentInline(admin.TabularInline):
    model = InputSuggestionDocument
    extra = 1  # Allows adding extra document fields directly in the admin view

@admin.register(InputSuggestion)
class InputSuggestionAdmin(admin.ModelAdmin):
    list_display = ('brief_description', 'created_at')
    search_fields = ('brief_description', 'exam_name__name', 'subject_name__name', 'area_name__name', 'part_name__name', 'topic_name__name')
    list_filter = ('exam_name', 'subject_name', 'created_at')

    inlines = [InputSuggestionImageInline, InputSuggestionDocumentInline]

    fieldsets = (
        (None, {
            'fields': (
                'language', 
                'script', 
                'evergreen_index', 
                'brief_description', 
                'details', 
                'exam_name', 
                'subject_name', 
                'area_name', 
                'part_name', 
                'chapter_name',  # Included chapter_name as it's in the model
                'topic_name'
            )
        }),
        ('Media & Links', {
            'fields': ('question_video', 'question_link')
        }),
        ('Additional Information', {
            'fields': ('other_text', 'created_by')
        }),
    )

    def view_on_site(self, obj):
        return obj.get_absolute_url()  # Allows viewing on site if there's a corresponding view

    # To handle display of many-to-many fields in list view
    def get_exam_name(self, obj):
        return ", ".join([exam.name for exam in obj.exam_name.all()])
    get_exam_name.short_description = 'Exam Name'

    def get_subject_name(self, obj):
        return ", ".join([subject.name for subject in obj.subject_name.all()])
    get_subject_name.short_description = 'Subject Name'

    list_display = ('brief_description', 'get_exam_name', 'get_subject_name', 'created_at', 'created_by')
    
@admin.register(InputSuggestionImage)
class InputSuggestionImageAdmin(admin.ModelAdmin):
    list_display = ('question', 'image')
    search_fields = ('question__brief_description',)

@admin.register(InputSuggestionDocument)
class InputSuggestionDocumentAdmin(admin.ModelAdmin):
    list_display = ('question', 'document')
    search_fields = ('question__brief_description',)


@admin.register(ExamName)
class ExamNameAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'exam')
    list_filter = ('exam',)

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    list_filter = ('subject',)

@admin.register(PartName)
class PartNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'area')
    list_filter = ('area',)

@admin.register(ChapterName)
class ChapterNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'part')
    list_filter = ('part',)

@admin.register(TopicName)
class TopicNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'chapter')
    list_filter = ('chapter',)



# Admin for QuoteIdiomPhrase
@admin.register(QuoteIdiomPhrase)
class QuoteIdiomPhraseAdmin(admin.ModelAdmin):
    list_display = ('type', 'status', 'content', 'get_exams', 'get_subjects', 'get_areas', 'get_parts', 'get_chapters', 'get_topics', 'created_at')
    search_fields = ('content', 'author', 'exams__name', 'subjects__name', 'areas__name', 'parts__name', 'chapters__name', 'topics__name')
    list_filter = ('type', 'exams', 'subjects', 'areas', 'parts', 'chapters')
    date_hierarchy = 'created_at'

    # Custom method to display exams in list_display
    def get_exams(self, obj):
        return ", ".join([exam.name for exam in obj.exams.all()])
    
    get_exams.short_description = 'Exams'  # Display name for the column

    # Custom method to display subjects in list_display
    def get_subjects(self, obj):
        return ", ".join([subject.name for subject in obj.subjects.all()])
    
    get_subjects.short_description = 'Subjects'  # Display name for the column

    # Custom method to display areas in list_display
    def get_areas(self, obj):
        return ", ".join([area.name for area in obj.areas.all()])
    
    get_areas.short_description = 'Areas'  # Display name for the column

    # Custom method to display parts in list_display
    def get_parts(self, obj):
        return ", ".join([part.name for part in obj.parts.all()])
    
    get_parts.short_description = 'Parts'  # Display name for the column

    # Custom method to display chapters in list_display
    def get_chapters(self, obj):
        return ", ".join([chapter.name for chapter in obj.chapters.all()])
    
    get_chapters.short_description = 'Chapters'  # Display name for the column

    # Custom method to display topics in list_display
    def get_topics(self, obj):
        return ", ".join([topic.name for topic in obj.topics.all()])
    
    get_topics.short_description = 'Topics'  # Display name for the column



admin.site.register(Report)