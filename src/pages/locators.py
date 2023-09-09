#Константы
mkit_login = 'mkit'
mkit_pass = 'newpassword'
bo_login = 'backoffice-manager'
bo_pass = 'newpassword!'
#Локаторы мКит
#Экраны мКит
mkit_dashboard = 'a[href="/dashboard"]'
mkit_campaigns = 'a[href="/campaigns"]'
mkit_recipients = 'a[href="/recipients"]'
mkit_conversations = 'a[href="/conversations"]'
mkit_financial_documents = 'a[href="/financial-documents"]'
mkit_reports = 'a[href="/reports"]'
mkit_assets = 'a[href="/assets"]'
mkit_user_management = 'a[href="/user-management"]'
mkit_audit = 'a[href="/audit"]'
mkit_account = 'a[href="/account"]'
mkit_close = 'a[href="/"] img[src*="5ea4c9ff"]'
#Dashboard
mkit_dashboard_label = 'h2[class="dashboard__top__title"]' # Надпись в названии экрана

#Contacts
mkit_contact_page = '//div[@class="side-menu"]//a[@href="/recipients"]' #Экран "Контакты"
mkit_skip_all = '//button[@class="basic-button basic-button_accent"]' #Кнопка "Skip all"
mkit_contact_save_contact = '//div[@class="create-contact-form__buttons"]//button[@class="basic-button basic-button_accent basic-button_new-style"]' #Кнопка сохранения контакта
mkit_contact_save_attrib = '//div[@class="creating-attributes-form__buttons-wrapper"]//button[@class="basic-button basic-button_accent"]' #Кнопка сохранения атрибута
mkit_contact_atr_add_value = '//button[@class="basic-button basic-button_primary"]'
mkit_contact_atr_settings = '//div[@class="basic-field-array"]//input[@class="basic-field__input-wrapper__input"]'
mkit_contact_del_contact = '//div[@class="ag-pinned-right-cols-container"]//div[@aria-rowindex="2"]//div[@tabindex="-1"]//div[@class="ag-react-container"]//div[@class="buttons-cell-renderer"]//button[@class="icon-button"][2]'
#mkit_contact_del = '//div[@class="delete-warning-modal__buttons"]/div[@class="basic-button basic-button_warn"]'
mkit_contact_label = 'h1[class="recipients-layout__header"]' # Надпись в названии экрана
mkit_contact_newContact = 'div[class="basic-button__text"]' # Кнопка NewContact
mkit_delete_button = '//div[@class ="ag-react-container"]//div[@class ="buttons-cell-renderer"]//button[@class ="icon-button"][2]//img[@src="/static/media/trash.f857e5b5.svg"]' #
mkit_import_contact = '//div[@class="side-menu"]//a[@href="/recipients"]//a[@href="/recipients/import"]' # Экран импорт контактов //span[@class="menu-item__label"]
mkit_Optout_words = '//div[@class="side-menu"]//a[@href="/recipients"]//a[@href="/recipients/stop-words"]'
mkit_contact_page2 = '//div[@class="side-menu"]//a[@href="/recipients"]//span[@class="menu-item__label"]'
mkit_new_optout_words_button = '//button[@class="basic-button basic-button_accent"]'
mkit_select_channel = '//button[@class="mkit-dropdown-field__control"]'
mkit_contact_first_record = '//div[@class="ag-center-cols-clipper"]//div[@row-index="0"]'
mkit_contact_attribute_manager = '//div[@class="table__header__right"]//div[@class="basic-button__content"]'
mkit_button_edit = '//div[@class="edit-contact-form__buttons"]//button[@class="basic-button basic-button_primary"]' # Кнопка Редактировать
mkit_button_cancel = '//button[@class="basic-button basic-button_cancel basic-button_new-style"]' #Кнопка Омена
mkit_button_delete = '//button[@class="basic-button basic-button_warn"]//div[@class="basic-button__content"]' #Кнопка Удалить
mkit_add_new_attribute = '//div[@class="ant-drawer ant-drawer-right ant-drawer-open"]//div[@class="attribute-manager__buttons"]//button[@class="basic-button basic-button_accent"]'
mkit_new_attribute_value_name = '//div[@class="basic-field__input-wrapper"]//input[@id="title"]'
mkit_contact_dropdown = '//div[@class="mkit-dropdown-field__overlay"]//div[@class="option"]'
mkit_Opt_Out_Effective_from = '//div[@class="date-picker-field"]//span[@class="datepicker datepicker_underline ant-calendar-picker"]//input[@placeholder="Effective from"]'
mkit_Opt_Out_Effective_from_value = '//tr[@role="row"]//td[@role="gridcell"][1]'
mkit_Opt_out_word = '//input[@id="optOutWord"]'
mkit_Opt_Out_Word_add = '//div[@class="add-stop-word__buttons__group"]'
mkit_Opt_Out_Word_no = '//button[@class="basic-button basic-button_primary"]'
mkit_Opt_Out_Word_yes = '//button[@class="basic-button basic-button_warn"]'
mkit_Opt_Out_Effective_till = '//div[@class="date-picker-field"]//span[@class="datepicker datepicker_underline ant-calendar-picker"]//input[@placeholder="Effective till"]'
mkit_Opt_Out_Effective_till_value = '//tbody[@class="ant-calendar-tbody"]//td[@role="gridcell"][7]'
mkit_import_contact_button = '//label[@class="file-field__input-wrapper"]' #Кнопка открытия загрузки контактов
mkit_filter = '//div[@class="ag-react-container"]//div[@class="mkit-ag-column-header__filter"]'
mkit_filter_enterMask = '//div[@class="ag-filter"]//input[@class="basic-field__input-wrapper__input"]'
mkit_filter_applay = '//div[@class="ag-filter"]//button[@class="basic-button basic-button_accent"]'#Кнопка Apply в фильтре
mkit_filter_dropdown = '//div[@class="present-block"]//input[@class="dropdown-specify-field__control__input"]'
mkit_filter_SaveFilter = '//div[@class="present-block"]//img[@src="/static/media/diskette-dark.24e07c18ef2cf0ecc4a04bca17a14684.svg"]'
proba = '//img[@src="/static/media/broadcasts.d1043e3ae836597bcded53b3d44e29fa.svg"]'

