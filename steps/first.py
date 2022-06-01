import time

from behave import *

use_step_matcher("re")


@given("user opens the homepage")
def user_opens_the_home_page(context):
    context.browser.visit('learning.elucidat.com/course/5c9126fd760e5-611a53751213a')
    time.sleep(3)


@step("user navigates to the vote page")
def user_navigates_to_the_vote_page(context):
    context.browser.find_by_id("pa_5c9126fe3b767_p15577f075e9-button__text").click()
    context.browser.find_by_id("pa_5c9126fe3f4fb_p179d7b273e1-caption__text-1").click()
    context.browser.find_by_id("pa_5c9126fe434ba_p15564daa856-button__text").click()


@step("user clicks the vote button")
def user_clicks_the_vote_button(context):
    context.browser.find_by_xpath("//a[@id='pa_5c9126fe47260_p15515116385-save_button']/i").click()


@when('user selects the "(?P<verdict>.+)" radio button')
def step_impl(context, verdict):
    context.browser.find_by_id("pa_5c9126fe47260_p15515116385-itemInner-1").click()


@then('user sees the "(?P<verdict_confirmation>.+)" modal pop up')
def step_impl(context, verdict_confirmation):
    # context.browser.find_by_xpath(
    #     "(.//*[normalize-space(text()) and normalize-space(.)='NOT GUILTY!'])[1]/following::h2[1]")
    pass


@step("user navigates to the next page")
def step_impl(context):
    pass


@when("user clicks the back arrow on the browser")
def step_impl(context):
    pass


@then("user sees the home page")
def step_impl(context):
    pass
