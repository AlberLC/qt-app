from PySide2 import QtGui

from resources import url_flag_spa


class Spanish:
    message_save_successful = 'Guardado con éxito.'
    message_save_question = '¿Quieres salir sin guardar?'
    message_save_panel_need_error_required = '''Los siguientes campos son obligatorios:
        - Potencia total
        - Precio 
        - Potencia del panel
        - Cotizador'''
    message_save_panel_quotation_error_required = '''Los siguientes campos son obligatorios:
        - Nombre de la compañía
        - Potencia total
        - Precio 
        - Potencia del panel
        - Cotizador'''
    message_save_error = 'No se pudo guardar.'
    message_save_error_required_name = 'El nombre es obligatorio.'
    message_save_error_not_null = '{} no puede estar vacío.'
    message_save_error_not_unique = '{} no puede estar repetido.'
    message_save_error_company_name_not_unique = 'Ya existe una compañía con ese nombre.'
    message_save_error_company_web_not_unique = 'Ya existe una compañía con esa web.'
    message_save_error_employee_not_unique = 'Ya existe este empleado.'
    message_save_error_need_not_unique = 'Ya existe esta necesidad.'
    message_save_error_quotation_not_unique = 'Ya existe esta cotización.'
    message_add_new_certificate = 'Se añadirá este nuevo certificado a la base de datos.'
    message_enter_a_name = 'Introduce un nombre.'
    message_enter_no_existent_name = 'Introduce un nombre que no esté en la lista.'
    message_enter_valid_name = 'Introduce un nombre válido.'
    message_delete_confirmation = '¿Quieres eliminar todas las seleccionadas?'
    message_delete_company_confirmation = '''¿Quieres eliminar también todas las cotizaciones relacionadas con las siguientes compañías?:
        {}'''

    title_sn = 'Qt app example'
    title_needs = 'Necesidades'
    title_quotations = 'Cotizaciones'
    title_panel_need = 'Necesidad de panel'
    title_panel_quotation = 'Cotización de panel'
    title_save = 'Guardar'
    title_error = 'Error'
    title_back = 'Atrás'
    title_add_new = 'Añadir nuevo'
    title_add_certificate = 'Añadir certificado'
    title_empty_name = 'Nombre en blanco'
    title_existent = 'Repetido'
    title_invalid = 'Inválido'
    title_database = 'Base de datos'
    title_chart = 'Media de precios de cotizaciones'

    label_found = 'Encontrados'
    label_total = 'Total'
    label_company = 'Compañía'
    label_mark = 'Marca'
    label_total_power = 'Potencia total'
    label_price = 'Precio'
    label_date_quotation = 'Fecha de cotización'
    label_date_validity = 'Fecha de validez'
    label_user = 'Cotizador'
    label_n_contacts = 'Nº de contactos'
    label_observations = 'Observaciones'
    label_type = 'Tipo'
    label_panel_types = 'Tipos de panel'
    label_inverter_types = 'Tipos de inversor'
    label_battery_types = 'Tipos de batería'
    label_structure_types = 'Tipos de estructura'
    label_bos_types = 'Tipos de BOS'
    label_cells = 'Nº de celdas'
    label_panel_power = 'Potencia'
    label_efficiency = 'Eficiencia'
    label_warranty_product = 'Garantía de producto'
    label_warranty_performance = 'Garantía de rendimiento'
    label_certificates = 'Certificados'
    label_incoterm = 'Incoterm'
    label_made_in = 'Fabricado en'
    label_origin = 'Origen'
    label_destination = 'Destino'
    label_current = 'Actual'
    label_all_average = 'Total'
    label_current_type_average = label_type
    label_current_power_average = 'Potencia'
    label_priority = 'Prio'
    label_name = 'Nombre'
    label_comments = 'Comentarios'
    label_source = 'Fuente'
    label_loader = 'Usuario cargador'
    label_date_loading = 'Fecha de carga'
    label_country = 'País'
    label_province = 'Provincia'
    label_geo_zone = 'Zona geográfica'
    label_address = 'Dirección'
    label_email = 'Email'
    label_phone = 'Teléfono'
    label_web = 'Web'
    label_id_document = 'Documento ID'
    label_date_verification = 'Fecha de verifiación'
    label_verification_user = 'Usuario verificador'
    label_tier = 'Nivel'
    label_formation_year = 'Año de formación'
    label_annual_capacity = 'Capacidad anual'
    label_scope_range = 'Rango de alcance'
    label_reply_ratio = 'Ratio de respuestas'
    label_n_replies = 'Nº de respuestas'
    label_solar_systems = 'Sistemas solares'
    label_assessment_services = 'Evaluación'
    label_project_dev_services = 'Desarrollo de proyectos'
    label_system_design_services = 'Diseño de sistemas'
    label_install_construct_services = 'Instalación y construcción'
    label_oper_main_services = 'Operación y mantenimiento'
    label_insurance_services = 'Seguros'
    label_financial_services = 'Financieros'
    label_logistic_services = 'Logistica'
    label_extra_services = 'Extra'
    label_position = 'Cargo'
    label_projects_type = 'Tipo de proyectos'
    label_linkedin = 'Linkedin'
    label_language = 'Idioma'
    label_general = 'General'
    label_companies = 'Compañías'
    label_panels = 'Paneles'
    label_bos = 'BOS'
    label_inverters = 'Inversores'
    label_structures = 'Estructuras'
    label_services = 'Servicios'
    label_others = 'Otros'

    button_accept = 'Aceptar'
    button_cancel = 'Cancelar'
    button_add_panel_n = 'Nueva n. de panel'
    button_add_inverter_n = 'Nueva n. de inversor'
    button_add_batteries_n = 'Nueva n. de batería'
    button_add_structure_n = 'Nueva n. de estructura'
    button_add_bos_n = 'Nueva n. de BOS'
    button_add_panel_q = 'Nueva c. de panel'
    button_add_inverter_q = 'Nueva c. de inversor'
    button_add_batteries_q = 'Nueva c. de batería'
    button_add_structure_q = 'Nueva c. de estructura'
    button_add_bos_q = 'Nueva c. de BOS'
    button_save = 'Guardar'
    button_new = 'Guardar nueva'
    button_overwrite = 'Sobrescribir'
    button_no_exit = 'No salir'
    button_exit_and_save = 'Guardar y salir'
    button_exit_no_save = 'Salir sin guardar'
    button_certificates = 'Certificados'
    button_incoterms = 'Incoterms'
    button_marks = 'Marcas'
    button_companies = 'Compañías'
    button_company_tiers = 'Niveles de compañía'
    button_company_types = 'Tipos de compañía'
    button_staff = 'Personal'
    button_panel_types = 'Tipos de panel'
    button_cells = 'Nº de Celdas'
    button_panel_needs = 'Necesidades de panel'
    button_panel_quotations = 'Cotizaciones de panel'
    button_bos_types = 'Tipos de BOS'
    button_inverter_types = 'Tipos de inversor'
    button_structure_types = 'Tipos de estructura'
    button_solar_systems = 'Sistemas solares'
    button_assessment_services = 'Servicios de evaluación'
    button_extra_services = 'Servicios extra'
    button_financial_services = 'Servicios financieros'
    button_install_construct_services = 'Servicios de instalación y construcción'
    button_insurance_services = 'Servicios de seguros'
    button_logistic_services = 'Servicios de logística'
    button_oper_main_services = 'Servicios de operación y mantenimiento'
    button_project_dev_services = 'Servicios de desarrollo de proyectos'
    button_system_design_services = 'Servicios  de diseño de sistemas'
    button_geo_zones = 'Zonas geográficas'
    button_languages = 'Idiomas'
    button_places = 'Lugares'
    button_scope_ranges = 'Rangos de alcance'
    button_users = 'Usuarios'

    check_priorities = 'Mostrar prioridades'

    radio_positive = 'Positiva'
    radio_negative = 'Negativa'
    radio_yes = 'Sí'
    radio_no = 'No'

    group_searcher = 'Buscador'
    group_panels = 'Paneles'
    group_inverters = 'Inversores'
    group_batteries = 'Baterías'
    group_structures = 'Estructuras'
    group_bos = 'BOS'
    group_general = 'Parámetros generales'
    group_panel = 'Parámetros de panel'
    group_geographical = 'Parámetros geográficos'
    group_tolerance = 'Tolerancia'
    group_related_panel_quotations = 'Cotizaciones de paneles relacionadas'
    group_sn_verification = 'Verificación SN'
    group_rel_with_this_company = 'Relación con esta empresa'
    group_signed_document = 'Documento firmado'
    group_products = 'Productos'
    group_systems_apps = 'Sistemas y aplicaciones'
    group_solar_components = 'Componentes solares'
    group_services = 'Servicios'
    group_consulting_services = 'Consultoría'
    group_building_operating_services = 'Construcción y explotación'
    group_auxiliary_services = 'Auxiliares'
    group_staff = 'Personal'

    action_delete = 'Eliminar'
    action_copy_row = 'Copiar fila'
    action_copy_rows = 'Copiar filas'
    action_copy_column = 'Copiar columna'
    action_copy_current_price = 'Copiar precio actual'
    action_copy_all_average = 'Copiar media de precios de todas'
    action_copy_current_type_average = 'Copiar media de precios de este tipo'
    action_copy_current_power_average = 'Copiar media de precios de esta potencia'
    action_copy_all = 'Copiar todo'
    action_save_image = 'Guardar imagen'

    suffix_year = 'año'
    suffix_years = 'años'

    icon_language = QtGui.QIcon(url_flag_spa)

    chart = 'gráfico'

    @staticmethod
    def title_employee(company_name):
        if company_name:
            text = f'Empleado de {company_name}'
        else:
            text = 'Empleado'
        return text
