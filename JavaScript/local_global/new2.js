var name = "tuhin";  //global variable

function add () {
	var name1 = "shahed";       //local variable
	name1 = "shahed";         //global variable
} 

add ();

document.write(name);