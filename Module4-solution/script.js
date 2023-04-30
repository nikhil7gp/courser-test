var names=new Array();
names[0]="Nikhil";
names[1]="jonny";
names[2]="FLash";
names[3]="Jogi";
names[4]="Naruto";
names[5]="johan";
names[6]="vinu";
names[7]="John";
names[8]="king";
names[9]="jin";

for (var i = 0;i < names.length;i++){
	if (names[i].charAt(0)=== "J" || names[i].charAt(0)=== "j" ) {
		console.log("Goodbye " + names[i]);
	}
	else{
		console.log("Hello " + names[i]);
	}
}