#Локаторы BO
#Экраны BO
bo_header_icon = '//button[@class="header__icon"]'
bo_button_save = 'span[class="bp3-button-text"] div[class*="1t8ts"]'
#Партнеры
bo_Partners_AddPartners_Country = 'path[d *= "0.45 11.55 0 11 0H1C0.45 0 0 0.4"]'

bo_first_record = '//div[@class="ag-center-cols-clipper"]//div[@row-index="1"]'

bo_EditButton = '//button[@class="bp3-button _type_default__KmFtD _view_outlined__3H9IA color_primary__3FwI9 color_select__3Rg8Y"]'

#Аккаунты
bo_Accounts_Accaunt = 'div[class*="sidebar__item__hidden sidebar__item__expanded"] a[href="/accounts"]'
bo_Accounts_NewAccaunt_button = 'path[d *= "0.45 11.55 0 11 0H1C0.45 0 0 0.4"]'
bo_Accounts_AddAccount_Partner = 'path[d *= "0.45 11.55 0 11 0H1C0.45 0 0 0.4"]'
bo_Accounts_AddAccount_Currency = '//div[@class="dropdown-field undefined"][2]//div[@class="dropdown-field__content"]'
bo_Accounts_Account = 'input[name="name"]'
bo_Accounts_Description = 'textarea[name="description"]'
bo_Accounts_Incredit = 'input[name="inCredit"]'
bo_Accounts_Company_name = 'input[name="legalCompanyName"]'
bo_Accounts_Tax_ID = 'input[name="taxID"]'
bo_Accounts_Legal_address = 'input[name="legalAddress"]'
bo_Accounts_Invoicing_address = 'input[name="billingAddress"]'
bo_Accounts_Bank_name = 'input[name="bankName"]'
bo_Accounts_Bank_address = 'input[name="bankAddress"]'
bo_Accounts_Bank_account_number = 'input[name="accountNumber"]'
bo_Accounts_SWIFT_code = 'input[name="swift"]'
bo_Accounts_Save = '//div[@class="form-buttons-group__buttons"]//button[@class="bp3-button _type_default__KmFtD _view_filled__4f7Pz color_primary__3FwI9 color_select__3Rg8Y"]'
bo_Accounts_result = '//div[text()="You should select a currency"]'

#Договоры
bo_Agreements_Agreement = 'div[class*="sidebar__item__hidden sidebar__item__expanded"] a[href*="/agreements"]'




#Версия релиза
release_version ="0.3.11"