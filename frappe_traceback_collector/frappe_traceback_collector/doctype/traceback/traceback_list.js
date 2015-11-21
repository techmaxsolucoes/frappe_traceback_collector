frappe.listview_settings["Traceback"] = {
    add_fields: ["parent_traceback", "relapses"],
    filters:[["parent_traceback","=",null]],
    get_indicator: function(doc){
        if (doc.parent_traceback && doc.parent_traceback.length){
            return [__("Relapse"), "orange", "parent_traceback,!=,"];
        } else {
            return [__("First Level"), "red", "parent_traceback,=,"];
        }
    },
    order_by: "relapses desc"
}