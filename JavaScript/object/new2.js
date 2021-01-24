var orc = {
	name : "tuhin",
	age : 24,
	study : true,
	
	eat : function() {
		document.write(" he can eat");
	}
};

//document.write(orc.name);

var currentage = orc.age + 6;


//document.write(orc.age);


//document.write(currentage);


orc.study = false;

if(orc.study == true) {
	orc.eat();
}

else {
	document.write("do not eat");
}