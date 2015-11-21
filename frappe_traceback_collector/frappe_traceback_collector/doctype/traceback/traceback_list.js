frappe.listview_settings["Traceback"] = {
    add_fields: ["parent_traceback", "relapses", "seen"],
    filters:[
        ["parent_traceback","=",null],
        ["seen", "=", false]
    ],
    get_indicator: function(doc){
        if (doc.parent_traceback && doc.parent_traceback.length){
            return [__("Relapsed"), !doc.seen ? "orange" : "blue", "parent_traceback,!=,"];
        } else {
            return [__("First Level"), !doc.seen ? "red" : "green", "parent_traceback,=,"];
        }
    },
    order_by: "relapses desc"
}