function con (name,ball) {
	if (ball <= 300 && ball > 0) {
		document.write("This is very good for " + name + ball);
	}
	
	else if (ball >= 300){
		document.write("Its not good " + name + ball);
	}
	
	else {
		document.write("bellow " + name + ball);
	}
}

con("tuhin ",0);