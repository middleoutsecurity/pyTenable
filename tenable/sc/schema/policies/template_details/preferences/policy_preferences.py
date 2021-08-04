'''
template details - preference key schema class for TenableSC template_details endpoint
'''
from marshmallow import Schema, fields


class PolicyTemplateDetailsPreferences(Schema):
    '''schema structure for policy_template_details api preferences dict response'''
    abort_generic_webapp_if_login_fails = fields.Bool(allow_none=True)
    adsi_query = fields.Bool(allow_none=True)
    arp_ping = fields.Bool(allow_none=True)
    auto_accept_disclaimer = fields.Bool(allow_none=True)
    av_grace_period = fields.Int(allow_none=True)
    cert_expiry_warning_days = fields.Int(allow_none=True)
    check_crl = fields.Bool(allow_none=True)
    combo_arg_values = fields.Str(allow_none=True)
    custom_find_filepath_exclusions = fields.Str(allow_none=True)
    custom_find_filesystem_exclusions = fields.Str(allow_none=True)
    detect_ssl = fields.Bool(allow_none=True)
    disable_dns_resolution = fields.Bool(allow_none=True)
    display_unicode_characters = fields.Bool(allow_none=True)
    display_unreachable_hosts = fields.Bool(allow_none=True)
    enable_file_scanning = fields.Bool(allow_none=True)
    enable_filescan_programdata = fields.Bool(allow_none=True)
    enable_filescan_programfiles = fields.Bool(allow_none=True)
    enable_filescan_programfilesx86 = fields.Bool(allow_none=True)
    enable_filescan_systemroot = fields.Bool(allow_none=True)
    enable_filescan_userprofiles = fields.Bool(allow_none=True)
    enum_domain_users_end_uid = fields.Int(allow_none=True)
    enum_domain_users_start_uid = fields.Int(allow_none=True)
    enum_local_users_end_uid = fields.Int(allow_none=True)
    enum_local_users_start_uid = fields.Int(allow_none=True)
    enumerate_all_ciphers = fields.Bool(allow_none=True)
    fast_network_discovery = fields.Bool(allow_none=True)
    filescan_custom_dir = fields.Str(allow_none=True)
    generateXCCDFResults = fields.Bool(allow_none=True)
    generic_webapp_tests = fields.Bool(allow_none=True)
    generic_webapp_tests_max_time = fields.Int(allow_none=True)
    host_tagging = fields.Bool(allow_none=True)
    host_whitelist = fields.Str(allow_none=True)
    http_param_pollution = fields.Bool(allow_none=True)
    hydra_add_other_accounts = fields.Bool(allow_none=True)
    hydra_always_enable = fields.Bool(allow_none=True)
    hydra_cisco_logon_pw = fields.Str(allow_none=True)
    hydra_empty_passwords = fields.Bool(allow_none=True)
    hydra_exit_on_success = fields.Bool(allow_none=True)
    hydra_ldap_dn = fields.Str(allow_none=True)
    hydra_login_as_pw = fields.Bool(allow_none=True)
    hydra_logins_file = fields.Str(allow_none=True)
    hydra_parallel_tasks = fields.Int(allow_none=True)
    hydra_passwords_file = fields.Str(allow_none=True)
    hydra_postgresql_db_name = fields.Str(allow_none=True)
    hydra_proxy_test_site = fields.Str(allow_none=True)
    hydra_timeout = fields.Int(allow_none=True)
    hydra_web_page = fields.Str(allow_none=True)
    hydra_win_account_type = fields.Str(allow_none=True)
    hydra_win_pw_as_hash = fields.Bool(allow_none=True)
    icmp_ping = fields.Bool(allow_none=True)
    icmp_ping_retries = fields.Int(allow_none=True)
    icmp_unreach_means_host_down = fields.Bool(allow_none=True)
    log_live_hosts = fields.Bool(allow_none=True)
    max_checks_per_host = fields.Int(allow_none=True)
    max_hosts_per_scan = fields.Int(allow_none=True)
    modbus_end_reg = fields.Str(allow_none=True)
    modbus_start_reg = fields.Int(allow_none=True)
    network_receive_timeout = fields.Int(allow_none=True)
    network_type = fields.Str(allow_none=True)
    only_portscan_if_enum_failed = fields.Bool(allow_none=True)
    ping_the_remote_host = fields.Bool(allow_none=True)
    portscan_range = fields.Str(allow_none=True)
    provided_creds_only = fields.Bool(allow_none=True)
    reduce_connections_on_congestion = fields.Bool(allow_none=True)
    report_paranoia = fields.Str(allow_none=True)
    report_superseded_patches = fields.Bool(allow_none=True)
    report_verbosity = fields.Str(allow_none=True)
    request_windows_domain_info = fields.Bool(allow_none=True)
    reverse_lookup = fields.Bool(allow_none=True)
    rid_brute_forcing = fields.Bool(allow_none=True)
    safe_checks = fields.Bool(allow_none=True)
    samr_enumeration = fields.Bool(allow_none=True)
    scan_malware = fields.Bool(allow_none=True)
    scan_netware_hosts = fields.Bool(allow_none=True)
    scan_network_printers = fields.Bool(allow_none=True)
    scan_ot_devices = fields.Bool(allow_none=True)
    scan_webapps = fields.Bool(allow_none=True)
    silent_dependencies = fields.Bool(allow_none=True)
    smtp_domain = fields.Str(allow_none=True)
    smtp_from = fields.Str(allow_none=True)
    smtp_to = fields.Str(allow_none=True)
    snmp_scanner = fields.Bool(allow_none=True)
    ssh_netstat_scanner = fields.Bool(allow_none=True)
    ssl_prob_ports = fields.Str(allow_none=True)
    start_cotp_tsap = fields.Int(allow_none=True)
    stop_at_first_flaw = fields.Str(allow_none=True)
    stop_cotp_tsap = fields.Int(allow_none=True)
    stop_scan_on_disconnect = fields.Bool(allow_none=True)
    svc_detection_on_all_ports = fields.Bool(allow_none=True)
    syn_firewall_detection = fields.Str(allow_none=True)
    syn_scanner = fields.Bool(allow_none=True)
    tcp_firewall_detection = fields.Str(allow_none=True)
    tcp_ping = fields.Bool(allow_none=True)
    tcp_ping_dest_ports = fields.Str(allow_none=True)
    tcp_scanner = fields.Bool(allow_none=True)
    test_default_oracle_accounts = fields.Bool(allow_none=True)
    test_embedded_web_servers = fields.Bool(allow_none=True)
    test_local_nessus_host = fields.Bool(allow_none=True)
    thorough_tests = fields.Bool(allow_none=True)
    try_all_http_methods = fields.Bool(allow_none=True)
    udp_ping = fields.Bool(allow_none=True)
    udp_scanner = fields.Bool(allow_none=True)
    unscanned_closed = fields.Bool(allow_none=True)
    url_for_rfi = fields.Str(allow_none=True)
    use_kernel_congestion_detection = fields.Str(allow_none=True)
    user_agent_string = fields.Str(allow_none=True)
    verify_open_ports = fields.Bool(allow_none=True)
    webcrawl_exclude_regex = fields.Str(allow_none=True)
    webcrawl_follow_dynamic_pages = fields.Bool(allow_none=True)
    webcrawl_max_depth = fields.Int(allow_none=True)
    webcrawler_max_pages = fields.Int(allow_none=True)
    webcrawler_start_page = fields.Str(allow_none=True)
    win_known_bad_hashes = fields.Str(allow_none=True)
    win_known_good_hashes = fields.Str(allow_none=True)
    wmi_netstat_scanner = fields.Bool(allow_none=True)
    wmi_query = fields.Bool(allow_none=True)
    wol_mac_addresses = fields.Str(allow_none=True)
    wol_wait_time = fields.Int(allow_none=True)
    yarascan_rules_file = fields.Str(allow_none=True)