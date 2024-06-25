function showResult(txt) {
    const result = $("#result");
    result.val(txt);
    result.css({ "display": "block" });
}

function reverse() {
    const url = $("#url").val();
    if (/^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$/.test(url)) {
        getUrl(url);
    } else {
        showResult("Invalid url.");
    }
}

function getUrl(url) {
    $.post("/geturl", { "url": url })
        .done((data) => showResult(data.url))
        .fail((err) => showResult("Something went wrong."));
}

$(document).ready(() => {
    $("#reverse").click(reverse);
    $("#url").on('keypress', function (e) {
        if (e.which == 13) reverse();
    });
});