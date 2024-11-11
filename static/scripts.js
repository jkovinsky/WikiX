function getInput() {
    const form = document.getElementById("usr-info");
    const firstName = form.elements["fname"].value;
    const lastName = form.elements["lname"].value;
    const email = form.elements["email"].value;
    if(!firstName | !lastName | !email){
        if (!firstName) {
            alert("Please fill in your first name.");
        }
        if (!lastName){
            alert("Please fill in your last name.");
        }
        if (!email){
            alert("Please fill in your email.");
        }
        return false; 
    }

    const user = {
        firstName: firstName,
        lastName: lastName,
        email: email
    };

    console.log("First Name:", user.firstName);
    console.log("Last Name:", user.lastName);
    console.log("Email:", user.email);

}