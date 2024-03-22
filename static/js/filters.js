document.addEventListener('DOMContentLoaded', function () {
    var urlParams = new URLSearchParams(window.location.search);
    var selectedUser = urlParams.get('user');
    var selectedCountry = urlParams.get('country');
    // Set dropdown values if parameters exist
    if (selectedUser) {
        var userDropdown = document.getElementById('user');
        if (userDropdown) {
            userDropdown.value = selectedUser;
            console.log("Selected User:", selectedUser);
        } else {
            console.error("User dropdown not found.");
        }
    }
    if (selectedCountry) {
        var countryDropdown = document.getElementById('country');
        if (countryDropdown) {
            countryDropdown.value = selectedCountry;
            console.log("Selected Country:", selectedCountry);
        } else {
            console.error("Country dropdown not found.");
        }
    }
    // Update hidden input fields with selected values before form submission
    document.querySelectorAll('form').forEach(function(form) {
        form.addEventListener('submit', function(event) {
            var userDropdown = document.getElementById('user');
            var countryDropdown = document.getElementById('country');
            var userHiddenInput = document.getElementById('user_hidden');
            var countryHiddenInput = document.getElementById('country_hidden');
            
            if (userDropdown && countryDropdown && userHiddenInput && countryHiddenInput) {
                userHiddenInput.value = userDropdown.value;
                countryHiddenInput.value = countryDropdown.value;
            }
        });
    });
});
