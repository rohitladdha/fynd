var map;
var markers = [];

function initMap() {
  var haightAshbury = {lat: 37.769, lng: -122.446};

  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 12,
    center: haightAshbury,
    mapTypeId: google.maps.MapTypeId.TERRAIN
  });

  // This event listener will call addMarker() when the map is clicked.
  map.addListener('click', function(event) {
    addMarker(event.latLng);
  });

  // Adds a marker at the center of the map.
  addMarker(haightAshbury);
}

// Adds a marker to the map and push to the array.
function addMarker(location) {
  var marker = new google.maps.Marker({
    position: location,
    map: map
  });
  deleteMarkers();
  markers.push(marker);
}

// Sets the map on all markers in the array.
function setMapOnAll(map) {
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(map);
  }
}

// Removes the markers from the map, but keeps them in the array.
function clearMarkers() {
  setMapOnAll(null);
}

// Shows any markers currently in the array.
function showMarkers() {
  setMapOnAll(map);
}

// Deletes all markers in the array by removing references to them.
function deleteMarkers() {
  clearMarkers();
  markers = [];
}


function send_preference()
{
	var url = "";
	var lat = markers[0]['lat'];
	var lng = markers[1]['lng'];
	var time = document.getElementById('travel_time');

	$.ajax({
	        type: "GET",
	        url: "http://10.1.6.24:8000/match/get_intersection",
	        data: {
	            'size': 1,
	            'lat1': lat,
	            'lon1': lng,
	            'range1': parseInt(time),
	            'range_type1':'time'
	        },
	        success: function (data) {
	            var json = JSON.parse(data);
	            var triangleCoords = [];
	            var coords = json[0][0];
	            
	            for(i=0;i<coords.length;i++)
	            {
	            	var coord_dict = {'lat': coords[i][0],'lng':coords[i][1]}
	            	triangleCoords.push(coord_dict);
	            }
	            
	            var polygon = new google.maps.Polygon({
					    paths: triangleCoords,
					    strokeColor: '#FF0000',
					    strokeOpacity: 0.8,
					    strokeWeight: 2,
					    fillColor: '#FF0000',
					    fillOpacity: 0.35
					  });
					  polygon.setMap(map);
		        },
		        error: function (err) {
		            console.log("Ajax: Get error for localities:", err);
		        }
            });
}
