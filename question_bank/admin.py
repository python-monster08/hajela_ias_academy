from django.contrib import admin
from .models import QuestionBank, InputSuggestion, InputSuggestionImage, InputSuggestionDocument, ExamName, Subject, Area, PartName,ChapterName ,TopicName

class QuestionBankAdmin(admin.ModelAdmin):
    list_display = ('question_number', 'exam_name', 'exam_year', 'type_of_question', 'question_sub_type', 'marks')
    list_filter = ('exam_name', 'exam_year', 'type_of_question', 'question_sub_type')
    list_filter = ('exam_name', 'exam_year', 'type_of_question', 'degree_of_difficulty')
    ordering = ('exam_year', 'exam_name', 'question_number')

    fieldsets = (
        ('Basic Information', {
            'fields': ('type_of_question', 'exam_name', 'exam_stage', 'exam_year', 'language', 'script', 'marks', 'negative_marks', 'degree_of_difficulty', 'question_sub_type')
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
            'fields': ('image', 'subject_name', 'area_name', 'part_name', 'chapter_name', 'topic_name')
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

admin.site.register(QuestionBank, QuestionBankAdmin)


class InputSuggestionImageInline(admin.TabularInline):
    model = InputSuggestionImage
    extra = 1  # Allows adding extra image fields directly in the admin view

class InputSuggestionDocumentInline(admin.TabularInline):
    model = InputSuggestionDocument
    extra = 1  # Allows adding extra document fields directly in the admin view

@admin.register(InputSuggestion)
class InputSuggestionAdmin(admin.ModelAdmin):
    list_display = ('brief_description', 'exam_name', 'subject_name', 'created_at')
    search_fields = ('brief_description', 'exam_name', 'subject_name', 'area_name', 'part_name', 'topic_name')
    list_filter = ('exam_name', 'subject_name', 'created_at')

    inlines = [InputSuggestionImageInline, InputSuggestionDocumentInline]

    fieldsets = (
        (None, {
            'fields': ('brief_description', 'details', 'exam_name', 'subject_name', 'area_name', 'part_name', 'topic_name')
        }),
        ('Media & Links', {
            'fields': ('question_video', 'question_link')
        }),
        ('Additional Information', {
            'fields': ('other_text',)
        }),
    )

    # To display images and documents in the admin view
    def view_on_site(self, obj):
        return obj.get_absolute_url()  # If you have a view for this object

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