# Copyright (c) 2019, Ivyngton Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


from frappe.model.document import Document


class WebsiteFilterField(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		fieldname: DF.Autocomplete | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
	# end: auto-generated types

	pass
