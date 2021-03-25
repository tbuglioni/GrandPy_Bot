$(document).ready(function() {

	
	$('form').on('submit', function(event) {
		
		$('#dialogue_zone').append(
			$('<div/>')
			  .addClass("user_bubble")
			  .append("<p/>")
				.text($('#my_text').val())
		  );
		
		$('#dialogue_zone').append(
			$('<div/>')
			  .addClass("bot_bubble")
			  .append("<p/>")
				.text("hum...hum...")
		  );
		$('#dialogue_zone').scrollTop($('#dialogue_zone')[0].scrollHeight);

		$.ajax({
			data : {
				my_text : $('#my_text').val()
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {
			document.querySelector("form").reset();
			$( '.bot_bubble:last' ).remove();
			$('#dialogue_zone').append(
				$('<div/>')
				  .addClass("bot_bubble")
			  );
			if (data.error) {
				$('.bot_bubble:last').text(data.error);
				
			}
			else {
				$('.bot_bubble:last').append($('<p/>')).append(data.random_text);
				$('.bot_bubble:last').append($('<p/>')).append(data.wiki_summary);
				$('.bot_bubble:last').append(
					$('<a/>')
						.attr({
							href: data.wiki_link, 
							target:"_blank" 
						})
						.text(" Lien vers wikipedia")
					);				
				$('#dialogue_zone').append(
					$('<div/>')
					  .addClass("map")
				  );
				
				function myMap(){
					const center = { lat: data.lat, lng: data.lng };
					const zoom = 14;
					const loader = new google.maps.plugins.loader.Loader({
					apiKey: data.google_key,
					version: "weekly",
					});
					loader.load().then(() => {
					  map = new google.maps.Map($(".map:last")[0], {
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
				$('#dialogue_zone').scrollTop($('#dialogue_zone')[0].scrollHeight);
				
				
				
			}

		});
		
		event.preventDefault();

	});

});