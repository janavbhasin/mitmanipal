document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('student-form');
    const resultTextArea = document.getElementById('details-output');
    const percentageLabel = document.getElementById('percentage');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        console.log("form submitted");
        const name = document.getElementById('name').value;
        const dob = document.getElementById('dob').value;
        const address = document.getElementById('address').value;
        const contact = document.getElementById('contact').value;
        const email = document.getElementById('email').value;
        const english = parseInt(document.getElementById('english').value);
        const physics = parseInt(document.getElementById('physics').value);
        const chemistry = parseInt(document.getElementById('chemistry').value);

        // Calculate total and percentage
        const totalMarks = english + physics + chemistry;
        const percentage = ((totalMarks) / 300) * 100;

        // Display the details
        const studentDetails = `
            Name: ${name}\n
            Date of Birth: ${dob}\n
            Address: ${address}\n
            Contact: ${contact}\n
            Email: ${email}\n
            English Marks: ${english}\n
            Physics Marks: ${physics}\n
            Chemistry Marks: ${chemistry}\n
            Total Marks: ${totalMarks}\n
        `;
        
        resultTextArea.value = studentDetails;
        percentageLabel.textContent = percentage.toFixed(2) + '%';
    });
});
