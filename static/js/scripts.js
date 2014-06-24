$(function(){
	if (navigator.geolocation){
		navigator.geolocation.getCurrentPosition(getCoords, getError);
	} else {
		initialize(9.8539661, -83.90957259999999);
	}
	
	function getCoords(position){
		var lat = position.coords.latitude;
		var lon = position.coords.longitude;
		
		initialize(lat, lon);
	}
	
	function getError(err){
		initialize(9.8539661, -83.90957259999999);	
	}
	
	function initialize(lat, lon){
		var latlng = new google.maps.LatLng(lat, lon);
		var mapSettings = {
			center: latlng,
			zoom: 15,
			mapTypeId: google.maps.MapTypeId.ROADMAP
		}
		
		map = new google.maps.Map($('#mapa').get(0), mapSettings);
		
		var marker = new google.maps.Marker({
			position: latlng,
			map: map,
			draggable: true,
			title: 'Arrastrame!'
		});
		
		google.maps.event.addListener(marker, 'position_changed', function(){
			getMarkerCoords(marker);
		});
	}
	
	function getMarkerCoords(marker){
		var markerCoords = marker.getPosition();
		$('#id_lat').val( markerCoords.lat() );
		$('#id_lon').val( markerCoords.lng() );
	}
	
	$('#form_coords').submit(function(e){
		e.preventDefault();
		
		$.post('/coords/save', $(this).serialize(), function(data){
			if(data.ok)
			{
				$('#data').html(data.msg);
				$('#form_coords').each(function() { this.reset(); });
			} else {
				alert(data.msg);
			} 
		}, 'json');	
	});
});
