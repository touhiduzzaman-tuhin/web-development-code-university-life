function statement (num, str) {
	
	if(num >= 50 && num < 100) {
		
		var num1 = "Fifty Plus";
	}
	
	else if (num >= 100) {
		
		var num1 = "Hundrad Plus";
	}
	
	else {
		var num1 = "Low Score"
	}
	
	
	document.write(num + str + " so " + num1);
}

statement(144, " Run in a single match");