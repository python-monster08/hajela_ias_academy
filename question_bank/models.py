from django.db import models

class ExamName(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=255)
    exam = models.ForeignKey(ExamName, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return f"{self.name} ({self.exam.name})"


class Area(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='areas')

    def __str__(self):
        return f"{self.name} ({self.subject.name})"


class PartName(models.Model):
    name = models.CharField(max_length=255)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='parts')

    def __str__(self):
        return f"{self.name} ({self.area.name})"
    

class TopicName(models.Model):
    name = models.CharField(max_length=255)
    part = models.ForeignKey(PartName, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return f"{self.name} ({self.part.name})"


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
    exam_name = models.CharField(max_length=100)
    exam_stage = models.CharField(max_length=100, blank=True, null=True)
    exam_year = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=100, default='', blank=True, null=True)
    script = models.TextField(blank=True, null=True)
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
    correct_answer_choice = models.CharField(max_length=1, blank=True, null=True)
    correct_answer_description = models.TextField(blank=True, null=True)

    # Extra Information Field
    image = models.ImageField(upload_to='Question Images', blank=True, null=True)
    subject_name = models.CharField(max_length=100)
    area_name = models.CharField(max_length=100)
    part_name = models.CharField(max_length=100)
    topic_name = models.CharField(max_length=255, null=True, blank=True)
    
    # New fields based on the table headings in the image
    # Table Header Fields
    table_head_a = models.CharField(max_length=100, null=True, blank=True)
    table_head_b = models.CharField(max_length=100, null=True, blank=True)
    table_head_c = models.CharField(max_length=100, null=True, blank=True)
    table_head_d = models.CharField(max_length=100, null=True, blank=True)
    
    # Table Data Fields
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



class DescriptiveTypeQuestion(models.Model):
    question_statement = models.TextField()
    question_images = models.FileField(upload_to='descriptive_questions/images/', blank=True, null=True)
    question_documents = models.FileField(upload_to='descriptive_questions/documents/', blank=True, null=True)
    question_video = models.FileField(upload_to='descriptive_questions/videos/', blank=True, null=True)
    question_link = models.URLField(blank=True, null=True)
    other_text = models.TextField(blank=True, null=True)
    exam_name = models.CharField(max_length=255)
    subject_name = models.CharField(max_length=255)
    area_name = models.CharField(max_length=255)
    part_name = models.CharField(max_length=255, blank=True, null=True)
    topic_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_statement[:50]


class QuestionImage(models.Model):
    question = models.ForeignKey(DescriptiveTypeQuestion, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='QuestionImage/images/')

class QuestionDocument(models.Model):
    question = models.ForeignKey(DescriptiveTypeQuestion, related_name='documents', on_delete=models.CASCADE)
    document = models.FileField(upload_to='QuestionImage/documents/')