
function apply () {
	var btn = document.querySelector('button');
	if (btn !== null) {				
		btn.onclick = function() {
			var city = document.getElementsByName('inputCity')[0].value;
			xhrRequest = new XMLHttpRequest();
			xhrRequest.open('POST', 'http://localhost/getWeather');
			xhrRequest.responseType = 'text';
			xhrRequest.onload = function() {
				if (xhrRequest.readyState == 4){
					if (xhrRequest.status == 200) {
						serverAnswer = xhrRequest.responseText;
						document.getElementById("answer").innerHTML = serverAnswer;
					}
				}
			}
			xhrRequest.send(city);
		} 
	} else {
			setTimeout(apply, 50);
	}
 
} 

apply();