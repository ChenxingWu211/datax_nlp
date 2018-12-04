from django import forms

ouput_choices = (
    ('title', 'Title'),
    ('author', 'Author'),
    ('link', 'Link'),
    ('article_type', 'Article Type'),
    ('study_design', 'Study Design'),
    ('result_sum', 'Result Summarization')
)

class table_query(forms.Form):
    choose_features = forms.MultipleChoiceField(
        required = False,
        widget = forms.CheckboxSelectMultiple,
        choices = ouput_choices,
    )
    paper_index = forms.CharField(label='paper_index')
    #end_time = forms.CharField(label='End time')
    #img_chosen = forms.CharField()
    #interval = forms.IntegerField(widget=NumberInput(attrs={'type': 'range', 'min': '0', 'max': '60', 'step':'1'}))

