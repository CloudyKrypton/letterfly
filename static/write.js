function sendLetter() {
    const html = quill.getSemanticHTML(0);
    const text = quill.getText(0);
    console.log(text);

    window.location.href = "/send";
}
