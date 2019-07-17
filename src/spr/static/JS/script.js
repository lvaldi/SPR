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
	var add_milestone = document.getElementById("addMilestone");

	//Append the element in page (in span).
	add_milestone.appendChild(list);
}

// function parse() {
// 	var milestone_list = milestone_var.split(',');
// 	var milestone = document.getElementById('milestone')
// 	for (var i = 0; i < milestone_list.length; i++) {
// 		var list = document.createElement("LI");
// 		var textnode = document.createTextNode(milestone_list[i]);
// 		list.appendChild(textnode);
// 		milestone.appendChild(list);
// 	}
// }