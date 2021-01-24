function changeStyle () {
	
	var paragraph = document.getElementsByClassName ("para");

	var newpara1 = paragraph[0].innerHTML;
	
	var newpara2 = paragraph[1].innerHTML;
	
	var newpara3 = paragraph[2].innerHTML = newpara1 + newpara2 ;
	
	var newpara1 = paragraph[0].innerHTML = "";
	
	var newpara2 = paragraph[1].innerHTML = "";
}