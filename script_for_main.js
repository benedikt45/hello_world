

	var mainMenu = document.querySelectorAll('a');

	
		for (var i = 0; i<mainMenu.length; i++) {
			btn = mainMenu[i].onclick = function(e){
				var httpRequest = new XMLHttpRequest();
				if (e.target.innerText=='������') {
					httpRequest.open('GET', 'http://localhost/getPageWeather');
				} else if (e.target.innerText=='������') {
					httpRequest.open('GET', 'http://localhost/getCurrency');
				}
				
				httpRequest.responseType = 'text';
				httpRequest.onload = function(){
					if (httpRequest.readyState == 4){
						if (httpRequest.status == 200) {
							serverAnswer = httpRequest.responseText;
							//var jsonResponse = JSON.parse(serverAnswer);
							document.getElementById("welcome").innerHTML = serverAnswer;
						}
					}
				}
				httpRequest.send();
				for (var i = 0; i<mainMenu.length; i++) {
					mainMenu[i].parentNode.removeAttribute('class');
				}
				e.target.parentNode.setAttribute('class', 'focus');
			}
		}
	
	