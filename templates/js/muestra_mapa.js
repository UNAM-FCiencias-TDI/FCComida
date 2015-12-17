  function initialize(lat, lng, id, nombre) {
    var latlng = new google.maps.LatLng(lat, lng);
        var mapCanvas = document.getElementById(id);
        var mapOptions = {
          center: new google.maps.LatLng(lat, lng),
          zoom: 15,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        }
        var map = new google.maps.Map(mapCanvas, mapOptions)
      var marker = new google.maps.Marker({
      position: latlng,
      map: map,
      draggable: false,
      title: 'El comercio '+nombre+' se encuentra aqui'
    });
}