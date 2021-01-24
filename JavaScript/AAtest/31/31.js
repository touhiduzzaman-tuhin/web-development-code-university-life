function tuhin () {
	
	var paragraph = document.getElementsByClassName("para");
	
	var para1 = paragraph[0].innerHTML;
	var para2 = paragraph[1].innerHTML;
	var para3 = paragraph[2].innerHTML = para1 + para2;
	
	var para1 = paragraph[0].innerHTML = "";
	var para2 = paragraph[1].innerHTML = "";
}