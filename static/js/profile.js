$(document).ready(function() {
    // Initially hide the form
    $('.profile-form').hide();

    // Edit button click handler
    $('#update-btn').click(function() {
        $('.profile-form').toggle();
    });

    // Form submission handling
    $('#profileForm').submit(function(e) {
        e.preventDefault(); // Prevent default form submission
        var formData = $(this).serialize(); // Serialize form data
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: formData,
            success: function(response) {
                // Update the static text with new data
                $('.profile-text').html(response.content);
                $('.profile-form').hide(); // Hide the form after successful submission
            },
            error: function(xhr, status, error) {
                // Handle errors
                console.error(xhr.responseText);
            }
        });
    });
});

