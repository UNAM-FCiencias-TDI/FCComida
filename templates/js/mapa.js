$(function() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(getCoords, getError);

	} else {

	}

	function getCoords(position) {
		var lat = position.coords.latitude;
		var lng = position.coords.longitude;

		initialize(lat,lng)
	}

	function getError (err){
		initialize(19.3234728, -99.181487);

	}

	function initialize (lat, lng) {
		var mapCanvas = document.getElementById('map');
		var latlng = new google.maps.LatLng(lat, lng);
		var mapSettings =   {
			center: latlng,
			zoom: 15,
			mapTypeId: google.maps.MapTypeId.ROADMAP
		}
		map = new google.maps.Map($('#mapa').get(0), mapSettings);
		var marker = new google.maps.Marker({
			position: latlng,
			map: map,
			draggable: true,
			title: 'Colocalo en la posición del comercio'
		});
		google.maps.event.addListener(marker, 'position_changed', function (){
			getMarkerCoords(marker)
		});

	}
	function getMarkerCoords(marker) {
		var markerCoords = marker.getPosition();
		$('#id_latitud').val(markerCoords.lat());
		$('#id_longitud').val(markerCoords.lng());
	}

});