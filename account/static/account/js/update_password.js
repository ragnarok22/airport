$(document).ready(function () {
    password = $('#id_password');
    repeat = $('#repeat');
    submit = $('#submit');
    submit.click(function (event) {
        if(password.val() != repeat.val()){
            event.preventDefault();
            alert("Error: son diferentes");
        }
    });
});