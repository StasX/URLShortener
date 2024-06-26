// Check if url valid
const isUrl = (url) => /^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$/.test(url);

// Display full Url
function showFullUrl(txt) {
    const result = $("#result");
    result.val(txt);
    result.css({ "display": "block" });
}
// Display short Url
function showShortedUrl(txt) {
    const shortUrl = $("#shortedUrl");
    shortUrl.val(txt);
    shortUrl.css({ "display": "block" });
}

// Get Full Url
function getFullUrl(url) {
    $.post("/geturl", { "url": url })
        .done((data) => showFullUrl(data.url))
        .fail((err) => showFullUrl("Something went wrong."));
}

function reverse() {
    const url = $("#url").val();
    isUrl(url) ? getFullUrl(url) : showFullUrl("Invalid url.");
}

// Generate Short Url
function getShortUrl(url) {

    $.post("/short", { "url": url })
        .done((data) => showShortedUrl(data.url))
        .fail((err) => showShortedUrl("Something went wrong."));
}

function shortIt() {
    const url = $("#fullUrl").val();
    isUrl(url) ? getShortUrl(url) : showShortedUrl("Invalid url.");
}

// Load document
$(document).ready(() => {
    // Add handlers to buttons and inputs
    $("#reverse").click(reverse);
    $("#url").on('keypress', function (e) {
        if (e.which == 13) reverse();
    });
    $("#shortIt").click(shortIt);
    $("#fullUrl").on('keypress', function (e) {
        if (e.which == 13) shortIt();
    });
});