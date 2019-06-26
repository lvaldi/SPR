function add() {

	//Create an input type dynamically.
	var list = document.createElement("LI");
	var element = document.createElement("INPUT")


	//Assign different attributes to the element.
	element.setAttribute("type", "text");
	element.setAttribute("value", "");
	element.setAttribute("name", "milestone");


	list.appendChild(element);

	// 'addMilestone' is the div id, where new fields are to be added
	var milestone = document.getElementById("addMilestone");

	//Append the element in page (in span).
	milestone.appendChild(list);
}