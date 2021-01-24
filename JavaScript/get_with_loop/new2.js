function changeStyle () {
	
	var paragraph = document.getElementsByTagName("p");
	
	for(var i = 0; i < paragraph.length; i++) {
		
		paragraph[i].style.fontStyle = "italic";
	}
}