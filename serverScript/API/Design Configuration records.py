# US-2025-0646 -- Design Performance after Design Configuration (full script was changed)
# get_list is not fetching the child table details
#so used get_docs to fetch full records
la_design_config_name = frappe.get_all(
    'Design Configuration', 
    fields=["name"],
)

# Step 2: Use get_doc to fetch full docs (includes child tables)
la_design_configuration = [
    frappe.get_doc("Design Configuration", l_name)
    for l_name in la_design_config_name
]

frappe.flags = la_design_configuration
frappe.response['message'] = la_design_configuration