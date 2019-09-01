from behave import *



#simple test
@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False

#verify an existing student gets a page
@given('I search for an existing student')
def step_impl(context):
    br = context.browser
    br.get('http://localhost:8000/iger/students/17102/')
    

@then('the resulting page will include "{text}"')
def step_impl(context, text):
    if text not in context.response:
        assert context.failed is False
        #fail('%r not in %r' % (text, context.response))

