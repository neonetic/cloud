from __future__ import unicode_literals

import frappe, os

from frappe.utils.email_lib.html2text import html2text

def execute():
	for page in frappe.conn.sql("""select * from `tabWeb Page`""", as_dict=1):
		# get parents
		
		route = frappe.conn.get_value("Website Route", {"ref_doctype":"Web Page", "docname": page.name},
			["name", "lft", "rgt"], as_dict=1)
			
		if route and page.parent_website_route:
			path = frappe.get_app_path("frappe_io", "templates", "statics", 
				*page.parent_website_route.split("/"))
				
			print path
			if not os.path.exists(path):
				os.makedirs(path)

			index_txt_path = os.path.join(path, "index.txt")
			if not os.path.exists(index_txt_path):
				with open(index_txt_path, "w") as f:
					f.write("\n".join(frappe.conn.sql_list("""select name from `tabWeb Page` 
						where parent_website_route=%s order by idx""", page.parent_website_route)))

			index_md = os.path.join(path, "index.md")
			if not os.path.exists(index_md):
				with open(index_md, "w") as f:
					f.write("")
				
			page_name = route.name.split("/")[-1]
			with open(os.path.join(path, page_name + ".md"), "w") as mdfile:
				mdfile.write(html2text(page.main_section or "").encode("utf-8"))
			
			# parents = frappe.conn.sql("""select name from `tabWebsite Route` where lft < %s and rgt > %s
			# 	order by lft asc""", (route.lft, route.rgt))
			
