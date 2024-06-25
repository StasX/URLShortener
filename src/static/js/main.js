
function reverse(url) {
    const result = $("#result");
    $.post("/geturl", { "url": url }).done((data) => {
        result.val(data.url);
        result.css({ "display": "block" });       
        console.log(data)
    }).fail((err) => {
        result.val("Something went wrong.");
        result.css({ "display": "block" });
    });
}

$(document).ready(() => {
    $("#reverse").click(() => {
        const url = $("#url").val();
        if (/^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$/.test(url)) {
            reverse(url);
        } else {
            const result = $("#result");
            result.val("Invalid url.");
            result.css({ "display": "block" });
        }

    });
});