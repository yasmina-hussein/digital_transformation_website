# Copyright (c) 2026, Yasmina Hussein and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PortfolioProject(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from digital_transformation.digital_transformation_website.doctype.portfolio_project_country.portfolio_project_country import PortfolioProjectCountry
		from digital_transformation.digital_transformation_website.doctype.tech_stack.tech_stack import TechStack
		from frappe.types import DF

		category: DF.Literal["", "Platforms", "Digital Products", "Data Services"]
		countries: DF.TableMultiSelect[PortfolioProjectCountry]
		description: DF.TextEditor | None
		image: DF.AttachImage | None
		tech_stack: DF.TableMultiSelect[TechStack]
		thematic_area: DF.Link | None
		title: DF.Data | None
		year: DF.Int
	# end: auto-generated types

	_DOCTYPE_NAME = "Portfolio Project"
