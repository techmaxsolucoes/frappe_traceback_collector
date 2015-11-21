frappe.listview_settings["Stack"] = {
    add_fields: ["parent_stack", "relapsed", "seen"],
    filters:[
        ["parent_stack","=",null],
        ["seen", "=", false]
    ],
    get_indicator: function(doc){
        if (doc.parent_stack && doc.parent_stack.length){
            return [__("Relapsed"), !doc.seen ? "orange" : "blue", "parent_stack,!=,"];
        } else {
            return [__("First Level"), !doc.seen ? "red" : "green", "parent_stack,=,"];
        }
    },
    order_by: "relapsed desc"
}