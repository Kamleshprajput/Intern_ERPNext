# ERPNext App Intelligence Snapshot

## App Information
- **Path:** C:\Users\kr425\OneDrive\Desktop\c tutorials\verilog\erpnext\erpnext_v14\erpnext
- **Commit:** 80359402633aaea17da16e8a787b11492d1cc191

## Global Hooks
- **app_name:** erpnext...
- **app_title:** ERPNext...
- **app_publisher:** Frappe Technologies Pvt. Ltd....
- **app_description:** ERP made simple...
- **app_icon:** fa fa-th...
- **app_color:** #e74c3c...
- **app_logo_url:** /assets/erpnext/images/erpnext-logo.svg...
- **override_doctype_class:** {'Address': 'erpnext.accounts.custom.address.ERPNextAddress'}...
- **before_install:** erpnext.setup.install.check_setup_wizard_not_completed...
- **after_install:** erpnext.setup.install.after_install...
- **on_session_creation:** ['erpnext.portal.utils.create_customer_or_supplier', 'erpnext.e_commerce.shopping_cart.utils.set_car...
- **on_logout:** erpnext.e_commerce.shopping_cart.utils.clear_cart_count...
- **doc_events:** {'*': {'validate': ['erpnext.support.doctype.service_level_agreement.service_level_agreement.apply',...
- **scheduler_events:** {'cron': {'0/15 * * * *': ['erpnext.manufacturing.doctype.bom_update_log.bom_update_log.resume_bom_c...

## DocTypes

### doctype
- **API Methods:** get_last_interaction
- **All Methods:** get_last_interaction, get_last_issue_from_customer, get_scheduled_employees_for_popup, strip_number...

### account
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** _make_test_records, get_inventory_account, create_account, test_rename_account, test_merge_account, test_account_sync, test_add_account_to_a_group, test_account_rename_sync, test_account_currency_sync, test_child_company_account_rename_sync...

### chart_of_accounts
- **All Methods:** go, get_default_account_types, get_xml_roots, get_csv_contents, get_account_types, make_maps_for_xml, make_maps_for_csv, make_account_trees, make_charts, create_all_roots_file...

### unverified

### verified
- **All Methods:** get...

### accounting_dimension
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** label, fieldname, document_type, disabled, dimension_defaults...
- **All Methods:** create_dimension, disable_dimension, setUp, test_dimension_against_sales_invoice, test_dimension_against_journal_entry, test_mandatory, tearDown...

### accounting_dimension_detail
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** company, reference_document, default_dimension, mandatory_for_bs, mandatory_for_pl, automatically_post_balancing_accounting_entry, offsetting_account, column_break_lqns...
- **All Methods:** ...

### accounting_dimension_filter
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** accounting_dimension, column_break_2, section_break_4, column_break_6, allow_or_restrict, accounts, dimensions, disabled, company, dimension_filter_help...
- **All Methods:** create_accounting_dimension_filter, disable_dimension_filter, setUp, test_allowed_dimension_validation, test_mandatory_dimension_validation, tearDown...

### accounting_period
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** period_name, start_date, end_date, column_break_4, company, section_break_7, closed_documents...
- **All Methods:** create_accounting_period, test_overlap, test_accounting_period, tearDown...

### accounts_settings
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** acc_frozen_upto, frozen_accounts_modifier, determine_address_tax_category_from, credit_controller, check_supplier_invoice_uniqueness, make_payment_via_journal_entry, unlink_payment_on_cancellation_of_invoice, unlink_advance_payment_on_cancelation_of_order, book_asset_depreciation_entry_automatically, add_taxes_from_item_tax_template...
- **All Methods:** tearDown, test_stale_days...

### regional

### account_closing_balance
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** closing_date, account, cost_center, debit, credit, account_currency, debit_in_account_currency, credit_in_account_currency, project, company...
- **All Methods:** ...

### advance_tax
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** reference_type, reference_name, reference_detail, account_head, allocated_amount...
- **All Methods:** ...

### advance_taxes_and_charges
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** charge_type, row_id, account_head, col_break_1, description, accounting_dimensions_section, cost_center, dimension_col_break, section_break_8, rate...
- **All Methods:** ...

### allowed_dimension
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** accounting_dimension, dimension_value...
- **All Methods:** ...

### allowed_to_transact_with
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** company...
- **All Methods:** ...

### applicable_on_account
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** applicable_on_account, is_mandatory...
- **All Methods:** ...

### bank
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** bank_name, bank_details_section, swift_number, column_break_1, address_and_contact, address_html, website, column_break_13, contact_html, data_import_configuration_section...
- **All Methods:** ...

### bank_account
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** account_name, account, bank, account_type, account_subtype, column_break_7, is_default, is_company_account, company, section_break_11...
- **All Methods:** test_validate_iban...

### bank_account_subtype
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** account_subtype...
- **All Methods:** ...

### bank_account_type
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** account_type...
- **All Methods:** ...

### bank_clearance
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** account, account_currency, from_date, to_date, column_break_5, bank_account, include_reconciled_entries, include_pos_transactions, section_break_10, payment_entries...
- **All Methods:** make_bank_account, create_loan_masters, add_transactions, make_loan, make_payment_entry, setUpClass, test_bank_clearance...

### bank_clearance_detail
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** payment_document, payment_entry, against_account, amount, column_break_5, posting_date, cheque_number, cheque_date, clearance_date...
- **All Methods:** ...

### bank_guarantee
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** bg_type, reference_doctype, reference_docname, customer, supplier, project, column_break_6, amount, start_date, validity...
- **All Methods:** ...

### bank_reconciliation_tool
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** company, bank_account, column_break_1, bank_statement_from_date, bank_statement_to_date, column_break_2, account_opening_balance, bank_statement_closing_balance, section_break_1, reconciliation_tool_cards...
- **All Methods:** ...

### bank_statement_import
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** company, bank_account, bank, download_template, import_file, import_preview, section_import_preview, template_options, import_log_section, import_log_preview...
- **All Methods:** ...

### bank_transaction
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** naming_series, date, column_break_2, status, bank_account, company, section_break_4, column_break_7, currency, section_break_10...
- **All Methods:** create_bank_account, create_gl_account, add_transactions, add_vouchers, create_loan_and_repayment, setUp, test_linked_payments, test_reconcile, test_cancel_voucher, test_debit_credit_output...

### bank_transaction_mapping
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** bank_transaction_field, file_field...
- **All Methods:** ...

### bank_transaction_payments
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** payment_document, payment_entry, allocated_amount, clearance_date...
- **All Methods:** ...

### bisect_accounting_statements
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** column_break_qxbi, from_date, to_date, algorithm, column_break_iwny, current_node, section_break_hmsy, current_from_date, current_to_date, column_break_uqyd...
- **All Methods:** ...

### bisect_nodes
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** root, left_child, right_child, period_from_date, period_to_date, difference, balance_sheet_summary, profit_loss_summary, generated...
- **All Methods:** ...

### budget
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** budget_against, company, cost_center, project, fiscal_year, column_break_3, monthly_distribution, amended_from, section_break_6, applicable_on_material_request...
- **All Methods:** set_total_expense_zero, make_budget, test_monthly_budget_crossed_ignore, test_monthly_budget_crossed_stop1, test_exception_approver_role, test_monthly_budget_crossed_for_mr, test_monthly_budget_crossed_for_po, test_monthly_budget_crossed_stop2, test_yearly_budget_crossed_stop1, test_yearly_budget_crossed_stop2...

### budget_account
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** account, budget_amount...
- **All Methods:** ...

### campaign_item
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** campaign...
- **All Methods:** ...

### cashier_closing
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** naming_series, user, date, from_time, time, expense, custody, returns, outstanding_amount, payments...
- **All Methods:** ...

### cashier_closing_payments
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** mode_of_payment, amount...
- **All Methods:** ...

### cash_flow_mapper
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** section_name, section_header, section_leader, section_subtotal, section_footer, accounts, position...
- **All Methods:** ...

### cash_flow_mapping
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** mapping_name, label, accounts, sb_1, is_finance_cost, is_working_capital, is_finance_cost_adjustment, is_income_tax_liability, is_income_tax_expense...
- **All Methods:** setUp, tearDown, test_multiple_selections_not_allowed...

### cash_flow_mapping_accounts
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** account...
- **All Methods:** ...

### cash_flow_mapping_template
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** template_name, mapping...
- **All Methods:** ...

### cash_flow_mapping_template_details
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** mapping...
- **All Methods:** ...

### chart_of_accounts_importer
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** company, import_file, chart_preview, chart_tree, download_template...
- **All Methods:** ...

### cheque_print_template
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** settings, has_print_format, primary_settings, bank_name, cheque_size, starting_position_from_top_edge, cheque_width, cheque_height, scanned_cheque, column_break_5...
- **All Methods:** ...

### closed_document
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** document_type, closed...
- **All Methods:** ...

### cost_center
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** create_cost_center, test_cost_center_creation_against_child_node...

### cost_center_allocation
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** main_cost_center, valid_from, column_break_2, section_break_5, company, allocation_percentages, amended_from...
- **All Methods:** create_cost_center_allocation, setUp, test_gle_based_on_cost_center_allocation, test_main_cost_center_cant_be_child, test_invalid_main_cost_center, test_if_child_cost_center_has_any_allocation_record, test_total_percentage, test_valid_from_based_on_existing_gle, test_multiple_cost_center_allocation_on_same_main_cost_center, test_debit_credit_on_cost_center_allocation_for_commercial_rounding...

### cost_center_allocation_percentage
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** cost_center, percentage...
- **All Methods:** ...

### coupon_code
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** coupon_name, coupon_type, customer, column_break_4, coupon_code, pricing_rule, uses, valid_from, valid_upto, maximum_use...
- **All Methods:** test_create_test_data, setUp, tearDown, test_sales_order_with_coupon_code...

### currency_exchange_settings
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** api_details_section, api_endpoint, url, column_break_3, help, section_break_2, req_params, column_break_4, result_key, service_provider...
- **All Methods:** ...

### currency_exchange_settings_details
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** key, value...
- **All Methods:** ...

### currency_exchange_settings_result
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** key...
- **All Methods:** ...

### customer_group_item
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** customer_group...
- **All Methods:** ...

### customer_item
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** customer...
- **All Methods:** ...

### discounted_invoice
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** sales_invoice, customer, posting_date, outstanding_amount, column_break_3, debit_to...
- **All Methods:** ...

### dunning
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** company, naming_series, sales_invoice, customer_name, outstanding_amount, column_break_3, posting_date, overdue_days, section_break_6, dunning_type...
- **All Methods:** create_dunning, create_dunning_with_zero_interest_rate, create_dunning_type, create_dunning_type_with_zero_interest_rate, setUpClass, tearDownClass, test_dunning, test_dunning_with_zero_interest_rate, test_gl_entries, test_payment_entry...

### dunning_letter_text
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** language, is_default_language, section_break_4, body_text, closing_text, section_break_7, body_and_closing_text_help...
- **All Methods:** ...

### dunning_type
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** dunning_type, dunning_fee, text_block_section, dunning_letter_text, column_break_4, section_break_6, column_break_8, overdue_interval_section, start_day, end_day...
- **All Methods:** ...

### exchange_rate_revaluation
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** posting_date, column_break_2, company, section_break_4, get_entries, accounts, section_break_6, amended_from, gain_loss_unbooked, gain_loss_booked...
- **All Methods:** setUp, tearDown, set_system_and_company_settings, test_01_revaluation_of_forex_balance, test_02_accounts_only_with_base_currency_balance, test_03_accounts_only_with_account_currency_balance, test_04_get_account_details_function...

### exchange_rate_revaluation_account
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** account, party_type, party, column_break_2, account_currency, balance_in_account_currency, balances, current_exchange_rate, balance_in_base_currency, column_break_9...
- **All Methods:** ...

### finance_book
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** finance_book_name...
- **All Methods:** create_finance_book, test_finance_book...

### fiscal_year
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** year, disabled, year_start_date, year_end_date, companies, auto_created, is_short_year...
- **All Methods:** test_record_generator, test_extra_year...

### fiscal_year_company
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** company...
- **All Methods:** ...

### gl_entry
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** posting_date, transaction_date, account, party_type, party, cost_center, debit, credit, account_currency, debit_in_account_currency...
- **All Methods:** test_round_off_entry, test_rename_entries...

### invoice_discounting
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** posting_date, loan_start_date, loan_period, loan_end_date, column_break_3, status, company, section_break_5, invoices, section_break_7...
- **All Methods:** create_invoice_discounting, setUp, test_total_amount, test_gl_entries_in_base_currency, test_loan_on_submit, test_on_disbursed, test_on_close_after_loan_period, test_on_close_after_loan_period_after_inv_payment, test_on_close_before_loan_period, test_make_payment_before_loan_period...

### item_tax_template
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### item_tax_template_detail
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** tax_type, tax_rate...
- **All Methods:** ...

### journal_entry
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** make_journal_entry, test_journal_entry_with_against_jv, test_jv_against_sales_order, test_jv_against_purchase_order, jv_against_voucher_testcase, advance_paid_testcase, cancel_against_voucher_testcase, test_jv_against_stock_account, test_multi_currency, test_reverse_journal_entry...

### journal_entry_account
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** account, account_type, cost_center, col_break1, party_type, party, currency_section, account_currency, column_break_10, exchange_rate...
- **All Methods:** ...

### journal_entry_template
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** section_break_1, voucher_type, company, column_break_3, is_opening, accounts, naming_series, template_title, section_break_3, multi_currency...
- **All Methods:** ...

### journal_entry_template_account
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** account...
- **All Methods:** ...

### ledger_health
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** voucher_type, voucher_no, debit_credit_mismatch, checked_on, general_and_payment_ledger_mismatch...
- **All Methods:** setUp, tearDown, configure_monitoring_tool, clear_old_entries, create_journal, test_debit_credit_mismatch, test_gl_and_pl_mismatch...

### ledger_health_monitor
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** enable_health_monitor, monitor_section, debit_credit_mismatch, general_and_payment_ledger_mismatch, monitor_for_last_x_days, section_break_xdsp, companies...
- **All Methods:** ...

### ledger_health_monitor_company
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** company...
- **All Methods:** ...

### ledger_merge
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** account, section_break_1, column_break_3, merge_accounts, section_break_5, company, status, root_type, account_name, is_group...
- **All Methods:** test_merge_success, test_partial_merge_success, tearDown...

### ledger_merge_accounts
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** account, merged, account_name...
- **All Methods:** ...

### loyalty_point_entry
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** loyalty_program, loyalty_program_tier, customer, redeem_against, loyalty_points, purchase_amount, expiry_date, posting_date, company, invoice_type...
- **All Methods:** ...

### loyalty_point_entry_redemption
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** sales_invoice, redemption_date, redeemed_points...
- **All Methods:** ...

### loyalty_program
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** loyalty_program_name, loyalty_program_type, from_date, to_date, column_break_7, customer_group, customer_territory, auto_opt_in, rules, collection_rules...
- **All Methods:** get_points_earned, create_sales_invoice_record, create_records, setUpClass, test_loyalty_points_earned_single_tier, test_loyalty_points_earned_multiple_tier, test_cancel_sales_invoice, test_sales_invoice_return, test_loyalty_points_for_dashboard, get_returned_amount...

### loyalty_program_collection
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** tier_name, min_spent, column_break_3, collection_factor...
- **All Methods:** ...

### mode_of_payment
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** mode_of_payment, type, accounts, enabled...
- **All Methods:** ...

### mode_of_payment_account
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** company, default_account...
- **All Methods:** ...

### monthly_distribution
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### monthly_distribution_percentage
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** month, percentage_allocation...
- **All Methods:** ...

### opening_invoice_creation_tool
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** company, create_missing_party, column_break_3, invoice_type, section_break_4, invoices, cost_center, accounting_dimensions_section, dimension_col_break...
- **All Methods:** get_opening_invoice_creation_dict, make_company, make_customer, setUpClass, make_invoices, test_opening_sales_invoice_creation, check_expected_values, test_opening_purchase_invoice_creation, test_opening_sales_invoice_creation_with_missing_debit_account, test_renaming_of_invoice_using_invoice_number_field...

### opening_invoice_creation_tool_item
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** party_type, party, temporary_opening_account, column_break_3, posting_date, due_date, section_break_5, item_name, outstanding_amount, column_break_4...
- **All Methods:** ...

### party_account
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** company, account...
- **All Methods:** ...

### party_link
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** primary_role, column_break_2, secondary_role, primary_party, secondary_party...
- **All Methods:** ...

### payment_entry
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** type_of_payment, naming_series, payment_type, column_break_5, posting_date, company, cost_center, mode_of_payment, party_section, party_type...
- **All Methods:** create_payment_entry, create_payment_terms_template, create_payment_terms_template_with_discount, create_payment_term, create_customer, tearDown, get_journals_for, test_payment_entry_against_order, test_payment_against_sales_order_usd_to_inr, test_payment_entry_for_blocked_supplier_invoice...

### payment_entry_deduction
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** account, cost_center, amount, column_break_2, description...
- **All Methods:** ...

### payment_entry_reference
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** reference_doctype, reference_name, due_date, bill_no, column_break_4, total_amount, outstanding_amount, allocated_amount, exchange_rate, payment_term...
- **All Methods:** payment_request_outstanding...

### payment_gateway_account
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** payment_gateway, is_default, column_break_4, payment_account, currency, payment_request_message, message, message_examples, payment_channel...
- **All Methods:** ...

### payment_ledger_entry
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** posting_date, account_type, account, party_type, party, voucher_type, voucher_no, against_voucher_type, against_voucher_no, amount...
- **All Methods:** setUp, tearDown, create_company, create_item, create_customer, create_sales_invoice, create_payment_entry, create_sales_order, clear_old_entries, create_journal_entry...

### payment_order
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** naming_series, company, party, column_break_2, posting_date, section_break_5, references, amended_from, payment_order_type, company_bank_account...
- **All Methods:** create_payment_order_against_payment_entry, setUp, tearDown, test_payment_order_creation_against_payment_entry...

### payment_order_reference
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** reference_doctype, reference_name, amount, column_break_4, supplier, payment_request, mode_of_payment, bank_account_details, bank_account, column_break_10...
- **All Methods:** ...

### payment_reconciliation
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** company, party_type, party, receivable_payable_account, bank_cash_account, col_break1, sec_break1, payments, sec_break2, invoices...
- **All Methods:** make_customer, make_supplier, setUp, tearDown, create_company, create_item, create_customer, create_account, create_sales_invoice, create_payment_entry...

### payment_reconciliation_allocation
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** invoice_number, allocated_amount, column_break_3, section_break_5, difference_account, column_break_7, difference_amount, reference_name, is_advance, reference_type...
- **All Methods:** get_list...

### payment_reconciliation_invoice
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** invoice_type, invoice_number, invoice_date, col_break1, amount, outstanding_amount, currency, exchange_rate...
- **All Methods:** get_list...

### payment_reconciliation_payment
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** reference_type, reference_name, posting_date, is_advance, reference_row, col_break1, amount, sec_break1, currency, difference_amount...
- **All Methods:** get_list...

### payment_request
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** payment_request_type, transaction_date, column_break_2, naming_series, mode_of_payment, party_details, party_type, party, column_break_4, reference_doctype...
- **All Methods:** setUp, test_payment_request_linkings, test_payment_entry_against_purchase_invoice, test_multiple_payment_entry_against_purchase_invoice, test_payment_entry, test_status, test_multiple_payment_entries_against_sales_order, test_conversion_on_foreign_currency_accounts, test_multiple_payment_if_partially_paid_for_same_currency, test_multiple_payment_if_partially_paid_for_multi_currency...

### payment_schedule
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** payment_term, description, due_date, invoice_portion, payment_amount, mode_of_payment, paid_amount, column_break_3, discounted_amount, outstanding...
- **All Methods:** ...

### payment_term
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### payment_terms_template
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** tearDown, test_create_template, test_credit_days, test_duplicate_terms...

### payment_terms_template_detail
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** payment_term, description, invoice_portion, due_date_based_on, credit_days, credit_months, mode_of_payment, column_break_3, section_break_8, discount_type...
- **All Methods:** ...

### period_closing_voucher
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** transaction_date, posting_date, fiscal_year, amended_from, company, column_break1, closing_account_head, remarks, gle_processing_status, error_message...
- **All Methods:** create_company, create_account, create_cost_center, test_closing_entry, test_cost_center_wise_posting, test_period_closing_with_finance_book_entries, test_gl_entries_restrictions, test_closing_balance_with_dimensions, make_period_closing_voucher...

### pos_closing_entry
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** period_start_date, period_end_date, column_break_3, posting_date, section_break_5, company, column_break_7, pos_profile, user, section_break_9...
- **All Methods:** init_user_and_profile, setUp, tearDown, test_pos_closing_entry, test_cancelling_of_pos_closing_entry...

### pos_closing_entry_detail
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** mode_of_payment, expected_amount, difference, opening_amount, closing_amount...
- **All Methods:** ...

### pos_closing_entry_taxes
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** rate, amount, account_head...
- **All Methods:** ...

### pos_customer_group
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** customer_group...
- **All Methods:** ...

### pos_field
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** fieldname, fieldtype, label, options, reqd, read_only, column_break_7, default_value...
- **All Methods:** ...

### pos_invoice
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** customer_section, title, naming_series, customer, customer_name, tax_id, is_pos, pos_profile, is_return, column_break1...
- **All Methods:** create_pos_invoice, make_batch_item, setUpClass, tearDown, test_timestamp_change, test_change_naming_series, test_discount_and_inclusive_tax, test_tax_calculation_with_multiple_items, test_tax_calculation_with_item_tax_template, test_tax_calculation_with_multiple_items_and_discount...

### pos_invoice_item
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** barcode, item_code, col_break1, item_name, customer_item_code, description_section, description, item_group, brand, image_section...
- **All Methods:** ...

### pos_invoice_merge_log
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** posting_date, customer, section_break_3, pos_invoices, references_section, amended_from, consolidated_invoice, column_break_7, consolidated_credit_note, column_break_3...
- **All Methods:** test_consolidated_invoice_creation, test_consolidated_credit_note_creation, test_consolidated_invoice_item_taxes, test_consolidation_round_off_error_1, test_consolidation_round_off_error_2, test_consolidation_round_off_error_3, test_consolidation_rounding_adjustment, test_serial_no_case_1...

### pos_invoice_reference
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** pos_invoice, column_break_3, customer, posting_date, grand_total, is_return, return_against...
- **All Methods:** ...

### pos_item_group
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** item_group...
- **All Methods:** ...

### pos_opening_entry
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** period_start_date, period_end_date, column_break_3, posting_date, section_break_5, company, pos_profile, column_break_7, user, section_break_9...
- **All Methods:** create_opening_entry...

### pos_opening_entry_detail
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** mode_of_payment, opening_amount...
- **All Methods:** ...

### pos_payment_method
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** default, mode_of_payment, allow_in_returns...
- **All Methods:** ...

### pos_profile
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** disabled, customer, company, country, campaign, company_address, column_break_9, section_break_15, applicable_for_users, section_break_11...
- **All Methods:** get_customers_list, get_items_list, make_pos_profile, test_pos_profile...

### pos_profile_user
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** default, user...
- **All Methods:** ...

### pos_search_fields
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** fieldname, field...
- **All Methods:** ...

### pos_settings
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** invoice_fields, pos_search_fields...
- **All Methods:** ...

### pricing_rule
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** applicability_section, title, disable, apply_on, price_or_product_discount, warehouse, column_break_7, items, item_groups, brands...
- **All Methods:** get_pricing_rules, sorted_by_priority, filter_pricing_rule_based_on_condition, _get_pricing_rules, apply_multiple_pricing_rules, _get_tree_conditions, get_other_conditions, filter_pricing_rules, validate_quantity_and_amount_for_suggestion, filter_pricing_rules_for_qty_amount...

### pricing_rule_brand
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** brand, uom...
- **All Methods:** ...

### pricing_rule_detail
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** pricing_rule, item_code, margin_type, rate_or_discount, child_docname, rule_applied...
- **All Methods:** ...

### pricing_rule_item_code
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** item_code, uom...
- **All Methods:** ...

### pricing_rule_item_group
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** item_group, uom...
- **All Methods:** ...

### process_deferred_accounting
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** type, amended_from, start_date, end_date, column_break_3, posting_date, account, company...
- **All Methods:** change_acc_settings, test_creation_of_ledger_entry_on_submit, test_pda_submission_and_cancellation...

### process_payment_reconciliation
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** status, company, party_type, column_break_io6c, party, receivable_payable_account, filter_section, from_invoice_date, to_invoice_date, column_break_kegk...
- **All Methods:** ...

### process_payment_reconciliation_log
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** allocations, reconciled, total_allocations, allocated, reconciled_entries, tasks_section, allocations_section, column_break_yhin, section_break_4ywv, error_log...
- **All Methods:** ...

### process_payment_reconciliation_log_allocations
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** reference_type, reference_name, reference_row, column_break_3, invoice_type, invoice_number, section_break_6, allocated_amount, unreconciled_amount, column_break_8...
- **All Methods:** ...

### process_statement_of_accounts
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** frequency, company, from_date, to_date, cost_center, project, section_break_3, column_break_6, section_break_11, column_break_14...
- **All Methods:** create_process_soa, setUp, test_process_soa_for_gl, test_process_soa_for_ar, test_auto_email_for_process_soa_ar, check_ageing_summary, tearDown...

### process_statement_of_accounts_customer
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** customer, primary_email, billing_email, customer_name...
- **All Methods:** ...

### promotional_scheme
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** section_break_1, apply_on, disable, column_break_3, items, item_groups, brands, mixed_conditions, is_cumulative, section_break_10...
- **All Methods:** make_promotional_scheme, setUp, test_promotional_scheme, test_promotional_scheme_without_applicable_for, test_change_applicable_for_in_promotional_scheme, test_change_applicable_for_values_in_promotional_scheme, test_min_max_amount_configuration, test_validation_on_recurse_with_mixed_condition...

### promotional_scheme_price_discount
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** disable, column_break_2, rule_description, section_break_2, min_qty, max_qty, column_break_3, min_amount, max_amount, section_break_6...
- **All Methods:** ...

### promotional_scheme_product_discount
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** disable, column_break_2, rule_description, section_break_1, min_qty, max_qty, column_break_3, min_amount, max_amount, section_break_6...
- **All Methods:** ...

### psoa_cost_center
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** cost_center_name...
- **All Methods:** ...

### psoa_project
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** project_name...
- **All Methods:** ...

### purchase_invoice
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** check_gl_entries, create_tax_witholding_category, unlink_payment_on_cancel_of_invoice, make_purchase_invoice, make_purchase_invoice_against_cost_center, setup_provisional_accounting, toggle_provisional_accounting_setting, setUpClass, tearDownClass, tearDown...

### purchase_invoice_advance
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** reference_type, reference_name, remarks, reference_row, col_break1, advance_amount, allocated_amount, exchange_gain_loss, ref_exchange_rate, difference_posting_date...
- **All Methods:** ...

### purchase_invoice_item
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** item_code, col_break1, item_name, description_section, description, image, image_view, quantity_and_rate, received_qty, qty...
- **All Methods:** ...

### purchase_taxes_and_charges
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** category, add_deduct_tax, charge_type, row_id, included_in_print_rate, col_break1, account_head, cost_center, description, section_break_10...
- **All Methods:** ...

### purchase_taxes_and_charges_template
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** title, is_default, disabled, column_break4, company, section_break6, taxes, tax_category...
- **All Methods:** ...

### repost_accounting_ledger
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** company, amended_from, vouchers, column_break_vpup, section_break_metl, delete_cancelled_entries...
- **All Methods:** update_repost_settings, setUp, tearDown, test_01_basic_functions, test_02_deferred_accounting_valiations, test_04_pcv_validation, test_03_deletion_flag_and_preview_function, test_05_without_deletion_flag, test_06_repost_purchase_receipt...

### repost_accounting_ledger_items
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** voucher_type, voucher_no...
- **All Methods:** ...

### repost_accounting_ledger_settings
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** allowed_types...
- **All Methods:** ...

### repost_allowed_types
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** document_type, allowed, column_break_sfzb...
- **All Methods:** ...

### repost_payment_ledger
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** posting_date, voucher_type, amended_from, company, selected_vouchers_section, filters_section, column_break_4, repost_vouchers, repost_status, status_section...
- **All Methods:** ...

### repost_payment_ledger_items
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** voucher_type, voucher_no...
- **All Methods:** ...

### sales_invoice
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** check_gl_entries, create_sales_invoice, create_sales_invoice_against_cost_center, get_outstanding_amount, get_taxes_and_charges, create_internal_parties, create_internal_supplier, setup_accounts, add_taxes, setUp...

### sales_invoice_advance
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** reference_type, reference_name, remarks, reference_row, col_break1, advance_amount, allocated_amount, exchange_gain_loss, ref_exchange_rate, difference_posting_date...
- **All Methods:** ...

### sales_invoice_item
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** barcode, item_code, col_break1, item_name, customer_item_code, description, image_view, image, quantity_and_rate, qty...
- **All Methods:** ...

### sales_invoice_payment
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** mode_of_payment, amount, column_break_3, account, type, base_amount, clearance_date, default...
- **All Methods:** ...

### sales_invoice_timesheet
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** time_sheet, billing_hours, billing_amount, timesheet_detail, activity_type, description, from_time, to_time, section_break_3, column_break_5...
- **All Methods:** ...

### sales_partner_item
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** sales_partner...
- **All Methods:** ...

### sales_taxes_and_charges
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** charge_type, row_id, account_head, cost_center, col_break_1, description, included_in_print_rate, section_break_8, rate, section_break_9...
- **All Methods:** ...

### sales_taxes_and_charges_template
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### shareholder
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### share_balance
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** share_type, from_no, rate, column_break_4, no_of_shares, to_no, amount, section_break_8, is_company, current_state...
- **All Methods:** ...

### share_transfer
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** transfer_type, column_break_1, date, section_break_1, from_shareholder, from_folio_no, equity_or_liability_account, asset_account, column_break_3, to_shareholder...
- **All Methods:** setUp, test_invalid_share_transfer...

### share_type
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### shipping_rule
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** create_shipping_rule, test_from_greater_than_to, test_many_zero_to_values, test_overlapping_conditions...

### shipping_rule_condition
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** from_value, to_value, shipping_amount...
- **All Methods:** ...

### shipping_rule_country
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** country...
- **All Methods:** ...

### south_africa_vat_account
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** account...
- **All Methods:** ...

### subscription
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** cb_1, status, subscription_period, cancelation_date, trial_period_start, trial_period_end, column_break_11, current_invoice_start, current_invoice_end, days_until_due...
- **All Methods:** create_plan, create_parties, setUp, tearDown, test_create_subscription_with_trial_with_correct_period, test_create_subscription_without_trial_with_correct_period, test_create_subscription_trial_with_wrong_dates, test_create_subscription_multi_with_different_billing_fails, test_invoice_is_generated_at_end_of_billing_period, test_status_goes_back_to_active_after_invoice_is_paid...

### subscription_invoice
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** document_type, invoice...
- **All Methods:** ...

### subscription_plan
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** plan_name, currency, column_break_3, item, section_break_5, price_determination, column_break_7, cost, price_list, section_break_11...
- **All Methods:** ...

### subscription_plan_detail
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** qty, plan...
- **All Methods:** ...

### subscription_settings
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** grace_period, cancel_after_grace, prorate...
- **All Methods:** ...

### supplier_group_item
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** supplier_group...
- **All Methods:** ...

### supplier_item
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** supplier...
- **All Methods:** ...

### tax_category
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### tax_rule
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** make_tax_rule, setUpClass, tearDownClass, setUp, test_conflict, test_conflict_with_non_overlapping_dates, test_for_parent_customer_group, test_conflict_with_overlapping_dates, test_tax_template, test_select_tax_rule_based_on_customer...

### tax_withheld_vouchers
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** voucher_type, voucher_name, taxable_amount...
- **All Methods:** ...

### tax_withholding_account
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** company, account...
- **All Methods:** ...

### tax_withholding_category
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** category_name, section_break_8, rates, section_break_7, accounts, category_details_section, column_break_2, consider_party_ledger_amount, tax_on_excess_amount, round_off_tax_amount...
- **All Methods:** cancel_invoices, create_purchase_invoice, create_purchase_order, create_sales_invoice, create_payment_entry, create_records, create_tax_withholding_category_records, create_tax_withholding_category, create_lower_deduction_certificate, make_pan_no_field...

### tax_withholding_rate
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** tax_withholding_rate, column_break_3, single_threshold, cumulative_threshold, from_date, to_date...
- **All Methods:** ...

### territory_item
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** territory...
- **All Methods:** ...

### transaction_deletion_record_details
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** doctype_name, docfield_name, no_of_docs, done...
- **All Methods:** ...

### unreconcile_payment
- **Module:** Accounts
- **Submittable:** 1
- **Fields:** amended_from, company, voucher_type, voucher_no, get_allocations, allocations...
- **API Methods:** doc_has_references, get_linked_payments_for_doc, create_unreconcile_doc_for_selection, get_allocations_from_payment
- **All Methods:** doc_has_references, get_linked_payments_for_doc, create_unreconcile_doc_for_selection, validate, get_allocations_from_payment, add_references, on_submit...

### unreconcile_payment_entries
- **Module:** Accounts
- **Submittable:** 0
- **Fields:** reference_name, allocated_amount, unlinked, reference_doctype, account, party_type, party, account_currency...
- **All Methods:** ...

### asset
- **Module:** Assets
- **Submittable:** 1
- **Fields:** naming_series, asset_name, item_code, item_name, asset_category, asset_owner, asset_owner_company, supplier, customer, image...
- **All Methods:** get_gl_entries, create_asset_data, create_asset, create_asset_category, create_fixed_asset_item, set_depreciation_settings_in_company, enable_cwip_accounting, setUpClass, tearDownClass, test_asset_category_is_fetched...

### asset_capitalization
- **Module:** Assets
- **Submittable:** 1
- **Fields:** title, target_item_code, target_item_name, target_is_fixed_asset, column_break_5, target_asset, target_asset_name, column_break_9, company, posting_date...
- **All Methods:** create_asset_capitalization_data, create_asset_capitalization, create_stock_reconciliation, create_depreciation_asset, get_actual_gle_dict, get_actual_sle_dict, setUp, test_capitalization_with_perpetual_inventory, test_capitalization_with_periodical_inventory, test_capitalization_with_wip_composite_asset...

### asset_capitalization_asset_item
- **Module:** Assets
- **Submittable:** 0
- **Fields:** asset, asset_name, column_break_3, item_code, item_name, section_break_6, asset_value, column_break_9, fixed_asset_account, cost_center...
- **All Methods:** ...

### asset_capitalization_service_item
- **Module:** Assets
- **Submittable:** 0
- **Fields:** item_code, item_name, column_break_3, expense_account, section_break_6, qty, uom, column_break_9, rate, amount...
- **All Methods:** ...

### asset_capitalization_stock_item
- **Module:** Assets
- **Submittable:** 0
- **Fields:** column_break_3, warehouse, batch_no, section_break_6, stock_qty, stock_uom, column_break_9, valuation_rate, amount, batch_and_serial_no_section...
- **All Methods:** ...

### asset_category
- **Module:** Assets
- **Submittable:** 0
- **Fields:** asset_category_name, column_break_3, finance_book_detail, finance_books, section_break_2, accounts, depreciation_options, enable_cwip_accounting...
- **All Methods:** test_mandatory_fields, test_cwip_accounting...

### asset_category_account
- **Module:** Assets
- **Submittable:** 0
- **Fields:** company_name, fixed_asset_account, accumulated_depreciation_account, depreciation_expense_account, capital_work_in_progress_account...
- **All Methods:** ...

### asset_finance_book
- **Module:** Assets
- **Submittable:** 0
- **Fields:** finance_book, depreciation_method, total_number_of_depreciations, column_break_5, frequency_of_depreciation, depreciation_start_date, expected_value_after_useful_life, value_after_depreciation, rate_of_depreciation, salvage_value_percentage...
- **All Methods:** ...

### asset_maintenance
- **Module:** Assets
- **Submittable:** 0
- **Fields:** asset_name, asset_category, item_code, item_name, column_break_3, company, section_break_6, maintenance_team, column_break_9, maintenance_manager...
- **All Methods:** create_asset_data, create_maintenance_team, get_maintenance_team, get_maintenance_tasks, create_asset_category, set_depreciation_settings_in_company, setUp, test_create_asset_maintenance, test_create_asset_maintenance_log...

### asset_maintenance_log
- **Module:** Assets
- **Submittable:** 1
- **Fields:** asset_maintenance, naming_series, asset_name, column_break_2, item_code, item_name, section_break_5, task, maintenance_type, periodicity...
- **All Methods:** ...

### asset_maintenance_task
- **Module:** Assets
- **Submittable:** 0
- **Fields:** maintenance_task, maintenance_type, column_break_2, maintenance_status, section_break_2, start_date, periodicity, column_break_4, end_date, certificate_required...
- **All Methods:** ...

### asset_maintenance_team
- **Module:** Assets
- **Submittable:** 0
- **Fields:** maintenance_team_name, maintenance_manager, maintenance_manager_name, column_break_2, company, section_break_2, maintenance_team_members...
- **All Methods:** ...

### asset_movement
- **Module:** Assets
- **Submittable:** 1
- **Fields:** company, purpose, transaction_date, column_break_4, reference, reference_doctype, reference_name, amended_from, section_break_10, assets...
- **All Methods:** create_asset_movement, make_location, setUp, test_movement, test_last_movement_cancellation...

### asset_movement_item
- **Module:** Assets
- **Submittable:** 0
- **Fields:** asset, asset_name, source_location, target_location, from_employee, to_employee, column_break_2, company...
- **All Methods:** ...

### asset_repair
- **Module:** Assets
- **Submittable:** 1
- **Fields:** naming_series, column_break_2, section_break_5, failure_date, column_break_6, completion_date, repair_status, section_break_9, description, column_break_9...
- **All Methods:** num_of_depreciations, create_asset_repair, setUpClass, test_update_status, test_stock_item_total_value, test_total_repair_cost, test_repair_status_after_submit, test_stock_items, test_warehouse, test_decrease_stock_quantity...

### asset_repair_consumed_item
- **Module:** Assets
- **Submittable:** 0
- **Fields:** valuation_rate, consumed_quantity, total_value, serial_no, item_code...
- **All Methods:** ...

### asset_shift_allocation
- **Module:** Assets
- **Submittable:** 1
- **Fields:** section_break_esaa, asset, naming_series, column_break_tdae, finance_book, depreciation_schedule_section, depreciation_schedule, amended_from...
- **All Methods:** create_asset_shift_factors, setUpClass, tearDownClass, test_asset_shift_allocation...

### asset_shift_factor
- **Module:** Assets
- **Submittable:** 0
- **Fields:** shift_name, shift_factor, default...
- **All Methods:** ...

### asset_value_adjustment
- **Module:** Assets
- **Submittable:** 1
- **Fields:** company, asset, asset_category, finance_book, journal_entry, column_break_4, date, current_asset_value, new_asset_value, difference_amount...
- **All Methods:** make_asset_value_adjustment, setUp, test_current_asset_value, test_asset_depreciation_value_adjustment...

### depreciation_schedule
- **Module:** Assets
- **Submittable:** 0
- **Fields:** finance_book, schedule_date, depreciation_amount, column_break_3, accumulated_depreciation_amount, journal_entry, make_depreciation_entry, finance_book_id, depreciation_method, shift...
- **All Methods:** ...

### linked_location
- **Module:** Assets
- **Submittable:** 0
- **Fields:** location...
- **All Methods:** ...

### location
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** runTest...

### maintenance_team_member
- **Module:** Assets
- **Submittable:** 0
- **Fields:** team_member, full_name, maintenance_role...
- **All Methods:** ...

### bulk_transaction_log
- **Module:** Bulk Transaction
- **Submittable:** 0
- **Fields:** date, log_entries, column_break_bsan, section_break_mdmv, succeeded, column_break_qryp, failed...
- **All Methods:** ...

### bulk_transaction_log_detail
- **Module:** Bulk Transaction
- **Submittable:** 0
- **Fields:** transaction_name, transaction_status, error_description, from_doctype, to_doctype, date, time, retried...
- **All Methods:** ...

### buying_settings
- **Module:** Buying
- **Submittable:** 0
- **Fields:** supp_master_name, supplier_group, buying_price_list, po_required, pr_required, maintain_same_rate, allow_multiple_items, subcontract, backflush_raw_materials_of_subcontract_based_on, over_transfer_allowance...
- **All Methods:** ...

### purchase_order
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** prepare_data_for_internal_transfer, make_pr_against_po, get_same_items, create_purchase_order, create_pr_against_po, get_ordered_qty, get_requested_qty, test_purchase_order_qty, test_make_purchase_receipt, test_ordered_qty...

### purchase_order_item
- **Module:** Buying
- **Submittable:** 0
- **Fields:** item_code, supplier_part_no, item_name, column_break_4, schedule_date, expected_delivery_date, section_break_5, description, col_break1, image...
- **All Methods:** on_doctype_update...

### purchase_order_item_supplied
- **Module:** Buying
- **Submittable:** 0
- **Fields:** main_item_code, rm_item_code, required_qty, rate, amount, column_break_6, bom_detail_no, reference_name, conversion_factor, stock_uom...
- **All Methods:** ...

### purchase_receipt_item_supplied
- **Module:** Buying
- **Submittable:** 0
- **Fields:** main_item_code, rm_item_code, description, batch_no, serial_no, col_break1, required_qty, consumed_qty, stock_uom, rate...
- **All Methods:** ...

### request_for_quotation
- **Module:** Buying
- **Submittable:** 1
- **Fields:** naming_series, company, vendor, column_break1, transaction_date, suppliers_section, suppliers, items_section, items, supplier_response_section...
- **All Methods:** make_request_for_quotation, get_supplier_data, test_quote_status, test_make_supplier_quotation, test_make_supplier_quotation_with_special_characters, test_make_supplier_quotation_from_portal, test_make_multi_uom_supplier_quotation, test_make_rfq_from_opportunity, test_get_link, test_get_pdf...

### request_for_quotation_item
- **Module:** Buying
- **Submittable:** 0
- **Fields:** item_code, supplier_part_no, column_break_3, item_name, section_break_5, description, image, image_view, quantity, qty...
- **All Methods:** ...

### request_for_quotation_supplier
- **Module:** Buying
- **Submittable:** 0
- **Fields:** send_email, email_sent, supplier, contact, quote_status, column_break_3, supplier_name, email_id...
- **All Methods:** ...

### supplier
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** create_supplier, test_get_supplier_group_details, test_supplier_default_payment_terms, test_supplier_disabled, test_supplier_country, test_party_details_tax_category, test_serach_fields_for_supplier...

### supplier_quotation
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** test_make_purchase_order...

### supplier_quotation_item
- **Module:** Buying
- **Submittable:** 0
- **Fields:** item_code, supplier_part_no, item_name, column_break_3, lead_time_days, section_break_5, description, col_break1, image, image_view...
- **All Methods:** ...

### supplier_scorecard
- **Module:** Buying
- **Submittable:** 0
- **Fields:** supplier, supplier_score, indicator_color, status, column_break_2, period, scoring_setup, weighting_function, standings, criteria_setup...
- **All Methods:** make_supplier_scorecard, delete_test_scorecards, test_create_scorecard, test_criteria_weight...

### supplier_scorecard_criteria
- **Module:** Buying
- **Submittable:** 0
- **Fields:** criteria_name, max_score, formula, weight...
- **All Methods:** delete_test_scorecards, test_variables_exist, test_formula_validate...

### supplier_scorecard_period
- **Module:** Buying
- **Submittable:** 1
- **Fields:** supplier, naming_series, total_score, column_break_2, start_date, end_date, section_break_11, criteria, variables, sec_ref...
- **All Methods:** ...

### supplier_scorecard_scoring_criteria
- **Module:** Buying
- **Submittable:** 0
- **Fields:** criteria_name, score, column_break_4, weight, max_score, section_break_6, formula...
- **All Methods:** ...

### supplier_scorecard_scoring_standing
- **Module:** Buying
- **Submittable:** 0
- **Fields:** standing_name, column_break_2, standing_color, section_break_4, min_grade, max_grade, actions, warn_rfqs, warn_pos, prevent_rfqs...
- **All Methods:** ...

### supplier_scorecard_scoring_variable
- **Module:** Buying
- **Submittable:** 0
- **Fields:** variable_label, description, value, param_name, path...
- **All Methods:** ...

### supplier_scorecard_standing
- **Module:** Buying
- **Submittable:** 0
- **Fields:** standing_name, standing_color, min_grade, max_grade, column_break_5, warn_rfqs, warn_pos, prevent_rfqs, prevent_pos, notify_supplier...
- **All Methods:** ...

### supplier_scorecard_variable
- **Module:** Buying
- **Submittable:** 0
- **Fields:** variable_label, is_custom, param_name, path, column_break_5, description...
- **All Methods:** test_variable_exist, test_path_exists...

### communication_medium
- **Module:** Communication
- **Submittable:** 0
- **Fields:** communication_medium_type, catch_all, column_break_3, provider, disabled, timeslots_section, timeslots, communication_channel...
- **All Methods:** ...

### communication_medium_timeslot
- **Module:** Communication
- **Submittable:** 0
- **Fields:** day_of_week, from_time, to_time, employee_group...
- **All Methods:** ...

### appointment
- **Module:** CRM
- **Submittable:** 0
- **Fields:** customer_details_section, customer_name, customer_phone_number, customer_skype, customer_details, scheduled_time, status, calendar_event, col_br_2, customer_email...
- **All Methods:** create_test_appointment, setUpClass, setUp, test_calendar_event_created, test_lead_linked...

### appointment_booking_settings
- **Module:** CRM
- **Submittable:** 0
- **Fields:** availability_of_slots, number_of_agents, holiday_list, appointment_duration, email_reminders, advance_booking_days, agent_list, enable_scheduling, agent_detail_section, appointment_details_section...
- **All Methods:** ...

### appointment_booking_slots
- **Module:** CRM
- **Submittable:** 0
- **Fields:** day_of_week, from_time, to_time...
- **All Methods:** ...

### availability_of_slots
- **Module:** CRM
- **Submittable:** 0
- **Fields:** day_of_week, from_time, to_time...
- **All Methods:** ...

### campaign
- **Module:** CRM
- **Submittable:** 0
- **Fields:** campaign, campaign_name, naming_series, campaign_schedules_section, campaign_schedules, description_section, description...
- **All Methods:** ...

### campaign_email_schedule
- **Module:** CRM
- **Submittable:** 0
- **Fields:** send_after_days, email_template...
- **All Methods:** ...

### competitor
- **Module:** CRM
- **Submittable:** 0
- **Fields:** competitor_name, website...
- **All Methods:** ...

### competitor_detail
- **Module:** CRM
- **Submittable:** 0
- **Fields:** competitor...
- **All Methods:** ...

### contract
- **Module:** CRM
- **Submittable:** 1
- **Fields:** party_type, is_signed, cb_party, party_name, party_user, status, fulfilment_status, sb_terms, start_date, cb_date...
- **All Methods:** get_contract, setUp, test_validate_start_date_before_end_date, test_unsigned_contract_status, test_active_signed_contract_status, test_past_inactive_signed_contract_status, test_future_inactive_signed_contract_status, test_contract_status_with_no_fulfilment_terms, test_unfulfilled_contract_status, test_fulfilled_contract_status...

### contract_fulfilment_checklist
- **Module:** CRM
- **Submittable:** 1
- **Fields:** fulfilled, cb_notes, requirement, sb_notes, notes, amended_from...
- **All Methods:** ...

### contract_template
- **Module:** CRM
- **Submittable:** 0
- **Fields:** title, contract_terms, sb_fulfilment, requires_fulfilment, fulfilment_terms, section_break_6, contract_template_help...
- **All Methods:** ...

### contract_template_fulfilment_terms
- **Module:** CRM
- **Submittable:** 0
- **Fields:** requirement...
- **All Methods:** ...

### crm_note
- **Module:** CRM
- **Submittable:** 0
- **Fields:** note, added_by, added_on...
- **All Methods:** ...

### crm_settings
- **Module:** CRM
- **Submittable:** 0
- **Fields:** campaign_naming_by, column_break_9, default_valid_till, section_break_5, allow_lead_duplication_based_on_emails, auto_creation_of_contact, opportunity_section, close_opportunity_after_days, column_break_4, quotation_section...
- **All Methods:** ...

### email_campaign
- **Module:** CRM
- **Submittable:** 0
- **Fields:** campaign_name, status, column_break_4, start_date, end_date, email_campaign_for, recipient, sender...
- **All Methods:** ...

### lead
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** create_event, create_todo, make_lead, test_make_customer, test_make_customer_from_organization, test_create_lead_and_unlinking_dynamic_links, test_prospect_creation_from_lead, test_opportunity_from_lead, test_copy_events_from_lead_to_prospect...

### lead_source
- **Module:** CRM
- **Submittable:** 0
- **Fields:** source_name, details...
- **All Methods:** ...

### linkedin_settings
- **Module:** CRM
- **Submittable:** 0
- **Fields:** account_name, oauth_details, consumer_key, consumer_secret, access_token, person_urn, column_break_5, user_details_section, session_status, column_break_2...
- **All Methods:** ...

### lost_reason_detail
- **Module:** CRM
- **Submittable:** 0
- **Fields:** lost_reason...
- **All Methods:** ...

### market_segment
- **Module:** CRM
- **Submittable:** 0
- **Fields:** market_segment...
- **All Methods:** ...

### opportunity
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** make_opportunity_from_lead, make_opportunity, create_communication, test_opportunity_status, test_make_new_lead_if_required, test_opportunity_item, test_carry_forward_of_email_and_comments...

### opportunity_item
- **Module:** CRM
- **Submittable:** 0
- **Fields:** item_code, col_break1, qty, item_group, brand, section_break_6, uom, item_name, description, column_break_8...
- **All Methods:** ...

### opportunity_lost_reason
- **Module:** CRM
- **Submittable:** 0
- **Fields:** lost_reason...
- **All Methods:** ...

### opportunity_lost_reason_detail
- **Module:** CRM
- **Submittable:** 0
- **Fields:** lost_reason...
- **All Methods:** ...

### opportunity_type
- **Module:** CRM
- **Submittable:** 0
- **Fields:** description...
- **All Methods:** ...

### prospect
- **Module:** CRM
- **Submittable:** 0
- **Fields:** company_name, industry, market_segment, customer_group, territory, column_break_6, no_of_employees, annual_revenue, fax, website...
- **All Methods:** make_prospect, make_address, test_add_lead_to_prospect_and_address_linking...

### prospect_lead
- **Module:** CRM
- **Submittable:** 0
- **Fields:** lead, lead_name, status, email, mobile_no, column_break_4, lead_owner...
- **All Methods:** ...

### prospect_opportunity
- **Module:** CRM
- **Submittable:** 0
- **Fields:** opportunity, amount, stage, probability, expected_closing, currency, column_break_4, deal_owner, contact_person...
- **All Methods:** ...

### sales_stage
- **Module:** CRM
- **Submittable:** 0
- **Fields:** stage_name...
- **All Methods:** ...

### social_media_post
- **Module:** CRM
- **Submittable:** 1
- **Fields:** text, image, twitter, linkedin, amended_from, content, post_status, twitter_post_id, linkedin_post_id, campaign_name...
- **All Methods:** ...

### twitter_settings
- **Module:** CRM
- **Submittable:** 0
- **Fields:** account_name, oauth_details, consumer_key, consumer_secret, column_break_5, profile_pic, session_status, access_token, access_token_secret...
- **API Methods:** callback, get_authorize_url
- **All Methods:** callback, get_authorize_url, get_access_token, get_api, post, upload_image, send_tweet, delete_tweet, get_tweet, api_error...

### code_list
- **Module:** EDI
- **Submittable:** 0
- **Fields:** title, publisher, version, description, canonical_uri, column_break_nkls, section_break_npxp, publisher_id, url, default_common_code...
- **All Methods:** ...

### common_code
- **Module:** EDI
- **Submittable:** 0
- **Fields:** code_list, title, column_break_wxsw, section_break_rhgh, applies_to, common_code, additional_data, description, canonical_uri...
- **All Methods:** ...

### exotel_settings
- **Module:** ERPNext Integrations
- **Submittable:** 0
- **Fields:** enabled, section_break_2, account_sid, api_token, api_key...
- **All Methods:** validate, verify_credentials...

### gocardless_mandate
- **Module:** ERPNext Integrations
- **Submittable:** 0
- **Fields:** disabled, customer, mandate, gocardless_customer...
- **All Methods:** ...

### gocardless_settings
- **Module:** ERPNext Integrations
- **Submittable:** 0
- **Fields:** gateway_name, section_break_2, access_token, webhooks_secret, use_sandbox, header_img...
- **All Methods:** ...

### mpesa_settings
- **Module:** ERPNext Integrations
- **Submittable:** 0
- **Fields:** payment_gateway_name, consumer_key, consumer_secret, till_number, sandbox, column_break_4, online_passkey, initiator_name, security_credential, account_balance...
- **All Methods:** create_mpesa_settings, get_test_account_balance_response, get_payment_request_response_payload, get_payment_callback_payload, get_account_balance_callback_payload, setUp, tearDown, test_creation_of_payment_gateway, test_processing_of_account_balance, test_processing_of_callback_payload...

### plaid_settings
- **Module:** ERPNext Integrations
- **Submittable:** 0
- **Fields:** enabled, automatic_sync, plaid_client_id, plaid_secret, plaid_env, column_break_2, section_break_4, column_break_7, enable_european_access...
- **All Methods:** setUp, tearDown, test_plaid_disabled, test_add_account_type, test_add_account_subtype, test_parent_bank_account_validation, test_new_transaction...

### quickbooks_migrator
- **Module:** ERPNext Integrations
- **Submittable:** 0
- **Fields:** status, application_settings, client_id, redirect_url, token_endpoint, application_column_break, client_secret, scope, api_endpoint, authorization_settings...
- **All Methods:** ...

### tally_migration
- **Module:** ERPNext Integrations
- **Submittable:** 0
- **Fields:** status, master_data, tally_creditors_account, column_break_2, tally_debtors_account, company_section, tally_company, column_break_8, erpnext_company, processed_files_section...
- **All Methods:** ...

### taxjar_nexus
- **Module:** ERPNext Integrations
- **Submittable:** 0
- **Fields:** region, region_code, country, country_code...
- **All Methods:** ...

### taxjar_settings
- **Module:** ERPNext Integrations
- **Submittable:** 0
- **Fields:** credentials, api_key, configuration, tax_account_head, shipping_account_head, is_sandbox, sandbox_api_key, taxjar_create_transactions, taxjar_calculate_tax, cb_keys...
- **All Methods:** ...

### woocommerce_settings
- **Module:** ERPNext Integrations
- **Submittable:** 0
- **Fields:** enable_sync, sb_00, woocommerce_server_url, secret, cb_00, api_consumer_key, api_consumer_secret, sb_accounting_details, tax_account, column_break_10...
- **API Methods:** generate_secret, get_series
- **All Methods:** generate_secret, get_series, validate, create_delete_custom_fields, validate_settings, create_webhook_url...

### e_commerce_settings
- **Module:** E-commerce
- **Submittable:** 0
- **Fields:** products_per_page, filter_categories_section, hide_variants, enable_field_filters, enable_attribute_filters, filter_fields, filter_attributes, enabled, store_page_docs, display_settings_section...
- **All Methods:** setup_e_commerce_settings, tearDown, test_tax_rule_validation, test_invalid_filter_fields...

### item_review
- **Module:** E-commerce
- **Submittable:** 0
- **Fields:** website_item, user, column_break_3, item, reviews_section, rating, comment, review_title, customer, published_on...
- **All Methods:** setUp, tearDown, test_add_and_get_item_reviews_from_customer, test_add_item_review_from_non_customer, test_add_item_reviews_from_guest_user...

### recommended_items
- **Module:** E-commerce
- **Submittable:** 0
- **Fields:** website_item, website_item_name, column_break_2, more_information_section, route, website_item_image, column_break_6, website_item_thumbnail, item_code...
- **All Methods:** ...

### website_item
- **Module:** E-commerce
- **Submittable:** 0
- **Fields:** web_item_name, column_break_3, item_code, item_name, section_break_6, route, ranking, slideshow, website_image, website_image_alt...
- **API Methods:** make_website_item, copy_specification_from_item_group
- **All Methods:** invalidate_cache_for_web_item, on_doctype_update, check_if_user_is_customer, make_website_item, autoname, onload, validate, on_update, on_trash, validate_duplicate_website_item...

### templates

### website_item_tabbed_section
- **Module:** E-commerce
- **Submittable:** 0
- **Fields:** label, content...
- **All Methods:** ...

### website_offer
- **Module:** E-commerce
- **Submittable:** 0
- **Fields:** offer_title, offer_subtitle, offer_details...
- **API Methods:** get_offer_details
- **All Methods:** get_offer_details...

### wishlist
- **Module:** E-commerce
- **Submittable:** 0
- **Fields:** user, section_break_2, items...
- **API Methods:** add_to_wishlist, remove_from_wishlist
- **All Methods:** add_to_wishlist, remove_from_wishlist...

### wishlist_item
- **Module:** E-commerce
- **Submittable:** 0
- **Fields:** item_code, website_item, column_break_3, item_name, item_details_section, description, column_break_7, image, image_view, warehouse_section...
- **All Methods:** ...

### loan
- **Module:** Loan Management
- **Submittable:** 1
- **Fields:** applicant_type, applicant, applicant_name, loan_application, loan_type, column_break_3, posting_date, company, status, section_break_8...
- **All Methods:** create_loan_scenario_for_penalty, create_loan_accounts, create_loan_type, create_loan_security_type, create_loan_security, create_loan_security_pledge, make_loan_disbursement_entry, create_loan_security_price, create_repayment_entry, create_loan_application...

### loan_application
- **Module:** Loan Management
- **Submittable:** 1
- **Fields:** applicant_type, applicant, applicant_name, column_break_2, posting_date, status, company, section_break_4, loan_type, loan_amount...
- **All Methods:** setUp, create_loan_application, test_loan_totals...

### loan_balance_adjustment
- **Module:** Loan Management
- **Submittable:** 1
- **Fields:** loan, applicant_type, applicant, column_break_3, company, posting_date, accounting_dimensions_section, cost_center, section_break_9, column_break_11...
- **All Methods:** ...

### loan_disbursement
- **Module:** Loan Management
- **Submittable:** 1
- **Fields:** against_loan, disbursement_date, disbursed_amount, amended_from, company, applicant, accounting_dimensions_section, cost_center, posting_date, column_break_4...
- **All Methods:** setUp, test_loan_topup, test_loan_topup_with_additional_pledge...

### loan_interest_accrual
- **Module:** Loan Management
- **Submittable:** 1
- **Fields:** loan, posting_date, pending_principal_amount, interest_amount, amended_from, applicant_type, applicant, column_break_4, interest_income_account, loan_account...
- **All Methods:** setUp, test_loan_interest_accural, test_accumulated_amounts...

### loan_refund
- **Module:** Loan Management
- **Submittable:** 1
- **Fields:** loan, applicant_type, applicant, column_break_3, company, posting_date, accounting_dimensions_section, cost_center, section_break_9, refund_account...
- **All Methods:** ...

### loan_repayment
- **Module:** Loan Management
- **Submittable:** 1
- **Fields:** against_loan, posting_date, payment_details_section, penalty_amount, interest_payable, column_break_3, applicant, loan_type, column_break_9, payable_amount...
- **All Methods:** ...

### loan_repayment_detail
- **Module:** Loan Management
- **Submittable:** 0
- **Fields:** loan_interest_accrual, paid_principal_amount, paid_interest_amount, accrual_type...
- **All Methods:** ...

### loan_security
- **Module:** Loan Management
- **Submittable:** 0
- **Fields:** loan_security_name, haircut, column_break_3, loan_security_type, loan_security_code, disabled, unit_of_measure...
- **All Methods:** ...

### loan_security_pledge
- **Module:** Loan Management
- **Submittable:** 1
- **Fields:** amended_from, applicant, loan_security_details_section, column_break_3, loan, loan_application, total_security_value, maximum_loan_value, loan_details_section, status...
- **All Methods:** ...

### loan_security_price
- **Module:** Loan Management
- **Submittable:** 0
- **Fields:** loan_security, column_break_2, uom, section_break_4, loan_security_price, section_break_6, valid_from, column_break_8, valid_upto, loan_security_type...
- **All Methods:** ...

### loan_security_shortfall
- **Module:** Loan Management
- **Submittable:** 0
- **Fields:** loan, loan_amount, security_value, shortfall_amount, section_break_3, shortfall_time, status, section_break_8, process_loan_security_shortfall, column_break_3...
- **All Methods:** ...

### loan_security_type
- **Module:** Loan Management
- **Submittable:** 0
- **Fields:** disabled, loan_security_type, haircut, unit_of_measure, column_break_5, loan_to_value_ratio...
- **All Methods:** ...

### loan_security_unpledge
- **Module:** Loan Management
- **Submittable:** 1
- **Fields:** loan_details_section, applicant, column_break_3, loan, status, unpledge_time, loan_security_details_section, amended_from, securities, company...
- **All Methods:** ...

### loan_type
- **Module:** Loan Management
- **Submittable:** 1
- **Fields:** loan_name, maximum_loan_amount, rate_of_interest, column_break_2, disabled, description, account_details_section, mode_of_payment, payment_account, loan_account...
- **All Methods:** ...

### loan_write_off
- **Module:** Loan Management
- **Submittable:** 1
- **Fields:** loan, posting_date, column_break_3, company, applicant_type, applicant, accounting_dimensions_section, cost_center, section_break_9, write_off_account...
- **All Methods:** ...

### pledge
- **Module:** Loan Management
- **Submittable:** 0
- **Fields:** loan_security, loan_security_type, loan_security_code, uom, qty, loan_security_price, haircut, amount, column_break_5, post_haircut_amount...
- **All Methods:** ...

### process_loan_interest_accrual
- **Module:** Loan Management
- **Submittable:** 1
- **Fields:** posting_date, amended_from, loan_type, loan, process_type, accrual_type...
- **All Methods:** ...

### process_loan_security_shortfall
- **Module:** Loan Management
- **Submittable:** 1
- **Fields:** amended_from, update_time...
- **All Methods:** ...

### proposed_pledge
- **Module:** Loan Management
- **Submittable:** 0
- **Fields:** loan_security_price, amount, haircut, qty, loan_security, post_haircut_amount, loan_security_name...
- **All Methods:** ...

### repayment_schedule
- **Module:** Loan Management
- **Submittable:** 0
- **Fields:** payment_date, principal_amount, interest_amount, total_payment, balance_loan_amount, is_accrued...
- **All Methods:** ...

### sanctioned_loan_amount
- **Module:** Loan Management
- **Submittable:** 0
- **Fields:** applicant_type, applicant, column_break_3, company, sanctioned_amount_limit...
- **All Methods:** ...

### unpledge
- **Module:** Loan Management
- **Submittable:** 0
- **Fields:** loan_security, loan_security_type, loan_security_code, uom, column_break_5, qty, haircut, loan_security_name...
- **All Methods:** ...

### maintenance_schedule
- **Module:** Maintenance
- **Submittable:** 1
- **Fields:** customer_details, naming_series, customer, column_break0, status, transaction_date, items_section, items, schedule, generate_schedule...
- **All Methods:** make_serial_item_with_serial, get_events, make_maintenance_schedule, test_events_should_be_created_and_deleted, test_make_schedule, test_serial_no_filters, test_schedule_with_serials...

### maintenance_schedule_detail
- **Module:** Maintenance
- **Submittable:** 0
- **Fields:** item_code, item_name, scheduled_date, actual_date, sales_person, serial_no, completion_status, column_break_3, section_break_6, column_break_8...
- **All Methods:** ...

### maintenance_schedule_item
- **Module:** Maintenance
- **Submittable:** 0
- **Fields:** item_code, item_name, description, schedule_details, start_date, end_date, periodicity, no_of_visits, sales_person, reference...
- **All Methods:** ...

### maintenance_visit
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** make_maintenance_visit, make_sales_person...

### maintenance_visit_purpose
- **Module:** Maintenance
- **Submittable:** 0
- **Fields:** item_code, item_name, serial_no, description, work_details, service_person, work_done, prevdoc_doctype, prevdoc_docname, column_break_3...
- **All Methods:** ...

### blanket_order
- **Module:** Manufacturing
- **Submittable:** 1
- **Fields:** naming_series, blanket_order_type, customer, customer_name, supplier, supplier_name, column_break_8, from_date, to_date, company...
- **All Methods:** make_blanket_order, setUp, test_sales_order_creation, test_purchase_order_creation, test_blanket_order_allowance, test_party_item_code...

### blanket_order_item
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** item_code, item_name, column_break_3, qty, rate, ordered_qty, section_break_7, terms_and_conditions, party_item_code...
- **All Methods:** ...

### bom
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** get_default_bom, level_order_traversal, create_nested_bom, reset_item_valuation_rate, create_bom_with_process_loss_item, create_process_loss_bom_items, create_process_loss_bom_item, test_get_items, test_get_items_exploded, test_get_items_list...

### bom_explosion_item
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** item_code, item_name, cb, source_warehouse, operation, section_break_3, description, column_break_2, image, image_view...
- **All Methods:** ...

### bom_item
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** item_code, item_name, operation, column_break_3, bom_no, source_warehouse, section_break_5, description, col_break1, image...
- **All Methods:** ...

### bom_operation
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** operation, workstation, description, col_break1, hour_rate, time_in_mins, fixed_time, operating_cost, base_hour_rate, base_operating_cost...
- **All Methods:** ...

### bom_scrap_item
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** item_code, item_name, quantity_and_rate, stock_qty, rate, amount, column_break_6, stock_uom, base_rate, base_amount...
- **All Methods:** ...

### bom_update_batch
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** level, batch_no, boms_updated, status...
- **All Methods:** ...

### bom_update_log
- **Module:** Manufacturing
- **Submittable:** 1
- **Fields:** current_bom, new_bom, column_break_3, update_type, status, amended_from, error_log, progress_section, processed_boms, bom_batches...
- **All Methods:** remove_bom, update_cost_in_all_boms_in_test, setUp, tearDown, test_bom_update_log_validate, test_bom_update_log_completion, test_bom_replace_for_root_bom...

### bom_update_tool
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** replace_bom_section, current_bom, new_bom, replace, update_cost_section, update_latest_price_in_all_boms...
- **All Methods:** tearDown, test_replace_bom, test_bom_cost...

### bom_website_item
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** item_code, item_name, description, qty, website_image...
- **All Methods:** ...

### bom_website_operation
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** operation, workstation, time_in_mins, website_image, thumbnail...
- **All Methods:** ...

### downtime_entry
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** workstation, from_time, to_time, column_break_4, operator, downtime_reason_section, downtime, stop_reason, column_break_9, remarks...
- **All Methods:** ...

### job_card
- **Module:** Manufacturing
- **Submittable:** 1
- **Fields:** work_order, bom_no, workstation, operation, column_break_4, posting_date, company, for_quantity, wip_warehouse, timing_detail...
- **All Methods:** create_bom_with_multiple_operations, make_wo_with_transfer_against_jc, make_bom_for_jc_tests, setUp, work_order, generate_required_stock, tearDown, test_job_card_operations, test_job_card_with_different_work_station, test_job_card_overlap...

### job_card_item
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** item_code, source_warehouse, uom, column_break_3, item_name, description, qty_section, required_qty, column_break_9, allow_alternative_item...
- **All Methods:** ...

### job_card_operation
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** status, completed_time, sub_operation, completed_qty...
- **All Methods:** ...

### job_card_scrap_item
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** item_code, item_name, column_break_3, description, quantity_and_rate, stock_qty, column_break_6, stock_uom...
- **All Methods:** ...

### job_card_time_log
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** from_time, to_time, column_break_2, time_in_mins, completed_qty, employee, operation...
- **All Methods:** ...

### manufacturing_settings
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** capacity_planning, allow_overtime, allow_production_on_holidays, column_break_3, capacity_planning_for_days, mins_between_operations, section_break_6, overproduction_percentage_for_sales_order, overproduction_percentage_for_work_order, backflush_raw_materials_based_on...
- **All Methods:** ...

### material_request_plan_item
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** item_code, item_name, warehouse, material_request_type, column_break_4, quantity, projected_qty, actual_qty, min_order_qty, section_break_8...
- **All Methods:** ...

### operation
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** make_operation...

### production_plan
- **Module:** Manufacturing
- **Submittable:** 1
- **Fields:** naming_series, company, get_items_from, column_break1, posting_date, filters, item_code, customer, warehouse, project...
- **All Methods:** create_production_plan, make_bom, setUp, tearDown, test_production_plan_mr_creation, test_production_plan_start_date, test_production_plan_for_existing_ordered_qty, test_production_plan_with_non_stock_item, test_production_plan_without_multi_level, test_production_plan_without_multi_level_for_existing_ordered_qty...

### production_plan_item
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** include_exploded_items, item_code, bom_no, planned_qty, column_break_6, warehouse, planned_start_date, section_break_9, pending_qty, ordered_qty...
- **All Methods:** ...

### production_plan_item_reference
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** sales_order, sales_order_item, qty, item_reference...
- **All Methods:** ...

### production_plan_material_request
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** material_request, col_break1, material_request_date...
- **All Methods:** ...

### production_plan_material_request_warehouse
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** warehouse...
- **All Methods:** ...

### production_plan_sales_order
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** sales_order, sales_order_date, col_break1, customer, grand_total...
- **All Methods:** ...

### production_plan_sub_assembly_item
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** item_name, column_break_3, work_order_details_section, column_break_7, qty, purchase_order, received_qty, bom_no, production_plan_item, parent_item_code...
- **All Methods:** ...

### routing
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** routing_name, disabled, operations...
- **All Methods:** setup_operations, create_routing, setup_bom, setUpClass, tearDownClass, test_sequence_id, test_update_bom_operation_time...

### sub_operation
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** operation, time_in_mins, column_break_5, description...
- **All Methods:** ...

### workstation
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** workstation_name, description, over_heads, hour_rate_electricity, hour_rate_consumable, column_break_11, hour_rate_rent, hour_rate_labour, hour_rate, working_hours_section...
- **All Methods:** get_data...

### workstation_type
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** workstation_type, over_heads, hour_rate_electricity, hour_rate_consumable, hour_rate_rent, hour_rate_labour, hour_rate, description, column_break_5, description_tab...
- **All Methods:** get_workstations, before_save, set_hour_rate...

### workstation_working_hour
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** start_time, column_break_2, end_time, enabled...
- **All Methods:** ...

### work_order
- **Module:** Manufacturing
- **Submittable:** 1
- **Fields:** item, naming_series, status, production_item, item_name, image, bom_no, allow_alternative_item, use_multi_level_bom, skip_transfer...
- **All Methods:** get_data...

### work_order_item
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** operation, item_code, source_warehouse, column_break_3, item_name, description, qty_section, required_qty, transferred_qty, allow_alternative_item...
- **All Methods:** on_doctype_update...

### work_order_operation
- **Module:** Manufacturing
- **Submittable:** 0
- **Fields:** details, operation, bom, description, completed_qty, status, workstation, estimated_time_and_cost, planned_start_time, planned_end_time...
- **All Methods:** ...

### homepage
- **Module:** Portal
- **Submittable:** 0
- **Fields:** company, hero_section_based_on, column_break_2, title, section_break_4, tag_line, description, hero_image, slideshow, hero_section...
- **All Methods:** test_homepage_load...

### homepage_featured_product
- **Module:** Portal
- **Submittable:** 0
- **Fields:** item_code, col_break1, item_name, view, section_break_5, description, column_break_7, image, thumbnail, route...
- **All Methods:** ...

### homepage_section
- **Module:** Portal
- **Submittable:** 0
- **Fields:** section_based_on, section_cards_section, section_cards, no_of_columns, custom_html_section, section_html, section_break_7, section_order...
- **All Methods:** test_homepage_section_custom_html...

### homepage_section_card
- **Module:** Portal
- **Submittable:** 0
- **Fields:** title, subtitle, image, content, route...
- **All Methods:** ...

### website_attribute
- **Module:** Portal
- **Submittable:** 0
- **Fields:** attribute...
- **All Methods:** ...

### website_filter_field
- **Module:** Portal
- **Submittable:** 0
- **Fields:** fieldname...
- **All Methods:** ...

### activity_cost
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** test_duplication...

### activity_type
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### dependent_task
- **Module:** Projects
- **Submittable:** 0
- **Fields:** task...
- **All Methods:** ...

### project
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** get_project, make_project, task_exists, calculate_end_date, test_project_with_template_having_no_parent_and_depend_tasks, test_project_template_having_parent_child_tasks, test_project_template_having_dependent_tasks, test_project_linking_with_sales_order, test_project_with_template_tasks_having_common_name...

### projects_settings
- **Module:** Projects
- **Submittable:** 0
- **Fields:** timesheet_sb, ignore_workstation_time_overlap, ignore_user_time_overlap, ignore_employee_time_overlap...
- **All Methods:** ...

### project_template
- **Module:** Projects
- **Submittable:** 0
- **Fields:** project_type, tasks...
- **All Methods:** make_project_template...

### project_template_task
- **Module:** Projects
- **Submittable:** 0
- **Fields:** task, subject...
- **All Methods:** ...

### project_type
- **Module:** Projects
- **Submittable:** 0
- **Fields:** project_type, description...
- **All Methods:** ...

### project_update
- **Module:** Projects
- **Submittable:** 1
- **Fields:** naming_series, project, sent, column_break_2, date, time, section_break_5, users, amended_from...
- **All Methods:** ...

### project_user
- **Module:** Projects
- **Submittable:** 0
- **Fields:** user, email, image, column_break_2, full_name, welcome_email_sent, view_attachments, section_break_5, project_status...
- **All Methods:** ...

### task
- **Module:** Projects
- **Submittable:** 0
- **Fields:** subject, project, issue, type, is_group, column_break0, status, priority, color, parent_task...
- **All Methods:** create_task, test_circular_reference, test_reschedule_dependent_task, test_close_assignment, test_overdue, assign, get_owner_and_status...

### task_depends_on
- **Module:** Projects
- **Submittable:** 0
- **Fields:** task, column_break_2, subject, project...
- **All Methods:** ...

### task_type
- **Module:** Projects
- **Submittable:** 0
- **Fields:** weight, description...
- **All Methods:** ...

### timesheet
- **Module:** Projects
- **Submittable:** 1
- **Fields:** title, naming_series, company, sales_invoice, column_break_3, status, employee_detail, employee, employee_name, department...
- **All Methods:** get_data...

### timesheet_detail
- **Module:** Projects
- **Submittable:** 0
- **Fields:** activity_type, from_time, section_break_3, expected_hours, hours, to_time, completed, project_details, project, column_break_2...
- **All Methods:** ...

### non_conformance
- **Module:** Quality Management
- **Submittable:** 0
- **Fields:** subject, procedure, status, section_break_4, details, process_owner, column_break_4, full_name, corrective_action, preventive_action...
- **All Methods:** ...

### quality_action
- **Module:** Quality Management
- **Submittable:** 0
- **Fields:** goal, date, procedure, status, corrective_preventive, cb_00, sb_00, resolutions, review, feedback...
- **All Methods:** ...

### quality_action_resolution
- **Module:** Quality Management
- **Submittable:** 0
- **Fields:** problem, resolution, status, responsible, completion_by...
- **All Methods:** ...

### quality_feedback
- **Module:** Quality Management
- **Submittable:** 0
- **Fields:** template, cb_00, sb_00, parameters, document_type, document_name...
- **All Methods:** test_quality_feedback...

### quality_feedback_parameter
- **Module:** Quality Management
- **Submittable:** 0
- **Fields:** parameter, cb_00, rating, sb_00, feedback...
- **All Methods:** ...

### quality_feedback_template
- **Module:** Quality Management
- **Submittable:** 0
- **Fields:** template, sb_00, parameters...
- **All Methods:** ...

### quality_feedback_template_parameter
- **Module:** Quality Management
- **Submittable:** 0
- **Fields:** parameter...
- **All Methods:** ...

### quality_goal
- **Module:** Quality Management
- **Submittable:** 0
- **Fields:** frequency, procedure, date, weekday, cb_00, sb_01, objectives, goal...
- **All Methods:** get_quality_goal, test_quality_goal...

### quality_goal_objective
- **Module:** Quality Management
- **Submittable:** 0
- **Fields:** objective, target, uom, cb_00...
- **All Methods:** ...

### quality_meeting
- **Module:** Quality Management
- **Submittable:** 0
- **Fields:** status, minutes, cb_00, sb_00, agenda, sb_01...
- **All Methods:** ...

### quality_meeting_agenda
- **Module:** Quality Management
- **Submittable:** 0
- **Fields:** agenda...
- **All Methods:** ...

### quality_meeting_minutes
- **Module:** Quality Management
- **Submittable:** 0
- **Fields:** sb_00, minute, document_type, cb_00, document_name...
- **All Methods:** ...

### quality_procedure
- **Module:** Quality Management
- **Submittable:** 0
- **Fields:** parent_quality_procedure, is_group, lft, rgt, old_parent, sb_00, processes, quality_procedure_name, process_owner, section_break_3...
- **All Methods:** create_procedure, test_add_node, test_remove_parent_from_old_child, remove_child_from_old_parent...

### quality_procedure_process
- **Module:** Quality Management
- **Submittable:** 0
- **Fields:** process_description, procedure...
- **All Methods:** ...

### quality_review
- **Module:** Quality Management
- **Submittable:** 0
- **Fields:** date, procedure, additional_information, cb_00, sb_00, sb_01, reviews, status, goal...
- **All Methods:** test_review_creation...

### quality_review_objective
- **Module:** Quality Management
- **Submittable:** 0
- **Fields:** objective, target, uom, review, sb_00, cb_00, status...
- **All Methods:** ...

### import_supplier_invoice
- **Module:** Regional
- **Submittable:** 0
- **Fields:** company, item_code, supplier_group, tax_account, column_break_5, zip_file, import_invoices, status, invoice_series, default_buying_price_list...
- **All Methods:** ...

### ksa_vat_purchase_account
- **Module:** Regional
- **Submittable:** 0
- **Fields:** account, title, item_tax_template...
- **All Methods:** ...

### ksa_vat_sales_account
- **Module:** Regional
- **Submittable:** 0
- **Fields:** account, title, item_tax_template...
- **All Methods:** ...

### ksa_vat_setting
- **Module:** Regional
- **Submittable:** 0
- **Fields:** company, ksa_vat_sales_accounts, ksa_vat_purchase_accounts...
- **All Methods:** ...

### lower_deduction_certificate
- **Module:** Regional
- **Submittable:** 0
- **Fields:** certificate_no, section_break_3, supplier, pan_no, validity_details_section, valid_upto, section_break_9, rate, certificate_limit, certificate_details_section...
- **All Methods:** ...

### product_tax_category
- **Module:** Regional
- **Submittable:** 0
- **Fields:** product_tax_code, description, category_name, column_break_2, section_break_4...
- **All Methods:** ...

### south_africa_vat_settings
- **Module:** Regional
- **Submittable:** 0
- **Fields:** company, vat_accounts...
- **All Methods:** ...

### uae_vat_account
- **Module:** Regional
- **Submittable:** 0
- **Fields:** account...
- **All Methods:** ...

### uae_vat_settings
- **Module:** Regional
- **Submittable:** 0
- **Fields:** company, uae_vat_accounts...
- **All Methods:** ...

### customer
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** get_customer_dict, set_credit_limit, create_internal_customer, setUp, tearDown, test_get_customer_group_details, test_party_details, test_party_details_tax_category, test_rename, test_freezed_customer...

### customer_credit_limit
- **Module:** Selling
- **Submittable:** 0
- **Fields:** credit_limit, column_break_2, company, bypass_credit_limit_check...
- **All Methods:** ...

### industry_type
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### installation_note
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### installation_note_item
- **Module:** Selling
- **Submittable:** 0
- **Fields:** item_code, serial_no, qty, description, prevdoc_detail_docname, prevdoc_docname, prevdoc_doctype...
- **All Methods:** ...

### party_specific_item
- **Module:** Selling
- **Submittable:** 0
- **Fields:** party_type, party, restrict_based_on, column_break_3, based_on_value...
- **All Methods:** create_party_specific_item, setUp, test_item_query_for_customer, test_item_query_for_supplier...

### product_bundle
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** make_product_bundle...

### product_bundle_item
- **Module:** Selling
- **Submittable:** 0
- **Fields:** item_code, qty, description, rate, uom...
- **All Methods:** ...

### quotation
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** enable_calculate_bundle_price, get_quotation_dict, make_quotation, test_make_quotation_without_terms, test_make_sales_order_terms_copied, test_do_not_add_ordered_items_in_new_sales_order, test_gross_profit, test_maintain_rate_in_sales_cycle_is_enforced, test_make_sales_order_with_different_currency, test_make_sales_order...

### quotation_item
- **Module:** Selling
- **Submittable:** 0
- **Fields:** item_code, customer_item_code, col_break1, item_name, section_break_5, description, image, image_view, quantity_and_rate, qty...
- **All Methods:** ...

### sales_order
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** compare_payment_schedules, make_sales_order, create_dn_against_so, get_reserved_qty, make_sales_order_workflow, setUpClass, tearDownClass, setUp, tearDown, test_sales_order_with_negative_rate...

### sales_order_item
- **Module:** Selling
- **Submittable:** 0
- **Fields:** item_code, customer_item_code, ensure_delivery_based_on_produced_serial_no, col_break1, item_name, section_break_5, description, delivery_date, image, image_view...
- **All Methods:** on_doctype_update...

### sales_partner_type
- **Module:** Selling
- **Submittable:** 0
- **Fields:** sales_partner_type...
- **All Methods:** ...

### sales_team
- **Module:** Selling
- **Submittable:** 0
- **Fields:** sales_person, contact_no, allocated_percentage, allocated_amount, commission_rate, incentives...
- **All Methods:** ...

### selling_settings
- **Module:** Selling
- **Submittable:** 0
- **Fields:** cust_master_name, customer_group, territory, selling_price_list, column_break_5, so_required, dn_required, sales_update_frequency, maintain_same_sales_rate, editable_price_list_rate...
- **All Methods:** test_defaults_populated...

### sms_center
- **Module:** Selling
- **Submittable:** 0
- **Fields:** send_to, customer, supplier, sales_partner, department, branch, create_receiver_list, receiver_list, column_break9, message...
- **API Methods:** create_receiver_list, send_sms
- **All Methods:** create_receiver_list, get_receiver_nos, send_sms...

### authorization_control
- **Module:** Setup
- **Submittable:** 0
- **Fields:** ...
- **All Methods:** get_appr_user_role, validate_auth_rule, bifurcate_based_on_type, validate_approving_authority, get_value_based_rule...

### authorization_rule
- **Module:** Setup
- **Submittable:** 0
- **Fields:** transaction, based_on, customer_or_item, master_name, column_break_3, company, section_break_17, value, section_break_7, system_role...
- **All Methods:** ...

### branch
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### brand
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### company
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** create_company_communication, create_child_company, create_test_lead_in_company, test_coa_based_on_existing_company, test_coa_based_on_country_template, delete_mode_of_payment, test_basic_tree, test_primary_address, get_no_of_children, test_change_parent_company...

### fixtures

### currency_exchange
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** save_new_records, patched_requests_get, clear_cache, tearDown, test_exchange_rate, test_exchange_rate_via_exchangerate_host, test_exchange_rate_strict, test_exchange_rate_strict_switched, __init__, raise_for_status...

### customer_group
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### department
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** create_department, test_remove_department_data...

### designation
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** create_designation...

### driver
- **Module:** Setup
- **Submittable:** 0
- **Fields:** naming_series, full_name, status, transporter, column_break_2, employee, cell_number, license_details, license_number, column_break_8...
- **All Methods:** ...

### driving_license_category
- **Module:** Setup
- **Submittable:** 0
- **Fields:** class, description, issuing_date, expiry_date...
- **All Methods:** ...

### email_digest
- **Module:** Setup
- **Submittable:** 0
- **Fields:** settings, column_break0, enabled, company, frequency, next_send, column_break1, accounts, accounts_module, income...
- **All Methods:** ...

### email_digest_recipient
- **Module:** Setup
- **Submittable:** 0
- **Fields:** recipient...
- **All Methods:** ...

### employee
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** make_employee, test_employee_status_left, test_user_has_employee, test_employee_user_permission, tearDown...

### employee_education
- **Module:** Setup
- **Submittable:** 0
- **Fields:** school_univ, qualification, level, year_of_passing, class_per, maj_opt_subj...
- **All Methods:** ...

### employee_external_work_history
- **Module:** Setup
- **Submittable:** 0
- **Fields:** company_name, designation, salary, address, contact, total_experience...
- **All Methods:** ...

### employee_group
- **Module:** Setup
- **Submittable:** 0
- **Fields:** employee_group_name, section_break_00, employee_list...
- **All Methods:** make_employee_group, get_employee_group...

### employee_group_table
- **Module:** Setup
- **Submittable:** 0
- **Fields:** employee, employee_name, user_id...
- **All Methods:** ...

### employee_internal_work_history
- **Module:** Setup
- **Submittable:** 0
- **Fields:** branch, department, designation, from_date, to_date...
- **All Methods:** ...

### global_defaults
- **Module:** Setup
- **Submittable:** 0
- **Fields:** default_company, country, default_distance_unit, column_break_8, default_currency, hide_currency_symbol, disable_rounded_total, disable_in_words...
- **All Methods:** ...

### holiday
- **Module:** Setup
- **Submittable:** 0
- **Fields:** holiday_date, description, weekly_off, column_break_2, section_break_4...
- **All Methods:** ...

### holiday_list
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** make_holiday_list, set_holiday_list, test_holiday_list, test_weekly_off, test_local_holidays, test_localized_country_names...

### incoterm
- **Module:** Setup
- **Submittable:** 0
- **Fields:** code, title, description...
- **All Methods:** ...

### item_group
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** test_basic_tree, get_no_of_children, test_recursion, test_rebuild_tree, move_it_back, test_move_group_into_another, test_move_group_into_root, print_tree, test_move_leaf_into_another_group, test_delete_leaf...

### party_type
- **Module:** Setup
- **Submittable:** 0
- **Fields:** party_type, account_type...
- **All Methods:** ...

### print_heading
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### quotation_lost_reason
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### quotation_lost_reason_detail
- **Module:** Setup
- **Submittable:** 0
- **Fields:** lost_reason...
- **All Methods:** ...

### sales_partner
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### sales_person
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### supplier_group
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### target_detail
- **Module:** Setup
- **Submittable:** 0
- **Fields:** item_group, fiscal_year, target_qty, target_amount, distribution_id...
- **All Methods:** ...

### terms_and_conditions
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### territory
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### transaction_deletion_record
- **Module:** Setup
- **Submittable:** 1
- **Fields:** company, doctypes, doctypes_to_be_ignored, amended_from, status, section_break_tbej, tasks_section, delete_bin_data, delete_leads_and_addresses, clear_notifications...
- **API Methods:** get_doctypes_to_be_ignored, is_deletion_doc_running, start_deletion_tasks
- **All Methods:** get_doctypes_to_be_ignored, is_deletion_doc_running, check_for_running_deletion_job, __init__, validate, validate_doctypes_to_be_ignored, generate_job_name_for_task, generate_job_name_for_next_tasks, generate_job_name_for_all_tasks, before_submit...

### transaction_deletion_record_item
- **Module:** Setup
- **Submittable:** 0
- **Fields:** doctype_name...
- **All Methods:** ...

### uom
- **Module:** Setup
- **Submittable:** 0
- **Fields:** uom_name, must_be_whole_number, enabled...
- **All Methods:** ...

### uom_conversion_factor
- **Module:** Setup
- **Submittable:** 0
- **Fields:** category, section_break_2, from_uom, to_uom, value...
- **All Methods:** ...

### vehicle
- **Module:** Setup
- **Submittable:** 0
- **Fields:** license_plate, make, column_break_3, model, vehicle_details, last_odometer, acquisition_date, location, column_break_8, chassis_no...
- **All Methods:** get_data...

### website_item_group
- **Module:** Setup
- **Submittable:** 0
- **Fields:** item_group...
- **All Methods:** ...

### batch
- **Module:** Stock
- **Submittable:** 0
- **Fields:** disabled, batch_id, item, image, parent_batch, manufacturing_date, column_break_3, expiry_date, source, supplier...
- **All Methods:** create_batch, create_price_list_for_batch, make_new_batch, test_item_has_batch_enabled, make_batch_item, test_purchase_receipt, test_stock_entry_incoming, test_delivery_note, test_delivery_note_fail, test_stock_entry_outgoing...

### bin
- **Module:** Stock
- **Submittable:** 0
- **Fields:** warehouse, item_code, reserved_qty, actual_qty, ordered_qty, indented_qty, planned_qty, projected_qty, reserved_qty_for_production, reserved_qty_for_sub_contract...
- **All Methods:** test_concurrent_inserts, test_index_exists...

### closing_stock_balance
- **Module:** Stock
- **Submittable:** 1
- **Fields:** naming_series, company, status, column_break_p0s0, from_date, to_date, filters_section, item_code, item_group, column_break_rm5w...
- **All Methods:** ...

### customs_tariff_number
- **Module:** Stock
- **Submittable:** 0
- **Fields:** tariff_number, description...
- **All Methods:** ...

### delivery_note
- **Module:** Stock
- **Submittable:** 1
- **Fields:** title, naming_series, customer, customer_name, column_break1, amended_from, company, posting_date, posting_time, set_posting_time...
- **All Methods:** create_delivery_note, test_over_billing_against_dn, test_delivery_note_no_gl_entry, test_delivery_note_gl_entry_packing_item, test_serialized, test_serialized_partial_sales_invoice, test_serialize_status, check_serial_no_values, test_sales_return_for_non_bundled_items_partial, test_sales_return_for_non_bundled_items_full...

### patches
- **All Methods:** execute...

### delivery_note_item
- **Module:** Stock
- **Submittable:** 0
- **Fields:** barcode, item_code, item_name, col_break1, customer_item_code, section_break_6, description, image, image_view, quantity_and_rate...
- **All Methods:** ...

### delivery_settings
- **Module:** Stock
- **Submittable:** 0
- **Fields:** sb_dispatch, dispatch_template, dispatch_attachment, send_with_attachment, cb_delivery, stop_delay...
- **All Methods:** ...

### delivery_stop
- **Module:** Stock
- **Submittable:** 0
- **Fields:** customer, address, locked, column_break_6, customer_address, visited, order_information_section, delivery_note, cb_order, grand_total...
- **All Methods:** ...

### delivery_trip
- **Module:** Stock
- **Submittable:** 1
- **Fields:** naming_series, company, column_break_2, email_notification_sent, section_break_3, driver, driver_name, total_distance, uom, column_break_4...
- **All Methods:** create_address, create_driver, create_delivery_notification, create_vehicle, create_delivery_trip, setUp, tearDown, test_delivery_trip_notify_customers, test_unoptimized_route_list_without_locks, test_unoptimized_route_list_with_locks...

### inventory_dimension
- **Module:** Stock
- **Submittable:** 0
- **Fields:** dimension_details_tab, reference_document, dimension_name, applicable_for_documents_tab, document_type, column_break_9, istable, condition, apply_to_all_doctypes, disabled...
- **All Methods:** get_voucher_sl_entries, create_store_dimension, prepare_test_data, create_inventory_dimension, prepare_data_for_internal_transfer, setUp, test_validate_inventory_dimension, test_delete_inventory_dimension, test_inventory_dimension, test_inventory_dimension_for_purchase_receipt_and_delivery_note...

### item
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** make_item, set_item_variant_settings, make_item_variant, create_item, setUp, get_item, test_get_item_details, test_get_asset_item_details, test_item_tax_template, test_item_defaults...

### item_alternative
- **Module:** Stock
- **Submittable:** 0
- **Fields:** item_code, alternative_item_code, two_way, column_break_4, item_name, alternative_item_name...
- **All Methods:** make_items, setUp, test_alternative_item_for_subcontract_rm, test_alternative_item_for_production_rm...

### item_attribute
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** setUp, test_numeric_item_attribute...

### item_attribute_value
- **Module:** Stock
- **Submittable:** 0
- **Fields:** attribute_value, abbr...
- **All Methods:** ...

### item_barcode
- **Module:** Stock
- **Submittable:** 0
- **Fields:** barcode, barcode_type, uom...
- **All Methods:** ...

### item_customer_detail
- **Module:** Stock
- **Submittable:** 0
- **Fields:** customer_name, customer_group, ref_code...
- **All Methods:** ...

### item_default
- **Module:** Stock
- **Submittable:** 0
- **Fields:** company, default_warehouse, column_break_3, default_price_list, purchase_defaults, buying_cost_center, default_supplier, column_break_8, expense_account, selling_defaults...
- **All Methods:** ...

### item_manufacturer
- **Module:** Stock
- **Submittable:** 0
- **Fields:** manufacturer, manufacturer_part_no, item_code, item_name, column_break_3, description, is_default...
- **All Methods:** ...

### item_price
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** setUp, test_template_item_price, test_duplicate_item, test_addition_of_new_fields, test_dates_validation_error, test_price_in_a_qty, test_price_with_no_qty, test_prices_at_date, test_prices_at_invalid_date, test_prices_outside_of_date...

### item_quality_inspection_parameter
- **Module:** Stock
- **Submittable:** 0
- **Fields:** specification, value, column_break_3, acceptance_formula, formula_based_criteria, min_value, max_value, numeric, parameter_group...
- **All Methods:** ...

### item_reorder
- **Module:** Stock
- **Submittable:** 0
- **Fields:** warehouse_group, warehouse, warehouse_reorder_level, warehouse_reorder_qty, material_request_type...
- **All Methods:** ...

### item_supplier
- **Module:** Stock
- **Submittable:** 0
- **Fields:** supplier, supplier_part_no...
- **All Methods:** ...

### item_tax
- **Module:** Stock
- **Submittable:** 0
- **Fields:** item_tax_template, tax_category, valid_from, maximum_net_rate, minimum_net_rate...
- **All Methods:** ...

### item_variant
- **Module:** Stock
- **Submittable:** 0
- **Fields:** item_attribute, item_attribute_value...
- **All Methods:** ...

### item_variant_attribute
- **Module:** Stock
- **Submittable:** 0
- **Fields:** variant_of, attribute, column_break_2, attribute_value, numeric_values, section_break_4, from_range, increment, column_break_8, to_range...
- **All Methods:** ...

### item_variant_settings
- **Module:** Stock
- **Submittable:** 0
- **Fields:** section_break_3, do_not_update_variants, allow_rename_attribute_value, copy_fields_to_variant, fields...
- **All Methods:** ...

### item_website_specification
- **Module:** Stock
- **Submittable:** 0
- **Fields:** label, description...
- **All Methods:** ...

### landed_cost_item
- **Module:** Stock
- **Submittable:** 0
- **Fields:** item_code, description, receipt_document_type, receipt_document, col_break2, qty, rate, amount, applicable_charges, purchase_receipt_item...
- **All Methods:** ...

### landed_cost_purchase_receipt
- **Module:** Stock
- **Submittable:** 0
- **Fields:** receipt_document_type, receipt_document, supplier, col_break1, posting_date, grand_total...
- **All Methods:** ...

### landed_cost_taxes_and_charges
- **Module:** Stock
- **Submittable:** 0
- **Fields:** description, col_break3, amount, expense_account, account_currency, exchange_rate, base_amount...
- **All Methods:** ...

### landed_cost_voucher
- **Module:** Stock
- **Submittable:** 1
- **Fields:** naming_series, company, purchase_receipts, purchase_receipt_items, get_items_from_purchase_receipts, items, sec_break1, taxes, section_break_9, total_taxes_and_charges...
- **All Methods:** make_landed_cost_voucher, create_landed_cost_voucher, distribute_landed_cost_on_items, test_landed_cost_voucher, assertPurchaseReceiptLCVGLEntries, test_landed_cost_voucher_stock_impact, test_landed_cost_voucher_for_zero_purchase_rate, test_landed_cost_voucher_against_purchase_invoice, test_landed_cost_voucher_for_serialized_item, test_serialized_lcv_delivered...

### manufacturer
- **Module:** Stock
- **Submittable:** 0
- **Fields:** short_name, full_name, website, country, logo, notes, address_contacts, address_html, column_break_8, contact_html...
- **All Methods:** ...

### material_request
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** get_in_transit_warehouse, make_material_request, test_make_purchase_order, test_make_supplier_quotation, test_make_stock_entry, test_in_transit_make_stock_entry, _insert_stock_entry, test_cannot_stop_cancelled_material_request, test_mr_changes_from_stopped_to_pending_after_reopen, test_cannot_submit_cancelled_mr...

### material_request_item
- **Module:** Stock
- **Submittable:** 0
- **Fields:** item_code, col_break1, item_name, section_break_4, description, image, quantity_and_warehouse, qty, uom, conversion_factor...
- **All Methods:** on_doctype_update...

### packed_item
- **Module:** Stock
- **Submittable:** 0
- **Fields:** parent_item, item_code, item_name, column_break_5, description, section_break_6, warehouse, target_warehouse, column_break_9, qty...
- **All Methods:** create_product_bundle, setUpClass, test_adding_bundle_item, test_updating_bundle_item, test_recurring_bundle_item, test_bundle_item_cumulative_price, test_newly_mapped_doc_packed_items, test_reposting_packed_items, assertReturns, test_returning_full_bundles...

### packing_slip
- **Module:** Stock
- **Submittable:** 1
- **Fields:** packing_slip_details, column_break0, delivery_note, column_break1, naming_series, section_break0, column_break2, from_case_no, column_break3, to_case_no...
- **All Methods:** create_items, test_packing_slip...

### packing_slip_item
- **Module:** Stock
- **Submittable:** 0
- **Fields:** item_code, column_break_2, item_name, batch_no, desc_section, description, quantity_section, qty, net_weight, column_break_10...
- **All Methods:** ...

### pick_list
- **Module:** Stock
- **Submittable:** 1
- **Fields:** company, column_break_4, section_break_6, parent_warehouse, customer, work_order, locations, for_qty, amended_from, purpose...
- **All Methods:** test_pick_list_picks_warehouse_for_each_item, test_pick_list_splits_row_according_to_warehouse_availability, test_pick_list_shows_serial_no_for_serialized_item, test_pick_list_shows_batch_no_for_batched_item, test_pick_list_for_batched_and_serialised_item, test_pick_list_for_items_from_multiple_sales_orders, test_pick_list_for_items_with_multiple_UOM, test_pick_list_grouping_before_print, test_multiple_dn_creation, test_picklist_with_multi_uom...

### pick_list_item
- **Module:** Stock
- **Submittable:** 0
- **Fields:** qty, picked_qty, warehouse, item_name, description, serial_no, batch_no, column_break_2, section_break_5, stock_uom...
- **All Methods:** ...

### price_list
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### price_list_country
- **Module:** Stock
- **Submittable:** 0
- **Fields:** country...
- **All Methods:** ...

### purchase_receipt
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** prepare_data_for_internal_transfer, get_sl_entries, get_gl_entries, get_taxes, get_items, make_purchase_receipt, setUp, test_purchase_receipt_received_qty, test_reverse_purchase_receipt_sle, test_make_purchase_invoice...

### purchase_receipt_item
- **Module:** Stock
- **Submittable:** 0
- **Fields:** barcode, section_break_2, item_code, supplier_part_no, column_break_2, item_name, section_break_4, description, image, image_view...
- **All Methods:** ...

### putaway_rule
- **Module:** Stock
- **Submittable:** 0
- **Fields:** item_code, item_name, warehouse, col_break_capacity, capacity, stock_uom, priority, company, disable, uom...
- **All Methods:** create_putaway_rule, setUp, assertUnchangedItemsOnResave, test_putaway_rules_priority, test_putaway_rules_with_same_priority, test_putaway_rules_with_insufficient_capacity, test_putaway_rules_multi_uom, test_putaway_rules_multi_uom_whole_uom, test_putaway_rules_with_reoccurring_item, test_validate_over_receipt_in_warehouse...

### quality_inspection
- **Module:** Stock
- **Submittable:** 1
- **Fields:** naming_series, report_date, column_break_4, inspection_type, reference_type, reference_name, section_break_7, item_code, item_serial_no, batch_no...
- **All Methods:** create_quality_inspection, create_quality_inspection_parameter, setUp, test_qa_for_delivery, test_qa_not_submit, test_value_based_qi_readings, test_formula_based_qi_readings, test_make_quality_inspections_from_linked_document, test_rejected_qi_validation, test_qi_status...

### quality_inspection_parameter
- **Module:** Stock
- **Submittable:** 0
- **Fields:** parameter, description, parameter_group...
- **All Methods:** ...

### quality_inspection_parameter_group
- **Module:** Stock
- **Submittable:** 0
- **Fields:** group_name...
- **All Methods:** ...

### quality_inspection_reading
- **Module:** Stock
- **Submittable:** 0
- **Fields:** specification, value, reading_1, reading_2, reading_3, reading_4, reading_5, reading_6, reading_7, reading_8...
- **All Methods:** ...

### quality_inspection_template
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** ...

### quick_stock_balance
- **Module:** Stock
- **Submittable:** 0
- **Fields:** warehouse, item, col_break, item_barcode, item_name, item_description, sec_break, qty, col_break2, value...
- **API Methods:** get_stock_item_details
- **All Methods:** get_stock_item_details...

### repost_item_valuation
- **Module:** Stock
- **Submittable:** 1
- **Fields:** item_code, warehouse, posting_date, posting_time, status, amended_from, column_break_5, error_section, error_log, company...
- **All Methods:** tearDown, test_repost_time_slot, test_clear_old_logs, test_create_item_wise_repost_item_valuation_entries, test_deduplication, test_stock_freeze_validation, test_prevention_of_cancelled_transaction_riv, test_queue_progress_serialization, test_gl_repost_progress, test_gl_complete_gl_reposting...

### sales_bom

### sales_bom_item

### serial_no
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** tearDown, test_cannot_create_direct, test_inter_company_transfer, test_inter_company_transfer_intermediate_cancellation, test_inter_company_transfer_fallback_on_cancel, test_auto_creation_of_serial_no, test_serial_no_sanitation, test_correct_serial_no_incoming_rate, test_auto_fetch...

### shipment
- **Module:** Stock
- **Submittable:** 1
- **Fields:** heading_pickup_from, pickup_from_type, pickup_company, pickup_customer, pickup_supplier, pickup, pickup_address_name, pickup_address, pickup_contact_name, pickup_contact_email...
- **All Methods:** create_test_delivery_note, create_test_shipment, get_shipment_customer_contact, get_shipment_customer_address, get_shipment_customer, get_shipment_company_address, get_shipment_company, get_shipment_item, create_shipment_address, create_customer_contact...

### shipment_delivery_note
- **Module:** Stock
- **Submittable:** 0
- **Fields:** delivery_note, grand_total...
- **All Methods:** ...

### shipment_parcel
- **Module:** Stock
- **Submittable:** 0
- **Fields:** length, width, height, weight, count...
- **All Methods:** ...

### shipment_parcel_template
- **Module:** Stock
- **Submittable:** 0
- **Fields:** length, width, height, weight, parcel_template_name...
- **All Methods:** ...

### stock_entry
- **Module:** N/A
- **Submittable:** 0
- **All Methods:** get_sle, make_serialized_item, get_qty_after_transaction, get_multiple_items, initialize_records_for_future_negative_sle_test, create_stock_entries, tearDown, test_fifo, test_auto_material_request, test_barcode_item_stock_entry...

### stock_entry_detail
- **Module:** Stock
- **Submittable:** 0
- **Fields:** barcode, section_break_2, s_warehouse, col_break1, t_warehouse, sec_break1, item_code, col_break2, item_name, section_break_8...
- **All Methods:** ...

### stock_entry_type
- **Module:** Stock
- **Submittable:** 0
- **Fields:** purpose, add_to_transit...
- **All Methods:** ...

### stock_ledger_entry
- **Module:** Stock
- **Submittable:** 0
- **Fields:** item_code, serial_no, batch_no, warehouse, posting_date, posting_time, voucher_type, voucher_no, voucher_detail_no, actual_qty...
- **All Methods:** create_repack_entry, create_product_bundle_item, create_items, setup_item_valuation_test, create_purchase_receipt_entries_for_batchwise_item_valuation_test, create_delivery_note_entries_for_batchwise_item_valuation_test, fetch_sle_details_for_doc_list, get_stock_value_from_q, create_stock_entry_entries_for_batchwise_item_valuation_test, get_unique_suffix...

### stock_reconciliation
- **Module:** Stock
- **Submittable:** 1
- **Fields:** naming_series, company, purpose, col1, posting_date, posting_time, set_posting_time, sb9, items, section_break_9...
- **All Methods:** create_batch_item_with_batch, insert_existing_sle, create_batch_or_serial_no_items, create_stock_reconciliation, set_valuation_method, setUpClass, tearDown, test_reco_for_fifo, test_reco_for_moving_average, _test_reco_sle_gle...

### stock_reconciliation_item
- **Module:** Stock
- **Submittable:** 0
- **Fields:** barcode, item_code, item_name, warehouse, column_break_6, qty, valuation_rate, amount, serial_no_and_batch_section, serial_no...
- **All Methods:** ...

### stock_reposting_settings
- **Module:** Stock
- **Submittable:** 0
- **Fields:** scheduling_section, start_time, end_time, limits_dont_apply_on, limit_reposting_timeslot, item_based_reposting, notify_reposting_error_to_role, errors_notification_section...
- **All Methods:** test_notify_reposting_error_to_role...

### stock_settings
- **Module:** Stock
- **Submittable:** 0
- **Fields:** item_naming_by, item_group, stock_uom, default_warehouse, sample_retention_warehouse, column_break_4, valuation_method, over_delivery_receipt_allowance, action_if_quality_inspection_is_not_submitted, show_barcode_field...
- **All Methods:** setUp, test_settings, test_clean_html...

### uom_category
- **Module:** Stock
- **Submittable:** 0
- **Fields:** category_name...
- **All Methods:** ...

### uom_conversion_detail
- **Module:** Stock
- **Submittable:** 0
- **Fields:** uom, conversion_factor...
- **All Methods:** ...

### variant_field
- **Module:** Stock
- **Submittable:** 0
- **Fields:** field_name...
- **All Methods:** ...

### warehouse
- **Module:** Stock
- **Submittable:** 0
- **Fields:** warehouse_detail, warehouse_name, is_group, company, disabled, column_break_4, account, address_and_contact, address_html, column_break_10...
- **API Methods:** get_children, add_node, convert_to_group_or_ledger
- **All Methods:** get_children, add_node, convert_to_group_or_ledger, get_child_warehouses, get_warehouses_based_on_account, apply_warehouse_filter, autoname, onload, validate, on_update...

### warehouse_type
- **Module:** Stock
- **Submittable:** 0
- **Fields:** description...
- **All Methods:** ...

### subcontracting_order
- **Module:** Subcontracting
- **Submittable:** 1
- **Fields:** title, naming_series, purchase_order, supplier, supplier_name, supplier_warehouse, column_break_7, company, transaction_date, schedule_date...
- **All Methods:** create_subcontracting_order, setUp, test_populate_items_table, test_set_missing_values, test_update_status, test_make_rm_stock_entry, test_make_rm_stock_entry_for_serial_items, test_make_rm_stock_entry_for_batch_items, test_make_rm_stock_entry_for_batch_items_with_less_transfer, test_update_reserved_qty_for_subcontracting...

### subcontracting_order_item
- **Module:** Subcontracting
- **Submittable:** 0
- **Fields:** item_code, item_name, column_break_3, schedule_date, expected_delivery_date, description_section, description, column_break_8, image, image_view...
- **All Methods:** ...

### subcontracting_order_service_item
- **Module:** Subcontracting
- **Submittable:** 0
- **Fields:** item_code, item_name, qty, rate, amount, fg_item, fg_item_qty, column_break_2, section_break_4, column_break_6...
- **All Methods:** ...

### subcontracting_order_supplied_item
- **Module:** Subcontracting
- **Submittable:** 0
- **Fields:** main_item_code, rm_item_code, column_break_3, stock_uom, conversion_factor, reserve_warehouse, column_break_6, bom_detail_no, reference_name, section_break_9...
- **All Methods:** ...

### subcontracting_receipt
- **Module:** Subcontracting
- **Submittable:** 1
- **Fields:** title, naming_series, supplier, supplier_name, column_break1, posting_date, posting_time, company, section_addresses, supplier_address...
- **All Methods:** make_return_subcontracting_receipt, get_items, setUp, test_subcontracting, test_available_qty_for_consumption, test_subcontracting_gle_fg_item_rate_zero, test_subcontracting_over_receipt, test_subcontracted_scr_for_multi_transfer_batches, test_subcontracting_receipt_partial_return, test_subcontracting_receipt_over_return...

### subcontracting_receipt_item
- **Module:** Subcontracting
- **Submittable:** 0
- **Fields:** item_code, column_break_2, item_name, section_break_4, description, image, image_view, received_and_accepted, received_qty, qty...
- **All Methods:** ...

### subcontracting_receipt_supplied_item
- **Module:** Subcontracting
- **Submittable:** 0
- **Fields:** main_item_code, rm_item_code, description, batch_no, serial_no, col_break1, required_qty, consumed_qty, stock_uom, rate...
- **All Methods:** ...

### issue
- **Module:** Support
- **Submittable:** 0
- **Fields:** subject_section, naming_series, subject, customer, raised_by, cb00, status, priority, issue_type, sb_details...
- **All Methods:** create_issue_and_communication, make_issue, create_customer, create_customer_group, create_territory, create_communication, setUp, test_response_time_and_resolution_time_based_on_different_sla, test_hold_time_on_replied, test_issue_close_after_on_hold...

### issue_priority
- **Module:** Support
- **Submittable:** 0
- **Fields:** description...
- **All Methods:** make_priorities, insert_priority, test_priorities...

### issue_type
- **Module:** Support
- **Submittable:** 0
- **Fields:** description...
- **All Methods:** ...

### pause_sla_on_status
- **Module:** Support
- **Submittable:** 0
- **Fields:** status...
- **All Methods:** ...

### service_day
- **Module:** Support
- **Submittable:** 0
- **Fields:** workday, section_break_2, start_time, column_break_3, end_time...
- **All Methods:** ...

### service_level_agreement
- **Module:** Support
- **Submittable:** 0
- **Fields:** service_level, holiday_list, column_break_2, agreement_details_section, start_date, column_break_7, end_date, response_and_resolution_time_section, support_and_resolution_section_break, support_and_resolution...
- **All Methods:** get_service_level_agreement, create_service_level_agreement, create_customer, create_customer_group, create_territory, create_service_level_agreements_for_issues, make_holiday_list, create_custom_doctype, make_lead, setUp...

### service_level_priority
- **Module:** Support
- **Submittable:** 0
- **Fields:** priority, sb_00, resolution_time, cb_00, cb_01, default_priority, response_time...
- **All Methods:** ...

### sla_fulfilled_on_status
- **Module:** Support
- **Submittable:** 0
- **Fields:** status...
- **All Methods:** ...

### support_search_source
- **Module:** Support
- **Submittable:** 0
- **Fields:** source_name, source_type, api_sb, base_url, query_options_sb, query_route, cb_1, search_term_param_name, response_options_sb, response_result_key_path...
- **All Methods:** ...

### support_settings
- **Module:** Support
- **Submittable:** 0
- **Fields:** issues_sb, close_issue_after_days, portal_sb, get_started_sections, show_latest_forum_posts, forum_sb, forum_url, get_latest_query, response_key_list, column_break_10...
- **All Methods:** ...

### warranty_claim
- **Module:** Support
- **Submittable:** 0
- **Fields:** naming_series, status, complaint_date, column_break0, serial_no, customer, section_break_7, complaint, issue_details, item_code...
- **API Methods:** make_maintenance_visit
- **All Methods:** make_maintenance_visit, get_feed, validate, on_cancel, on_update, _update_links...

### call_log
- **Module:** Telephony
- **Submittable:** 0
- **Fields:** id, from, to, status, duration, recording_url, medium, type, recording_html, section_break_19...
- **All Methods:** ...

### incoming_call_handling_schedule
- **Module:** Telephony
- **Submittable:** 0
- **Fields:** day_of_week, from_time, to_time, agent_group...
- **All Methods:** ...

### incoming_call_settings
- **Module:** Telephony
- **Submittable:** 0
- **Fields:** call_routing, greeting_message, agent_busy_message, agent_unavailable_message, column_break_2, section_break_6, call_handling_schedule...
- **All Methods:** ...

### telephony_call_type
- **Module:** Telephony
- **Submittable:** 1
- **Fields:** call_type, amended_from...
- **All Methods:** ...

### voice_call_settings
- **Module:** Telephony
- **Submittable:** 0
- **Fields:** user, greeting_message, agent_busy_message, agent_unavailable_message, call_receiving_device, column_break_3...
- **All Methods:** ...

### rename_tool
- **Module:** Utilities
- **Submittable:** 0
- **Fields:** select_doctype, file_to_rename, rename_log...
- **API Methods:** get_doctypes, upload
- **All Methods:** get_doctypes, upload...

### sms_log
- **Module:** Utilities
- **Submittable:** 0
- **Fields:** sender_name, sent_on, column_break0, message, sec_break1, no_of_requested_sms, requested_numbers, column_break1, no_of_sent_sms, sent_to...
- **All Methods:** ...

### video
- **Module:** Utilities
- **Submittable:** 0
- **Fields:** title, provider, url, column_break_4, publish_date, duration, section_break_7, description, like_count, view_count...
- **API Methods:** get_id_from_url, batch_update_youtube_data
- **All Methods:** is_tracking_enabled, get_frequency, update_youtube_data, get_formatted_ids, get_id_from_url, batch_update_youtube_data, validate, set_video_id, set_youtube_statistics, get_youtube_statistics...

### video_settings
- **Module:** Utilities
- **Submittable:** 0
- **Fields:** enable_youtube_tracking, api_key, frequency...
- **All Methods:** validate, validate_youtube_api_key...

## Custom API Endpoints
- **e_commerce:** 2 methods

## Custom Modules
- **accounts:** 5 files
- **accounts.custom:** 1 files
- **accounts.dashboard_chart_source.account_balance_timeline:** 1 files
- **accounts.notification.notification_for_new_fiscal_year:** 1 files
- **accounts.report:** 3 files
- **accounts.report.accounts_payable:** 2 files
- **accounts.report.accounts_payable_summary:** 1 files
- **accounts.report.accounts_receivable:** 2 files
- **accounts.report.accounts_receivable_summary:** 2 files
- **accounts.report.account_balance:** 2 files
- **accounts.report.asset_depreciations_and_balances:** 1 files
- **accounts.report.asset_depreciation_ledger:** 1 files
- **accounts.report.balance_sheet:** 2 files
- **accounts.report.bank_clearance_summary:** 1 files
- **accounts.report.bank_reconciliation_statement:** 2 files
- **accounts.report.billed_items_to_be_received:** 1 files
- **accounts.report.budget_variance_report:** 1 files
- **accounts.report.cash_flow:** 2 files
- **accounts.report.cheques_and_deposits_incorrectly_cleared:** 1 files
- **accounts.report.consolidated_financial_statement:** 1 files
- **accounts.report.customer_ledger_summary:** 1 files
- **accounts.report.deferred_revenue_and_expense:** 2 files
- **accounts.report.delivered_items_to_be_billed:** 1 files
- **accounts.report.dimension_wise_accounts_balance_report:** 1 files
- **accounts.report.general_and_payment_ledger_comparison:** 2 files
- **accounts.report.general_ledger:** 2 files
- **accounts.report.gross_and_net_profit_report:** 1 files
- **accounts.report.gross_profit:** 2 files
- **accounts.report.inactive_sales_items:** 1 files
- **accounts.report.invalid_ledger_entries:** 1 files
- **accounts.report.item_wise_purchase_register:** 2 files
- **accounts.report.item_wise_sales_register:** 2 files
- **accounts.report.payment_ledger:** 2 files
- **accounts.report.payment_period_based_on_invoice_date:** 1 files
- **accounts.report.pos_register:** 1 files
- **accounts.report.profitability_analysis:** 1 files
- **accounts.report.profit_and_loss_statement:** 1 files
- **accounts.report.purchase_invoice_trends:** 1 files
- **accounts.report.purchase_register:** 2 files
- **accounts.report.received_items_to_be_billed:** 1 files
- **accounts.report.sales_invoice_trends:** 1 files
- **accounts.report.sales_payment_summary:** 2 files
- **accounts.report.sales_register:** 2 files
- **accounts.report.share_balance:** 1 files
- **accounts.report.share_ledger:** 1 files
- **accounts.report.supplier_ledger_summary:** 1 files
- **accounts.report.tax_detail:** 1 files
- **accounts.report.tds_computation_summary:** 1 files
- **accounts.report.tds_payable_monthly:** 2 files
- **accounts.report.trial_balance:** 2 files
- **accounts.report.trial_balance_for_party:** 1 files
- **accounts.report.voucher_wise_balance:** 1 files
- **accounts.test:** 3 files
- **assets:** 1 files
- **assets.report.fixed_asset_register:** 1 files
- **buying:** 1 files
- **buying.report.procurement_tracker:** 1 files
- **buying.report.purchase_analytics:** 1 files
- **buying.report.purchase_order_analysis:** 1 files
- **buying.report.purchase_order_trends:** 1 files
- **buying.report.requested_items_to_order_and_receive:** 2 files
- **buying.report.subcontracted_item_to_be_received:** 2 files
- **buying.report.subcontracted_raw_materials_to_be_transferred:** 2 files
- **buying.report.subcontract_order_summary:** 1 files
- **buying.report.supplier_quotation_comparison:** 1 files
- **config:** 1 files
- **controllers:** 13 files
- **controllers.tests:** 7 files
- **crm:** 1 files
- **crm.report.campaign_efficiency:** 1 files
- **crm.report.first_response_time_for_opportunity:** 1 files
- **crm.report.lead_conversion_time:** 1 files
- **crm.report.lead_details:** 1 files
- **crm.report.lead_owner_efficiency:** 1 files
- **crm.report.lost_opportunity:** 1 files
- **crm.report.opportunity_summary_by_sales_stage:** 2 files
- **crm.report.prospects_engaged_but_not_converted:** 1 files
- **crm.report.sales_pipeline_analytics:** 2 files
- **domains:** 4 files
- **erpnext_integrations:** 4 files
- **erpnext_integrations.connectors:** 1 files
- **e_commerce:** 2 files
- **e_commerce.product_data_engine:** 4 files
- **e_commerce.shopping_cart:** 4 files
- **e_commerce.variant_selector:** 3 files
- **loan_management.dashboard_chart_source.top_10_pledged_loan_securities:** 1 files
- **loan_management.report.applicant_wise_loan_security_exposure:** 1 files
- **loan_management.report.loan_interest_report:** 1 files
- **loan_management.report.loan_repayment_and_closure:** 1 files
- **loan_management.report.loan_security_exposure:** 1 files
- **loan_management.report.loan_security_status:** 1 files
- **manufacturing:** 1 files
- **manufacturing.notification.material_request_receipt_notification:** 1 files
- **manufacturing.report:** 1 files
- **manufacturing.report.bom_explorer:** 1 files
- **manufacturing.report.bom_operations_time:** 1 files
- **manufacturing.report.bom_stock_calculated:** 2 files
- **manufacturing.report.bom_stock_report:** 2 files
- **manufacturing.report.bom_variance_report:** 1 files
- **manufacturing.report.cost_of_poor_quality_report:** 1 files
- **manufacturing.report.downtime_analysis:** 1 files
- **manufacturing.report.exponential_smoothing_forecasting:** 1 files
- **manufacturing.report.job_card_summary:** 1 files
- **manufacturing.report.process_loss_report:** 1 files
- **manufacturing.report.production_analytics:** 1 files
- **manufacturing.report.production_planning_report:** 1 files
- **manufacturing.report.production_plan_summary:** 1 files
- **manufacturing.report.quality_inspection_summary:** 1 files
- **manufacturing.report.work_order_consumed_materials:** 1 files
- **manufacturing.report.work_order_stock_report:** 1 files
- **manufacturing.report.work_order_summary:** 1 files
- **patches.v10_0:** 6 files
- **patches.v10_1:** 1 files
- **patches.v11_0:** 42 files
- **patches.v11_1:** 14 files
- **patches.v12_0:** 69 files
- **patches.v13_0:** 116 files
- **patches.v14_0:** 75 files
- **patches.v16_0:** 1 files
- **patches.v4_2:** 2 files
- **patches.v5_7:** 1 files
- **patches.v8_1:** 1 files
- **portal:** 1 files
- **projects:** 1 files
- **projects.report:** 1 files
- **projects.report.daily_timesheet_summary:** 1 files
- **projects.report.delayed_tasks_summary:** 2 files
- **projects.report.employee_billing_summary:** 1 files
- **projects.report.project_billing_summary:** 1 files
- **projects.report.project_summary:** 1 files
- **projects.report.project_wise_stock_tracking:** 1 files
- **projects.web_form.tasks:** 1 files
- **regional.address_template:** 2 files
- **regional.france:** 2 files
- **regional.italy:** 2 files
- **regional.report.electronic_invoice_register:** 1 files
- **regional.report.fichier_des_ecritures_comptables_[fec]:** 1 files
- **regional.report.irs_1099:** 1 files
- **regional.report.ksa_vat:** 1 files
- **regional.report.uae_vat_201:** 2 files
- **regional.report.vat_audit_report:** 2 files
- **regional.saudi_arabia:** 2 files
- **regional.saudi_arabia.wizard.operations:** 1 files
- **regional.south_africa:** 1 files
- **regional.turkey:** 1 files
- **regional.united_arab_emirates:** 2 files
- **regional.united_states:** 2 files
- **selling.page.point_of_sale:** 1 files
- **selling.page.sales_funnel:** 1 files
- **selling.report.address_and_contacts:** 1 files
- **selling.report.available_stock_for_packing_items:** 1 files
- **selling.report.customer_acquisition_and_loyalty:** 1 files
- **selling.report.customer_credit_balance:** 1 files
- **selling.report.customer_wise_item_price:** 1 files
- **selling.report.inactive_customers:** 1 files
- **selling.report.item_wise_sales_history:** 1 files
- **selling.report.lost_quotations:** 1 files
- **selling.report.payment_terms_status_for_sales_order:** 2 files
- **selling.report.pending_so_items_for_purchase_request:** 2 files
- **selling.report.quotation_trends:** 1 files
- **selling.report.sales_analytics:** 2 files
- **selling.report.sales_order_analysis:** 2 files
- **selling.report.sales_order_trends:** 1 files
- **selling.report.sales_partner_commission_summary:** 1 files
- **selling.report.sales_partner_target_variance_based_on_item_group:** 3 files
- **selling.report.sales_partner_transaction_summary:** 1 files
- **selling.report.sales_person_commission_summary:** 1 files
- **selling.report.sales_person_target_variance_based_on_item_group:** 2 files
- **selling.report.sales_person_wise_transaction_summary:** 1 files
- **selling.report.territory_target_variance_based_on_item_group:** 1 files
- **selling.report.territory_wise_sales:** 1 files
- **setup:** 5 files
- **setup.setup_wizard:** 1 files
- **setup.setup_wizard.data:** 1 files
- **setup.setup_wizard.operations:** 4 files
- **startup:** 4 files
- **stock:** 6 files
- **stock.dashboard:** 2 files
- **stock.dashboard_chart_source.warehouse_wise_stock_value:** 1 files
- **stock.report:** 1 files
- **stock.report.available_batch_report:** 1 files
- **stock.report.batch_item_expiry_status:** 1 files
- **stock.report.batch_wise_balance_history:** 1 files
- **stock.report.bom_search:** 1 files
- **stock.report.cogs_by_item_group:** 1 files
- **stock.report.delayed_item_report:** 1 files
- **stock.report.delayed_order_report:** 1 files
- **stock.report.delivery_note_trends:** 1 files
- **stock.report.fifo_queue_vs_qty_after_transaction_comparison:** 1 files
- **stock.report.incorrect_balance_qty_after_transaction:** 1 files
- **stock.report.incorrect_serial_no_valuation:** 1 files
- **stock.report.incorrect_stock_value_report:** 1 files
- **stock.report.itemwise_recommended_reorder_level:** 1 files
- **stock.report.item_prices:** 1 files
- **stock.report.item_price_stock:** 1 files
- **stock.report.item_shortage_report:** 2 files
- **stock.report.item_variant_details:** 1 files
- **stock.report.product_bundle_balance:** 1 files
- **stock.report.purchase_receipt_trends:** 1 files
- **stock.report.serial_no_ledger:** 1 files
- **stock.report.stock_ageing:** 2 files
- **stock.report.stock_analytics:** 2 files
- **stock.report.stock_and_account_value_comparison:** 1 files
- **stock.report.stock_balance:** 2 files
- **stock.report.stock_ledger:** 2 files
- **stock.report.stock_ledger_invariant_check:** 1 files
- **stock.report.stock_ledger_variance:** 1 files
- **stock.report.stock_projected_qty:** 1 files
- **stock.report.stock_qty_vs_serial_no_count:** 1 files
- **stock.report.supplier_wise_sales_analytics:** 1 files
- **stock.report.total_stock_summary:** 1 files
- **stock.report.warehouse_wise_item_balance_age_and_value:** 1 files
- **stock.report.warehouse_wise_stock_balance:** 1 files
- **stock.tests:** 3 files
- **support.report.first_response_time_for_issues:** 1 files
- **support.report.issue_analytics:** 2 files
- **support.report.issue_summary:** 1 files
- **support.report.support_hour_distribution:** 1 files
- **support.web_form.issues:** 1 files
- **templates:** 1 files
- **templates.pages:** 14 files
- **templates.pages.integrations:** 2 files
- **tests:** 11 files
- **utilities:** 7 files
- **utilities.report.youtube_interactions:** 1 files
- **utilities.web_form.addresses:** 1 files
- **www:** 1 files
- **www.all-products:** 1 files
- **www.book_appointment:** 1 files
- **www.book_appointment.verify:** 1 files
- **www.shop-by-category:** 1 files
- **www.support:** 1 files

