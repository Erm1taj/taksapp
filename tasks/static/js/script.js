$(document).ready(function() {
	$(document).on('click', '.checkbox', function() {
		$(this).parent().addClass('completed');
		$(this).attr('disabled', true);

		id = $(this).attr('data-uid');
		$.get("/tasks/completed/" + id);
	}); 
	$(document).on('click', '.remove', function(){
		$(this).parent().remove();

		id = $(this).attr('data-uid');
		$.get("/tasks/delete/" + id)
	});
});