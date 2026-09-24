# Copyright (c) 2026, Yasmina Hussein and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class TeamMember(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from digital_transformation.digital_transformation_website.doctype.projects.projects import Projects
		from digital_transformation.digital_transformation_website.doctype.specialization_tag.specialization_tag import SpecializationTag
		from frappe.types import DF

		bio: DF.SmallText | None
		department: DF.Literal["", "Leadership", "Product", "Technology", "Volunteers", "Contributors"]
		full_name: DF.Data | None
		linked_projects: DF.TableMultiSelect[Projects]
		photo: DF.AttachImage | None
		profile_slug: DF.Data | None
		role_title: DF.Data | None
		spacialization: DF.Table[SpecializationTag]
	# end: auto-generated types

	_DOCTYPE_NAME = "Team Member"
