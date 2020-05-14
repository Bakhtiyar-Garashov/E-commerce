function togglePasswordField() {
    var pwrdField = document.getElementById('InputPassword1'); // get password field by id
    if (pwrdField.type === "password") { //if type is pswrd, make it text to show
        pwrdField.type = "text";
    } else {
        pwrdField.type = "password"; //if type is not pswrd, make it pswrd
    }

}