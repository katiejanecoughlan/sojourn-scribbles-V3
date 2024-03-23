$(document).ready(function(){
    // Show popover on page load
    $('#popover-content').popover({
        container: 'body',
        placement: 'bottom',
        trigger: 'manual',
        html: true
    }).popover('show');

    // Close popover when close button is clicked
    $('#close-popover').on('click', function() {
        $('#popover-content').popover('dispose');
    });
});