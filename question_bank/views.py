from django.shortcuts import render, redirect
from django.contrib import messages
from .models import QuestionBank

def add_question(request):
    if request.method == 'POST':
        # Extract common fields
        type_of_question = request.POST.get('questionType', '')
        question_part_first = request.POST.get('question_part_first', '')
        correct_answer_choice = request.POST.get('correct_answer_choice', '')
        correct_answer_description = request.POST.get('correct_answer_description', '')
        exam_name = request.POST.get('exam_name', '')
        exam_year = request.POST.get('exam_year', None)
        marks = request.POST.get('marks', 0.0)
        negative_marks = request.POST.get('negative_marks', 0.0)
        degree_of_difficulty = request.POST.get('degree_of_difficulty', '')
        subject_name = request.POST.get('subject_name', '')
        area_name = request.POST.get('area_name', '')
        part_name = request.POST.get('part_name', '')

        # Initialize the QuestionBank object
        question = QuestionBank(
            type_of_question=type_of_question,
            question_part_first=question_part_first,
            correct_answer_choice=correct_answer_choice,
            correct_answer_description=correct_answer_description,
            exam_name=exam_name,
            exam_year=exam_year if exam_year else None,
            marks=float(marks),
            negative_marks=float(negative_marks),
            degree_of_difficulty=degree_of_difficulty,
            subject_name=subject_name,
            area_name=area_name,
            part_name=part_name,
        )

        # Process question type specific fields
        if type_of_question == 'simple_type':
            question.answer_option_a = request.POST.get('answer_option_a', '')
            question.answer_option_b = request.POST.get('answer_option_b', '')
            question.answer_option_c = request.POST.get('answer_option_c', '')
            question.answer_option_d = request.POST.get('answer_option_d', '')

        elif type_of_question == 'r_and_a_type':
            question.reason = request.POST.get('reason', '')
            question.assertion = request.POST.get('assertion', '')
            question.question_part_third = request.POST.get('question_part_third', '')

        elif type_of_question == 'list_type_1':
            question.list_1_row1 = request.POST.get('list_1_row1', '')
            question.list_1_row2 = request.POST.get('list_1_row2', '')
            question.list_1_row3 = request.POST.get('list_1_row3', '')
            question.list_1_row4 = request.POST.get('list_1_row4', '')
            question.list_1_row5 = request.POST.get('list_1_row5', '')
            question.list_1_row6 = request.POST.get('list_1_row6', '')
            question.list_1_row7 = request.POST.get('list_1_row7', '')
            question.list_1_row8 = request.POST.get('list_1_row8', '')
            question.question_part_third = request.POST.get('question_part_third', '')

        elif type_of_question == 'list_type_2':
            question.list_1_name = request.POST.get('list_1_name', '')
            question.list_2_name = request.POST.get('list_2_name', '')
            question.list_1_row1 = request.POST.get('list_1_row1', '')
            question.list_2_row1 = request.POST.get('list_2_row1', '')
            question.list_1_row2 = request.POST.get('list_1_row2', '')
            question.list_2_row2 = request.POST.get('list_2_row2', '')
            question.list_1_row3 = request.POST.get('list_1_row3', '')
            question.list_2_row3 = request.POST.get('list_2_row3', '')
            question.list_1_row4 = request.POST.get('list_1_row4', '')
            question.list_2_row4 = request.POST.get('list_2_row4', '')
            question.list_1_row5 = request.POST.get('list_1_row5', '')
            question.list_2_row5 = request.POST.get('list_2_row5', '')
            question.question_part_third = request.POST.get('question_part_third', '')

        # Save the question to the database
        question.save()

        messages.success(request, 'Question has been added successfully!')
        return redirect('add-question')  # Redirect back to the form

    return render(request, 'question_bank/add-question.html')
