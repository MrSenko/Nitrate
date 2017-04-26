# -*- coding: utf-8 -*-
# FIXME: Use signal to handle log
from tcms.testplans.helpers import email


def on_plan_save(sender, instance, created=False, **kwargs):
    # email changes
    if not created:
        if instance.emailing.notify_on_plan_update:
            email.email_plan_update(instance)


def on_plan_delete(sender, instance, **kwargs):
    from tcms.testplans.models import TestPlanEmailSettings
    print "*************", TestPlanEmailSettings.objects.count()

    # email this deletion
    if instance.emailing.notify_on_plan_delete:
        email.email_plan_deletion(instance)


def pre_save_clean(sender, **kwargs):
    instance = kwargs['instance']
    instance.clean()
