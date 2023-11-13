#from accounts import auth_views
from django.urls import re_path, include
from django.contrib.auth import views as auth_views

from userena import settings as userena_settings
import accounts.views as userena_views
from accounts.compat import auth_views_compat_quirks, password_reset_uid_kwarg


def merged_dict(dict_a, dict_b):
    """Merges two dicts and returns output. It's purpose is to ease use of
    ``auth_views_compat_quirks``
    """
    dict_a.update(dict_b)
    return dict_a


urlpatterns = [
    re_path(r'^getTelegram/$',
        userena_views.get_telegram,
        name='getTelegram'),
    re_path(r'^newDeposit/$',
        userena_views.new_deposit,
        name='newDeposit'),
    re_path(r'^getWallet/$',
        userena_views.get_wallet,
        name='getWallet'),
    re_path(r'^checkDeposits/$',
        userena_views.check_deposits,
        name='checkDeposits'),
    re_path(r'^getDeposits/$',
        userena_views.get_deposits,
        name='getDeposits'),
    re_path(r'^signup/$',
        userena_views.signupsample,
        name='userena_signup'),

    re_path(r'^settings/$',
        userena_views.settings,
        name='settings'),

    re_path(r'^signin/$',
        userena_views.signin,
        name='userena_signin'),
    # url(r'^landing', userena_views.landing, name='index'),
    # url(r'^signupsample', userena_views.signupsample, name='index'),
    # Signup, signin and signout
    # url(r'^signup/$',
    #     userena_views.signup,
    #     name='userena_signup'),
    # url(r'^signin/$',
    #     userena_views.signin,
    #     name='userena_signin'),
    re_path(r'^signout/$',
        userena_views.signout,
        name='userena_signout'),

    # Reset password
    re_path(
        r'^password/reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='userena/password_reset_form.html',
            email_template_name='userena/emails/password_reset_message.txt',
            extra_context={'without_usernames': userena_settings.USERENA_WITHOUT_USERNAMES},
        ),
        name='password_reset'
    ),
    re_path(
        r'^password/reset/done/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name='userena/password_reset_done.html',
        ),
        name='userena_password_reset_done'
    ),
    #re_path(
    #    r'^password/reset/confirm/(?P<%s>[0-9A-Za-z]+)-(?P<token>.+)/$' % password_reset_uid_kwarg,
    #    auth_views.PasswordResetConfirmView.as_view(
    #        template_name='userena/password_reset_confirm_form.html',
    #        **auth_views_compat_quirks.get('userena_password_reset_confirm', {}),
    #    ),
    #    name='userena_password_reset_confirm'
    #),

    re_path(
        r'^password/reset/confirm/complete/$',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='userena/password_reset_complete.html',
        ),
        name='userena_password_reset_complete'
    ),

    # Signup
    re_path(r'^(?P<username>[\@\.\w-]+)/signup/complete/$',
        userena_views.direct_to_user_template,
        {'template_name': 'userena/signup_complete.html',
         'extra_context': {'userena_activation_required': userena_settings.USERENA_ACTIVATION_REQUIRED,
                           'userena_activation_days': userena_settings.USERENA_ACTIVATION_DAYS}},
        name='userena_signup_complete'),

    # Activate
    re_path(r'^activate/(?P<activation_key>\w+)/$',
        userena_views.activate,
        name='userena_activate'),

    # Retry activation
    re_path(r'^activate/retry/(?P<activation_key>\w+)/$',
        userena_views.activate_retry,
        name='userena_activate_retry'),

    # Change email and confirm it
    re_path(r'^(?P<username>[\@\.\w-]+)/email/$',
        userena_views.email_change,
        name='userena_email_change'),
    re_path(r'^(?P<username>[\@\.\w-]+)/email/complete/$',
        userena_views.direct_to_user_template,
        {'template_name': 'userena/email_change_complete.html'},
        name='userena_email_change_complete'),
    re_path(r'^(?P<username>[\@\.\w-]+)/confirm-email/complete/$',
        userena_views.direct_to_user_template,
        {'template_name': 'userena/email_confirm_complete.html'},
        name='userena_email_confirm_complete'),
    re_path(r'^confirm-email/(?P<confirmation_key>\w+)/$',
        userena_views.email_confirm,
        name='userena_email_confirm'),

    # Disabled account
    re_path(r'^(?P<username>[\@\.\w-]+)/disabled/$',
        userena_views.disabled_account,
        {'template_name': 'userena/disabled.html'},
        name='userena_disabled'),

    # Change password
    re_path(r'^(?P<username>[\@\.\w-]+)/password/$',
        userena_views.password_change,
        name='userena_password_change'),
    re_path(r'^(?P<username>[\@\.\w-]+)/password/complete/$',
        userena_views.direct_to_user_template,
        {'template_name': 'userena/password_complete.html'},
        name='userena_password_change_complete'),

    # Edit profile
    re_path(r'^(?P<username>[\@\.\w-]+)/edit/$',
        userena_views.profile_edit,
        name='userena_profile_edit'),
    re_path(r'^status/',
        userena_views.account_status,
        name='accountStatus'),

    # View profiles
    re_path(r'^(?P<username>(?!(signout|signup|signin)/)[\@\.\w-]+)/$',
        userena_views.profile_detail,
        name='userena_profile_detail'),
    re_path(r'^page/(?P<page>[0-9]+)/$',
        userena_views.ProfileListView.as_view(),
        name='userena_profile_list_paginated'),
    re_path(r'^$',
        userena_views.ProfileListView.as_view(),
        name='userena_profile_list'),
]
