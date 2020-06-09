function sendMail(contactForm) {
    emailjs.send("gmail", "contact", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "project_request": contactForm.projectsummary.value
    })
        .then(
            function (response) {
                console.log("SUCCESS", response);
                contactForm.name.value = ""
                contactForm.emailaddress.value = ""
                contactForm.projectsummary.value = ""
            },
            function (error) {
                console.log("FAILED", error);
            }
        );
    return false;  // To block from loading a new page
}