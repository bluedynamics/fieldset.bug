# -*- coding: utf-8 -*-
from plone.app.dexterity import PloneMessageFactory as _PMF
from plone.app.dexterity.behaviors.metadata import IPublication
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from z3c.form.interfaces import IEditForm, IAddForm
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IFieldsetBugBehavior(IPublication):
    """
    """

    # dates fieldset
    model.fieldset(
        'dates',
        label=_PMF(u'label_schema_dates', default=u'Dates'),
        fields=['mytextline'],
    )

    mytextline = schema.TextLine(
        title=(u"mytextline"),
        description=(u""),
        required=False
    )


    # form.omitted('effective', 'expires')
    # form.no_omit(IEditForm, 'effective', 'expires')
    # form.no_omit(IAddForm, 'effective', 'expires')
