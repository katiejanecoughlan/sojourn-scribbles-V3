// Create a script element to load jQuery
var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
script.onload = function() {
    // jQuery is now loaded, so we can continue with our script

    // Assigning jQuery.noConflict() to a new alias
    var $j = jQuery.noConflict();

    // jQuery document ready function
    $j(document).ready(function() {
        // Initially hide the profile form
        $j('#profileForm').hide();

        // Edit button click handler to toggle visibility of profile form
        $j('#update-btn').click(function() {
            $j('#profileForm').toggle();
        });

        // Profile form submission handling
        $j('#profileForm').submit(function(e) {
            e.preventDefault(); // Prevent default form submission
            var formData = $j(this).serialize(); // Serialize form data
            $j.ajax({
                type: 'POST',
                url: $j(this).attr('action'),
                data: formData,
                success: function(response) {
                    // Redirect to the profile page
                    window.location.href = '/profiles/'; // Update the URL to the profile page
                },
                error: function(xhr, status, error) {
                    // Handle errors
                    console.error(xhr.responseText);
                }
            });
        });

        // Event listener for form field changes in profile form
        $j('#profileForm input, #profileForm textarea').on('input', function() {
            // Construct HTML elements to match the semantic structure
            var formDataHtml = '<h2>' + $j('#id_journal_title').val() + '</h2>';
            formDataHtml += '<p>' + $j('#id_bio').val() + '</p>';
            // Update the static text block with the constructed HTML
            $j('.profile-text .col-md-8').html(formDataHtml);
        });

        // Prevent submission of post form when pressing enter in any field
        $j('#postForm').on('keypress', function(e) {
            return e.which !== 13;
        });

        // Reset post form errors when profile form is submitted
        $j('#profileForm').submit(function() {
            $j('#postForm .errorlist').remove(); // Remove any existing error messages
        });

        // Ensure profile form is hidden when the page loads
        $j('#profileForm').hide();
    });
};

// Append the script element to the head to start loading jQuery
document.head.appendChild(script);
