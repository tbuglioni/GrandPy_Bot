$("#map").hide();
$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				my_text : $('#my_text').val()
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error);
				$("#map").show();
			}
			else {
				$('#successAlert').text(data.name);
				
			}

		});

		event.preventDefault();

	});

});