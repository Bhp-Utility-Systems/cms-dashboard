"""potlako_dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/"""
from edc_dashboard import UrlConfig

from .patterns import identifier
from .views import (
    ContractListBoardView, ConsultantListBoardView,
    ConsultantContractListBoardView, EmployeeListBoardView,
    EmpContractListBoardView, PiListBoardView, PiContractListBoardView)

app_name = 'cms_dashboard'

contract_listboard_url_config = UrlConfig(
    url_name='contract_listboard_url',
    view_class=ContractListBoardView,
    label='contract_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

empcontract_listboard_url_config = UrlConfig(
    url_name='emp_contract_listboard_url',
    view_class=EmpContractListBoardView,
    label='allcontracts_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

consultant_listboard_url_config = UrlConfig(
    url_name='consultant_listboard_url',
    view_class=ConsultantListBoardView,
    label='consultant_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

consultant_contract_listboard_url_config = UrlConfig(
    url_name='consultant_contract_listboard_url',
    view_class=ConsultantContractListBoardView,
    label='allcontracts_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

employee_dashboard_url_config = UrlConfig(
    url_name='employee_listboard_url',
    view_class=EmployeeListBoardView,
    label='employee_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

pi_dashboard_url_config = UrlConfig(
    url_name='pi_listboard_url',
    view_class=PiListBoardView,
    label='pi_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

pi_contract_dashboard_url_config = UrlConfig(
    url_name='pi_contract_listboard_url',
    view_class=PiContractListBoardView,
    label='allcontracts_listboard',
    identifier_label='identifier',
    identifier_pattern=identifier)

urlpatterns = []
urlpatterns += contract_listboard_url_config.listboard_urls
urlpatterns += consultant_contract_listboard_url_config.listboard_urls
urlpatterns += consultant_listboard_url_config.listboard_urls
urlpatterns += employee_dashboard_url_config.listboard_urls
urlpatterns += empcontract_listboard_url_config.listboard_urls
urlpatterns += pi_dashboard_url_config.listboard_urls
urlpatterns += pi_contract_dashboard_url_config.listboard_urls
