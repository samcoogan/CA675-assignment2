$(document).ready(function () {

	$("#search-btn").click(function()){

		$.ajax({
			url"/search-tweets",
			type: "POST",
			data JSON.stringify(info),
			contentType: "application/json",
		}).done(function (data)){
			var $tweetsOut =
		}
	}


})