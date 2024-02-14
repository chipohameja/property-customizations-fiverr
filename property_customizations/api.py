import frappe

def cancel_contract(doc, method):
	if doc.custom_tenancy:
		tenancy_doc = frappe.get_doc("Tenancy", doc.custom_tenancy)
		tenancy_doc.flags.ignore_links = True
		tenancy_doc.cancel()

@frappe.whitelist()
def create_tenancy(doc, method):
	property_asset_doc = frappe.get_doc("Asset", doc.custom_property)

	new_tenancy = frappe.get_doc({
		"doctype": "Tenancy",
		"custom_contract": doc.name,
		"asset": doc.custom_property,
		"tenant": doc.party_name,
		"company": frappe.defaults.get_user_default("Company")
	})

	for row in property_asset_doc.schedules:
		new_tenancy.append("tenant_schedule", {
			"schedule_date": row.schedule_date,
			"tenant_schedule_id": row.name,
			"amount": row.depreciation_amount,
			"total_amount": row.accumulated_depreciation_amount,
		})

	new_tenancy.insert()
	new_tenancy.submit()

	doc.custom_tenancy = new_tenancy.name