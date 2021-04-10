from PySide2 import QtGui

from resources import url_flag_eng


class English:
    message_save_successful = 'Successfully saved.'
    message_save_question = 'Do you want to leave without saving?'
    message_save_panel_need_error_required = '''The following fields are required:
        - Total power
        - Price
        - Power of the panel
        - Quoting'''
    message_save_panel_quotation_error_required = '''The following fields are required:
        - Name of the company
        - Total power
        - Price
        - Power of the panel
        - Quoting'''
    message_save_error = 'Could not save.'
    message_save_error_required_name = 'The name is required.'
    message_save_error_not_null = '{} can not be empty.'
    message_save_error_not_unique = '{} can not be repeated.'
    message_save_error_company_name_not_unique = 'There is already a company with that name.'
    message_save_error_company_web_not_unique = 'There is already a company with that web.'
    message_save_error_employee_not_unique = 'This employee already exists.'
    message_save_error_need_not_unique = 'This need already exists.'
    message_save_error_quotation_not_unique = 'This quotation already exists.'
    message_add_new_certificate = 'current new certificate will be added to the database.'
    message_enter_a_name = 'Enter a name.'
    message_enter_no_existent_name = 'Enter a name that is not in the list.'
    message_enter_valid_name = 'Enter a valid name.'
    message_delete_confirmation = 'Do you want to delete all the selected ones?'
    message_delete_company_confirmation = '''Do you also want to eliminate all quotations related to the following companies?:
        {}'''

    title_sn = 'Qt app example'
    title_needs = 'Needs'
    title_quotations = 'Quotations'
    title_panel_need = 'Panel need'
    title_panel_quotation = 'Panel quote'
    title_save = 'Save'
    title_error = 'Error'
    title_back = 'Back'
    title_add_new = 'Add new'
    title_add_certificate = 'Add certificate'
    title_empty_name = 'Empty name'
    title_existent = 'Repeated'
    title_invalid = 'Invalid'
    title_database = 'Database'
    title_chart = 'Quotation prices average'

    label_found = 'Found'
    label_total = 'Total'
    label_company = 'Company'
    label_mark = 'Mark'
    label_total_power = 'Total power'
    label_price = 'Price'
    label_date_quotation = 'Quotation date'
    label_date_validity = 'Validity date'
    label_user = 'Quoting'
    label_n_contacts = 'Nº of contacts'
    label_observations = 'Observations'
    label_type = 'Type'
    label_panel_types = 'Panel types'
    label_inverter_types = 'Inverter types'
    label_battery_types = 'Battery types'
    label_structure_types = 'Structure types'
    label_bos_types = 'BOS types'
    label_cells = 'Nº of cells'
    label_panel_power = 'Power'
    label_efficiency = 'Efficiency'
    label_warranty_product = 'Product warranty'
    label_warranty_performance = 'Performance warranty'
    label_certificates = 'Certificates'
    label_incoterm = 'Incoterm'
    label_made_in = 'Made in'
    label_origin = 'Origin'
    label_destination = 'Destination'
    label_current = 'Current'
    label_all_average = label_total
    label_current_type_average = label_type
    label_current_power_average = 'Power'
    label_priority = 'Prio'
    label_name = 'Name'
    label_comments = 'Comments'
    label_source = 'Source'
    label_loader = 'Loader'
    label_date_loading = 'Loading date'
    label_country = 'Country'
    label_province = 'Province'
    label_geo_zone = 'Geographical zone'
    label_address = 'Address'
    label_email = 'Email'
    label_phone = 'Phone'
    label_web = 'Web'
    label_id_document = 'ID document'
    label_date_verification = 'Verification date'
    label_verification_user = 'Verification user'
    label_tier = 'Tier'
    label_formation_year = 'Formation year'
    label_annual_capacity = 'Annual capacity'
    label_scope_range = 'Scope range'
    label_reply_ratio = 'Reply ratio'
    label_n_replies = 'Nº of replies'
    label_solar_systems = 'Solar systems'
    label_assessment_services = 'Assessment'
    label_project_dev_services = 'Project development'
    label_system_design_services = 'System design'
    label_install_construct_services = 'Install and construction'
    label_oper_main_services = 'Operation and maintenance'
    label_insurance_services = 'Insurance'
    label_financial_services = 'Financial'
    label_logistic_services = 'Logistic'
    label_extra_services = 'Extra'
    label_position = 'Position'
    label_projects_type = 'Projects type'
    label_linkedin = 'Linkedin'
    label_language = 'Language'
    label_general = 'General'
    label_companies = 'Companies'
    label_panels = 'Panels'
    label_bos = 'BOS'
    label_inverters = 'Inverters'
    label_structures = 'Structures'
    label_services = 'Services'
    label_others = 'Others'

    button_accept = 'OK'
    button_cancel = 'Cancel'
    button_add_panel_n = 'New panel need'
    button_add_inverter_n = 'New inverter need'
    button_add_batteries_n = 'New battery need'
    button_add_structure_n = 'New structure need'
    button_add_bos_n = 'New BOS need'
    button_add_panel_q = 'New panel q.'
    button_add_inverter_q = 'New inverter q.'
    button_add_batteries_q = 'New battery q.'
    button_add_structure_q = 'New structure q.'
    button_add_bos_q = 'New BOS q.'
    button_save = 'Save'
    button_new = 'Save new'
    button_overwrite = 'Overwrite'
    button_no_exit = "Don't exit"
    button_exit_and_save = 'Save and exit'
    button_exit_no_save = 'Exit without saving'
    button_certificates = 'Certificates'
    button_incoterms = 'Incoterms'
    button_marks = 'Marks'
    button_companies = 'Companies'
    button_company_tiers = 'Company tiers'
    button_company_types = 'Company types'
    button_staff = 'Staff'
    button_panel_types = 'Panel types'
    button_cells = 'Nº of cells'
    button_panel_needs = 'Panel needs'
    button_panel_quotations = 'Panel quotations'
    button_bos_types = 'BOS types'
    button_inverter_types = 'Inverter types'
    button_structure_types = 'Structure types'
    button_solar_systems = 'Solar systems'
    button_assessment_services = 'Assessment services'
    button_extra_services = 'Extra services'
    button_financial_services = 'Financial services'
    button_install_construct_services = 'Install and construction services'
    button_insurance_services = 'Insurance services'
    button_logistic_services = 'Logistic services'
    button_oper_main_services = 'Operation and maintenance services'
    button_project_dev_services = 'Project development services'
    button_system_design_services = 'Sytem design services'
    button_geo_zones = 'Geo zones'
    button_languages = 'Languages'
    button_places = 'Places'
    button_scope_ranges = 'Scope ranges'
    button_users = 'Users'

    check_priorities = 'Show priorities'

    radio_positive = 'Positive'
    radio_negative = 'Negative'
    radio_yes = 'Yes'
    radio_no = 'No'

    group_searcher = 'Searcher'
    group_panels = 'Panels'
    group_inverters = 'Inverters'
    group_batteries = 'Batteries'
    group_structures = 'Structures'
    group_bos = 'BOS'
    group_general = 'General parameters'
    group_panel = 'Panel parameters'
    group_geographical = 'Geographical parameters'
    group_tolerance = 'Tolerance'
    group_related_panel_quotations = 'Related panel quotations'
    group_sn_verification = 'SN verification'
    group_rel_with_this_company = 'Relationship with this company'
    group_signed_document = 'Signed document'
    group_products = 'Products'
    group_systems_apps = 'Systems and apps'
    group_solar_components = 'Solar components'
    group_services = 'Services'
    group_consulting_services = 'Consulting'
    group_building_operating_services = 'Building and operating'
    group_auxiliary_services = 'Auxiliaries'
    group_staff = 'Staff'

    action_delete = 'Delete'
    action_copy_row = 'Copy row'
    action_copy_rows = 'Copy rows'
    action_copy_column = 'Copy column'
    action_copy_current_price = 'Copy current price'
    action_copy_all_average = 'Copy average prices of all'
    action_copy_current_type_average = 'Copy average of prices of current type'
    action_copy_current_power_average = 'Copy average of prices of current power'
    action_copy_all = 'Copy all'
    action_save_image = 'Save image'

    suffix_year = 'year'
    suffix_years = 'years'

    icon_language = QtGui.QIcon(url_flag_eng)

    chart = 'chart'

    @staticmethod
    def title_employee(company_name):
        if company_name:
            text = f'{company_name} employee'
        else:
            text = 'Employee'
        return text
