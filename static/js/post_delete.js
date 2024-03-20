// delete_modal.js

document.addEventListener('DOMContentLoaded', function() {
    // Attach event listener to delete button inside the post delete confirmation modal
    document.getElementById('deleteModal').addEventListener('click', function(event) {
        if (event.target.id === 'deleteConfirm') {
            // Submit the form when delete button is clicked
            document.getElementById('deletePostForm').submit();
        }
    });
});
