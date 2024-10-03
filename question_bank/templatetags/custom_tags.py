

from django import template

register = template.Library()

@register.filter
def to_range(value):
    return range(1, int(value) + 1)



@register.filter
def get_user_data(data_list, email):
    """
    Custom template filter to return data (idioms or input suggestions) for a specific user.
    """
    for data in data_list:
        if data['created_by__email'] == email:
            # Return the idioms or suggestions count based on available data
            return data.get('total_idioms') or data.get('total_suggestions', 0)
    return 0