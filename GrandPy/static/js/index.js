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
				
			}
			else {
				$('#successAlert').text(data.name);
				$('#successAlert').append(data.lat);
				$('#successAlert').append(data.lng);
				$('#successAlert').append(data.formated_location);
				$('#successAlert').append(data.wiki_summary);
				$('#successAlert').append(data.wiki_link);
				$("#map").show();
				
				function myMap(){
					const center = { lat: data.lat, lng: data.lng };
					const zoom = 14;
					const loader = new google.maps.plugins.loader.Loader({
					apiKey: data.google_key,
					version: "weekly",
					});
					loader.load().then(() => {
					  map = new google.maps.Map(document.getElementById("map"), {
						center,
						zoom,
					  });
					  new google.maps.Marker({
						position: center,
						map
					  });
					  
					});
					
					}
			
				myMap()
				
				
			}

		});

		event.preventDefault();

	});

});