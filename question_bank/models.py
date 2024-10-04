from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User  # Import the User model
from django.conf import settings

class ExamName(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=255)
    exam = models.ForeignKey(ExamName, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return f"{self.name} --> ({self.exam.name})"


class Area(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='areas')

    def __str__(self):
        return f"{self.name} --> ({self.subject.name} - {self.subject.exam.name})"


class PartName(models.Model):
    name = models.CharField(max_length=255)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='parts')

    def __str__(self):
        return f"{self.name} ({self.area.name} - {self.area.subject.name} - {self.area.subject.exam.name})"


# New Model: ChapterName refers to PartName
class ChapterName(models.Model):
    name = models.CharField(max_length=255)
    part = models.ForeignKey(PartName, on_delete=models.CASCADE, related_name='chapters')

    def __str__(self):
        return f"{self.name} ({self.part.name} - {self.part.area.name} - {self.part.area.subject.name})"


# New Model: TopicName refers to ChapterName
class TopicName(models.Model):
    name = models.CharField(max_length=255)
    chapter = models.ForeignKey(ChapterName, on_delete=models.CASCADE, related_name='topics', null=True, blank=True)

    def __str__(self):
        # Handle cases where chapter or part might be None
        chapter_name = self.chapter.name if self.chapter else "No Chapter"
        part_name = self.chapter.part.name if self.chapter and self.chapter.part else "No Part"
        return f"{self.name} ({chapter_name} - {part_name})"



# Question Bank Model that store the all type of question data
class QuestionBank(models.Model):
    QUESTION_TYPES = (
        ('simple_type', 'Simple Type'),
        ('r_and_a_type', 'R & A Type'),
        ('list_type_1', 'List Type 1'),
        ('list_type_2', 'List Type 2'),
        ('true_and_false_type', 'True & False'),
        ('fill_in_the_blank_type', 'Fill in the Blank'),
    )
    # Question Information Fields 
    type_of_question = models.CharField(max_length=100, default='mcq1')
    
    # Change CharField to ManyToManyField to allow multiple selections
    exam_name = models.ManyToManyField('ExamName', related_name='questions')
    subject_name = models.ManyToManyField('Subject', related_name='questions')
    area_name = models.ManyToManyField('Area', related_name='questions')
    part_name = models.ManyToManyField('PartName', related_name='questions')
    chapter_name = models.ManyToManyField('ChapterName', related_name='questions', blank=True)
    topic_name = models.ManyToManyField('TopicName', related_name='questions', blank=True)

    exam_stage = models.CharField(max_length=100, blank=True, null=True)
    exam_year = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=100, default='', blank=True, null=True)
    script = models.TextField(blank=True, null=True)
    evergreen_index = models.PositiveIntegerField(default=5, null=True, blank=True)  # New Evergreen Index field
    marks = models.FloatField(default=0.0)
    negative_marks = models.FloatField(default=0.0)
    degree_of_difficulty = models.CharField(max_length=100)
    question_sub_type = models.CharField(max_length=100, choices=QUESTION_TYPES, default='simple_type')

    # Question fields 
    question_number = models.PositiveIntegerField(unique=True, blank=True, null=True)
    question_part = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    assertion = models.TextField(blank=True, null=True)
    question_part_first = models.TextField(blank=True, null=True)  # if r_and_a, list 1 and list 2 is present then Add this part in place of question part and not added question part in this question

    list_1_name = models.CharField(max_length=100, blank=True, null=True)
    list_2_name = models.CharField(max_length=100, blank=True, null=True)

    list_1_row1 = models.CharField(max_length=255, blank=True, null=True)
    list_1_row2 = models.CharField(max_length=255, blank=True, null=True)
    list_1_row3 = models.CharField(max_length=255, blank=True, null=True)
    list_1_row4 = models.CharField(max_length=255, blank=True, null=True)
    list_1_row5 = models.CharField(max_length=255, blank=True, null=True)
    list_1_row6 = models.CharField(max_length=255, blank=True, null=True)
    list_1_row7 = models.CharField(max_length=255, blank=True, null=True)
    list_1_row8 = models.CharField(max_length=255, blank=True, null=True)

    list_2_row1 = models.CharField(max_length=255, blank=True, null=True)
    list_2_row2 = models.CharField(max_length=255, blank=True, null=True)
    list_2_row3 = models.CharField(max_length=255, blank=True, null=True)
    list_2_row4 = models.CharField(max_length=255, blank=True, null=True)
    list_2_row5 = models.CharField(max_length=255, blank=True, null=True)
    list_2_row6 = models.CharField(max_length=255, blank=True, null=True)
    list_2_row7 = models.CharField(max_length=255, blank=True, null=True)
    list_2_row8 = models.CharField(max_length=255, blank=True, null=True)

    question_part_third = models.TextField(blank=True, null=True)

    # Objective Fields
    answer_option_a = models.TextField(blank=True, null=True)
    answer_option_b = models.TextField(blank=True, null=True)
    answer_option_c = models.TextField(blank=True, null=True)
    answer_option_d = models.TextField(blank=True, null=True)

    # Correct Answer Fields 
    correct_answer_choice = models.CharField(max_length=255, blank=True, null=True)
    correct_answer_description = models.TextField(blank=True, null=True)

    # Extra Information Field
    image = models.ImageField(upload_to='Question Images', blank=True, null=True)

    # Table Data Fields
    table_head_a = models.CharField(max_length=100, null=True, blank=True)
    table_head_b = models.CharField(max_length=100, null=True, blank=True)
    table_head_c = models.CharField(max_length=100, null=True, blank=True)
    table_head_d = models.CharField(max_length=100, null=True, blank=True)
    
    head_a_data1 = models.CharField(max_length=100, null=True, blank=True)
    head_a_data2 = models.CharField(max_length=100, null=True, blank=True)
    head_a_data3 = models.CharField(max_length=100, null=True, blank=True)
    head_a_data4 = models.CharField(max_length=100, null=True, blank=True)
    head_b_data1 = models.CharField(max_length=100, null=True, blank=True)
    head_b_data2 = models.CharField(max_length=100, null=True, blank=True)
    head_b_data3 = models.CharField(max_length=100, null=True, blank=True)
    head_b_data4 = models.CharField(max_length=100, null=True, blank=True)
    head_c_data1 = models.CharField(max_length=100, null=True, blank=True)
    head_c_data2 = models.CharField(max_length=100, null=True, blank=True)
    head_c_data3 = models.CharField(max_length=100, null=True, blank=True)
    head_c_data4 = models.CharField(max_length=100, null=True, blank=True)
    head_d_data1 = models.CharField(max_length=100, null=True, blank=True)
    head_d_data2 = models.CharField(max_length=100, null=True, blank=True)
    head_d_data3 = models.CharField(max_length=100, null=True, blank=True)
    head_d_data4 = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.question_number is None:
            last_question = QuestionBank.objects.all().order_by('question_number').last()
            if last_question and last_question.question_number:
                self.question_number = int(last_question.question_number) + 1
            else:
                self.question_number = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Question {self.question_number} - {self.exam_name} {self.exam_year}"

