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
                $('.profile-text .col-md-8').html(response.content);
                $('.profile-form').hide(); // Hide the form after successful submission
            },
            error: function(xhr, status, error) {
                // Handle errors
                console.error(xhr.responseText);
            }
        });
    });

    // Event listener for form field changes
    $('#profileForm input, #profileForm textarea').on('input', function() {
        // Construct HTML elements to match the semantic structure
        var formDataHtml = '<h2>' + $('#id_title').val() + '</h2>';
        formDataHtml += '<p>' + $('#id_content').val() + '</p>';
        // Update the static text block with the constructed HTML
        $('.profile-text .col-md-8').html(formDataHtml);
    });
});
