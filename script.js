var x = 0;

function changeText() {
    // Get the paragraph element by its id
    var paragraph = document.getElementById("pingpong");

    // Change the text content
    if (x == 0) {
        paragraph.innerHTML = "Ping!";
        x = 1;
    }
    else if (x == 1) {
        paragraph.innerHTML = "Pong!"
        x = 2;
    }
    else {
        paragraph.innerHTML = "Ping!";
        x = 1;
    }
}