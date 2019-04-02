function validform() {

    var first_name = document.forms["my-form"]["first-name"].value;
    var last_name = document.forms["my-form"]["last-name"].value;
    var email = document.forms["my-form"]["email-address"].value;
    var u_name = document.forms["my-form"]["username"].value;
    var phone_num = document.forms["my-form"]["phone_number"].value;
    var present_addr = document.forms["my-form"]["permanent-address"].value;

    // nullity check
    if (first_name==null || first_name=="")
    {
        alert("Please Enter Your First Name");
        return false;
    } else if (last_name==null || last_name=="") 
    {
        alert("Please Enter Your Last Name");
        return false;
    } else if (email==null || email=="")
    {
        alert("Please Enter Your Email Address");
        return false;
    } else if (u_name==null || u_name=="")
    {
        alert("Please Enter Your Username");
        return false;
    } else if (phone_num==null || phone_num=="")
    {
        alert("Please Enter Your Phone Number");
        return false;
    } else if (present_addr==null || present_addr=="")
    {
        alert("Please Enter Your Permanent Address");
        return false;
    } 

    // validity check
    else if (validateEmail(email)==false)
    {
        alert("Email entered is invalid");
        return false;
    } else if (validatePhoneNum(phone_num)==false)
    {
        alert("Phone number entered is invalid");
        return false;
    } else {
        // form submission
        alert("Your have successfully registered!");
        // redirect to login page?
    }
}

function validateEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}

function validatePhoneNum(number) {
    var re = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    return re.test(number);
}