# Input Suggestion Model
class InputSuggestion(models.Model):
    language = models.CharField(max_length=100, default='', blank=True, null=True)
    script = models.TextField(blank=True, null=True)
    evergreen_index = models.PositiveIntegerField(default=5, null=True, blank=True)
    brief_description = models.TextField()
    details = models.TextField()  # TinyMCE will handle this as rich text
    question_video = models.FileField(upload_to='input_suggestion/videos/', blank=True, null=True)
    question_link = models.URLField(max_length=255, blank=True, null=True)
    other_text = models.TextField(blank=True, null=True)

    # Many-to-Many relationships with unique related names
    exam_name = models.ManyToManyField('ExamName', related_name='input_suggestions')
    subject_name = models.ManyToManyField('Subject', related_name='input_suggestions')
    area_name = models.ManyToManyField('Area', related_name='input_suggestions')
    part_name = models.ManyToManyField('PartName', related_name='input_suggestions')
    chapter_name = models.ManyToManyField('ChapterName', related_name='input_suggestions', blank=True)
    topic_name = models.ManyToManyField('TopicName', related_name='input_suggestions', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.brief_description[:50]

    def get_absolute_url(self):
        return reverse('view-input-suggestion', args=[str(self.id)])
    

class InputSuggestionImage(models.Model):
    question = models.ForeignKey(InputSuggestion, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='input_suggestion/images/')


class InputSuggestionDocument(models.Model):
    question = models.ForeignKey(InputSuggestion, related_name='documents', on_delete=models.CASCADE)
    document = models.FileField(upload_to='input_suggestion/documents/')


class QuoteIdiomPhrase(models.Model):
    TYPE_CHOICES = (
        ('quote', 'Quote'),
        ('idiom', 'Idiom'),
        ('phrase', 'Phrase'),
    )

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('staff_approved', 'Staff Approved'),
        ('admin_approved', 'Admin Approved'),
        ('rejected', 'Rejected'),
    )

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    content = models.TextField()
    meaning = models.TextField(blank=True, null=True)  # Meaning for idioms and phrases
    author = models.CharField(max_length=255, blank=True, null=True)  # Optional field for author or source
    exams = models.ManyToManyField('ExamName', blank=True)
    subjects = models.ManyToManyField('Subject', blank=True)
    areas = models.ManyToManyField('Area', blank=True)
    parts = models.ManyToManyField('PartName', blank=True)
    chapters = models.ManyToManyField('ChapterName', blank=True)
    topics = models.ManyToManyField('TopicName', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use the custom user model defined in settings
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    staff_approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='staff_approved_quotes', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    admin_approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='admin_approved_quotes', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    rejected_reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_type_display()}: {self.content[:50]}..."



class Report(models.Model):
    REPORT_TYPE_CHOICES = (
        ('this_week', 'This Week Report'),
        ('earlier', 'Earlier Report'),
    )
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)
    report_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_questions = models.IntegerField(default=0)
    total_phrases = models.IntegerField(default=0)
    total_suggestions = models.IntegerField(default=0)
    simple_type_count = models.IntegerField(default=0)
    list_1_type_count = models.IntegerField(default=0)
    list_2_type_count = models.IntegerField(default=0)
    ra_type_count = models.IntegerField(default=0)
    true_false_type_count = models.IntegerField(default=0)
    fill_blank_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.get_report_type_display()} - {self.report_date}"

