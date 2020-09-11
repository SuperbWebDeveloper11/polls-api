
# create Poll instances using PollSerializer class 

>>> from polls.models import Poll, Choice, Vote
>>> from polls.serializers import PollSerializer

>>> serializer = PollSerializer(data={'question' 'what does it meen rolling in the deep' 'created_b' 1})

>>> serializer.is_valid()
False

>>> serializer.errors
{'created_by' [ErrorDetail(string='This field is required.' code='required')]}

>>> serializer = PollSerializer(data={'question' 'what does it meen rolling in the deep' 'created_by' 1})

>>> poll_instance = serializer.save()
Traceback (most recent call last):
    File "<console>" line 1, in <module>
File "/home/moona/Desktop/workspace/polls-env/lib/python3.6/site-packages/rest_framework/serializers.py" line 178, in save
'You must call `.is_valid()` before calling `.save()`.'
AssertionError: You must call `.is_valid()` before calling `.save()`.

>>> serializer.is_valid()
True

>>> poll_instance = serializer.save()
>>> poll_instance.pk
4

>>> poll_instance
<Poll: what does it meen rolling in the deep>

>>> serializer.data
{
    'id' 4, 
    'choices' [], 
    'question': 'what does it meen rolling in the deep',
    'pub_date': '2020-09-09T20:42:25.682429Z',
    'created_by' 1
} 
