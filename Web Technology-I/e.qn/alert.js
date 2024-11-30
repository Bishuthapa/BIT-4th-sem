/*var name = document.getElementById("name");
var password = document.getElementById("password");
var email = document.getElementById("email");
var country = document.getElementById("country");

function validateForm() {
    if(name.value.length < 5) {
        alert("Username must be at least 5 characters long.");
        return false;
    }

    const passwordPattern = /^[0-9][a_zA-Z0-9]*$/;
    if(!passwordPattern.test(password.value)) {
        alert("Password must start with a digit and be alphanumeric.");
        return false;
    }
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if(!emailPattern.test(email.value)){
        alert("Please enter a valid email address.");
        return false;
    }

    return true;


}*/