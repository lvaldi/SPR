function add() {

	//Create an input type dynamically.
	var element = document.createElement("input");


	//Assign different attributes to the element.
	element.setAttribute("type", "text");
	element.setAttribute("value", "");
	element.setAttribute("name", "milestone");
	element.setAttribute("style", "width:200px");

	// 'addMilestone' is the div id, where new fields are to be added
	var milestone = document.getElementById("addMilestone");

	//Append the element in page (in span).
	milestone.appendChild(element);
}